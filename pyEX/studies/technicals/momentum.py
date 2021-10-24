# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
import talib as t


def adx(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of average directional movement index for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate adx across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    adx = t.ADX(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "adx": adx,
        }
    )


def adxr(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of average directional movement index rating for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    adx = t.ADXR(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "adx": adx,
        }
    )


def apo(
    client, symbol, range="6m", col="close", fastperiod=12, slowperiod=26, matype=0
):
    """This will return a dataframe of Absolute Price Oscillator for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        fastperiod (int): fast period to calculate across
        slowperiod (int): slow period to calculate across
        matype (int): moving average type (0-sma)

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    apo = t.APO(df[col].values.astype(float), fastperiod, slowperiod, matype)
    return pd.DataFrame({col: df[col].values, "apo": apo})


def aroon(client, symbol, range="6m", highcol="high", lowcol="low", period=14):
    """This will return a dataframe of
    Aroon
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    aroondown, aroonup = t.AROON(
        df[highcol].values.astype(float), df[lowcol].values.astype(float), period
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            "aroonup": aroonup,
            "aroondown": aroondown,
        }
    )


def aroonosc(client, symbol, range="6m", highcol="high", lowcol="low", period=14):
    """This will return a dataframe of
    Aroon Oscillator
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.AROONOSC(
        df[highcol].values.astype(float), df[lowcol].values.astype(float), period
    )
    return pd.DataFrame(
        {highcol: df[highcol].values, lowcol: df[lowcol].values, "aroonosc": x}
    )


def bop(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    volumecol="volume",
):
    """This will return a dataframe of
    Balance of power
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        volumecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.BOP(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        df[volumecol].values.astype(float),
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            volumecol: df[volumecol].values,
            "bop": x,
        }
    )


def cci(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of
    Commodity Channel Index
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.CCI(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "cci": x,
        }
    )


def cmo(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    Chande Momentum Oscillator
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {col: df[col].values, "cmo": t.CMO(df[col].values.astype(float), period)}
    )


def dx(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of
    Directional Movement Index
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.DX(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "dx": x,
        }
    )


def macd(
    client,
    symbol,
    range="6m",
    col="close",
    fastperiod=12,
    slowperiod=26,
    signalperiod=9,
):
    """This will return a dataframe of Moving Average Convergence/Divergence for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        fastperiod (int): fast period to calculate across
        slowperiod (int): slow period to calculate across
        signalperiod (int): macd signal period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    macd, macdsignal, macdhist = t.MACD(
        df[col].values.astype(float), fastperiod, slowperiod, signalperiod
    )
    return pd.DataFrame(
        {
            col: df[col].values,
            "macd": macd,
            "macdsignal": macdsignal,
            "macdhist": macdhist,
        }
    )


def macdext(
    client,
    symbol,
    range="6m",
    col="close",
    fastperiod=12,
    fastmatype=0,
    slowperiod=26,
    slowmatype=0,
    signalperiod=9,
    signalmatype=0,
):
    """This will return a dataframe of Moving Average Convergence/Divergence for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        fastperiod (int): fast period to calculate across
        fastmatype (int): moving average type (0-sma)
        slowperiod (int): slow period to calculate across
        slowmatype (int): moving average type (0-sma)
        signalperiod (int): macd signal period
        signalmatype (int): moving average type (0-sma)

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    macd, macdsignal, macdhist = t.MACDEXT(
        df[col].values.astype(float), fastperiod, slowperiod, signalperiod
    )
    return pd.DataFrame(
        {
            col: df[col].values,
            "macd": macd,
            "macdsignal": macdsignal,
            "macdhist": macdhist,
        }
    )


def mfi(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    volumecol="volume",
    period=14,
):
    """This will return a dataframe of
    Money Flow Index
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.MFI(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        df[volumecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            volumecol: df[volumecol].values,
            "mfi": x,
        }
    )


def minus_di(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of
    Minus Directional Indicator
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.MINUS_DI(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "minus_di": x,
        }
    )


def minus_dm(client, symbol, range="6m", highcol="high", lowcol="low", period=14):
    """This will return a dataframe of
    Minus Directional Movement
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.MINUS_DM(
        df[highcol].values.astype(float), df[lowcol].values.astype(float), period
    )
    return pd.DataFrame(
        {highcol: df[highcol].values, lowcol: df[lowcol].values, "minus_dm": x}
    )


def mom(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    Momentum
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {col: df[col].values, "mom": t.MOM(df[col].values.astype(float), period)}
    )


def plus_di(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of
    Plus Directional Movement
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.PLUS_DI(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "plus_di": x,
        }
    )


def plus_dm(client, symbol, range="6m", highcol="high", lowcol="low", period=14):
    """This will return a dataframe of
    Plus Directional Movement
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.PLUS_DM(
        df[highcol].values.astype(float), df[lowcol].values.astype(float), period
    )
    return pd.DataFrame(
        {highcol: df[highcol].values, lowcol: df[lowcol].values, "plus_dm": x}
    )


def ppo(
    client, symbol, range="6m", col="close", fastperiod=12, slowperiod=26, matype=0
):
    """This will return a dataframe of Percentage Price Oscillator for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        fastperiod (int): fast period to calculate across
        slowperiod (int): slow period to calculate across
        matype (int): moving average type (0-sma)

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    ppo = t.PPO(df[col].values.astype(float), fastperiod, slowperiod, matype)
    return pd.DataFrame({col: df[col].values, "ppo": ppo})


def roc(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    Rate of change: ((price/prevPrice)-1)*100
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {col: df[col].values, "roc": t.ROC(df[col].values.astype(float), period)}
    )


def rocp(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    Rate of change Percentage: (price-prevPrice)/prevPrice
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {col: df[col].values, "rocp": t.ROCP(df[col].values.astype(float), period)}
    )


def rocr(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    Rate of change ratio: (price/prevPrice)
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {col: df[col].values, "rocr": t.ROCR(df[col].values.astype(float), period)}
    )


def rocr100(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    Rate of change ratio 100 scale: (price/prevPrice)*100
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {
            col: df[col].values,
            "rocr100": t.ROCR100(df[col].values.astype(float), period),
        }
    )


def rsi(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    Relative Strength Index
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {col: df[col].values, "rsi": t.RSI(df[col].values.astype(float), period)}
    )


def stoch(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    fastk_period=5,
    slowk_period=3,
    slowk_matype=0,
    slowd_period=3,
    slowd_matype=0,
):
    """This will return a dataframe of
    Stochastic
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        fastk_period (int): fastk_period
        slowk_period (int): slowk_period
        slowk_matype (int): slowk_matype
        slowd_period (int): slowd_period
        slowd_matype (int): slowd_matype

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    slowk, slowd = t.STOCH(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        fastk_period=fastk_period,
        slowk_period=slowk_period,
        slowk_matype=slowk_matype,
        slowd_period=slowd_period,
        slowd_matype=slowd_matype,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "slowk": slowk,
            "slowd": slowd,
        }
    )


def stochf(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    fastk_period=5,
    slowk_period=3,
    slowk_matype=0,
    slowd_period=3,
    slowd_matype=0,
):
    """This will return a dataframe of
    Stochastic Fast
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        fastk_period (int): fastk_period
        slowk_period (int): slowk_period
        slowk_matype (int): slowk_matype
        slowd_period (int): slowd_period
        slowd_matype (int): slowd_matype

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    fastk, fastd = t.STOCHF(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        fastk_period=fastk_period,
        slowk_period=slowk_period,
        slowk_matype=slowk_matype,
        slowd_period=slowd_period,
        slowd_matype=slowd_matype,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "fastk": fastk,
            "fastd": fastd,
        }
    )


def stochrsi(
    client,
    symbol,
    range="6m",
    closecol="close",
    period=14,
    fastk_period=5,
    fastd_period=3,
    fastd_matype=0,
):
    """This will return a dataframe of
    Stochastic Relative Strength Index
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        closecol (string): column to use to calculate
        period (int): period to calculate across
        fastk_period (int): fastk_period
        fastd_period (int): fastd_period
        fastd_matype (int): moving average type (0-sma)

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    fastk, fastd = t.STOCHRSI(
        df[closecol].values.astype(float),
        timeperiod=period,
        fastk_period=fastk_period,
        fastd_period=fastd_period,
        fastd_matype=fastd_matype,
    )
    return pd.DataFrame({closecol: df[closecol].values, "fastk": fastk, "fastd": fastd})


def trix(client, symbol, range="6m", col="close", period=14):
    """This will return a dataframe of
    1-day Rate-Of-Change(ROC) of a Triple Smooth EMA
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        col (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    return pd.DataFrame(
        {col: df[col].values, "trix": t.TRIX(df[col].values.astype(float), period)}
    )


def ultosc(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period1=7,
    period2=14,
    period3=28,
):
    """This will return a dataframe of
    Ultimate Oscillator
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period1 (int): period to calculate across
        period2 (int): period to calculate across
        period3 (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.ULTOSC(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        timeperiod1=period1,
        timeperiod2=period2,
        timeperiod3=period3,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "ultosc": x,
        }
    )


def willr(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of
    Williams' % R
    for the given symbol across the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): period to calculate across

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.WILLR(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        period,
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "willr": x,
        }
    )
