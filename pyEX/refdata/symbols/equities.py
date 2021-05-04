# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ...common import _UTC, _expire, _get, _reindex, _toDatetime


@_expire(hour=8, tz=_UTC)
def symbols(token="", version="stable", filter="", format="json"):
    """This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/symbols", token=token, version=version, filter=filter, format=format
    )


@_expire(hour=8, tz=_UTC)
def internationalSymbols(
    region="",
    exchange="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (str): region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (str): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    if region:
        return _get(
            "ref-data/region/{region}/symbols".format(region=region),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    elif exchange:
        return _get(
            "ref-data/exchange/{exchange}/symbols".format(exchange=exchange),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/region/us/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(symbols)
def symbolsDF(*args, **kwargs):
    df = pd.DataFrame(symbols(*args, **kwargs))
    _toDatetime(df)
    _reindex(df, "symbol")
    df.sort_index(inplace=True)
    return df


@wraps(internationalSymbols)
def internationalSymbolsDF(*args, **kwargs):
    df = _reindex(
        _toDatetime(pd.DataFrame(internationalSymbols(*args, **kwargs))), "symbol"
    )
    df.sort_index(inplace=True)
    return df


@wraps(symbols)
def symbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in symbols(*args, **kwargs)])


@wraps(internationalSymbols)
def internationalSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in internationalSymbols(*args, **kwargs)])
