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
    _reindex,
    _toDatetime,
)


def sectorPerformance(token="", version="stable", filter="", format="json"):
    """This returns an array of each sector and performance for the current trading day. Performance is based on each sector ETF.

    https://iexcloud.io/docs/api/#sector-performance
    8am-5pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/sector-performance", token, version, filter)


@wraps(sectorPerformance)
def sectorPerformanceDF(*args, **kwargs):
    return _reindex(
        _toDatetime(
            pd.DataFrame(sectorPerformance(*args, **kwargs)),
            cols=[],
            tcols=["lastUpdated"],
        ),
        "name",
    )
