# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailmojo.api_client import ApiClient


class AutomationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_campaign_by_id(self, campaign_id, **kwargs):  # noqa: E501
        """Retrieve an automation campaign by id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_campaign_by_id(campaign_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int campaign_id: ID of the automation campaign to retrieve. (required)
        :return: CampaignDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_campaign_by_id_with_http_info(campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_campaign_by_id_with_http_info(campaign_id, **kwargs)  # noqa: E501
            return data

    def get_campaign_by_id_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Retrieve an automation campaign by id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_campaign_by_id_with_http_info(campaign_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int campaign_id: ID of the automation campaign to retrieve. (required)
        :return: CampaignDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_campaign_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `get_campaign_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/campaigns/{campaign_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CampaignDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
