# -*- coding: utf-8 -*-

# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from inspect import signature, Signature, Parameter, isclass
from typing import Any, Optional

from ..utils import get_main_type_from_annotations_type
from ..base.address import Address
from ..base.exception import IconScoreException, IconTypeError, InvalidParamsException
from .icon_score_constant import ConstBitFlag, CONST_BIT_FLAG, CONST_INDEXED_ARGS_COUNT, STR_FALLBACK, BaseType
from ..base.type_converter import TypeConverter


class ScoreApiGenerator:

    __API_TYPE = 'type'
    __API_NAME = 'name'
    __API_INPUTS = 'inputs'
    __API_OUTPUTS = 'outputs'
    __API_PAYABLE = 'payable'
    __API_READONLY = 'readonly'
    __API_INPUTS_INDEXED = 'indexed'
    __API_INPUTS_DEFAULT = 'default'
    __API_PARAMS_ADDRESS = 'Address'
    __API_PARAMS_INDEXED = 'Indexed'
    __API_TYPE_FUNCTION = 'function'
    __API_TYPE_EVENT = 'eventlog'
    __API_TYPE_FALLBACK = STR_FALLBACK

    __API_TYPE_ON_INSTALL = 'on_install'
    __API_TYPE_ON_UPDATE = 'on_update'

    @staticmethod
    def generate(score_funcs: list) -> list:
        api = []
        ScoreApiGenerator.__generate_functions(api, score_funcs)
        ScoreApiGenerator.__generate_events(api, score_funcs)
        return api

    @staticmethod
    def check_on_deploy(score_funcs: list) -> None:
        for func in score_funcs:
            if func.__name__ == ScoreApiGenerator.__API_TYPE_ON_INSTALL or \
                    func.__name__ == ScoreApiGenerator.__API_TYPE_ON_UPDATE:
                ScoreApiGenerator.__check_on_deploy_function(signature(func))

    @staticmethod
    def __check_on_deploy_function(sig_info: 'Signature') -> None:
        params = dict(sig_info.parameters)
        for param_name, param in params.items():
            if param_name == 'self' or param_name == 'cls':
                continue
            if param.kind != Parameter.VAR_KEYWORD:
                ScoreApiGenerator.__generate_inputs(dict(sig_info.parameters))

    @staticmethod
    def __generate_functions(src: list, score_funcs: list) -> None:

        for func in score_funcs:
            const_bit_flag = getattr(func, CONST_BIT_FLAG, 0)
            is_readonly = const_bit_flag & ConstBitFlag.ReadOnly == ConstBitFlag.ReadOnly
            is_payable = const_bit_flag & ConstBitFlag.Payable == ConstBitFlag.Payable

            try:
                if const_bit_flag & ConstBitFlag.External and func.__name__ != STR_FALLBACK:
                    src.append(ScoreApiGenerator.__generate_normal_function(
                        func.__name__, is_readonly, is_payable, signature(func)))
                elif func.__name__ == ScoreApiGenerator.__API_TYPE_FALLBACK:
                    src.append(ScoreApiGenerator.__generate_fallback_function(
                            func.__name__, is_payable, signature(func)))
            except IconTypeError as e:
                raise IconScoreException(f"{e.message} at {func.__name__}")

    @staticmethod
    def __generate_normal_function(func_name: str, is_readonly: bool, is_payable: bool, sig_info: 'Signature') -> dict:
        info = dict()

        info[ScoreApiGenerator.__API_TYPE] = \
            ScoreApiGenerator.__API_TYPE_FUNCTION
        info[ScoreApiGenerator.__API_NAME] = func_name
        info[ScoreApiGenerator.__API_INPUTS] = \
            ScoreApiGenerator.__generate_inputs(dict(sig_info.parameters))
        info[ScoreApiGenerator.__API_OUTPUTS] = \
            ScoreApiGenerator.__generate_output(
                sig_info.return_annotation, is_readonly)

        if is_readonly:
            info[ScoreApiGenerator.__API_READONLY] = is_readonly
        if is_payable:
            info[ScoreApiGenerator.__API_PAYABLE] = is_payable

        return info

    @staticmethod
    def __generate_fallback_function(func_name: str, is_payable: bool, sig_info: 'Signature') -> dict:
        info = dict()
        info[ScoreApiGenerator.__API_TYPE] = ScoreApiGenerator.__API_TYPE_FALLBACK
        info[ScoreApiGenerator.__API_NAME] = func_name
        info[ScoreApiGenerator.__API_INPUTS] = ScoreApiGenerator.__generate_inputs(dict(sig_info.parameters))

        if is_payable:
            info[ScoreApiGenerator.__API_PAYABLE] = is_payable

        return info

    @staticmethod
    def __generate_events(src: list, score_funcs: list) -> None:

        event_funcs = {func.__name__: signature(func) for func in score_funcs
                       if getattr(func, CONST_BIT_FLAG, 0) & ConstBitFlag.EventLog}

        indexed_args_counts = {func.__name__: getattr(func, CONST_INDEXED_ARGS_COUNT, 0)
                               for func in score_funcs
                               if getattr(func, CONST_INDEXED_ARGS_COUNT, 0)}

        for func_name, event in event_funcs.items():
            index_args_count = indexed_args_counts.get(func_name, 0)
            src.append(ScoreApiGenerator.__generate_event(func_name, event, index_args_count))

    @staticmethod
    def __generate_event(func_name: str, sig_info: 'Signature', index_args_count: int) -> dict:
        info = dict()
        info[ScoreApiGenerator.__API_TYPE] = ScoreApiGenerator.__API_TYPE_EVENT
        info[ScoreApiGenerator.__API_NAME] = func_name
        info[ScoreApiGenerator.__API_INPUTS] = \
            ScoreApiGenerator.__generate_inputs(dict(sig_info.parameters), index_args_count)
        return info

    @staticmethod
    def __generate_output(params_type: Any, is_readonly: bool) -> list:
        info_list = []

        if not is_readonly:
            return info_list

        if params_type is Signature.empty:
            raise IconTypeError(
                f"'Returning type should be declared in read-only functions")

        main_type = get_main_type_from_annotations_type(params_type)
        main_type = ScoreApiGenerator.__convert_str_to_type(main_type)

        # At first, finds if the type is a 'list' or a 'dict'
        # if not, finds a base type
        find = (t for t in [list, dict]
                if isclass(main_type) and issubclass(main_type, t))
        api_type = next(find, None)
        if api_type is None:
            api_type = ScoreApiGenerator.__find_base_super_type(main_type)
        if api_type is None:
            raise IconTypeError(f"'Unsupported type for '{params_type}'")

        info = dict()
        info[ScoreApiGenerator.__API_TYPE] = api_type.__name__
        info_list.append(info)
        return info_list

    @staticmethod
    def __convert_str_to_type(params_type: Any) -> Any:
        if not isinstance(params_type, str):
            return params_type

        if params_type == 'Address':
            return Address
        else:
            return params_type

    @staticmethod
    def __generate_inputs(params: dict, index_args_count: int = 0) -> list:
        tmp_list = []
        args_index = 0
        for param_name, param in params.items():
            if param_name == 'self' or param_name == 'cls':
                continue
            is_indexed = args_index < index_args_count
            args_index += 1
            ScoreApiGenerator.__generate_input(tmp_list, param, is_indexed)
        return tmp_list

    @staticmethod
    def __generate_input(src: list, param: 'Parameter', is_indexed: bool):
        # If there's no hint of argument in the function declaration,
        # raise an exception
        if param.annotation is Parameter.empty:
            raise IconTypeError(f"Missing argument hint for '{param.name}'")

        main_type = get_main_type_from_annotations_type(param.annotation)
        main_type = ScoreApiGenerator.__convert_str_to_type(main_type)
        api_type = ScoreApiGenerator.__find_base_super_type(main_type)
        if api_type is None:
            raise IconTypeError(
                f"'Unsupported type for '{param.name}: {param.annotation}'")
        info = dict()
        info[ScoreApiGenerator.__API_NAME] = param.name
        info[ScoreApiGenerator.__API_TYPE] = api_type.__name__
        if is_indexed:
            info[ScoreApiGenerator.__API_INPUTS_INDEXED] = is_indexed
        if param.default is not Parameter.empty:
            if param.default is not None and not isinstance(param.default, main_type):
                raise InvalidParamsException(f'default params type mismatch. value: {param.default} type: {main_type}')
            info[ScoreApiGenerator.__API_INPUTS_DEFAULT] = TypeConverter.convert_type_reverse(param.default)
        src.append(info)

    @staticmethod
    def __find_base_super_type(t: type) -> Optional[type]:
        """
        Finds a base type of the input and returns it if any
        :param t: target
        :return: base_super_type
        """
        find = (base_type for base_type in BaseType.__constraints__
                if isclass(t) and issubclass(t, base_type))
        return next(find, None)
