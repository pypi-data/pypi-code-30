# for compatibility, expose cheroot webtest here
import warnings

from cheroot.test.webtest import (  # noqa
    interface, TerseTestResult, TerseTestRunner,
    ReloadingTestLoader, WebCase, cleanHeaders, shb, openURL,
    ServerError, server_error,
)


warnings.warn('Use cheroot.test.webtest', DeprecationWarning)
