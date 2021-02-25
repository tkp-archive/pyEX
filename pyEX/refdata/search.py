# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _get, _interval, _quoteSymbols


@_interval(hours=24)  # TODO make this smaller?
def search(fragment, token="", version="stable", filter="", format="json"):
    """Returns an array of symbols up to the top 10 matches. Results will be sorted for relevancy. Search currently defaults to equities only, where the symbol returned is supported by endpoints listed under the Stocks category.

    https://iexcloud.io/docs/api/#search

    Args:
        fragment (str): URL encoded search string. Currently search by symbol or security name.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    fragment = _quoteSymbols(fragment)
    return _get(
        "search/{}".format(fragment),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(search)
def searchDF(*args, **kwargs):
    return pd.DataFrame(search(*args, **kwargs))
