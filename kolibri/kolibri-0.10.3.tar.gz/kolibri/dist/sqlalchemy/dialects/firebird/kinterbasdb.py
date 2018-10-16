# firebird/kinterbasdb.py
# Copyright (C) 2005-2018 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""
.. dialect:: firebird+kinterbasdb
    :name: kinterbasdb
    :dbapi: kinterbasdb
    :connectstring: firebird+kinterbasdb://user:password@host:port/path/to/db\
[?key=value&key=value...]
    :url: http://firebirdsql.org/index.php?op=devel&sub=python

Arguments
----------

The Kinterbasdb backend accepts the ``enable_rowcount`` and ``retaining``
arguments accepted by the :mod:`sqlalchemy.dialects.firebird.fdb` dialect.
In addition, it also accepts the following:

* ``type_conv`` - select the kind of mapping done on the types: by default
  SQLAlchemy uses 200 with Unicode, datetime and decimal support.  See
  the linked documents below for further information.

* ``concurrency_level`` - set the backend policy with regards to threading
  issues: by default SQLAlchemy uses policy 1.  See the linked documents
  below for further information.

.. seealso::

    http://sourceforge.net/projects/kinterbasdb

    http://kinterbasdb.sourceforge.net/dist_docs/usage.html#adv_param_conv_dynamic_type_translation

    http://kinterbasdb.sourceforge.net/dist_docs/usage.html#special_issue_concurrency

"""

from .base import FBDialect, FBExecutionContext
from ... import util, types as sqltypes
from re import match
import decimal


class _kinterbasdb_numeric(object):
    def bind_processor(self, dialect):
        def process(value):
            if isinstance(value, decimal.Decimal):
                return str(value)
            else:
                return value
        return process


class _FBNumeric_kinterbasdb(_kinterbasdb_numeric, sqltypes.Numeric):
    pass


class _FBFloat_kinterbasdb(_kinterbasdb_numeric, sqltypes.Float):
    pass


class FBExecutionContext_kinterbasdb(FBExecutionContext):
    @property
    def rowcount(self):
        if self.execution_options.get('enable_rowcount',
                                      self.dialect.enable_rowcount):
            return self.cursor.rowcount
        else:
            return -1


class FBDialect_kinterbasdb(FBDialect):
    driver = 'kinterbasdb'
    supports_sane_rowcount = False
    supports_sane_multi_rowcount = False
    execution_ctx_cls = FBExecutionContext_kinterbasdb

    supports_native_decimal = True

    colspecs = util.update_copy(
        FBDialect.colspecs,
        {
            sqltypes.Numeric: _FBNumeric_kinterbasdb,
            sqltypes.Float: _FBFloat_kinterbasdb,
        }

    )

    def __init__(self, type_conv=200, concurrency_level=1,
                 enable_rowcount=True,
                 retaining=False, **kwargs):
        super(FBDialect_kinterbasdb, self).__init__(**kwargs)
        self.enable_rowcount = enable_rowcount
        self.type_conv = type_conv
        self.concurrency_level = concurrency_level
        self.retaining = retaining
        if enable_rowcount:
            self.supports_sane_rowcount = True

    @classmethod
    def dbapi(cls):
        return __import__('kinterbasdb')

    def do_execute(self, cursor, statement, parameters, context=None):
        # kinterbase does not accept a None, but wants an empty list
        # when there are no arguments.
        cursor.execute(statement, parameters or [])

    def do_rollback(self, dbapi_connection):
        dbapi_connection.rollback(self.retaining)

    def do_commit(self, dbapi_connection):
        dbapi_connection.commit(self.retaining)

    def create_connect_args(self, url):
        opts = url.translate_connect_args(username='user')
        if opts.get('port'):
            opts['host'] = "%s/%s" % (opts['host'], opts['port'])
            del opts['port']
        opts.update(url.query)

        util.coerce_kw_type(opts, 'type_conv', int)

        type_conv = opts.pop('type_conv', self.type_conv)
        concurrency_level = opts.pop('concurrency_level',
                                     self.concurrency_level)

        if self.dbapi is not None:
            initialized = getattr(self.dbapi, 'initialized', None)
            if initialized is None:
                # CVS rev 1.96 changed the name of the attribute:
                # http://kinterbasdb.cvs.sourceforge.net/viewvc/kinterbasdb/
                # Kinterbasdb-3.0/__init__.py?r1=1.95&r2=1.96
                initialized = getattr(self.dbapi, '_initialized', False)
            if not initialized:
                self.dbapi.init(type_conv=type_conv,
                                concurrency_level=concurrency_level)
        return ([], opts)

    def _get_server_version_info(self, connection):
        """Get the version of the Firebird server used by a connection.

        Returns a tuple of (`major`, `minor`, `build`), three integers
        representing the version of the attached server.
        """

        # This is the simpler approach (the other uses the services api),
        # that for backward compatibility reasons returns a string like
        #   LI-V6.3.3.12981 Firebird 2.0
        # where the first version is a fake one resembling the old
        # Interbase signature.

        fbconn = connection.connection
        version = fbconn.server_version

        return self._parse_version_info(version)

    def _parse_version_info(self, version):
        m = match(
            r'\w+-V(\d+)\.(\d+)\.(\d+)\.(\d+)( \w+ (\d+)\.(\d+))?', version)
        if not m:
            raise AssertionError(
                "Could not determine version from string '%s'" % version)

        if m.group(5) != None:
            return tuple([int(x) for x in m.group(6, 7, 4)] + ['firebird'])
        else:
            return tuple([int(x) for x in m.group(1, 2, 3)] + ['interbase'])

    def is_disconnect(self, e, connection, cursor):
        if isinstance(e, (self.dbapi.OperationalError,
                          self.dbapi.ProgrammingError)):
            msg = str(e)
            return ('Unable to complete network request to host' in msg or
                    'Invalid connection state' in msg or
                    'Invalid cursor state' in msg or
                    'connection shutdown' in msg)
        else:
            return False

dialect = FBDialect_kinterbasdb
