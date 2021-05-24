# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
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
    _raiseIfNotStr,
    _toDatetime,
    _timeseriesWrapper,
)
from ..timeseries import timeSeries


def futures(
    contract, token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Futures EOD prices
    Args:
        contract (str): Specific dated future contract, e.g. NG0Z
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(contract)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id=contract,
        key="chart",
        token=token,
        version=version,
        overrideBase="futures",
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(futures)
def futuresDF(*args, **kwargs):
    return _toDatetime(
        pd.DataFrame(futures(*args, **kwargs)),
        reformatcols=["datetime", "date", "updated"],
    )
