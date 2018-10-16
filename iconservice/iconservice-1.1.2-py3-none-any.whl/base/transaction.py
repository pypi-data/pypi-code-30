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

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .address import Address


class Transaction(object):
    """Contains transaction info
    """

    def __init__(self,
                 tx_hash: Optional[bytes] = None,
                 index: int = 0,
                 origin: Optional['Address'] = None,
                 timestamp: int = None,
                 nonce: int = None) -> None:
        """Transaction class for icon score context
        """
        self._hash = tx_hash
        self._index = index
        self._origin = origin
        self._timestamp = timestamp
        self._nonce = nonce

    @property
    def origin(self) -> 'Address':
        """transaction creator
        """
        return self._origin

    @property
    def index(self) -> int:
        """tx index in a block
        """
        return self._index

    @property
    def hash(self) -> bytes:
        """transaction hash
        """
        return self._hash

    @property
    def timestamp(self) -> int:
        """timestamp of a transaction request
        This is NOT a block timestamp
        """
        return self._timestamp

    @property
    def nonce(self) -> int:
        """nonce of a transaction request
        """
        return self._nonce

