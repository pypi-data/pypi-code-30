# -*- coding: utf-8 -*-
import logging
import re

from clarifai.rest.grpc.custom_converters.custom_dict_to_message import dict_to_protobuf
from clarifai.rest.grpc.custom_converters.custom_message_to_dict import protobuf_to_dict
from clarifai.rest.grpc.proto.clarifai.api.endpoint_pb2 import _V2
from clarifai.rest.http_client import HttpClient

BASE_URL = "https://api.clarifai.com"
URL_TEMPLATE_PARAM_REGEX = re.compile(r'\{{1}(.*?)\}{1}')

logger = logging.getLogger('clarifai')


class GRPCJSONChannel(object):
  """ This mimics the behaviour of a grpc channel object but allows transport over https with
  json request and response bodies.

  Currently there is only support for unary_unary requests. If you have any other type of grpc
  request this channel will nicely fail when trying to use within a grpc stub.

  Example:
    Assuming your top level endpoints are called V2 and in a proto/clarifai/api/endpoint.proto file,
    then you build those in python and can import the spec to use in GRPCJSONChannel as follows:

    from clarifai.rest.grpc.proto.clarifai.api.endpoint_pb2_grpc import V2Stub
    from clarifai.rest.grpc.proto.clarifai.api.endpoint_pb2 import _V2
    channel = GRPCJSONChannel(key="api key", service_descriptor=_V2)
    stub = V2Stub(channel)

    # Then you can use the stub to call just like grpc directly!!!
    result = stub.PostInputs(PostInputsRequest(inputs=[Input(data=Data(image=Image(
      url="http://...")))]))
  """

  def __init__(self, key, base_url=BASE_URL, service_descriptor=_V2):
    """
    Args:
      key: a string api key to use in the {"Authorization": "Key %s" % key} headers to send in each
    request.
      base_url: if you want to point at a different url than the default.
      service_description: This is a ServiceDescriptor object found in the compiled grpc-gateway
    .proto results. For example if your proto defining the endpoints is in endpoint.proto then look
    in endpoint_pb2.py file for ServiceDescriptor and use that.
    """
    self.base_url = base_url
    self.key = key
    self.name_to_resources = {}

    for m in service_descriptor.methods:
      # This gets the google.api.http object from the .proto file that looks like this:
      # option (google.api.http) = {
      #   delete: "/v2/users/{user_app_id.user_id}/apps/{user_app_id.app_id}/models/{model_id}"
      #   additional_bindings {
      #     delete: "/v2/models/{model_id}"
      #   }
      # Then we check if there are additional_bindings and use that if so (because we've had the
      # convention of having the default urls in there and the not yet used urls at the top level.

      base_http_rule = m.GetOptions().ListFields()[0][1]

      protobuf_name = '/' + service_descriptor.full_name + '/' + m.name
      self.name_to_resources[protobuf_name] = (m.input_type, [])

      for http_rule in base_http_rule.additional_bindings or [base_http_rule]:
        # Get the url template and the method to use for http.
        if http_rule.HasField('get'):
          method = 'GET'
          url_template = base_url + http_rule.get
        elif http_rule.HasField('post'):
          method = 'POST'
          url_template = base_url + http_rule.post
        elif http_rule.HasField('patch'):
          method = 'PATCH'
          url_template = base_url + http_rule.patch
        elif http_rule.HasField('put'):
          method = 'PUT'
          url_template = base_url + http_rule.put
        elif http_rule.HasField('delete'):
          method = 'DELETE'
          url_template = base_url + http_rule.delete
        else:
          raise Exception("Failed to parse the grpc-gateway service spec.")

        self.name_to_resources[protobuf_name][1].append((url_template, method))

  def unary_unary(self, name, request_serializer, response_deserializer):
    """ Method to create the callable JSONUnaryUnary. """
    request_message_descriptor, resources = self.name_to_resources[name]
    return JSONUnaryUnary(self.key, request_message_descriptor, resources, request_serializer,
                          response_deserializer)


class JSONUnaryUnary(object):
  """ This mimics the unary_unary calls and is actually the thing doing the http requests.
  """

  def __init__(self, key, request_message_descriptor, resources, request_serializer,
               response_deserializer):
    """
    Args:
      key: a string api key to use in the {"Authorization": "Key %s" % key} headers to send in each
           request.
      request_message_descriptor: this is a MessageDescriptor for the input type.
      resources: a list of available resource endpoints
      request_serializer: the method to use to serialize the request proto
      response_deserializer: the response proto deserializer which will be used to convert the http
                             response will be parsed into this.

    Returns:
      response: a proto object of class response_deserializer filled in with the response.
    """
    self.key = key
    self.request_message_descriptor = request_message_descriptor
    self.resources = resources
    self.request_serializer = request_serializer
    self.response_deserializer = response_deserializer
    self.http_client = HttpClient(key)

  def __call__(self, request, metadata=None):
    """ This is where the actually calls come through when the stub is called such as
    stub.PostInputs(). They get passed to this method which actually makes the request.

    Args:
      request: the proto object for the request. It must be the proper type for the request or the
        server will complain. Note: this doesn't type check the incoming request in the client but
        does make sure it can serialize before sending to the server atleast.
      metadata: not used currently, just added to match grpc.

    Returns:
      response: the proto object that this method returns.
    """
    if metadata is not None:
      raise Exception("No support currently for metadata field.")

    # There is no __self__ attribute on the request_serializer unfortunately.
    expected_object_name = self.request_message_descriptor.name
    if type(request).__name__ != expected_object_name:
      raise Exception("The input request must be of type: %s from %s" %
                      (expected_object_name, self.request_message_descriptor.file.name))

    params = protobuf_to_dict(request)

    url, method = _pick_proper_endpoint(self.resources, params)

    response_json = self.http_client.execute_request(method, params, url)

    # Get the actual message object to construct
    message = self.response_deserializer
    result = dict_to_protobuf(message, response_json)

    return result


def _pick_proper_endpoint(resources, request_dict):
  """
  Fills in the url template with the actual url params from the request body.
  Picks the most appropriate url depending on which parameters are present in the request body.
  Args:
    resources: all available resource endpoints for this method.
    request_dict: a dictionary form of the request from json_format.MessageToDict(request,
                  preserving_proto_field_name=True) so that we can recursively lookup url params.
  Returns:
    url: the url string to use in requests.
    method: one of get/post/patch/delete.
  """

  best_match_url = None
  best_match_method = None
  best_match_count = -1

  all_fields = []
  for url_template, method in resources:
    all_arguments_translated = True

    url = url_template
    count = 0
    for field in re.findall(URL_TEMPLATE_PARAM_REGEX, url_template):
      all_fields.append(field)

      field_value = request_dict.get(field.split('.')[-1])
      if not field_value:
        all_arguments_translated = False
        break

      count += 1

      url = url.replace('{' + field + '}', field_value)

    if all_arguments_translated:
      if best_match_count < count:
        best_match_url = url
        best_match_method = method
        best_match_count = count

  if not best_match_url:
    raise Exception("You must set one case of the following fields in your request proto: "
                    "%s" % all_fields)

  return best_match_url, best_match_method
