# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _expire, _getJson


@_expire(hour=8)
def exchanges(token="", version="", filter=""):
    """Returns an array of U.S. exchanges.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    return _getJson("ref-data/market/us/exchanges", token, version, filter)


@wraps(exchanges)
def exchangesDF(token="", version="", filter=""):
    return pd.DataFrame(exchanges(token, version, filter))


@_expire(hour=8)
def internationalExchanges(token="", version="", filter=""):
    """Returns an array of exchanges.

    https://iexcloud.io/docs/api/#international-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    return _getJson("ref-data/exchanges", token, version, filter)


@wraps(internationalExchanges)
def internationalExchangesDF(token="", version="", filter=""):
    return pd.DataFrame(internationalExchanges(token, version, filter))
