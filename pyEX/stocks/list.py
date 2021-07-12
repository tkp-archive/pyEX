# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import (
    _LIST_OPTIONS,
    PyEXception,
    _get,
    _reindex,
    _toDatetime,
)


def list(
    option="mostactive",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Returns an array of quotes for the top 10 symbols in a specified list.


    https://iexcloud.io/docs/api/#list
    Updated intraday

    Args:
        option (str): Option to query
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if option not in _LIST_OPTIONS:
        raise PyEXception("Option must be in %s" % str(_LIST_OPTIONS))
    return _get("stock/market/list/" + option, token, version, filter)


@wraps(list)
def listDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(list(*args, **kwargs))), "symbol")
