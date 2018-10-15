# coding: utf-8

"""
    Assetic Integration API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from assetic.api_client import ApiClient


class WorkRequestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def work_request_add_supporting_information_for_work_request(self, id, supporting_information_representation, **kwargs):  # noqa: E501
        """Add supporting information to work request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_add_supporting_information_for_work_request(id, supporting_information_representation, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str id: Work Request Guid (required)
        :param Assetic3IntegrationRepresentationsSupportingInformation supporting_information_representation: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.work_request_add_supporting_information_for_work_request_with_http_info(id, supporting_information_representation, **kwargs)  # noqa: E501
        else:
            (data) = self.work_request_add_supporting_information_for_work_request_with_http_info(id, supporting_information_representation, **kwargs)  # noqa: E501
            return data

    def work_request_add_supporting_information_for_work_request_with_http_info(self, id, supporting_information_representation, **kwargs):  # noqa: E501
        """Add supporting information to work request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_add_supporting_information_for_work_request_with_http_info(id, supporting_information_representation, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str id: Work Request Guid (required)
        :param Assetic3IntegrationRepresentationsSupportingInformation supporting_information_representation: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'supporting_information_representation']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method work_request_add_supporting_information_for_work_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `work_request_add_supporting_information_for_work_request`")  # noqa: E501
        # verify the required parameter 'supporting_information_representation' is set
        if ('supporting_information_representation' not in params or
                params['supporting_information_representation'] is None):
            raise ValueError("Missing the required parameter `supporting_information_representation` when calling `work_request_add_supporting_information_for_work_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'supporting_information_representation' in params:
            body_params = params['supporting_information_representation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/x-www-form-urlencoded', 'application/hal+json', 'application/hal+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workrequest/{id}/supportinginfo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def work_request_get(self, id, **kwargs):  # noqa: E501
        """Get specific work request by providing Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_get(id, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str id: Work request id (required)
        :return: Assetic3IntegrationRepresentationsWorkRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.work_request_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.work_request_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def work_request_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get specific work request by providing Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_get_with_http_info(id, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str id: Work request id (required)
        :return: Assetic3IntegrationRepresentationsWorkRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method work_request_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `work_request_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workrequest/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Assetic3IntegrationRepresentationsWorkRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def work_request_get_supporting_information_for_work_request(self, id, **kwargs):  # noqa: E501
        """Get supporting information history as a list by providing work request guid  # noqa: E501

        Sample request: <br /><pre>   /api/v2/workrequest/592325B7-A10E-E711-80BB-005056947278/supportinginfo      </pre>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_get_supporting_information_for_work_request(id, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str id: Work Request Guid (required)
        :return: list[Assetic3IntegrationRepresentationsSupportingInformation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.work_request_get_supporting_information_for_work_request_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.work_request_get_supporting_information_for_work_request_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def work_request_get_supporting_information_for_work_request_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get supporting information history as a list by providing work request guid  # noqa: E501

        Sample request: <br /><pre>   /api/v2/workrequest/592325B7-A10E-E711-80BB-005056947278/supportinginfo      </pre>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_get_supporting_information_for_work_request_with_http_info(id, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str id: Work Request Guid (required)
        :return: list[Assetic3IntegrationRepresentationsSupportingInformation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method work_request_get_supporting_information_for_work_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `work_request_get_supporting_information_for_work_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workrequest/{id}/supportinginfo', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Assetic3IntegrationRepresentationsSupportingInformation]',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def work_request_get_work_request_type(self, **kwargs):  # noqa: E501
        """Get specific work request type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_get_work_request_type(async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param list[str] request_params_sorts:
        :param list[str] request_params_filters:
        :param int request_params_page:
        :param int request_params_page_size:
        :return: Assetic3IntegrationRepresentationsWorkRequestTypeList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.work_request_get_work_request_type_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.work_request_get_work_request_type_with_http_info(**kwargs)  # noqa: E501
            return data

    def work_request_get_work_request_type_with_http_info(self, **kwargs):  # noqa: E501
        """Get specific work request type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_get_work_request_type_with_http_info(async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param list[str] request_params_sorts:
        :param list[str] request_params_filters:
        :param int request_params_page:
        :param int request_params_page_size:
        :return: Assetic3IntegrationRepresentationsWorkRequestTypeList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_params_sorts', 'request_params_filters', 'request_params_page', 'request_params_page_size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method work_request_get_work_request_type" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_params_sorts' in params:
            query_params.append(('requestParams.sorts', params['request_params_sorts']))  # noqa: E501
            collection_formats['requestParams.sorts'] = 'multi'  # noqa: E501
        if 'request_params_filters' in params:
            query_params.append(('requestParams.filters', params['request_params_filters']))  # noqa: E501
            collection_formats['requestParams.filters'] = 'multi'  # noqa: E501
        if 'request_params_page' in params:
            query_params.append(('requestParams.page', params['request_params_page']))  # noqa: E501
        if 'request_params_page_size' in params:
            query_params.append(('requestParams.pageSize', params['request_params_page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/hal+json', 'application/hal+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workrequesttype', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Assetic3IntegrationRepresentationsWorkRequestTypeList',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def work_request_post(self, work_request, **kwargs):  # noqa: E501
        """Create new Work Request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_post(work_request, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param Assetic3IntegrationRepresentationsWorkRequest work_request: Work request details to be saved (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.work_request_post_with_http_info(work_request, **kwargs)  # noqa: E501
        else:
            (data) = self.work_request_post_with_http_info(work_request, **kwargs)  # noqa: E501
            return data

    def work_request_post_with_http_info(self, work_request, **kwargs):  # noqa: E501
        """Create new Work Request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.work_request_post_with_http_info(work_request, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param Assetic3IntegrationRepresentationsWorkRequest work_request: Work request details to be saved (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method work_request_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_request' is set
        if ('work_request' not in params or
                params['work_request'] is None):
            raise ValueError("Missing the required parameter `work_request` when calling `work_request_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'work_request' in params:
            body_params = params['work_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/x-www-form-urlencoded', 'application/hal+json', 'application/hal+xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workrequest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
