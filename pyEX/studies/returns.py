# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#


def returns(client, symbol, range="6m"):
    """Calculate returns using daily close price

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        range (string); range to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    c = client.chartDF(symbol, range)["close"]
    return (c / c.shift(1)).fillna(1)


def dailyReturns(client, symbol, range="6m"):
    """Calculate returns of buying at open and selling at close daily

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        range (string); range to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    c = client.chartDF(symbol, range)[["open", "close"]]
    return (c["close"] - c["open"]) / c["open"]
