# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from ...common import _EST, _expire
from ...files import files, download


@_expire(hour=10, tz=_EST)
def stockResearchReportValuEngine(symbol="", date=None, token="", version="stable"):
    """ValuEngine provides research on over 5,000 stocks with stock valuations, Buy/Hold/Sell recommendations, and forecasted target prices, so that you the individual investor can make informed decisions. Every ValuEngine Valuation and Forecast model for the U.S. equities markets has been extensively back-tested. ValuEngine’s performance exceeds that of many well-known stock-picking styles. Reports available since March 19th, 2020.
    https://iexcloud.io/docs/api/#valuengine-stock-research-report

    Args:
        symbol (str): symbol to use
        date (str): date to access
    """
    return files(
        id="VALUENGINE_REPORT", symbol=symbol, date=date, token=token, version=version
    )


@_expire(hour=10, tz=_EST)
def downloadStockResearchReportValuEngine(
    symbol="", date=None, token="", version="stable"
):
    """ValuEngine provides research on over 5,000 stocks with stock valuations, Buy/Hold/Sell recommendations, and forecasted target prices, so that you the individual investor can make informed decisions. Every ValuEngine Valuation and Forecast model for the U.S. equities markets has been extensively back-tested. ValuEngine’s performance exceeds that of many well-known stock-picking styles. Reports available since March 19th, 2020.
    https://iexcloud.io/docs/api/#valuengine-stock-research-report

    Args:
        symbol (str): symbol to use
        date (str): date to access
    """
    return download(
        id="VALUENGINE_REPORT", symbol=symbol, date=date, token=token, version=version
    )
