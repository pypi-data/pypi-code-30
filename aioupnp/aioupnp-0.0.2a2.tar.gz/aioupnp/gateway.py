import logging
import socket
from collections import OrderedDict
from typing import Dict, List, Union, Type
from aioupnp.util import get_dict_val_case_insensitive, BASE_PORT_REGEX, BASE_ADDRESS_REGEX
from aioupnp.constants import SPEC_VERSION, SERVICE
from aioupnp.commands import SOAPCommands
from aioupnp.device import Device, Service
from aioupnp.protocols.ssdp import fuzzy_m_search, m_search
from aioupnp.protocols.scpd import scpd_get
from aioupnp.protocols.soap import SOAPCommand
from aioupnp.serialization.ssdp import SSDPDatagram
from aioupnp.util import flatten_keys
from aioupnp.fault import UPnPError

log = logging.getLogger(__name__)

return_type_lambas = {
    Union[None, str]: lambda x: x if x is not None and str(x).lower() not in ['none', 'nil'] else None
}


def get_action_list(element_dict: dict) -> List:  # [(<method>, [<input1>, ...], [<output1, ...]), ...]
    service_info = flatten_keys(element_dict, "{%s}" % SERVICE)
    if "actionList" in service_info:
        action_list = service_info["actionList"]
    else:
        return []
    if not len(action_list):  # it could be an empty string
        return []

    result: list = []
    if isinstance(action_list["action"], dict):
        arg_dicts = action_list["action"]['argumentList']['argument']
        if not isinstance(arg_dicts, list):  # when there is one arg
            arg_dicts = [arg_dicts]
        return [[
            action_list["action"]['name'],
            [i['name'] for i in arg_dicts if i['direction'] == 'in'],
            [i['name'] for i in arg_dicts if i['direction'] == 'out']
        ]]
    for action in action_list["action"]:
        if not action.get('argumentList'):
            result.append((action['name'], [], []))
        else:
            arg_dicts = action['argumentList']['argument']
            if not isinstance(arg_dicts, list):  # when there is one arg
                arg_dicts = [arg_dicts]
            result.append((
                action['name'],
                [i['name'] for i in arg_dicts if i['direction'] == 'in'],
                [i['name'] for i in arg_dicts if i['direction'] == 'out']
            ))
    return result


class Gateway:
    def __init__(self, ok_packet: SSDPDatagram, m_search_args: OrderedDict, lan_address: str,
                 gateway_address: str) -> None:
        self._ok_packet = ok_packet
        self._m_search_args = m_search_args
        self._lan_address = lan_address
        self.usn = (ok_packet.usn or '').encode()
        self.ext = (ok_packet.ext or '').encode()
        self.server = (ok_packet.server or '').encode()
        self.location = (ok_packet.location or '').encode()
        self.cache_control = (ok_packet.cache_control or '').encode()
        self.date = (ok_packet.date or '').encode()
        self.urn = (ok_packet.st or '').encode()

        self._xml_response = b""
        self._service_descriptors: Dict = {}
        self.base_address = BASE_ADDRESS_REGEX.findall(self.location)[0]
        self.port = int(BASE_PORT_REGEX.findall(self.location)[0])
        self.base_ip = self.base_address.lstrip(b"http://").split(b":")[0]
        assert self.base_ip == gateway_address.encode()
        self.path = self.location.split(b"%s:%i/" % (self.base_ip, self.port))[1]

        self.spec_version = None
        self.url_base = None

        self._device: Union[None, Device] = None
        self._devices: List = []
        self._services: List = []

        self._unsupported_actions: Dict = {}
        self._registered_commands: Dict = {}
        self.commands = SOAPCommands()

    def gateway_descriptor(self) -> dict:
        r = {
            'server': self.server.decode(),
            'urlBase': self.url_base,
            'location': self.location.decode(),
            "specVersion": self.spec_version,
            'usn': self.usn.decode(),
            'urn': self.urn.decode(),
        }
        return r

    @property
    def manufacturer_string(self) -> str:
        if not self.devices:
            raise NotImplementedError()
        device = list(self.devices.values())[0]
        return "%s %s" % (device.manufacturer, device.modelName)

    @property
    def services(self) -> Dict:
        if not self._device:
            return {}
        return {service.serviceType: service for service in self._services}

    @property
    def devices(self) -> Dict:
        if not self._device:
            return {}
        return {device.udn: device for device in self._devices}

    def get_service(self, service_type: str) -> Union[Type[Service], None]:
        for service in self._services:
            if service.serviceType.lower() == service_type.lower():
                return service
        return None

    @property
    def _soap_requests(self) -> Dict:
        return {
            name: getattr(self.commands, name)._requests for name in self._registered_commands.keys()
        }

    def debug_gateway(self) -> Dict:
        return {
            'gateway_address': self.base_ip,
            'soap_port': self.port,
            'm_search_args': self._m_search_args,
            'reply': self._ok_packet.as_dict(),
            'registered_soap_commands': self._registered_commands,
            'unsupported_soap_commands': self._unsupported_actions,
            'gateway_xml': self._xml_response,
            'service_descriptors': self._service_descriptors,
            'soap_requests': self._soap_requests
        }

    @classmethod
    async def discover_gateway(cls, lan_address: str, gateway_address: str, timeout: int = 30,
                               igd_args: OrderedDict = None,  ssdp_socket: socket.socket = None,
                               soap_socket: socket.socket = None):
        if not igd_args:
            m_search_args, datagram = await fuzzy_m_search(lan_address, gateway_address, timeout, ssdp_socket)
        else:
            m_search_args = OrderedDict(igd_args)
            datagram = await m_search(lan_address, gateway_address, igd_args, timeout, ssdp_socket)
        gateway = cls(datagram, m_search_args, lan_address, gateway_address)
        await gateway.discover_commands(soap_socket)
        return gateway

    async def discover_commands(self, soap_socket: socket.socket = None):
        response, xml_bytes = await scpd_get(self.path.decode(), self.base_ip.decode(), self.port)
        self._xml_response = xml_bytes
        self.spec_version = get_dict_val_case_insensitive(response, SPEC_VERSION)
        self.url_base = get_dict_val_case_insensitive(response, "urlbase")
        if not self.url_base:
            self.url_base = self.base_address.decode()
        if response:
            self._device = Device(
                self._devices, self._services, **get_dict_val_case_insensitive(response, "device")
            )
        else:
            self._device = Device(self._devices, self._services)
        for service_type in self.services.keys():
            await self.register_commands(self.services[service_type], soap_socket)

    async def register_commands(self, service: Service, soap_socket: socket.socket = None):
        if not service.SCPDURL:
            raise UPnPError("no scpd url")
        service_dict, xml_bytes = await scpd_get(service.SCPDURL, self.base_ip.decode(), self.port)
        self._service_descriptors[service.SCPDURL] = xml_bytes

        if not service_dict:
            return

        action_list = get_action_list(service_dict)

        for name, inputs, outputs in action_list:
            try:
                current = getattr(self.commands, name)
                annotations = current.__annotations__
                return_types = annotations.get('return', None)
                if return_types:
                    if isinstance(return_types, type):
                        return_types = (return_types, )
                    else:
                        return_types = tuple([return_type_lambas.get(a, a) for a in return_types.__args__])
                    return_types = {r: t for r, t in zip(outputs, return_types)}
                param_types = {}
                for param_name, param_type in annotations.items():
                    if param_name == "return":
                        continue
                    param_types[param_name] = param_type
                command = SOAPCommand(
                    self.base_ip.decode(), self.port, service.controlURL, service.serviceType.encode(),
                    name, param_types, return_types, inputs, outputs, soap_socket)
                setattr(command, "__doc__", current.__doc__)
                setattr(self.commands, command.method, command)

                self._registered_commands[command.method] = service.serviceType
                log.debug("registered %s::%s", service.serviceType, command.method)
            except AttributeError:
                s = self._unsupported_actions.get(service.serviceType, [])
                s.append(name)
                self._unsupported_actions[service.serviceType] = s
                log.debug("available command for %s does not have a wrapper implemented: %s %s %s",
                          service.serviceType, name, inputs, outputs)
