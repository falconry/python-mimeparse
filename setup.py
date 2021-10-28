#!/usr/bin/env python

import codecs
import os
import re

from setuptools import setup


def get_version(filename):
    """
    Return package version as listed in `__version__` in 'filename'.
    """
    with open(filename) as fp:
        contents = fp.read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)


version = get_version('mimeparse.py')
if not version:
    raise RuntimeError('Cannot find version information')


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with codecs.open(path, encoding='utf-8') as fp:
        return fp.read()


setup(
    name="python-mimeparse",
    py_modules=["mimeparse"],
    version=version,
    description=("A module provides basic functions for parsing mime-type "
                 "names and matching them against a list of media-ranges."),
    author="DB Tsai",
    license="MIT",
    author_email="dbtsai@dbtsai.com",
    url="https://github.com/dbtsai/python-mimeparse",
    download_url=("https://github.com/dbtsai/python-mimeparse/tarball/" + version),
    keywords=["mime-type"],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=read('README.rst')
)
