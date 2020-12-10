# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _interval, _getJson


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
    return _getJson("search/{}".format(fragment), token, version, filter)


@wraps(search)
def searchDF(fragment, token="", version="", filter=""):
    return pd.DataFrame(search(fragment, token, version, filter))
