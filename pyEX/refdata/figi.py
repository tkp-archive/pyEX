# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _get, _raiseIfNotStr


def figi(figi_=None, token="", version="stable", format="json"):
    """Helper call to convert FIGI to IEX Cloud symbols. Note that due to licensing restrictions we are unable to return the FIGI.

    https://iexcloud.io/docs/api/#figi-mapping

    Args:
        figi_ (str): figi to lookup
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(figi_)
    return _get(
        "ref-data/figi?figi={}".format(figi_),
        token=token,
        version=version,
        format=format,
    )


@wraps(figi)
def figiDF(*args, **kwargs):
    return pd.DataFrame(figi(*args, **kwargs))
