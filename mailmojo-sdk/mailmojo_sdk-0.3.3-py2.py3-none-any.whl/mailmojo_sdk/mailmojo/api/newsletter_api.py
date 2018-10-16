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


class NewsletterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_newsletter(self, **kwargs):  # noqa: E501
        """Create a newsletter draft.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_newsletter(async=True)
        >>> result = thread.get()

        :param async bool
        :param NewsletterCreation config:
        :return: Newsletter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_newsletter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_newsletter_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_newsletter_with_http_info(self, **kwargs):  # noqa: E501
        """Create a newsletter draft.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_newsletter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param NewsletterCreation config:
        :return: Newsletter
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_newsletter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'config' in params:
            body_params = params['config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/newsletters/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Newsletter',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_newsletter_by_id(self, newsletter_id, **kwargs):  # noqa: E501
        """Retrieve a newsletter by id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_newsletter_by_id(newsletter_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int newsletter_id: ID of the newsletter to retrieve. (required)
        :return: Newsletter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_newsletter_by_id_with_http_info(newsletter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_newsletter_by_id_with_http_info(newsletter_id, **kwargs)  # noqa: E501
            return data

    def get_newsletter_by_id_with_http_info(self, newsletter_id, **kwargs):  # noqa: E501
        """Retrieve a newsletter by id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_newsletter_by_id_with_http_info(newsletter_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int newsletter_id: ID of the newsletter to retrieve. (required)
        :return: Newsletter
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['newsletter_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_newsletter_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'newsletter_id' is set
        if ('newsletter_id' not in params or
                params['newsletter_id'] is None):
            raise ValueError("Missing the required parameter `newsletter_id` when calling `get_newsletter_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'newsletter_id' in params:
            path_params['newsletter_id'] = params['newsletter_id']  # noqa: E501

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
            '/newsletters/{newsletter_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Newsletter',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_newsletters(self, **kwargs):  # noqa: E501
        """Retrieve all newsletters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_newsletters(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: The current page of items (1 indexed).
        :param int per_page: The number of items returned per page.
        :return: PaginatedResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_newsletters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_newsletters_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_newsletters_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all newsletters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_newsletters_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: The current page of items (1 indexed).
        :param int per_page: The number of items returned per page.
        :return: PaginatedResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_newsletters" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

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
            '/newsletters/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_newsletter(self, newsletter_id, **kwargs):  # noqa: E501
        """Send a newsletter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_newsletter(newsletter_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int newsletter_id: ID of the newsletter to retrieve. (required)
        :param NewsletterSend config:
        :return: Newsletter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_newsletter_with_http_info(newsletter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.send_newsletter_with_http_info(newsletter_id, **kwargs)  # noqa: E501
            return data

    def send_newsletter_with_http_info(self, newsletter_id, **kwargs):  # noqa: E501
        """Send a newsletter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_newsletter_with_http_info(newsletter_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int newsletter_id: ID of the newsletter to retrieve. (required)
        :param NewsletterSend config:
        :return: Newsletter
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['newsletter_id', 'config']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_newsletter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'newsletter_id' is set
        if ('newsletter_id' not in params or
                params['newsletter_id'] is None):
            raise ValueError("Missing the required parameter `newsletter_id` when calling `send_newsletter`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'newsletter_id' in params:
            path_params['newsletter_id'] = params['newsletter_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'config' in params:
            body_params = params['config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/newsletters/{newsletter_id}/send/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Newsletter',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_newsletter(self, newsletter_id, **kwargs):  # noqa: E501
        """Send a test newsletter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_newsletter(newsletter_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int newsletter_id: ID of the newsletter to retrieve. (required)
        :param NewsletterSendTest config:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.test_newsletter_with_http_info(newsletter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.test_newsletter_with_http_info(newsletter_id, **kwargs)  # noqa: E501
            return data

    def test_newsletter_with_http_info(self, newsletter_id, **kwargs):  # noqa: E501
        """Send a test newsletter.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.test_newsletter_with_http_info(newsletter_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int newsletter_id: ID of the newsletter to retrieve. (required)
        :param NewsletterSendTest config:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['newsletter_id', 'config']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_newsletter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'newsletter_id' is set
        if ('newsletter_id' not in params or
                params['newsletter_id'] is None):
            raise ValueError("Missing the required parameter `newsletter_id` when calling `test_newsletter`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'newsletter_id' in params:
            path_params['newsletter_id'] = params['newsletter_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'config' in params:
            body_params = params['config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mailmojo_auth']  # noqa: E501

        return self.api_client.call_api(
            '/newsletters/{newsletter_id}/send_test/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
