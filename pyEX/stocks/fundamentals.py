# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import numpy as np
import pandas as pd

from ..common import (
    _TIMEFRAME_DIVSPLIT,
    _UTC,
    PyEXception,
    _checkPeriodLast,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
)
from ..timeseries import timeSeries


@_expire(hour=8, tz=_UTC)
def balanceSheet(
    symbol,
    period="quarter",
    last=1,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Pulls balance sheet data. Available quarterly (4 quarters) and annually (4 years)

    https://iexcloud.io/docs/api/#balance-sheet
    Updates at 8am, 9am UTC daily


    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, last)
    return _get(
        "stock/{}/balance-sheet?period={}&last={}".format(symbol, period, last),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("balancesheet", [])


@wraps(balanceSheet)
def balanceSheetDF(*args, **kwargs):
    return _reindex(
        _toDatetime(pd.DataFrame(balanceSheet(*args, **kwargs))), "reportDate"
    )


@_expire(hour=8, tz=_UTC)
def cashFlow(
    symbol,
    period="quarter",
    last=1,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Pulls cash flow data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#cash-flow
    Updates at 8am, 9am UTC daily


    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, last)
    return _get(
        "stock/{}/cash-flow?period={}&last={}".format(symbol, period, last),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("cashflow", [])


@wraps(cashFlow)
def cashFlowDF(*args, **kwargs):
    df = _reindex(
        _toDatetime(pd.DataFrame(cashFlow(*args, **kwargs))),
        "reportDate",
    )
    df.replace(to_replace=[None], value=np.nan, inplace=True)
    return df


@_expire(hour=9, tz=_UTC)
def dividends(
    symbol,
    timeframe="ytd",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Dividend history

    https://iexcloud.io/docs/api/#dividends
    Updated at 9am UTC every day

    Args:
        symbol (str): Ticker to request
        timeframe (str): timeframe for data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception("Range must be in %s" % str(_TIMEFRAME_DIVSPLIT))
    return _get(
        "stock/" + symbol + "/dividends/" + timeframe,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _dividendsToDF(d):
    return _reindex(_toDatetime(pd.DataFrame(d)), "exDate")


@wraps(dividends)
def dividendsDF(*args, **kwargs):
    return _dividendsToDF(dividends(*args, **kwargs))


@_expire(hour=9, tz=_UTC)
def earnings(
    symbol,
    period="quarter",
    last=1,
    field="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        field (str): Subfield to fetch
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, last)
    if not field:
        return _get(
            "stock/{}/earnings?period={}&last={}".format(symbol, period, last),
            token=token,
            version=version,
            filter=filter,
            format=format,
        ).get("earnings", [])
    return _get(
        "stock/{}/earnings/{}/{}?period={}".format(symbol, last, field, period),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("earnings", [])


def _earningsToDF(e):
    """internal"""
    if e:
        df = _reindex(_toDatetime(pd.DataFrame(e)), "EPSReportDate")
    else:
        df = pd.DataFrame()
    return df


@wraps(earnings)
def earningsDF(*args, **kwargs):
    return _earningsToDF(earnings(*args, **kwargs))


@_expire(hour=8, tz=_UTC)
def financials(
    symbol, period="quarter", token="", version="stable", filter="", format="json"
):
    """Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

    https://iexcloud.io/docs/api/#financials
    Updates at 8am, 9am UTC daily

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, 1)
    return _get(
        "stock/{}/financials?period={}".format(symbol, period),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("financials", [])


def _financialsToDF(f):
    """internal"""
    if f:
        df = _reindex(_toDatetime(pd.DataFrame(f)), "reportDate")
    else:
        df = pd.DataFrame()
    return df


@wraps(financials)
def financialsDF(*args, **kwargs):
    return _financialsToDF(financials(*args, **kwargs))


@_expire(hour=8, tz=_UTC)
def fundamentals(
    symbol, period="quarter", token="", version="stable", filter="", format="json"
):
    """Pulls fundamentals data.

    https://iexcloud.io/docs/api/#advanced-fundamentals
    Updates at 8am, 9am UTC daily

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, 1)
    return _get(
        "stock/{}/fundamentals?period={}".format(symbol, period),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("fundamentals", [])


def _fundamentalsToDF(f):
    """internal"""
    if f:
        df = _reindex(_toDatetime(pd.DataFrame(f)), "reportDate")
    else:
        df = pd.DataFrame()
    return df


@wraps(fundamentals)
def fundamentalsDF(*args, **kwargs):
    return _fundamentalsToDF(fundamentals(*args, **kwargs))


@_expire(hour=8, tz=_UTC)
def incomeStatement(
    symbol,
    period="quarter",
    last=1,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Pulls income statement data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#income-statement
    Updates at 8am, 9am UTC daily

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, last)
    return _get(
        "stock/{}/income?period={}&last={}".format(symbol, period, last),
        token,
        version,
        filter,
    ).get("income", [])


@wraps(incomeStatement)
def incomeStatementDF(*args, **kwargs):
    return _reindex(
        _toDatetime(pd.DataFrame(incomeStatement(*args, **kwargs))), "reportDate"
    )


@_expire(hour=9, tz=_UTC)
def stockSplits(
    symbol, timeframe="ytd", token="", version="stable", filter="", format="json"
):
    """Stock split history

    https://iexcloud.io/docs/api/#splits
    Updated at 9am UTC every day

    Args:
        symbol (str): Ticker to request
        timeframe (str): timeframe for data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception("Range must be in %s" % str(_TIMEFRAME_DIVSPLIT))
    return _get(
        "stock/" + symbol + "/splits/" + timeframe,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _splitsToDF(d):
    return _reindex(_toDatetime(pd.DataFrame(d)), "exDate")


@wraps(stockSplits)
def stockSplitsDF(*args, **kwargs):
    return _splitsToDF(stockSplits(*args, **kwargs))


@wraps(timeSeries)
def tenQ(symbol, **kwargs):
    kwargs.pop("id")
    kwargs.pop("key")
    kwargs.pop("subkey")
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="10-Q", **kwargs)


@wraps(timeSeries)
def tenK(symbol, **kwargs):
    kwargs.pop("id")
    kwargs.pop("key")
    kwargs.pop("subkey")
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="10-K", **kwargs)


@wraps(timeSeries)
def twentyF(symbol, **kwargs):
    kwargs.pop("id")
    kwargs.pop("key")
    kwargs.pop("subkey")
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="20-F", **kwargs)


@wraps(timeSeries)
def fortyF(symbol, **kwargs):
    kwargs.pop("id")
    kwargs.pop("key")
    kwargs.pop("subkey")
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="40-F", **kwargs)
