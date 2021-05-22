# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _quoteSymbols, _raiseIfNotStr, _timeseriesWrapper
from ..timeseries import timeSeries


def bonusIssue(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Bonus Issue Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#bonus-issue

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_bonus",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(bonusIssue)
def bonusIssueDF(*args, **kwargs):
    return pd.DataFrame(bonusIssue(*args, **kwargs))


def distribution(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Distribution Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#distribution

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_distribution",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(distribution)
def distributionDF(*args, **kwargs):
    return pd.DataFrame(distribution(*args, **kwargs))


def dividends(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Obtain up-to-date and detailed information on all new dividend announcements, as well as 12+ years of historical dividend records. This endpoint covers over 39,000 US equities, mutual funds, ADRs, and ETFs.
    You’ll be provided with:
        Detailed information on both cash and stock dividends including record, payment, ex, and announce dates
        Gross and net amounts
        Details of all currencies in which a dividend can be paid
        Tax information
        The ability to keep up with the growing number of complex dividend distributions

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#dividends

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_dividends",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(dividends)
def dividendsDF(*args, **kwargs):
    return pd.DataFrame(dividends(*args, **kwargs))


def returnOfCapital(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Return of capital up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#return-of-capital

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_return_of_capital",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(returnOfCapital)
def returnOfCapitalDF(*args, **kwargs):
    return pd.DataFrame(returnOfCapital(*args, **kwargs))


def rightsIssue(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Rights issue up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#rights-issue

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_rights",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(rightsIssue)
def rightsIssueDF(*args, **kwargs):
    return pd.DataFrame(rightsIssue(*args, **kwargs))


def rightToPurchase(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Right to purchase up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#right-to-purchase

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_right_to_purchase",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(rightToPurchase)
def rightToPurchaseDF(*args, **kwargs):
    return pd.DataFrame(rightToPurchase(*args, **kwargs))


def securityReclassification(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Security reclassification up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-reclassification

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_security_reclassification",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(securityReclassification)
def securityReclassificationDF(*args, **kwargs):
    return pd.DataFrame(securityReclassification(*args, **kwargs))


def securitySwap(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Security Swap up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-swap

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_security_swap",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(securitySwap)
def securitySwapDF(*args, **kwargs):
    return pd.DataFrame(securitySwap(*args, **kwargs))


def spinoff(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Security spinoff up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#spinoff

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_spinoff",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(spinoff)
def spinoffDF(*args, **kwargs):
    return pd.DataFrame(spinoff(*args, **kwargs))


def splits(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Security splits up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#splits

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_splits",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(splits)
def splitsDF(*args, **kwargs):
    return pd.DataFrame(splits(*args, **kwargs))
