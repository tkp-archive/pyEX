# -*- coding: utf-8 -*-


def returns(client, symbol, timeframe="6m"):
    """Calculate returns using daily close price

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    c = client.chartDF(symbol, timeframe)["close"]
    return (c / c.shift(1)).fillna(1)


def dailyReturns(client, symbol, timeframe="6m"):
    """Calculate returns of buying at open and selling at close daily

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    c = client.chartDF(symbol, timeframe)[["open", "close"]]
    return (c["close"] - c["open"]) / c["open"]
