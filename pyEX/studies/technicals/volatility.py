# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import talib as t
import pandas as pd


def atr(
    client,
    symbol,
    timeframe="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of average true range for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): time period to calculate over

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    atr = t.ATR(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "atr": atr,
        }
    )


def natr(
    client,
    symbol,
    timeframe="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of normalized average true range for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): time period to calculate over

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    natr = t.NATR(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "natr": natr,
        }
    )


def trange(
    client, symbol, timeframe="6m", highcol="high", lowcol="low", closecol="close"
):
    """This will return a dataframe of true range for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    trange = t.TRANGE(df[highcol].values, df[lowcol].values, df[closecol].values)
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "trange": trange,
        }
    )
