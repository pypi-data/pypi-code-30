'''
Wrappers for the "CoreML" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-CoreML',
    description = "Wrappers for the framework CoreML on macOS",
    min_os_level="10.13",
    packages = [ "CoreML" ],
    ext_modules = [
        Extension("CoreML._CoreML",
            [ "Modules/_CoreML.m" ],
            extra_link_args=["-framework", "CoreML"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_CoreML')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
