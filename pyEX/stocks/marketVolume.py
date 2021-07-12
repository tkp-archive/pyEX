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
    _get,
    _toDatetime,
)


def marketVolume(token="", version="stable", filter="", format="json"):
    """This endpoint returns real time traded volume on U.S. markets.

    https://iexcloud.io/docs/api/#market-volume-u-s
    7:45am-5:15pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("market/", token, version, filter)


@wraps(marketVolume)
def marketVolumeDF(token="", version="stable", filter="", format="json"):
    df = pd.DataFrame(marketVolume())
    _toDatetime(df, cols=[], tcols=["lastUpdated"])
    return df
