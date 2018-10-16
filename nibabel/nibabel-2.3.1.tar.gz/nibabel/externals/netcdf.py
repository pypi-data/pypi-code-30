"""
NetCDF reader/writer module.

This module is used to read and create NetCDF files. NetCDF files are
accessed through the `netcdf_file` object. Data written to and from NetCDF
files are contained in `netcdf_variable` objects. Attributes are given
as member variables of the `netcdf_file` and `netcdf_variable` objects.

This module implements the Scientific.IO.NetCDF API to read and create
NetCDF files. The same API is also used in the PyNIO and pynetcdf
modules, allowing these modules to be used interchangeably when working
with NetCDF files.
"""

from __future__ import division, print_function, absolute_import

# TODO:
# * properly implement ``_FillValue``.
# * implement Jeff Whitaker's patch for masked variables.
# * fix character variables.
# * implement PAGESIZE for Python 2.6?

# The Scientific.IO.NetCDF API allows attributes to be added directly to
# instances of ``netcdf_file`` and ``netcdf_variable``. To differentiate
# between user-set attributes and instance attributes, user-set attributes
# are automatically stored in the ``_attributes`` attribute by overloading
#``__setattr__``. This is the reason why the code sometimes uses
#``obj.__dict__['key'] = value``, instead of simply ``obj.key = value``;
# otherwise the key would be inserted into userspace attributes.


__all__ = ['netcdf_file']


from operator import mul
from mmap import mmap, ACCESS_READ

import numpy as np  # noqa
from ..py3k import asbytes, asstr
from numpy import fromstring, ndarray, dtype, empty, array, asarray
from numpy import little_endian as LITTLE_ENDIAN
from functools import reduce

from six import integer_types


ABSENT = b'\x00\x00\x00\x00\x00\x00\x00\x00'
ZERO = b'\x00\x00\x00\x00'
NC_BYTE = b'\x00\x00\x00\x01'
NC_CHAR = b'\x00\x00\x00\x02'
NC_SHORT = b'\x00\x00\x00\x03'
NC_INT = b'\x00\x00\x00\x04'
NC_FLOAT = b'\x00\x00\x00\x05'
NC_DOUBLE = b'\x00\x00\x00\x06'
NC_DIMENSION = b'\x00\x00\x00\n'
NC_VARIABLE = b'\x00\x00\x00\x0b'
NC_ATTRIBUTE = b'\x00\x00\x00\x0c'


TYPEMAP = {NC_BYTE: ('b', 1),
            NC_CHAR: ('c', 1),
            NC_SHORT: ('h', 2),
            NC_INT: ('i', 4),
            NC_FLOAT: ('f', 4),
            NC_DOUBLE: ('d', 8)}

REVERSE = {('b', 1): NC_BYTE,
            ('B', 1): NC_CHAR,
            ('c', 1): NC_CHAR,
            ('h', 2): NC_SHORT,
            ('i', 4): NC_INT,
            ('f', 4): NC_FLOAT,
            ('d', 8): NC_DOUBLE,

            # these come from asarray(1).dtype.char and asarray('foo').dtype.char,
            # used when getting the types from generic attributes.
            ('l', 4): NC_INT,
            ('S', 1): NC_CHAR}


class netcdf_file(object):
    """
    A file object for NetCDF data.

    A `netcdf_file` object has two standard attributes: `dimensions` and
    `variables`. The values of both are dictionaries, mapping dimension
    names to their associated lengths and variable names to variables,
    respectively. Application programs should never modify these
    dictionaries.

    All other attributes correspond to global attributes defined in the
    NetCDF file. Global file attributes are created by assigning to an
    attribute of the `netcdf_file` object.

    Parameters
    ----------
    filename : string or file-like
        string -> filename
    mode : {'r', 'w'}, optional
        read-write mode, default is 'r'
    mmap : None or bool, optional
        Whether to mmap `filename` when reading.  Default is True
        when `filename` is a file name, False when `filename` is a
        file-like object
    version : {1, 2}, optional
        version of netcdf to read / write, where 1 means *Classic
        format* and 2 means *64-bit offset format*.  Default is 1.  See
        `here <https://www.unidata.ucar.edu/software/netcdf/docs/netcdf/Which-Format.html>`_
        for more info.

    Notes
    -----
    The major advantage of this module over other modules is that it doesn't
    require the code to be linked to the NetCDF libraries. This module is
    derived from `pupynere <https://bitbucket.org/robertodealmeida/pupynere/>`_.

    NetCDF files are a self-describing binary data format. The file contains
    metadata that describes the dimensions and variables in the file. More
    details about NetCDF files can be found `here
    <https://www.unidata.ucar.edu/software/netcdf/docs/netcdf.html>`_. There
    are three main sections to a NetCDF data structure:

    1. Dimensions
    2. Variables
    3. Attributes

    The dimensions section records the name and length of each dimension used
    by the variables. The variables would then indicate which dimensions it
    uses and any attributes such as data units, along with containing the data
    values for the variable. It is good practice to include a
    variable that is the same name as a dimension to provide the values for
    that axes. Lastly, the attributes section would contain additional
    information such as the name of the file creator or the instrument used to
    collect the data.

    When writing data to a NetCDF file, there is often the need to indicate the
    'record dimension'. A record dimension is the unbounded dimension for a
    variable. For example, a temperature variable may have dimensions of
    latitude, longitude and time. If one wants to add more temperature data to
    the NetCDF file as time progresses, then the temperature variable should
    have the time dimension flagged as the record dimension.

    In addition, the NetCDF file header contains the position of the data in
    the file, so access can be done in an efficient manner without loading
    unnecessary data into memory. It uses the ``mmap`` module to create
    Numpy arrays mapped to the data on disk, for the same purpose.

    Examples
    --------
    To create a NetCDF file:

    Make a temporary file for testing:

        >>> import os
        >>> from tempfile import mkdtemp
        >>> tmp_pth = mkdtemp()
        >>> fname = os.path.join(tmp_pth, 'test.nc')

    Then:

        >>> f = netcdf_file(fname, 'w')
        >>> f.history = 'Created for a test'
        >>> f.createDimension('time', 10)
        >>> time = f.createVariable('time', 'i', ('time',))
        >>> time[:] = np.arange(10)
        >>> time.units = 'days since 2008-01-01'
        >>> f.close()

    Note the assignment of ``range(10)`` to ``time[:]``.  Exposing the slice
    of the time variable allows for the data to be set in the object, rather
    than letting ``range(10)`` overwrite the ``time`` variable.

    To read the NetCDF file we just created:

        >>> f = netcdf_file(fname, 'r')
        >>> f.history == b'Created for a test'
        True
        >>> time = f.variables['time']
        >>> time.units == b'days since 2008-01-01'
        True
        >>> time.shape == (10,)
        True
        >>> time[-1]
        9
        >>> f.close()

    A NetCDF file can also be used as context manager:

        >>> with netcdf_file(fname, 'r') as f:
        ...     print(f.variables['time'].shape == (10,))
        True

    Delete our temporary directory and file:

        >>> del f, time # needed for windows unlink
        >>> os.unlink(fname)
        >>> os.rmdir(tmp_pth)
    """
    def __init__(self, filename, mode='r', mmap=None, version=1):
        """Initialize netcdf_file from fileobj (str or file-like)."""
        if hasattr(filename, 'seek'):  # file-like
            self.fp = filename
            self.filename = 'None'
            if mmap is None:
                mmap = False
            elif mmap and not hasattr(filename, 'fileno'):
                raise ValueError('Cannot use file object for mmap')
        else:  # maybe it's a string
            self.filename = filename
            self.fp = open(self.filename, '%sb' % mode)
            if mmap is None:
                mmap = True
        try:
            self.fp.seek(0, 2)
        except ValueError:
            self.file_bytes = -1 # Unknown file length (gzip).
        else:
            self.file_bytes = self.fp.tell()
            self.fp.seek(0)

        self.use_mmap = mmap
        self.version_byte = version

        if not mode in 'rw':
            raise ValueError("Mode must be either 'r' or 'w'.")
        self.mode = mode

        self.dimensions = {}
        self.variables = {}

        self._dims = []
        self._recs = 0
        self._recsize = 0

        self._attributes = {}

        if mode == 'r':
            self._read()

    def __setattr__(self, attr, value):
        # Store user defined attributes in a separate dict,
        # so we can save them to file later.
        try:
            self._attributes[attr] = value
        except AttributeError:
            pass
        self.__dict__[attr] = value

    def close(self):
        """Closes the NetCDF file."""
        if not self.fp.closed:
            try:
                self.flush()
            finally:
                self.fp.close()
    __del__ = close

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createDimension(self, name, length):
        """
        Adds a dimension to the Dimension section of the NetCDF data structure.

        Note that this function merely adds a new dimension that the variables can
        reference.  The values for the dimension, if desired, should be added as
        a variable using `createVariable`, referring to this dimension.

        Parameters
        ----------
        name : str
            Name of the dimension (Eg, 'lat' or 'time').
        length : int
            Length of the dimension.

        See Also
        --------
        createVariable

        """
        self.dimensions[name] = length
        self._dims.append(name)

    def createVariable(self, name, type, dimensions):
        """
        Create an empty variable for the `netcdf_file` object, specifying its data
        type and the dimensions it uses.

        Parameters
        ----------
        name : str
            Name of the new variable.
        type : dtype or str
            Data type of the variable.
        dimensions : sequence of str
            List of the dimension names used by the variable, in the desired order.

        Returns
        -------
        variable : netcdf_variable
            The newly created ``netcdf_variable`` object.
            This object has also been added to the `netcdf_file` object as well.

        See Also
        --------
        createDimension

        Notes
        -----
        Any dimensions to be used by the variable should already exist in the
        NetCDF data structure or should be created by `createDimension` prior to
        creating the NetCDF variable.

        """
        shape = tuple([self.dimensions[dim] for dim in dimensions])
        shape_ = tuple([dim or 0 for dim in shape])  # replace None with 0 for numpy

        type = dtype(type)
        typecode, size = type.char, type.itemsize
        if (typecode, size) not in REVERSE:
            raise ValueError("NetCDF 3 does not support type %s" % type)

        data = empty(shape_, dtype=type.newbyteorder("B"))  # convert to big endian always for NetCDF 3
        self.variables[name] = netcdf_variable(data, typecode, size, shape, dimensions)
        return self.variables[name]

    def flush(self):
        """
        Perform a sync-to-disk flush if the `netcdf_file` object is in write mode.

        See Also
        --------
        sync : Identical function

        """
        if hasattr(self, 'mode') and self.mode is 'w':
            self._write()
    sync = flush

    def _write(self):
        self.fp.seek(0)
        self.fp.write(b'CDF')
        self.fp.write(array(self.version_byte, '>b').tostring())

        # Write headers and data.
        self._write_numrecs()
        self._write_dim_array()
        self._write_gatt_array()
        self._write_var_array()

    def _write_numrecs(self):
        # Get highest record count from all record variables.
        for var in self.variables.values():
            if var.isrec and len(var.data) > self._recs:
                self.__dict__['_recs'] = len(var.data)
        self._pack_int(self._recs)

    def _write_dim_array(self):
        if self.dimensions:
            self.fp.write(NC_DIMENSION)
            self._pack_int(len(self.dimensions))
            for name in self._dims:
                self._pack_string(name)
                length = self.dimensions[name]
                self._pack_int(length or 0)  # replace None with 0 for record dimension
        else:
            self.fp.write(ABSENT)

    def _write_gatt_array(self):
        self._write_att_array(self._attributes)

    def _write_att_array(self, attributes):
        if attributes:
            self.fp.write(NC_ATTRIBUTE)
            self._pack_int(len(attributes))
            for name, values in attributes.items():
                self._pack_string(name)
                self._write_values(values)
        else:
            self.fp.write(ABSENT)

    def _write_var_array(self):
        if self.variables:
            self.fp.write(NC_VARIABLE)
            self._pack_int(len(self.variables))

            # Sort variables non-recs first, then recs. We use a DSU
            # since some people use pupynere with Python 2.3.x.
            deco = [(v._shape and not v.isrec, k) for (k, v) in self.variables.items()]
            deco.sort()
            variables = [k for (unused, k) in deco][::-1]

            # Set the metadata for all variables.
            for name in variables:
                self._write_var_metadata(name)
            # Now that we have the metadata, we know the vsize of
            # each record variable, so we can calculate recsize.
            self.__dict__['_recsize'] = sum([
                    var._vsize for var in self.variables.values()
                    if var.isrec])
            # Set the data for all variables.
            for name in variables:
                self._write_var_data(name)
        else:
            self.fp.write(ABSENT)

    def _write_var_metadata(self, name):
        var = self.variables[name]

        self._pack_string(name)
        self._pack_int(len(var.dimensions))
        for dimname in var.dimensions:
            dimid = self._dims.index(dimname)
            self._pack_int(dimid)

        self._write_att_array(var._attributes)

        nc_type = REVERSE[var.typecode(), var.itemsize()]
        self.fp.write(asbytes(nc_type))

        if not var.isrec:
            vsize = var.data.size * var.data.itemsize
            vsize += -vsize % 4
        else:  # record variable
            try:
                vsize = var.data[0].size * var.data.itemsize
            except IndexError:
                vsize = 0
            rec_vars = len([var for var in self.variables.values()
                    if var.isrec])
            if rec_vars > 1:
                vsize += -vsize % 4
        self.variables[name].__dict__['_vsize'] = vsize
        self._pack_int(vsize)

        # Pack a bogus begin, and set the real value later.
        self.variables[name].__dict__['_begin'] = self.fp.tell()
        self._pack_begin(0)

    def _write_var_data(self, name):
        var = self.variables[name]

        # Set begin in file header.
        the_beguine = self.fp.tell()
        self.fp.seek(var._begin)
        self._pack_begin(the_beguine)
        self.fp.seek(the_beguine)

        # Write data.
        if not var.isrec:
            self.fp.write(var.data.tostring())
            count = var.data.size * var.data.itemsize
            self.fp.write(b'0' * (var._vsize - count))
        else:  # record variable
            # Handle rec vars with shape[0] < nrecs.
            if self._recs > len(var.data):
                shape = (self._recs,) + var.data.shape[1:]
                var.data.resize(shape)

            pos0 = pos = self.fp.tell()
            for rec in var.data:
                # Apparently scalars cannot be converted to big endian. If we
                # try to convert a ``=i4`` scalar to, say, '>i4' the dtype
                # will remain as ``=i4``.
                if not rec.shape and (rec.dtype.byteorder == '<' or
                        (rec.dtype.byteorder == '=' and LITTLE_ENDIAN)):
                    rec = rec.byteswap()
                self.fp.write(rec.tostring())
                # Padding
                count = rec.size * rec.itemsize
                self.fp.write(b'0' * (var._vsize - count))
                pos += self._recsize
                self.fp.seek(pos)
            self.fp.seek(pos0 + var._vsize)

    def _write_values(self, values):
        if hasattr(values, 'dtype'):
            nc_type = REVERSE[values.dtype.char, values.dtype.itemsize]
        else:
            types = [(t, NC_INT) for t in integer_types]
            types += [
                    (float, NC_FLOAT),
                    (str, NC_CHAR),
                    ]
            try:
                sample = values[0]
            except TypeError:
                sample = values
            for class_, nc_type in types:
                if isinstance(sample, class_):
                    break

        typecode, size = TYPEMAP[nc_type]
        dtype_ = '>%s' % typecode

        values = asarray(values, dtype=dtype_)

        self.fp.write(asbytes(nc_type))

        if values.dtype.char == 'S':
            nelems = values.itemsize
        else:
            nelems = values.size
        self._pack_int(nelems)

        if not values.shape and (values.dtype.byteorder == '<' or
                (values.dtype.byteorder == '=' and LITTLE_ENDIAN)):
            values = values.byteswap()
        self.fp.write(values.tostring())
        count = values.size * values.itemsize
        self.fp.write(b'0' * (-count % 4))  # pad

    def _read(self):
        # Check magic bytes and version
        magic = self.fp.read(3)
        if not magic == b'CDF':
            raise TypeError("Error: %s is not a valid NetCDF 3 file" %
                            self.filename)
        self.__dict__['version_byte'] = fromstring(self.fp.read(1), '>b')[0]

        # Read file headers and set data.
        self._read_numrecs()
        self._read_dim_array()
        self._read_gatt_array()
        self._read_var_array()

    def _read_numrecs(self):
        self.__dict__['_recs'] = self._unpack_int()

    def _read_dim_array(self):
        header = self.fp.read(4)
        if not header in [ZERO, NC_DIMENSION]:
            raise ValueError("Unexpected header.")
        count = self._unpack_int()

        for dim in range(count):
            name = asstr(self._unpack_string())
            length = self._unpack_int() or None  # None for record dimension
            self.dimensions[name] = length
            self._dims.append(name)  # preserve order

    def _read_gatt_array(self):
        for k, v in self._read_att_array().items():
            self.__setattr__(k, v)

    def _read_att_array(self):
        header = self.fp.read(4)
        if not header in [ZERO, NC_ATTRIBUTE]:
            raise ValueError("Unexpected header.")
        count = self._unpack_int()

        attributes = {}
        for attr in range(count):
            name = asstr(self._unpack_string())
            attributes[name] = self._read_values()
        return attributes

    def _read_var_array(self):
        header = self.fp.read(4)
        if not header in [ZERO, NC_VARIABLE]:
            raise ValueError("Unexpected header.")

        begin = 0
        dtypes = {'names': [], 'formats': []}
        rec_vars = []
        count = self._unpack_int()
        for var in range(count):
            (name, dimensions, shape, attributes,
             typecode, size, dtype_, begin_, vsize) = self._read_var()
            # https://www.unidata.ucar.edu/software/netcdf/docs/netcdf.html
            # Note that vsize is the product of the dimension lengths
            # (omitting the record dimension) and the number of bytes
            # per value (determined from the type), increased to the
            # next multiple of 4, for each variable. If a record
            # variable, this is the amount of space per record. The
            # netCDF "record size" is calculated as the sum of the
            # vsize's of all the record variables.
            #
            # The vsize field is actually redundant, because its value
            # may be computed from other information in the header. The
            # 32-bit vsize field is not large enough to contain the size
            # of variables that require more than 2^32 - 4 bytes, so
            # 2^32 - 1 is used in the vsize field for such variables.
            if shape and shape[0] is None:  # record variable
                rec_vars.append(name)
                # The netCDF "record size" is calculated as the sum of
                # the vsize's of all the record variables.
                self.__dict__['_recsize'] += vsize
                if begin == 0:
                    begin = begin_
                dtypes['names'].append(name)
                dtypes['formats'].append(str(shape[1:]) + dtype_)

                # Handle padding with a virtual variable.
                if typecode in 'bch':
                    actual_size = reduce(mul, (1,) + shape[1:]) * size
                    padding = -actual_size % 4
                    if padding:
                        dtypes['names'].append('_padding_%d' % var)
                        dtypes['formats'].append('(%d,)>b' % padding)

                # Data will be set later.
                data = None
            else:  # not a record variable
                # Calculate size to avoid problems with vsize (above)
                a_size = reduce(mul, shape, 1) * size
                if self.file_bytes >= 0 and begin_ + a_size > self.file_bytes:
                    data = fromstring(b'\x00'*a_size, dtype=dtype_)
                elif self.use_mmap:
                    mm = mmap(self.fp.fileno(), begin_+a_size, access=ACCESS_READ)
                    data = ndarray.__new__(ndarray, shape, dtype=dtype_,
                            buffer=mm, offset=begin_, order=0)
                else:
                    pos = self.fp.tell()
                    self.fp.seek(begin_)
                    # Try to read file, which may fail because the data is
                    # at or past the end of file. In that case, we treat
                    # this data as zeros.
                    buf = self.fp.read(a_size)
                    if len(buf) < a_size:
                        buf = b'\x00'*a_size
                    data = fromstring(buf, dtype=dtype_)
                    data.shape = shape
                    self.fp.seek(pos)

            # Add variable.
            self.variables[name] = netcdf_variable(
                    data, typecode, size, shape, dimensions, attributes)

        if rec_vars:
            # Remove padding when only one record variable.
            if len(rec_vars) == 1:
                dtypes['names'] = dtypes['names'][:1]
                dtypes['formats'] = dtypes['formats'][:1]

            # Build rec array.
            if self.use_mmap:
                mm = mmap(self.fp.fileno(), begin+self._recs*self._recsize, access=ACCESS_READ)
                rec_array = ndarray.__new__(ndarray, (self._recs,), dtype=dtypes,
                        buffer=mm, offset=begin, order=0)
            else:
                pos = self.fp.tell()
                self.fp.seek(begin)
                rec_array = fromstring(self.fp.read(self._recs*self._recsize), dtype=dtypes)
                rec_array.shape = (self._recs,)
                self.fp.seek(pos)

            for var in rec_vars:
                self.variables[var].__dict__['data'] = rec_array[var]

    def _read_var(self):
        name = asstr(self._unpack_string())
        dimensions = []
        shape = []
        dims = self._unpack_int()

        for i in range(dims):
            dimid = self._unpack_int()
            dimname = self._dims[dimid]
            dimensions.append(dimname)
            dim = self.dimensions[dimname]
            shape.append(dim)
        dimensions = tuple(dimensions)
        shape = tuple(shape)

        attributes = self._read_att_array()
        nc_type = self.fp.read(4)
        vsize = self._unpack_int()
        begin = [self._unpack_int, self._unpack_int64][self.version_byte-1]()

        typecode, size = TYPEMAP[nc_type]
        dtype_ = '>%s' % typecode

        return name, dimensions, shape, attributes, typecode, size, dtype_, begin, vsize

    def _read_values(self):
        nc_type = self.fp.read(4)
        n = self._unpack_int()

        typecode, size = TYPEMAP[nc_type]

        count = n*size
        values = self.fp.read(int(count))
        self.fp.read(-count % 4)  # read padding

        if typecode is not 'c':
            values = fromstring(values, dtype='>%s' % typecode)
            if values.shape == (1,):
                values = values[0]
        else:
            values = values.rstrip(b'\x00')
        return values

    def _pack_begin(self, begin):
        if self.version_byte == 1:
            self._pack_int(begin)
        elif self.version_byte == 2:
            self._pack_int64(begin)

    def _pack_int(self, value):
        self.fp.write(array(value, '>i').tostring())
    _pack_int32 = _pack_int

    def _unpack_int(self):
        return int(fromstring(self.fp.read(4), '>i')[0])
    _unpack_int32 = _unpack_int

    def _pack_int64(self, value):
        self.fp.write(array(value, '>q').tostring())

    def _unpack_int64(self):
        return fromstring(self.fp.read(8), '>q')[0]

    def _pack_string(self, s):
        count = len(s)
        self._pack_int(count)
        self.fp.write(asbytes(s))
        self.fp.write(b'0' * (-count % 4))  # pad

    def _unpack_string(self):
        count = self._unpack_int()
        s = self.fp.read(count).rstrip(b'\x00')
        self.fp.read(-count % 4)  # read padding
        return s


class netcdf_variable(object):
    """
    A data object for the `netcdf` module.

    `netcdf_variable` objects are constructed by calling the method
    `netcdf_file.createVariable` on the `netcdf_file` object. `netcdf_variable`
    objects behave much like array objects defined in numpy, except that their
    data resides in a file. Data is read by indexing and written by assigning
    to an indexed subset; the entire array can be accessed by the index ``[:]``
    or (for scalars) by using the methods `getValue` and `assignValue`.
    `netcdf_variable` objects also have attribute `shape` with the same meaning
    as for arrays, but the shape cannot be modified. There is another read-only
    attribute `dimensions`, whose value is the tuple of dimension names.

    All other attributes correspond to variable attributes defined in
    the NetCDF file. Variable attributes are created by assigning to an
    attribute of the `netcdf_variable` object.

    Parameters
    ----------
    data : array_like
        The data array that holds the values for the variable.
        Typically, this is initialized as empty, but with the proper shape.
    typecode : dtype character code
        Desired data-type for the data array.
    size : int
        Desired element size for the data array.
    shape : sequence of ints
        The shape of the array.  This should match the lengths of the
        variable's dimensions.
    dimensions : sequence of strings
        The names of the dimensions used by the variable.  Must be in the
        same order of the dimension lengths given by `shape`.
    attributes : dict, optional
        Attribute values (any type) keyed by string names.  These attributes
        become attributes for the netcdf_variable object.


    Attributes
    ----------
    dimensions : list of str
        List of names of dimensions used by the variable object.
    isrec, shape
        Properties

    See also
    --------
    isrec, shape

    """
    def __init__(self, data, typecode, size, shape, dimensions, attributes=None):
        self.data = data
        self._typecode = typecode
        self._size = size
        self._shape = shape
        self.dimensions = dimensions

        self._attributes = attributes or {}
        for k, v in self._attributes.items():
            self.__dict__[k] = v

    def __setattr__(self, attr, value):
        # Store user defined attributes in a separate dict,
        # so we can save them to file later.
        try:
            self._attributes[attr] = value
        except AttributeError:
            pass
        self.__dict__[attr] = value

    def isrec(self):
        """Returns whether the variable has a record dimension or not.

        A record dimension is a dimension along which additional data could be
        easily appended in the netcdf data structure without much rewriting of
        the data file. This attribute is a read-only property of the
        `netcdf_variable`.

        """
        return self.data.shape and not self._shape[0]
    isrec = property(isrec)

    def shape(self):
        """Returns the shape tuple of the data variable.

        This is a read-only attribute and can not be modified in the
        same manner of other numpy arrays.
        """
        return self.data.shape
    shape = property(shape)

    def getValue(self):
        """
        Retrieve a scalar value from a `netcdf_variable` of length one.

        Raises
        ------
        ValueError
            If the netcdf variable is an array of length greater than one,
            this exception will be raised.

        """
        return self.data.item()

    def assignValue(self, value):
        """
        Assign a scalar value to a `netcdf_variable` of length one.

        Parameters
        ----------
        value : scalar
            Scalar value (of compatible type) to assign to a length-one netcdf
            variable. This value will be written to file.

        Raises
        ------
        ValueError
            If the input is not a scalar, or if the destination is not a length-one
            netcdf variable.

        """
        if not self.data.flags.writeable:
            # Work-around for a bug in NumPy.  Calling itemset() on a read-only
            # memory-mapped array causes a seg. fault.
            # See NumPy ticket #1622, and SciPy ticket #1202.
            # This check for `writeable` can be removed when the oldest version
            # of numpy still supported by scipy contains the fix for #1622.
            raise RuntimeError("variable is not writeable")

        self.data.itemset(value)

    def typecode(self):
        """
        Return the typecode of the variable.

        Returns
        -------
        typecode : char
            The character typecode of the variable (eg, 'i' for int).

        """
        return self._typecode

    def itemsize(self):
        """
        Return the itemsize of the variable.

        Returns
        -------
        itemsize : int
            The element size of the variable (eg, 8 for float64).

        """
        return self._size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, data):
        # Expand data for record vars?
        if self.isrec:
            if isinstance(index, tuple):
                rec_index = index[0]
            else:
                rec_index = index
            if isinstance(rec_index, slice):
                recs = (rec_index.start or 0) + len(data)
            else:
                recs = rec_index + 1
            if recs > len(self.data):
                shape = (recs,) + self._shape[1:]
                self.data.resize(shape)
        self.data[index] = data


NetCDFFile = netcdf_file
NetCDFVariable = netcdf_variable
