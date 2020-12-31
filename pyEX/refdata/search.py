# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _getJson, _interval, _quoteSymbols


@_interval(hours=24)  # TODO make this smaller?
def search(fragment, token="", version="", filter=""):
    """Returns an array of symbols up to the top 10 matches. Results will be sorted for relevancy. Search currently defaults to equities only, where the symbol returned is supported by endpoints listed under the Stocks category.

    https://iexcloud.io/docs/api/#search

    Args:
        fragment (str): URL encoded search string. Currently search by symbol or security name.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    fragment = _quoteSymbols(fragment)
    return _getJson("search/{}".format(fragment), token, version, filter)


@wraps(search)
def searchDF(fragment, token="", version="", filter=""):
    return pd.DataFrame(search(fragment, token, version, filter))
