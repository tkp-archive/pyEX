# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ...common import _UTC, _expire
from ...timeseries import timeSeries, timeSeriesDF


@_expire(hour=8, tz=_UTC)
def _base(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeries(**kwargs)


@_expire(hour=8, tz=_UTC)
def _baseDF(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def nonTimelyFilingsFraudFactors(symbol="", **kwargs):
    """The data set records the date in which a firm files a Non-Timely notification with the SEC.
    Companies regulated by the SEC are required to file a Non-Timely notification when they are unable to file their annual or quarterly disclosures on time. In most cases, the inability to file annual/quarterly disclosures on time is a red-flag and thus a valuable signal for algorithmic strategies and fundamental investing alike.
    Data available from 1994 with coverage of about 18,000 equities
    https://iexcloud.io/docs/api/#non-timely-filings

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_FRAUD_FACTORS_NON_TIMELY_FILINGS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def nonTimelyFilingsFraudFactorsDF(symbol="", **kwargs):
    """The data set records the date in which a firm files a Non-Timely notification with the SEC.
    Companies regulated by the SEC are required to file a Non-Timely notification when they are unable to file their annual or quarterly disclosures on time. In most cases, the inability to file annual/quarterly disclosures on time is a red-flag and thus a valuable signal for algorithmic strategies and fundamental investing alike.
    Data available from 1994 with coverage of about 18,000 equities
    https://iexcloud.io/docs/api/#non-timely-filings

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(
        id="PREMIUM_FRAUD_FACTORS_NON_TIMELY_FILINGS", symbol=symbol, **kwargs
    )
