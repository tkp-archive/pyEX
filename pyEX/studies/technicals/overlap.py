# -*- coding: utf-8 -*-
import talib as t
import pandas as pd
from ..utils import tolist


def bollinger(client, symbol, timeframe="6m", col="close", period=2):
    """This will return a dataframe of bollinger bands for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period for the bollinger bands

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    bb = t.BBANDS(df[col].values, period)
    return pd.DataFrame(
        {col: df[col].values, "upper": bb[0], "middle": bb[1], "lower": bb[2]}
    )


def dema(client, symbol, timeframe="6m", col="close", periods=None):
    """This will return a dataframe of double exponential moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods

    Returns:
        DataFrame: result
    """
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["ema-{}".format(per)] = t.DEMA(df[col].values, per)
    return pd.DataFrame(build)


def ema(client, symbol, timeframe="6m", col="close", periods=None):
    """This will return a dataframe of exponential moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods

    Returns:
        DataFrame: result
    """
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["ema-{}".format(per)] = t.EMA(df[col].values, per)
    return pd.DataFrame(build)


def ht_trendline(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of hilbert trendline
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    build["ht-{}".format(col)] = t.HT_TRENDLINE(df[col].values)
    return pd.DataFrame(build)


def kama(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of kaufman adaptive moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); time period for kama

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    build["kama-{}".format(col)] = t.KAMA(df[col].values, period)
    return pd.DataFrame(build)


def mama(client, symbol, timeframe="6m", col="close", fastlimit=0, slowlimit=0):
    """This will return a dataframe of mesa adaptive moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        fastlimit (int); fastlimit for mama
        slowlimit (int); slowlimit for mama
    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    build["mama-{}".format(col)], build["fama-{}".format(col)] = t.MAMA(
        df[col].values, fastlimit=fastlimit, slowlimit=slowlimit
    )
    return pd.DataFrame(build)


def mavp(
    client,
    symbol,
    timeframe="6m",
    col="close",
    periods=None,
    minperiod=2,
    maxperiod=30,
    matype=0,
):
    """This will return a dataframe of moving average with variable period
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods
        minperiod (int); minperiod
        maxperiod (int); maxperiod
        matype (int); matype
    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["mavp-{}".format(per)] = t.MAVP(
            df[col].values, per, minperiod=minperiod, maxperiod=maxperiod, matype=matype
        )
    return pd.DataFrame(build)


def midpoint(client, symbol, timeframe="6m", col="close", period=14):
    """This will return a dataframe of midpoint over period
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); time period for kama

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    build["kama-{}".format(col)] = t.MIDPOINT(df[col].values, period)
    return pd.DataFrame(build)


def midpice(client, symbol, timeframe="6m", col="close", period=14):
    """This will return a dataframe of midprice over period
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); time period for kama

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    build["kama-{}".format(col)] = t.MIDPRICE(df[col].values, period)
    return pd.DataFrame(build)


def sar(
    client,
    symbol,
    timeframe="6m",
    highcol="high",
    lowcol="low",
    acceleration=0,
    maximum=0,
):
    """This will return a dataframe of parabolic sar
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); high column to use
        lowcol (string); low column to use
        acceleration (int); acceleration
        maximum (int); maximum

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    sar = t.SAR(
        df[highcol].values,
        df[lowcol].values,
        acceleration=acceleration,
        maximum=maximum,
    )
    return pd.DataFrame(
        {highcol: df[highcol].values, lowcol: df[lowcol].values, "sar": sar}
    )


def sarext(
    client,
    symbol,
    timeframe="6m",
    highcol="high",
    lowcol="low",
    startvalue=0,
    offsetonreverse=0,
    accelerationinitlong=0,
    accelerationlong=0,
    accelerationmaxlong=0,
    accelerationinitshort=0,
    accelerationshort=0,
    accelerationmaxshort=0,
):
    """This will return a dataframe of parabolic sar extended
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); high column to use
        lowcol (string); low column to use
        startvalue (int); startvalue
        offsetonreverse (int); offsetonreverse
        accelerationinitlong (int); accelerationinitlong
        accelerationlong (int); accelerationlong
        accelerationmaxlong (int); accelerationmaxlong
        accelerationinitshort (int); accelerationinitshort
        accelerationshort (int); accelerationshort
        accelerationmaxshort (int); accelerationmaxshort

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    sar = t.SAREXT(
        df[highcol].values,
        df[lowcol].values,
        startvalue=startvalue,
        offsetonreverse=offsetonreverse,
        accelerationinitlong=accelerationinitlong,
        accelerationlong=accelerationlong,
        accelerationmaxlong=accelerationmaxlong,
        accelerationinitshort=accelerationinitshort,
        accelerationshort=accelerationshort,
        accelerationmaxshort=accelerationmaxshort,
    )
    return pd.DataFrame(
        {highcol: df[highcol].values, lowcol: df[lowcol].values, "sar": sar}
    )


def sma(client, symbol, timeframe="6m", col="close", periods=None):
    """This will return a dataframe of exponential moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods

    Returns:
        DataFrame: result
    """
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["sma-{}".format(per)] = t.EMA(df[col].values, per)
    return pd.DataFrame(build)


def t3(client, symbol, timeframe="6m", col="close", periods=None, vfactor=0):
    """This will return a dataframe of tripple exponential moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods
        vfactor (int); vfactor

    Returns:
        DataFrame: result
    """
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["t3-{}".format(per)] = t.T3(df[col].values, per, vfactor=vfactor)
    return pd.DataFrame(build)


def tema(client, symbol, timeframe="6m", col="close", periods=None):
    """This will return a dataframe of triple exponential moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods

    Returns:
        DataFrame: result
    """
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["sma-{}".format(per)] = t.TEMA(df[col].values, per)
    return pd.DataFrame(build)


def trima(client, symbol, timeframe="6m", col="close", periods=None):
    """This will return a dataframe of triangular moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods

    Returns:
        DataFrame: result
    """
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["trima-{}".format(per)] = t.TRIMA(df[col].values, per)
    return pd.DataFrame(build)


def wma(client, symbol, timeframe="6m", col="close", periods=None):
    """This will return a dataframe of weighted moving average
     for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        periods (int); periods

    Returns:
        DataFrame: result
    """
    if periods is None:
        periods = [30]
    periods = tolist(periods)

    df = client.chartDF(symbol, timeframe)

    build = {col: df[col].values}
    for per in periods:
        build["wma-{}".format(per)] = t.WMA(df[col].values, per)
    return pd.DataFrame(build)
