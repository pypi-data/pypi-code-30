"""
Script for building the example:

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions=["Bookmarks", "*"],
            CFBundleTypeName="Bookmarks File",
            CFBundleTypeRole="Editor",
            NSDocumentClass="BookmarksDocument",
        ),
    ],
)

setup(
    name="Bookmarks",
    app=["Bookmarks.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
