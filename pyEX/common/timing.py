# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from __future__ import print_function

import os
import os.path
import tempfile

import pytz
from temporalcache import expire, interval

_PYEX_CACHE_FOLDER = os.path.abspath(os.path.join(tempfile.gettempdir(), "pyEX"))
_UTC = pytz.UTC
_EST = pytz.timezone("EST")


def _expire(**temporal_args):
    if not os.path.exists(_PYEX_CACHE_FOLDER):
        os.makedirs(_PYEX_CACHE_FOLDER)

    def _wrapper(foo):
        temporal_args["persistent"] = os.path.join(_PYEX_CACHE_FOLDER, foo.__name__)
        return expire(**temporal_args)(foo)

    return _wrapper


def _interval(**temporal_args):
    if not os.path.exists(_PYEX_CACHE_FOLDER):
        os.makedirs(_PYEX_CACHE_FOLDER)

    def _wrapper(foo):
        temporal_args["persistent"] = os.path.join(_PYEX_CACHE_FOLDER, foo.__name__)
        return interval(**temporal_args)(foo)

    return _wrapper
