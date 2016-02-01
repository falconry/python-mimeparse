# Travis CI Build Status [![Build Status](https://travis-ci.org/dbtsai/python-mimeparse.svg?branch=master)](https://travis-ci.org/dbtsai/python-mimeparse)

This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of
the HTTP specification [RFC 2616] for a complete explanation.

   http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1

Contents:
    - parse_mime_type():   Parses a mime-type into its component parts.
    - parse_media_range(): Media-ranges are mime-types with wild-cards and a "q" quality parameter.
    - quality():           Determines the quality ("q") of a mime-type when compared against a list of media-ranges.
    - quality_parsed():    Just like quality() except the second parameter must be pre-parsed.
    - best_match():        Choose the mime-type with the highest quality ("q") from a list of candidates.

Testing
=======
The format of the JSON test data file is as follows:
A top-level JSON object which has a key for each of the functions to be tested. The value corresponding to that key is a list of tests. Each test contains: the argument or arguments to the function being tested, the expected results and an optional description.

Python
======
The Python tests require Python 2.6.

Run the tests by typing:
python mimeparse_test.py

To make sure that the package works in all the supported environments, you can run tox tests:
pip install tox
tox
