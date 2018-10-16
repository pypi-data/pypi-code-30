# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the NiBabel package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
''' Test Analyze headers

See test_wrapstruct.py for tests of the wrapped structarr-ness of the Analyze
header
'''

import os
import re
import logging
import pickle
import itertools

import numpy as np

from six import BytesIO, StringIO
from ..spatialimages import (HeaderDataError, HeaderTypeError,
                             supported_np_types)
from ..analyze import AnalyzeHeader, AnalyzeImage
from ..nifti1 import Nifti1Header
from ..loadsave import read_img_data
from .. import imageglobals
from ..casting import as_int
from ..tmpdirs import InTemporaryDirectory
from ..arraywriters import WriterError

from nose.tools import (assert_equal, assert_not_equal, assert_true,
                        assert_false, assert_raises)

from numpy.testing import (assert_array_equal, assert_array_almost_equal)

from ..testing import (assert_equal, assert_not_equal, assert_true,
                       assert_false, assert_raises, data_path,
                       suppress_warnings, assert_dt_equal)

from .test_wrapstruct import _TestLabeledWrapStruct
from . import test_spatialimages as tsi
from .test_helpers import bytesio_filemap, bytesio_round_trip

header_file = os.path.join(data_path, 'analyze.hdr')

PIXDIM0_MSG = 'pixdim[1,2,3] should be non-zero; setting 0 dims to 1'


def add_intp(supported_np_types):
    # Add intp, uintp to supported types as necessary
    supported_dtypes = [np.dtype(t) for t in supported_np_types]
    for np_type in (np.intp, np.uintp):
        if np.dtype(np_type) in supported_dtypes:
            supported_np_types.add(np_type)


class TestAnalyzeHeader(_TestLabeledWrapStruct):
    header_class = AnalyzeHeader
    example_file = header_file
    sizeof_hdr = AnalyzeHeader.sizeof_hdr
    supported_np_types = set((np.uint8,
                              np.int16,
                              np.int32,
                              np.float32,
                              np.float64,
                              np.complex64))
    add_intp(supported_np_types)

    def test_supported_types(self):
        hdr = self.header_class()
        assert_equal(self.supported_np_types,
                     supported_np_types(hdr))

    def get_bad_bb(self):
        # A value for the binary block that should raise an error
        # Completely zeros binary block (nearly) always (fairly) bad
        return b'\x00' * self.header_class.template_dtype.itemsize

    def test_general_init(self):
        super(TestAnalyzeHeader, self).test_general_init()
        hdr = self.header_class()
        # an empty header has shape (0,) - like an empty array
        # (np.array([]))
        assert_equal(hdr.get_data_shape(), (0,))
        # The affine is always homogenous 3D regardless of shape. The
        # default affine will have -1 as the X zoom iff default_x_flip
        # is True (which it is by default). We have to be careful of the
        # translations though - these arise from SPM's use of the origin
        # field, and the center of the image.
        assert_array_equal(np.diag(hdr.get_base_affine()),
                           [-1, 1, 1, 1])
        # But zooms only go with number of dimensions
        assert_equal(hdr.get_zooms(), (1.0,))

    def test_header_size(self):
        assert_equal(self.header_class.template_dtype.itemsize, self.sizeof_hdr)

    def test_empty(self):
        hdr = self.header_class()
        assert_true(len(hdr.binaryblock) == self.sizeof_hdr)
        assert_true(hdr['sizeof_hdr'] == self.sizeof_hdr)
        assert_true(np.all(hdr['dim'][1:] == 1))
        assert_true(hdr['dim'][0] == 0)
        assert_true(np.all(hdr['pixdim'] == 1))
        assert_true(hdr['datatype'] == 16)  # float32
        assert_true(hdr['bitpix'] == 32)

    def _set_something_into_hdr(self, hdr):
        # Called from test_bytes test method.  Specific to the header data type
        with suppress_warnings():
            hdr.set_data_shape((1, 2, 3))

    def test_checks(self):
        # Test header checks
        hdr_t = self.header_class()
        # _dxer just returns the diagnostics as a string
        assert_equal(self._dxer(hdr_t), '')
        hdr = hdr_t.copy()
        hdr['sizeof_hdr'] = 1
        with suppress_warnings():
            assert_equal(self._dxer(hdr), 'sizeof_hdr should be ' +
                         str(self.sizeof_hdr))
        hdr = hdr_t.copy()
        hdr['datatype'] = 0
        assert_equal(self._dxer(hdr), 'data code 0 not supported\n'
                     'bitpix does not match datatype')
        hdr = hdr_t.copy()
        hdr['bitpix'] = 0
        assert_equal(self._dxer(hdr), 'bitpix does not match datatype')

    def test_pixdim_checks(self):
        hdr_t = self.header_class()
        for i in (1, 2, 3):
            hdr = hdr_t.copy()
            hdr['pixdim'][i] = -1
            assert_equal(self._dxer(hdr), 'pixdim[1,2,3] should be positive')

    def test_log_checks(self):
        # Test logging, fixing, errors for header checking
        HC = self.header_class
        # magic
        hdr = HC()
        with suppress_warnings():
            hdr['sizeof_hdr'] = 350  # severity 30
            fhdr, message, raiser = self.log_chk(hdr, 30)
        assert_equal(fhdr['sizeof_hdr'], self.sizeof_hdr)
        assert_equal(message,
                     'sizeof_hdr should be {0}; set sizeof_hdr to {0}'.format(
                         self.sizeof_hdr))
        assert_raises(*raiser)
        # RGB datatype does not raise error
        hdr = HC()
        hdr.set_data_dtype('RGB')
        fhdr, message, raiser = self.log_chk(hdr, 0)
        # datatype not recognized
        hdr = HC()
        hdr['datatype'] = -1  # severity 40
        with suppress_warnings():
            fhdr, message, raiser = self.log_chk(hdr, 40)
        assert_equal(message, 'data code -1 not recognized; '
                     'not attempting fix')

        assert_raises(*raiser)
        # datatype not supported
        hdr['datatype'] = 255  # severity 40
        fhdr, message, raiser = self.log_chk(hdr, 40)
        assert_equal(message, 'data code 255 not supported; '
                     'not attempting fix')
        assert_raises(*raiser)
        # bitpix
        hdr = HC()
        hdr['datatype'] = 16  # float32
        hdr['bitpix'] = 16  # severity 10
        fhdr, message, raiser = self.log_chk(hdr, 10)
        assert_equal(fhdr['bitpix'], 32)
        assert_equal(message, 'bitpix does not match datatype; '
                     'setting bitpix to match datatype')
        assert_raises(*raiser)

    def test_pixdim_log_checks(self):
        # pixdim positive
        HC = self.header_class
        hdr = HC()
        hdr['pixdim'][1] = -2  # severity 35
        fhdr, message, raiser = self.log_chk(hdr, 35)
        assert_equal(fhdr['pixdim'][1], 2)
        assert_equal(message, 'pixdim[1,2,3] should be positive; '
                     'setting to abs of pixdim values')
        assert_raises(*raiser)
        hdr = HC()
        hdr['pixdim'][1] = 0  # severity 30
        fhdr, message, raiser = self.log_chk(hdr, 30)
        assert_equal(fhdr['pixdim'][1], 1)
        assert_equal(message, PIXDIM0_MSG)
        assert_raises(*raiser)
        # both
        hdr = HC()
        hdr['pixdim'][1] = 0  # severity 30
        hdr['pixdim'][2] = -2  # severity 35
        fhdr, message, raiser = self.log_chk(hdr, 35)
        assert_equal(fhdr['pixdim'][1], 1)
        assert_equal(fhdr['pixdim'][2], 2)
        assert_equal(message, 'pixdim[1,2,3] should be '
                     'non-zero and pixdim[1,2,3] should '
                     'be positive; setting 0 dims to 1 '
                     'and setting to abs of pixdim values')
        assert_raises(*raiser)

    def test_no_scaling_fixes(self):
        # Check we do not fix slope or intercept
        #
        # We used to fix difficult-to-interpret slope and intercept values in
        # headers that support them.  Now we pass everything and let the
        # `get_slope_inter()` routine reinterpet diffireinterpet difficult
        # values.
        # Analyze doesn't support slope or intercept; the tests are here for
        # children of this class that do support them.
        HC = self.header_class
        if not HC.has_data_slope:
            return
        hdr = HC()
        has_inter = HC.has_data_intercept
        slopes = (1, 0, np.nan, np.inf, -np.inf)
        inters = (0, np.nan, np.inf, -np.inf) if has_inter else (0,)
        for slope, inter in itertools.product(slopes, inters):
            hdr['scl_slope'] = slope
            if has_inter:
                hdr['scl_inter'] = inter
            self.assert_no_log_err(hdr)

    def test_logger_error(self):
        # Check that we can reset the logger and error level
        HC = self.header_class
        hdr = HC()
        # Make a new logger
        str_io = StringIO()
        logger = logging.getLogger('test.logger')
        logger.addHandler(logging.StreamHandler(str_io))
        # Prepare a defect: bitpix not matching data type
        hdr['datatype'] = 16  # float32
        hdr['bitpix'] = 16  # severity 10
        logger.setLevel(10)
        log_cache = imageglobals.logger, imageglobals.error_level
        try:
            # Check log message appears in new logger
            imageglobals.logger = logger
            hdr.copy().check_fix()
            assert_equal(str_io.getvalue(),
                         'bitpix does not match datatype; '
                         'setting bitpix to match datatype\n')
            # Check that error_level in fact causes error to be raised
            imageglobals.error_level = 10
            assert_raises(HeaderDataError, hdr.copy().check_fix)
        finally:
            imageglobals.logger, imageglobals.error_level = log_cache

    def test_data_dtype(self):
        # check getting and setting of data type
        # codes / types supported by all binary headers
        all_supported_types = ((2, np.uint8),
                               (4, np.int16),
                               (8, np.int32),
                               (16, np.float32),
                               (32, np.complex64),
                               (64, np.float64),
                               (128, np.dtype([('R', 'u1'),
                                               ('G', 'u1'),
                                               ('B', 'u1')])))
        # and unsupported - here using some labels instead
        all_unsupported_types = (np.void, 'none', 'all', 0)

        def assert_set_dtype(dt_spec, np_dtype):
            hdr = self.header_class()
            hdr.set_data_dtype(dt_spec)
            assert_dt_equal(hdr.get_data_dtype(), np_dtype)
        # Test code, type known to be supported by all types
        for code, npt in all_supported_types:
            # Can set with code value
            assert_set_dtype(code, npt)
            # or numpy type
            assert_set_dtype(npt, npt)
            # or numpy dtype
            assert_set_dtype(np.dtype(npt), npt)
        # Test numerical types supported by this header type
        for npt in self.supported_np_types:
            # numpy type
            assert_set_dtype(npt, npt)
            # or numpy dtype
            assert_set_dtype(np.dtype(npt), npt)
            # or swapped numpy dtype
            assert_set_dtype(np.dtype(npt).newbyteorder(), npt)
            # or string dtype code
            assert_set_dtype(np.dtype(npt).str, npt)
            # or string dtype code without byteorder
            if np.dtype(npt).str[0] in '=|<>':
                assert_set_dtype(np.dtype(npt).str[1:], npt)
        # Test aliases to Python types
        assert_set_dtype(float, np.float64)  # float64 always supported
        np_sys_int = np.dtype(int).type  # int could be 32 or 64 bit
        if np_sys_int in self.supported_np_types:  # no int64 for Analyze
            assert_set_dtype(int, np_sys_int)
        hdr = self.header_class()
        for inp in all_unsupported_types:
            assert_raises(HeaderDataError, hdr.set_data_dtype, inp)

    def test_shapes(self):
        # Test that shape checks work
        hdr = self.header_class()
        for shape in ((2, 3, 4), (2, 3, 4, 5), (2, 3), (2,)):
            hdr.set_data_shape(shape)
            assert_equal(hdr.get_data_shape(), shape)
        # Check max works, but max+1 raises error
        dim_dtype = hdr.structarr['dim'].dtype
        # as_int for safety to deal with numpy 1.4.1 int conversion errors
        mx = as_int(np.iinfo(dim_dtype).max)
        shape = (mx,)
        hdr.set_data_shape(shape)
        assert_equal(hdr.get_data_shape(), shape)
        shape = (mx + 1,)
        assert_raises(HeaderDataError, hdr.set_data_shape, shape)
        # Lists or tuples or arrays will work for setting shape
        shape = (2, 3, 4)
        for constructor in (list, tuple, np.array):
            hdr.set_data_shape(constructor(shape))
            assert_equal(hdr.get_data_shape(), shape)

    def test_read_write_data(self):
        # Check reading and writing of data
        hdr = self.header_class()
        # Trying to read data from an empty header gives no data
        bytes = hdr.data_from_fileobj(BytesIO())
        assert_equal(len(bytes), 0)
        # Setting no data into an empty header results in - no data
        str_io = BytesIO()
        hdr.data_to_fileobj([], str_io)
        assert_equal(str_io.getvalue(), b'')
        # Setting more data then there should be gives an error
        assert_raises(HeaderDataError,
                      hdr.data_to_fileobj,
                      np.zeros(3),
                      str_io)
        # Test valid write
        hdr.set_data_shape((1, 2, 3))
        hdr.set_data_dtype(np.float32)
        S = BytesIO()
        data = np.arange(6, dtype=np.float64)
        # data have to be the right shape
        assert_raises(HeaderDataError, hdr.data_to_fileobj, data, S)
        data = data.reshape((1, 2, 3))
        # and size
        assert_raises(HeaderDataError, hdr.data_to_fileobj, data[:, :, :-1], S)
        assert_raises(HeaderDataError, hdr.data_to_fileobj, data[:, :-1, :], S)
        # OK if so
        hdr.data_to_fileobj(data, S)
        # Read it back
        data_back = hdr.data_from_fileobj(S)
        # Should be about the same
        assert_array_almost_equal(data, data_back)
        # but with the header dtype, not the data dtype
        assert_equal(hdr.get_data_dtype(), data_back.dtype)
        # this is with native endian, not so for swapped
        S2 = BytesIO()
        hdr2 = hdr.as_byteswapped()
        hdr2.set_data_dtype(np.float32)
        hdr2.set_data_shape((1, 2, 3))
        hdr2.data_to_fileobj(data, S2)
        data_back2 = hdr2.data_from_fileobj(S2)
        # Compares the same
        assert_array_almost_equal(data_back, data_back2)
        # Same dtype names
        assert_equal(data_back.dtype.name, data_back2.dtype.name)
        # But not the same endianness
        assert_not_equal(data.dtype.byteorder, data_back2.dtype.byteorder)
        # Try scaling down to integer
        hdr.set_data_dtype(np.uint8)
        S3 = BytesIO()
        # Analyze header cannot do scaling, so turn off scaling with
        # 'rescale=False'
        with np.errstate(invalid='ignore'):
            hdr.data_to_fileobj(data, S3, rescale=False)
        data_back = hdr.data_from_fileobj(S3)
        assert_array_almost_equal(data, data_back)
        # If the header can't do scaling, rescale raises an error
        if not hdr.has_data_slope:
            assert_raises(HeaderTypeError, hdr.data_to_fileobj, data, S3)
            assert_raises(HeaderTypeError, hdr.data_to_fileobj, data, S3,
                          rescale=True)
        # If not scaling we lose precision from rounding
        data = np.arange(6, dtype=np.float64).reshape((1, 2, 3)) + 0.5
        with np.errstate(invalid='ignore'):
            hdr.data_to_fileobj(data, S3, rescale=False)
        data_back = hdr.data_from_fileobj(S3)
        assert_false(np.allclose(data, data_back))
        # Test RGB image
        dtype = np.dtype([('R', 'uint8'), ('G', 'uint8'), ('B', 'uint8')])
        data = np.ones((1, 2, 3), dtype)
        hdr.set_data_dtype(dtype)
        S4 = BytesIO()
        hdr.data_to_fileobj(data, S4)
        data_back = hdr.data_from_fileobj(S4)
        assert_array_equal(data, data_back)

    def test_datatype(self):
        ehdr = self.header_class()
        codes = self.header_class._data_type_codes
        for code in codes.value_set():
            npt = codes.type[code]
            if npt is np.void:
                assert_raises(
                    HeaderDataError,
                    ehdr.set_data_dtype,
                    code)
                continue
            dt = codes.dtype[code]
            ehdr.set_data_dtype(npt)
            assert_true(ehdr['datatype'] == code)
            assert_true(ehdr['bitpix'] == dt.itemsize * 8)
            ehdr.set_data_dtype(code)
            assert_true(ehdr['datatype'] == code)
            ehdr.set_data_dtype(dt)
            assert_true(ehdr['datatype'] == code)

    def test_offset(self):
        # Test get / set offset
        hdr = self.header_class()
        offset = hdr.get_data_offset()
        hdr.set_data_offset(offset + 16)
        assert_equal(hdr.get_data_offset(), offset + 16)

    def test_data_shape_zooms_affine(self):
        hdr = self.header_class()
        for shape in ((1, 2, 3), (0,), (1,), (1, 2), (1, 2, 3, 4)):
            L = len(shape)
            hdr.set_data_shape(shape)
            if L:
                assert_equal(hdr.get_data_shape(), shape)
            else:
                assert_equal(hdr.get_data_shape(), (0,))
            # Default zoom - for 3D - is 1(())
            assert_equal(hdr.get_zooms(), (1,) * L)
            # errors if zooms do not match shape
            if len(shape):
                assert_raises(HeaderDataError,
                              hdr.set_zooms,
                              (1,) * (L - 1))
                # Errors for negative zooms
                assert_raises(HeaderDataError,
                              hdr.set_zooms,
                              (-1,) + (1,) * (L - 1))
            assert_raises(HeaderDataError,
                          hdr.set_zooms,
                          (1,) * (L + 1))
            # Errors for negative zooms
            assert_raises(HeaderDataError,
                          hdr.set_zooms,
                          (-1,) * L)
        # reducing the dimensionality of the array and then increasing
        # it again reverts the previously set zoom values to 1.0
        hdr = self.header_class()
        hdr.set_data_shape((1, 2, 3))
        hdr.set_zooms((4, 5, 6))
        assert_array_equal(hdr.get_zooms(), (4, 5, 6))
        hdr.set_data_shape((1, 2))
        assert_array_equal(hdr.get_zooms(), (4, 5))
        hdr.set_data_shape((1, 2, 3))
        assert_array_equal(hdr.get_zooms(), (4, 5, 1))
        # Setting zooms changes affine
        assert_array_equal(np.diag(hdr.get_base_affine()),
                           [-4, 5, 1, 1])
        hdr.set_zooms((1, 1, 1))
        assert_array_equal(np.diag(hdr.get_base_affine()),
                           [-1, 1, 1, 1])

    def test_default_x_flip(self):
        hdr = self.header_class()
        hdr.default_x_flip = True
        hdr.set_data_shape((1, 2, 3))
        hdr.set_zooms((1, 1, 1))
        assert_array_equal(np.diag(hdr.get_base_affine()),
                           [-1, 1, 1, 1])
        hdr.default_x_flip = False
        # Check avoids translations
        assert_array_equal(np.diag(hdr.get_base_affine()),
                           [1, 1, 1, 1])

    def test_from_eg_file(self):
        fileobj = open(self.example_file, 'rb')
        hdr = self.header_class.from_fileobj(fileobj, check=False)
        assert_equal(hdr.endianness, '>')
        assert_equal(hdr['sizeof_hdr'], self.sizeof_hdr)

    def test_orientation(self):
        # Test flips
        hdr = self.header_class()
        assert_true(hdr.default_x_flip)
        hdr.set_data_shape((3, 5, 7))
        hdr.set_zooms((4, 5, 6))
        aff = np.diag((-4, 5, 6, 1))
        aff[:3, 3] = np.array([1, 2, 3]) * np.array([-4, 5, 6]) * -1
        assert_array_equal(hdr.get_base_affine(), aff)
        hdr.default_x_flip = False
        assert_false(hdr.default_x_flip)
        aff[0] *= -1
        assert_array_equal(hdr.get_base_affine(), aff)

    def test_str(self):
        super(TestAnalyzeHeader, self).test_str()
        hdr = self.header_class()
        s1 = str(hdr)
        # check the datacode recoding
        rexp = re.compile('^datatype +: float32', re.MULTILINE)
        assert_true(rexp.search(s1) is not None)

    def test_from_header(self):
        # check from header class method.
        klass = self.header_class
        empty = klass.from_header()
        assert_equal(klass(), empty)
        empty = klass.from_header(None)
        assert_equal(klass(), empty)
        hdr = klass()
        hdr.set_data_dtype(np.float64)
        hdr.set_data_shape((1, 2, 3))
        hdr.set_zooms((3.0, 2.0, 1.0))
        for check in (True, False):
            copy = klass.from_header(hdr, check=check)
            assert_equal(hdr, copy)
            assert_false(hdr is copy)

        class C(object):

            def get_data_dtype(self): return np.dtype('i2')

            def get_data_shape(self): return (5, 4, 3)

            def get_zooms(self): return (10.0, 9.0, 8.0)
        converted = klass.from_header(C())
        assert_true(isinstance(converted, klass))
        assert_equal(converted.get_data_dtype(), np.dtype('i2'))
        assert_equal(converted.get_data_shape(), (5, 4, 3))
        assert_equal(converted.get_zooms(), (10.0, 9.0, 8.0))

    def test_base_affine(self):
        klass = self.header_class
        hdr = klass()
        hdr.set_data_shape((3, 5, 7))
        hdr.set_zooms((3, 2, 1))
        assert_true(hdr.default_x_flip)
        assert_array_almost_equal(
            hdr.get_base_affine(),
            [[-3., 0., 0., 3.],
             [0., 2., 0., -4.],
             [0., 0., 1., -3.],
             [0., 0., 0., 1.]])
        hdr.set_data_shape((3, 5))
        assert_array_almost_equal(
            hdr.get_base_affine(),
            [[-3., 0., 0., 3.],
             [0., 2., 0., -4.],
             [0., 0., 1., -0.],
             [0., 0., 0., 1.]])
        hdr.set_data_shape((3, 5, 7))
        assert_array_almost_equal(
            hdr.get_base_affine(),
            [[-3., 0., 0., 3.],
             [0., 2., 0., -4.],
             [0., 0., 1., -3.],
             [0., 0., 0., 1.]])

    def test_scaling(self):
        # Test integer scaling from float
        # Analyze headers cannot do float-integer scaling
        hdr = self.header_class()
        assert_true(hdr.default_x_flip)
        shape = (1, 2, 3)
        hdr.set_data_shape(shape)
        hdr.set_data_dtype(np.float32)
        data = np.ones(shape, dtype=np.float64)
        S = BytesIO()
        # Writing to float datatype doesn't need scaling
        hdr.data_to_fileobj(data, S)
        rdata = hdr.data_from_fileobj(S)
        assert_array_almost_equal(data, rdata)
        # Now test writing to integers
        hdr.set_data_dtype(np.int32)
        # Writing to int needs scaling, and raises an error if we can't scale
        if not hdr.has_data_slope:
            assert_raises(HeaderTypeError, hdr.data_to_fileobj, data, BytesIO())
        # But if we aren't scaling, convert the floats to integers and write
        with np.errstate(invalid='ignore'):
            hdr.data_to_fileobj(data, S, rescale=False)
        rdata = hdr.data_from_fileobj(S)
        assert_true(np.allclose(data, rdata))
        # This won't work for floats that aren't close to integers
        data_p5 = data + 0.5
        with np.errstate(invalid='ignore'):
            hdr.data_to_fileobj(data_p5, S, rescale=False)
        rdata = hdr.data_from_fileobj(S)
        assert_false(np.allclose(data_p5, rdata))

    def test_slope_inter(self):
        hdr = self.header_class()
        assert_equal(hdr.get_slope_inter(), (None, None))
        for slinter in ((None,),
                        (None, None),
                        (np.nan, np.nan),
                        (np.nan, None),
                        (None, np.nan),
                        (1.0,),
                        (1.0, None),
                        (None, 0),
                        (1.0, 0)):
            hdr.set_slope_inter(*slinter)
            assert_equal(hdr.get_slope_inter(), (None, None))
        assert_raises(HeaderTypeError, hdr.set_slope_inter, 1.1)
        assert_raises(HeaderTypeError, hdr.set_slope_inter, 1.0, 0.1)

    def test_from_analyze_map(self):
        # Test that any header can pass values from a mapping
        klass = self.header_class
        # Header needs to implement data_dtype, data_shape, zooms

        class H1(object):
            pass
        assert_raises(AttributeError, klass.from_header, H1())

        class H2(object):

            def get_data_dtype(self):
                return np.dtype('u1')
        assert_raises(AttributeError, klass.from_header, H2())

        class H3(H2):

            def get_data_shape(self):
                return (2, 3, 4)
        assert_raises(AttributeError, klass.from_header, H3())

        class H4(H3):

            def get_zooms(self):
                return 4., 5., 6.
        exp_hdr = klass()
        exp_hdr.set_data_dtype(np.dtype('u1'))
        exp_hdr.set_data_shape((2, 3, 4))
        exp_hdr.set_zooms((4, 5, 6))
        assert_equal(klass.from_header(H4()), exp_hdr)
        # cal_max, cal_min get properly set from ``as_analyze_map``

        class H5(H4):

            def as_analyze_map(self):
                return dict(cal_min=-100, cal_max=100)
        exp_hdr['cal_min'] = -100
        exp_hdr['cal_max'] = 100
        assert_equal(klass.from_header(H5()), exp_hdr)
        # set_* methods override fields fron header

        class H6(H5):

            def as_analyze_map(self):
                return dict(datatype=4, bitpix=32,
                            cal_min=-100, cal_max=100)
        assert_equal(klass.from_header(H6()), exp_hdr)
        # Any mapping will do, including a Nifti header

        class H7(H5):

            def as_analyze_map(self):
                n_hdr = Nifti1Header()
                n_hdr.set_data_dtype(np.dtype('i2'))
                n_hdr['cal_min'] = -100
                n_hdr['cal_max'] = 100
                return n_hdr
        # Values from methods still override values from header (shape, dtype,
        # zooms still at defaults from n_hdr header fields above)
        assert_equal(klass.from_header(H7()), exp_hdr)


def test_best_affine():
    hdr = AnalyzeHeader()
    hdr.set_data_shape((3, 5, 7))
    hdr.set_zooms((4, 5, 6))
    assert_array_equal(hdr.get_base_affine(), hdr.get_best_affine())


def test_data_code_error():
    # test analyze raising error for unsupported codes
    hdr = Nifti1Header()
    hdr['datatype'] = 256
    assert_raises(HeaderDataError, AnalyzeHeader.from_header, hdr)


class TestAnalyzeImage(tsi.TestSpatialImage, tsi.MmapImageMixin):
    image_class = AnalyzeImage
    can_save = True
    supported_np_types = TestAnalyzeHeader.supported_np_types
    # Flag to skip bz2 save tests if they are going to break
    bad_bz2 = False

    def test_supported_types(self):
        img = self.image_class(np.zeros((2, 3, 4)), np.eye(4))
        assert_equal(self.supported_np_types,
                     supported_np_types(img))

    def test_default_header(self):
        # Check default header is as expected
        arr = np.arange(24, dtype=np.int16).reshape((2, 3, 4))
        img = self.image_class(arr, None)
        hdr = self.image_class.header_class()
        hdr.set_data_shape(arr.shape)
        hdr.set_data_dtype(arr.dtype)
        hdr.set_data_offset(0)
        hdr.set_slope_inter(np.nan, np.nan)
        assert_equal(img.header, hdr)

    def test_data_hdr_cache(self):
        # test the API for loaded images, such that the data returned
        # from img.get_data() is not affected by subsequent changes to
        # the header.
        IC = self.image_class
        # save an image to a file map
        fm = IC.make_file_map()
        for key, value in fm.items():
            fm[key].fileobj = BytesIO()
        shape = (2, 3, 4)
        data = np.arange(24, dtype=np.int8).reshape(shape)
        affine = np.eye(4)
        hdr = IC.header_class()
        hdr.set_data_dtype(np.int16)
        img = IC(data, affine, hdr)
        img.to_file_map(fm)
        img2 = IC.from_file_map(fm)
        assert_equal(img2.shape, shape)
        assert_equal(img2.get_data_dtype().type, np.int16)
        hdr = img2.header
        hdr.set_data_shape((3, 2, 2))
        assert_equal(hdr.get_data_shape(), (3, 2, 2))
        hdr.set_data_dtype(np.uint8)
        assert_equal(hdr.get_data_dtype(), np.dtype(np.uint8))
        assert_array_equal(img2.get_data(), data)
        # now check read_img_data function - here we do see the changed
        # header
        sc_data = read_img_data(img2)
        assert_equal(sc_data.shape, (3, 2, 2))
        us_data = read_img_data(img2, prefer='unscaled')
        assert_equal(us_data.shape, (3, 2, 2))

    def test_affine_44(self):
        IC = self.image_class
        shape = (2, 3, 4)
        data = np.arange(24, dtype=np.int16).reshape(shape)
        affine = np.diag([2, 3, 4, 1])
        # OK - affine correct shape
        img = IC(data, affine)
        assert_array_equal(affine, img.affine)
        # OK - affine can be array-like
        img = IC(data, affine.tolist())
        assert_array_equal(affine, img.affine)
        # Not OK - affine wrong shape
        assert_raises(ValueError, IC, data, np.diag([2, 3, 4]))

    def test_offset_to_zero(self):
        # Check offset is always set to zero when creating images
        img_klass = self.image_class
        arr = np.arange(24, dtype=np.int16).reshape((2, 3, 4))
        aff = np.eye(4)
        img = img_klass(arr, aff)
        assert_equal(img.header.get_data_offset(), 0)
        # Save to BytesIO object(s), make sure offset still zero
        bytes_map = bytesio_filemap(img_klass)
        img.to_file_map(bytes_map)
        assert_equal(img.header.get_data_offset(), 0)
        # Set offset in in-memory image
        big_off = 1024
        img.header.set_data_offset(big_off)
        assert_equal(img.header.get_data_offset(), big_off)
        # Offset is in proxy but not in image after saving to fileobj
        img_rt = bytesio_round_trip(img)
        assert_equal(img_rt.dataobj.offset, big_off)
        assert_equal(img_rt.header.get_data_offset(), 0)
        # The original header still has the big_off value
        img.header.set_data_offset(big_off)
        # Making a new image with this header resets to zero
        img_again = img_klass(arr, aff, img.header)
        assert_equal(img_again.header.get_data_offset(), 0)

    def test_big_offset_exts(self):
        # Check writing offset beyond data works for different file extensions
        img_klass = self.image_class
        arr = np.arange(24, dtype=np.int16).reshape((2, 3, 4))
        aff = np.eye(4)
        img_ext = img_klass.files_types[0][1]
        compressed_exts = ['', '.gz']
        if not self.bad_bz2:
            compressed_exts.append('.bz2')
        with InTemporaryDirectory():
            for offset in (0, 2048):
                # Set offset in in-memory image
                for compressed_ext in compressed_exts:
                    img = img_klass(arr, aff)
                    img.header.set_data_offset(offset)
                    fname = 'test' + img_ext + compressed_ext
                    img.to_filename(fname)
                    img_back = img_klass.from_filename(fname)
                    assert_array_equal(arr, img_back.dataobj)
            del img, img_back

    def test_header_updating(self):
        # Only update on changes
        img_klass = self.image_class
        # With a None affine - don't overwrite zooms
        img = img_klass(np.zeros((2, 3, 4)), None)
        hdr = img.header
        hdr.set_zooms((4, 5, 6))
        # Save / reload using bytes IO objects
        for key, value in img.file_map.items():
            value.fileobj = BytesIO()
        img.to_file_map()
        hdr_back = img.from_file_map(img.file_map).header
        assert_array_equal(hdr_back.get_zooms(), (4, 5, 6))
        # With a real affine, update zooms
        img = img_klass(np.zeros((2, 3, 4)), np.diag([2, 3, 4, 1]), hdr)
        hdr = img.header
        assert_array_equal(hdr.get_zooms(), (2, 3, 4))
        # Modify affine in-place? Update on save.
        img.affine[0, 0] = 9
        for key, value in img.file_map.items():
            value.fileobj = BytesIO()
        img.to_file_map()
        hdr_back = img.from_file_map(img.file_map).header
        assert_array_equal(hdr.get_zooms(), (9, 3, 4))
        # Modify data in-place?  Update on save
        data = img.get_data()
        data.shape = (3, 2, 4)
        img.to_file_map()
        img_back = img.from_file_map(img.file_map)
        assert_array_equal(img_back.shape, (3, 2, 4))

    def test_pickle(self):
        # Test that images pickle
        # Image that is not proxied can pickle
        img_klass = self.image_class
        img = img_klass(np.zeros((2, 3, 4)), None)
        img_str = pickle.dumps(img)
        img2 = pickle.loads(img_str)
        assert_array_equal(img.get_data(), img2.get_data())
        assert_equal(img.header, img2.header)
        # Save / reload using bytes IO objects
        for key, value in img.file_map.items():
            value.fileobj = BytesIO()
        img.to_file_map()
        img_prox = img.from_file_map(img.file_map)
        img_str = pickle.dumps(img_prox)
        img2_prox = pickle.loads(img_str)
        assert_array_equal(img.get_data(), img2_prox.get_data())

    def test_no_finite_values(self):
        # save of data with no finite values to int type raises error if we have
        # no scaling
        data = np.zeros((2, 3, 4))
        data[:, 0] = np.nan
        data[:, 1] = np.inf
        data[:, 2] = -np.inf
        img = self.image_class(data, None)
        img.set_data_dtype(np.int16)
        assert_equal(img.get_data_dtype(), np.dtype(np.int16))
        fm = bytesio_filemap(img)
        if not img.header.has_data_slope:
            assert_raises(WriterError, img.to_file_map, fm)
            return
        img.to_file_map(fm)
        img_back = self.image_class.from_file_map(fm)
        assert_array_equal(img_back.dataobj, 0)


def test_unsupported():
    # analyze does not support uint32
    data = np.arange(24, dtype=np.int32).reshape((2, 3, 4))
    affine = np.eye(4)
    data = np.arange(24, dtype=np.uint32).reshape((2, 3, 4))
    assert_raises(HeaderDataError, AnalyzeImage, data, affine)
