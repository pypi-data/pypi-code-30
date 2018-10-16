#!/usr/bin/env python3
#
#   (c) 2018  Universite de Rennes 1
#
# Contact address: <t3devkit@irisa.fr>
#
#
# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
#


from ttproto.core.lib.ieee802154 import Ieee802154
from ttproto.core.lib.inet.meta import *
from ttproto.core.lib.inet.basics import *
from ttproto.core.lib.inet.sixlowpan import SixLowpan

import ttproto.core.lib.inet.udp

__all__ = [
    'ZigBeeEncapsulationProtocol'
]

class ZigBeeEncapsulationProtocol(
    metaclass=InetPacketClass,
    fields=[
        ("Protocol ID string", "pid", Hex(UInt16)),
        ("Version", "ver", UInt8),
        ("Type", "type", UInt8),
        ("Channel", "ch", UInt8),
        ("Device ID", "did", UInt16),
        ("LQI/CRC Mode", "mode", UInt8),
        ("LQI Value", "lqi", UInt8),
        ("NTP timestamp (s)", "nts", Hex(UInt32)),
        ("NTP timestamp fraction (ms)", "nts_frac", Hex(UInt32)),
        ("Sequence number", "seq", UInt32),
        ("future", "fut", Hex(UInt80)),
        ("Length", "len", UInt8),
        ("Payload", "pl", Ieee802154),
    ]):
    pass

ttproto.core.lib.inet.udp.udp_port_map[17754] = ZigBeeEncapsulationProtocol
