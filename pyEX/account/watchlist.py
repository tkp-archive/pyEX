# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _get


def getWatchlist(
    id="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """
    Args:
        id (str): watchlist ID
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    url = "/account/watchlist"

    if id:
        url += "/{}/contents".format(id)
    return _get(url, token, version, filter, format)


@wraps(getWatchlist)
def getWatchlistDF(*args, **kwargs):
    return pd.DataFrame(getWatchlist(*args, **kwargs))
