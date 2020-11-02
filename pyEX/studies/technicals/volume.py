# -*- coding: utf-8 -*-
import talib as t
import pandas as pd


def ad(
    client,
    symbol,
    timeframe="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    volumecol="volume",
):
    """This will return a dataframe of Chaikin A/D Line for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        volumecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    ad = t.AD(
        df[highcol].values, df[lowcol].values, df[closecol].values, df[volumecol].values
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            volumecol: df[volumecol].values,
            "a/d": ad,
        }
    )


def adosc(
    client,
    symbol,
    timeframe="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    volumecol="volume",
    fastperiod=3,
    slowperiod=10,
):
    """This will return a dataframe of Chaikin A/D Oscillator for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        volumecol (string): column to use to calculate
        fastperiod (int): fast period to calculate across
        slowperiod (int): slow period to calculate across
    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    adosc = t.ADOSC(
        df[highcol].values,
        df[lowcol].values,
        df[closecol].values,
        df[volumecol].values,
        fastperiod,
        slowperiod,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            volumecol: df[volumecol].values,
            "a/d": adosc,
        }
    )


def obv(client, symbol, timeframe="6m", closecol="close", volumecol="volume"):
    """This will return a dataframe of On Balance Volume for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        closecol (string): column to use to calculate
        volumecol (string): column to use to calculate
    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    obv = t.OBV(df[closecol].values, df[volumecol].values)
    return pd.DataFrame(
        {closecol: df[closecol].values, volumecol: df[volumecol].values, "obv": obv}
    )
