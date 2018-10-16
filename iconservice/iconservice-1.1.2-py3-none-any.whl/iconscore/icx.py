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

from typing import TYPE_CHECKING

from ..base.address import Address, GOVERNANCE_SCORE_ADDRESS

if TYPE_CHECKING:
    from .icon_score_context import IconScoreContext


class Icx(object):
    """Class for handling ICX coin transfer
    """

    def __init__(self, context: 'IconScoreContext', address: 'Address') -> None:
        """Constructor
        """
        self._context = context
        self._address = address

    def transfer(self, addr_to: 'Address', amount: int) -> None:
        """transfer the amount of icx to the given 'addr_to'
        If failed, an exception will be raised

        :param addr_to: receiver address
        :param amount: the amount of icx to transfer
        """
        self._context.internal_call.icx_transfer_call(self._address, addr_to, amount)

    def send(self, addr_to: 'Address', amount: int) -> bool:
        """transfer the amount of icx to the given 'addr_to'

        :param addr_to: receiver address
        :param amount: the amount of icx to transfer
        :return: True(success) False(failed)
        """
        try:
            self.transfer(addr_to, amount)
            if not addr_to.is_contract and self._is_icx_send_defective():
                return False
            return True
        except:
            return False

    def get_balance(self, address: 'Address') -> int:
        return self._context.internal_call.get_icx_balance(address)

    # noinspection PyBroadException
    def _is_icx_send_defective(self) -> bool:
        try:
            governance_score = self._context.get_icon_score(GOVERNANCE_SCORE_ADDRESS)
            if governance_score is not None:
                if hasattr(governance_score, 'getVersion'):
                    version = governance_score.getVersion()
                    return version == '0.0.2'
        except BaseException:
            pass

        return False
