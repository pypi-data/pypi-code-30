#!/usr/bin/env python

# Copyright (c) 2018, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import collections
import numbers

import awkward.array.base
import awkward.type
import awkward.util

class MaskedArray(awkward.array.base.AwkwardArrayWithContent):
    ### WTF were the designers of numpy.ma thinking?
    # @staticmethod
    # def is_masked(x):
    #     return awkward.util.numpy.ma.is_masked(x)
    # masked = awkward.util.numpy.ma.masked

    @staticmethod
    def is_masked(x):
        if isinstance(x, MaskedArray):
            # numpy.ma.is_masked(array) if any element is masked
            if x.maskedwhen:
                return x.mask.any()
            else:
                return not x.mask.all()
        else:
            # numpy.ma.is_masked(x) if x represents a masked constant
            return x is MaskedArray.masked
    masked = None

    def __init__(self, mask, content, maskedwhen=True):
        self.mask = mask
        self.content = content
        self.maskedwhen = maskedwhen

    def copy(self, mask=None, content=None, maskedwhen=None):
        out = self.__class__.__new__(self.__class__)
        out._mask = self._mask
        out._content = self._content
        out._maskedwhen = self._maskedwhen
        if mask is not None:
            out._mask = mask
        if content is not None:
            out._content = content
        if maskedwhen is not None:
            out._maskedwhen = maskedwhen
        return out

    def deepcopy(self, mask=None, content=None):
        out = self.copy(mask=mask, content=content)
        out._mask = awkward.util.deepcopy(out._mask)
        out._content = awkward.util.deepcopy(out._content)
        return out

    def _mine(self, overrides):
        mine = {}
        mine["maskedwhen"] = overrides.pop("maskedwhen", self._maskedwhen)
        return mine

    def empty_like(self, **overrides):
        mine = self._mine(overrides)
        if isinstance(self._content, awkward.util.numpy.ndarray):
            return self.copy(content=awkward.util.numpy.empty_like(self._content), **mine)
        else:
            return self.copy(content=self._content.empty_like(**overrides), **mine)

    def zeros_like(self, **overrides):
        mine = self._mine(overrides)
        if isinstance(self._content, awkward.util.numpy.ndarray):
            return self.copy(content=awkward.util.numpy.zeros_like(self._content), **mine)
        else:
            return self.copy(content=self._content.zeros_like(**overrides), **mine)

    def ones_like(self, **overrides):
        mine = self._mine(overrides)
        if isinstance(self._content, awkward.util.numpy.ndarray):
            return self.copy(content=awkward.util.numpy.ones_like(self._content), **mine)
        else:
            return self.copy(content=self._content.ones_like(**overrides), **mine)

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, value):
        value = awkward.util.toarray(value, awkward.util.MASKTYPE, awkward.util.numpy.ndarray)
        if len(value.shape) != 1:
            raise ValueError("mask must have 1-dimensional shape")
        if not issubclass(value.dtype.type, (awkward.util.numpy.bool_, awkward.util.numpy.bool)):
            value = (value != 0)
        self._mask = value

    def boolmask(self, maskedwhen=True):
        if maskedwhen == self._maskedwhen:
            return self._mask
        else:
            return awkward.util.numpy.logical_not(self._mask)

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = awkward.util.toarray(value, awkward.util.DEFAULTTYPE)

    @property
    def maskedwhen(self):
        return self._maskedwhen

    @maskedwhen.setter
    def maskedwhen(self, value):
        self._maskedwhen = bool(value)

    @property
    def dtype(self):
        return self._content.dtype

    def __len__(self):
        return len(self._mask)

    @property
    def shape(self):
        return (len(self._mask),) + self._content.shape[1:]

    @property
    def type(self):
        return awkward.type.ArrayType(len(self._mask), awkward.type.fromarray(self._content).to)

    def _valid(self):
        if len(self._mask) > len(self._content):
            raise ValueError("mask length ({0}) must be the same as (or shorter than) the content length ({1})".format(len(self._mask), len(self._content)))

    def __iter__(self):
        self._valid()

        mask = self._mask
        lenmask = len(mask)
        content = self._content
        maskedwhen = self._maskedwhen
        masked = self.masked

        i = 0
        while i < lenmask:
            if mask[i] == maskedwhen:
                yield masked
            else:
                yield content[i]
            i += 1

    def __getitem__(self, where):
        self._valid()

        if awkward.util.isstringslice(where):
            return self.copy(content=self._content[where])

        if isinstance(where, tuple) and len(where) == 0:
            return self
        if not isinstance(where, tuple):
            where = (where,)
        head, tail = where[0], where[1:]

        if isinstance(head, awkward.util.integer):
            if self._mask[head] == self._maskedwhen:
                if tail != ():
                    raise ValueError("masked element ({0}) is not subscriptable".format(self.masked))
                return self.masked
            else:
                return self._content[:len(self._mask)][(head,) + tail]

        else:
            mask = self._mask[head]
            if tail != () and ((self._maskedwhen and mask.any()) or (not self._maskedwhen and not mask.all())):
                raise ValueError("masked element ({0}) is not subscriptable".format(self.masked))
            else:
                return self.copy(mask=mask, content=self._content[:len(self._mask)][(head,) + tail])
        
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        import awkward.array.objects

        if method != "__call__":
            return NotImplemented

        tokeep = None
        for x in inputs:
            if isinstance(x, MaskedArray):
                x._valid()
                if tokeep is None:
                    tokeep = x.boolmask(maskedwhen=False)
                else:
                    tokeep = tokeep & x.boolmask(maskedwhen=False)

        assert tokeep is not None

        inputs = list(inputs)
        for i in range(len(inputs)):
            if isinstance(inputs[i], IndexedMaskedArray):
                inputs[i] = inputs[i]._content[inputs[i]._mask[tokeep]]
            elif isinstance(inputs[i], MaskedArray):
                inputs[i] = inputs[i]._content[tokeep]
            elif isinstance(inputs[i], (awkward.util.numpy.ndarray, awkward.array.base.AwkwardArray)):
                inputs[i] = inputs[i][tokeep]
            else:
                try:
                    for first in inputs[i]:
                        break
                except TypeError:
                    pass
                else:
                    inputs[i] = awkward.util.numpy.array(inputs[i], copy=False)[tokeep]

        # compute only the non-masked elements
        result = getattr(ufunc, method)(*inputs, **kwargs)

        # put the masked out values back
        index = awkward.util.numpy.full(len(tokeep), -1, dtype=awkward.util.INDEXTYPE)
        index[tokeep] = awkward.util.numpy.arange(awkward.util.numpy.count_nonzero(tokeep))

        if isinstance(result, tuple):
            return tuple(awkward.array.objects.Methods.maybemixin(type(x), IndexedMaskedArray)(index, x, maskedwhen=-1) if isinstance(x, (awkward.util.numpy.ndarray, awkward.array.base.AwkwardBase)) else x for x in result)
        elif method == "at":
            return None
        else:
            return awkward.array.objects.Methods.maybemixin(type(result), IndexedMaskedArray)(index, result, maskedwhen=-1)

    def indexed(self):
        maskindex = awkward.util.numpy.arange(len(self), dtype=awkward.util.INDEXTYPE)
        maskindex[self.boolmask(maskedwhen=True)] = -1
        return IndexedMaskedArray(maskindex, self._content, maskedwhen=-1)

    def any(self):
        return self._content[self.boolmask(maskedwhen=False)].any()

    def all(self):
        return self._content[self.boolmask(maskedwhen=False)].all()

    @classmethod
    def concat(cls, first, *rest):
        raise NotImplementedError

    def pandas(self):
        raise NotImplementedError

class BitMaskedArray(MaskedArray):
    def __init__(self, mask, content, maskedwhen=True, lsborder=False):
        super(BitMaskedArray, self).__init__(mask, content, maskedwhen=maskedwhen)
        self.lsborder = lsborder

    @classmethod
    def fromboolmask(cls, mask, content, maskedwhen=True, lsborder=False):
        return BitMaskedArray(BitMaskedArray.bool2bit(mask, lsborder=lsborder), content, maskedwhen=maskedwhen, lsborder=lsborder)
        
    def copy(self, mask=None, content=None, maskedwhen=None, lsborder=None):
        out = super(BitMaskedArray, self).copy(mask=mask, content=content, maskedwhen=maskedwhen)
        out._lsborder = self._lsborder
        if lsborder is not None:
            out._lsborder = lsborder
        return out

    def _mine(self, overrides):
        mine = {}
        mine["maskedwhen"] = overrides.pop("maskedwhen", self._maskedwhen)
        mine["lsborder"] = overrides.pop("lsborder", self._lsborder)
        return mine

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, value):
        value = awkward.util.toarray(value, awkward.util.BITMASKTYPE, awkward.util.numpy.ndarray)
        if len(value.shape) != 1:
            raise ValueError("mask must have 1-dimensional shape")
        self._mask = value.view(awkward.util.BITMASKTYPE)

    def __len__(self):
        return len(self._content)

    @property
    def shape(self):
        return self._content.shape

    @staticmethod
    def _ceildiv8(x):
        return -(-x >> 3)   # this is int(math.ceil(x / 8))

    @staticmethod
    def bit2bool(bitmask, lsborder=False):
        out = awkward.util.numpy.unpackbits(bitmask)
        if lsborder:
            out = out.reshape(-1, 8)[:,::-1].reshape(-1)
        return out.view(awkward.util.MASKTYPE)
        
    @staticmethod
    def bool2bit(boolmask, lsborder=False):
        boolmask = awkward.util.toarray(boolmask, awkward.util.MASKTYPE, awkward.util.numpy.ndarray)
        if len(boolmask.shape) != 1:
            raise ValueError("boolmask must have 1-dimensional shape")
        if not issubclass(boolmask.dtype.type, (awkward.util.numpy.bool_, awkward.util.numpy.bool)):
            boolmask = (boolmask != 0)

        if lsborder:
            # maybe pad the length for reshape
            length = BitMaskedArray._ceildiv8(len(boolmask)) * 8
            if length != len(boolmask):
                out = awkward.util.numpy.empty(length, dtype=boolmask.dtype)
                out[:len(boolmask)] = boolmask
            else:
                out = boolmask

            # reverse the order in groups of 8
            out = out.reshape(-1, 8)[:,::-1].reshape(-1)

        else:
            # numpy.packbits encodes as msb (most significant bit); already in the right order
            out = boolmask

        return awkward.util.numpy.packbits(out)

    def boolmask(self, maskedwhen=True):
        if maskedwhen == self._maskedwhen:
            bitmask = self._mask
        else:
            bitmask = awkward.util.numpy.bitwise_not(self._mask)
        return self.bit2bool(bitmask, lsborder=self._lsborder)[:len(self._content)]

    @property
    def lsborder(self):
        return self._lsborder

    @lsborder.setter
    def lsborder(self, value):
        self._lsborder = bool(value)

    def _valid(self):
        if len(self._mask) != self._ceildiv8(len(self._content)):
            raise ValueError("mask length ({0}) must be equal to ceil(content length / 8) ({1})".format(len(self._mask), self._ceildiv8(len(self._content))))

    def __iter__(self):
        self._valid()

        one = awkward.util.numpy.uint8(1)
        zero = awkward.util.numpy.uint8(0)
        mask = self._mask
        content = self._content
        lencontent = len(content)
        maskedwhen = self._maskedwhen
        masked = self.masked

        if self._lsborder:
            byte = i = 0
            bit = start = awkward.util.numpy.uint8(1)
            while i < lencontent:
                if ((mask[byte] & bit) != 0) == self._maskedwhen:
                    yield masked
                else:
                    yield content[i]
                bit <<= one
                if bit == zero:
                    bit = start
                    byte += 1
                i += 1

        else:
            byte = i = 0
            bit = start = awkward.util.numpy.uint8(128)
            while i < lencontent:
                if ((mask[byte] & bit) != 0) == self._maskedwhen:
                    yield masked
                else:
                    yield content[i]
                bit >>= one
                if bit == zero:
                    bit = start
                    byte += 1
                i += 1

    def _maskat(self, where):
        bytepos = awkward.util.numpy.right_shift(where, 3)    # where // 8
        bitpos  = where - 8*bytepos                           # where % 8

        if self._lsborder:
            bitmask = awkward.util.numpy.left_shift(1, bitpos)
        else:
            bitmask = awkward.util.numpy.right_shift(128, bitpos)

        if isinstance(bitmask, awkward.util.numpy.ndarray):
            bitmask = bitmask.astype(awkward.util.BITMASKTYPE)
        else:
            bitmask = awkward.util.BITMASKTYPE.type(bitmask)

        return bytepos, bitmask

    def _maskwhere(self, where):
        if isinstance(where, awkward.util.integer):
            bytepos, bitmask = self._maskat(where)
            return awkward.util.numpy.bitwise_and(self._mask[bytepos], bitmask) != 0

        elif isinstance(where, slice):
            # assumes a small slice; for a big slice, it could be faster to unpack the whole mask
            return self._maskwhere(awkward.util.numpy.arange(*where.indices(len(self._content))))

        else:
            where = awkward.util.numpy.array(where, copy=False)
            if len(where.shape) == 1 and issubclass(where.dtype.type, awkward.util.numpy.integer):
                byteposes, bitmasks = self._maskat(where)
                awkward.util.numpy.bitwise_and(bitmasks, self._mask[byteposes], bitmasks)
                return bitmasks.astype(awkward.util.numpy.bool_)
        
            elif len(where.shape) == 1 and issubclass(where.dtype.type, (awkward.util.numpy.bool, awkward.util.numpy.bool_)):
                # scales with the size of the mask anyway, so go ahead and unpack the whole mask
                unpacked = awkward.util.numpy.unpackbits(self._mask).view(awkward.util.MASKTYPE)

                if self._lsborder:
                    unpacked = unpacked.reshape(-1, 8)[:,::-1].reshape(-1)[:len(where)]
                else:
                    unpacked = unpacked[:len(where)]

                return unpacked[where]

            else:
                raise TypeError("cannot interpret shape {0}, dtype {1} as a fancy index or mask".format(where.shape, where.dtype))

    def __getitem__(self, where):
        self._valid()

        if awkward.util.isstringslice(where):
            return self.copy(content=self._content[where])

        if isinstance(where, tuple) and len(where) == 0:
            return self
        if not isinstance(where, tuple):
            where = (where,)
        head, tail = where[0], where[1:]

        if isinstance(head, awkward.util.integer):
            if self._maskwhere(head) == self._maskedwhen:
                if tail != ():
                    raise ValueError("masked element ({0}) is not subscriptable".format(self.masked))
                return self.masked
            else:
                return self._content[(head,) + tail]

        else:
            mask = self._maskwhere(head)
            if tail != () and ((self._maskedwhen and mask.any()) or (not self._maskedwhen and not mask.all())):
                raise ValueError("masked element ({0}) is not subscriptable".format(self.masked))
            else:
                return self.copy(mask=self.bool2bit(mask, lsborder=self._lsborder), content=self._content[(head,) + tail], lsborder=self._lsborder)

    @classmethod
    def concat(cls, first, *rest):
        raise NotImplementedError

    def pandas(self):
        raise NotImplementedError

class IndexedMaskedArray(MaskedArray):
    def __init__(self, mask, content, maskedwhen=-1):
        super(IndexedMaskedArray, self).__init__(mask, content, maskedwhen=maskedwhen)
        self._isvalid = False

    def copy(self, mask=None, content=None, maskedwhen=None):
        out = self.__class__.__new__(self.__class__)
        out._mask = self._mask
        out._content = self._content
        out._maskedwhen = self._maskedwhen
        out._isvalid = self._isvalid
        if mask is not None:
            out._mask = mask
        if content is not None:
            out._content = content
        if maskedwhen is not None:
            out._maskedwhen = maskedwhen
        return out

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, value):
        value = awkward.util.toarray(value, awkward.util.INDEXTYPE, awkward.util.numpy.ndarray)
        if not issubclass(value.dtype.type, awkward.util.numpy.integer):
            raise TypeError("starts must have integer dtype")
        if len(value.shape) != 1:
            raise ValueError("mask must have 1-dimensional shape")
        self._mask = value
        self._isvalid = False

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = awkward.util.toarray(value, awkward.util.DEFAULTTYPE)
        self._isvalid = False

    @property
    def maskedwhen(self):
        return self._maskedwhen

    @maskedwhen.setter
    def maskedwhen(self, value):
        if not isinstance(value, awkward.util.integer):
            raise TypeError("maskedwhen must be an integer for IndexedMaskedArray")
        self._maskedwhen = value

    def boolmask(self, maskedwhen=True):
        if maskedwhen:
            return self._mask == self._maskedwhen
        else:
            return self._mask != self._maskedwhen

    def _valid(self):
        if not self._isvalid:
            if len(self._mask) != 0:
                if self._mask.max() > len(self._content):
                    raise ValueError("maximum mask-index ({0}) is beyond the length of the content ({1})".format(self._mask.max(), len(self._content)))
                if (self._mask[self._mask != self._maskedwhen] < 0).any():
                    raise ValueError("mask-index has negative values (other than maskedwhen)")
            self._isvalid = True

    def __iter__(self):
        self._valid()

        mask = self._mask
        lenmask = len(mask)
        content = self._content
        maskedwhen = self._maskedwhen
        masked = self.masked

        i = 0
        while i < lenmask:
            maskindex = mask[i]
            if maskindex == maskedwhen:
                yield masked
            else:
                yield content[maskindex]
            i += 1

    def __getitem__(self, where):
        self._valid()

        if awkward.util.isstringslice(where):
            return self.copy(content=self._content[where])

        if isinstance(where, tuple) and len(where) == 0:
            return self
        if not isinstance(where, tuple):
            where = (where,)
        head, tail = where[0], where[1:]

        if isinstance(head, awkward.util.integer):
            maskindex = self._mask[head]
            if maskindex == self._maskedwhen:
                if tail != ():
                    raise ValueError("masked element ({0}) is not subscriptable".format(self.masked))
                return self.masked
            else:
                return self._content[(maskindex,) + tail]

        else:
            maskindex = self._mask[head]
            if tail != () and (maskindex == self._maskedwhen).any():
                raise ValueError("masked element ({0}) is not subscriptable".format(self.masked))
            else:
                return self.copy(mask=maskindex)

    def indexed(self):
        return self

    @classmethod
    def concat(cls, first, *rest):
        raise NotImplementedError

    def pandas(self):
        raise NotImplementedError
