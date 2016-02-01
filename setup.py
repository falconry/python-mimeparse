#!/usr/bin/env python

import os
import codecs
import mimeparse
from setuptools import setup


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(path, encoding='utf-8').read()

setup(
    name="python-mimeparse",
    py_modules=["mimeparse"],
    version=mimeparse.__version__,
    description=("A module provides basic functions for parsing mime-type "
                 "names and matching them against a list of media-ranges."),
    author="DB Tsai",
    author_email="dbtsai@dbtsai.com",
    url="https://github.com/dbtsai/python-mimeparse",
    download_url=("http://pypi.python.org/packages/source/p/python-mimeparse/"
                  "python-mimeparse-" + mimeparse.__version__ + ".tar.gz"),
    keywords=["mime-type"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=read('README.md')
)
