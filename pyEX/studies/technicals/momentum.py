# -*- coding: utf-8 -*-
import talib as t
import pandas as pd


def adx(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', period=14):
    '''This will return a dataframe of average directional movement index for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    adx = t.ADX(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'adx': adx})


def adxr(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', period=14):
    '''This will return a dataframe of average directional movement index rating for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    adx = t.ADXR(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'adx': adx})


# APO - Absolute Price Oscillator
# real = APO(close, fastperiod=12, slowperiod=26, matype=0)

def aroon(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', period=14):
    '''This will return a dataframe of
    Aroon
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    aroondown, aroonup = t.AROON(df[highcol].values, df[lowcol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, 'aroonup': aroonup, 'aroondown': aroondown})


def aroonosc(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', period=14):
    '''This will return a dataframe of
    Aroon Oscillator
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.AROONOSC(df[highcol].values, df[lowcol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, 'aroonosc': x})


def bop(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', volumecol='volume'):
    '''This will return a dataframe of
    Balance of power
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        volumecol (string); column to use to calculate

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.BOP(df[highcol].values, df[lowcol].values, df[closecol].values, df[volumecol].values)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, volumecol: df[volumecol].values, 'bop': x})


def cci(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', period=14):
    '''This will return a dataframe of
    Commodity Channel Index
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.CCI(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'cci': x})


def cmo(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    Chande Momentum Oscillator
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'cmo': t.CMO(df[col].values, period)})


def dx(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', period=14):
    '''This will return a dataframe of
    Directional Movement Index
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.DX(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'dx': x})

# MACD - Moving Average Convergence/Divergence
# macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

# MACDEXT - MACD with controllable MA type
# macd, macdsignal, macdhist = MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
# macd, macdsignal, macdhist = MACDFIX(close, signalperiod=9)


def mfi(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', volumecol='volume', period=14):
    '''This will return a dataframe of
    Money Flow Index
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.MFI(df[highcol].values, df[lowcol].values, df[closecol].values, df[volumecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, volumecol: df[volumecol].values, 'mfi': x})


def minus_di(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', period=14):
    '''This will return a dataframe of
    Minus Directional Indicator
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.MINUS_DI(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'minus_di': x})


def minus_dm(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', period=14):
    '''This will return a dataframe of
    Minus Directional Movement
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.MINUS_DM(df[highcol].values, df[lowcol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, 'minus_dm': x})


def mom(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    Momentum
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'mom': t.MOM(df[col].values, period)})


def plus_di(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', period=14):
    '''This will return a dataframe of
    Plus Directional Movement
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.PLUS_DI(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'plus_di': x})


def plus_dm(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', period=14):
    '''This will return a dataframe of
    Plus Directional Movement
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.PLUS_DM(df[highcol].values, df[lowcol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, 'plus_dm': x})

# PPO - Percentage Price Oscillator
# real = PPO(close, fastperiod=12, slowperiod=26, matype=0)


def roc(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    Rate of change: ((price/prevPrice)-1)*100
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'roc': t.ROC(df[col].values, period)})


def rocp(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    Rate of change Percentage: (price-prevPrice)/prevPrice
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'rocp': t.ROCP(df[col].values, period)})


def rocr(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    Rate of change ratio: (price/prevPrice)
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'rocr': t.ROCR(df[col].values, period)})


def rocr100(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    Rate of change ratio 100 scale: (price/prevPrice)*100
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'rocr100': t.ROCR100(df[col].values, period)})


def rsi(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    Relative Strength Index
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'rsi': t.RSI(df[col].values, period)})


def stoch(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    '''This will return a dataframe of
    Stochastic
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        fastk_period (int); fastk_period
        slowk_period (int); slowk_period
        slowk_matype (int); slowk_matype
        slowd_period (int); slowd_period
        slowd_matype (int); slowd_matype

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    slowk, slowd = t.STOCH(df[highcol].values, df[lowcol].values, df[closecol].values, fastk_period=fastk_period,
                           slowk_period=slowk_period, slowk_matype=slowk_matype, slowd_period=slowd_period, slowd_matype=slowd_matype)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'slowk': slowk, 'slowd': slowd})


def stochf(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    '''This will return a dataframe of
    Stochastic Fast
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        fastk_period (int); fastk_period
        slowk_period (int); slowk_period
        slowk_matype (int); slowk_matype
        slowd_period (int); slowd_period
        slowd_matype (int); slowd_matype

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    fastk, fastd = t.STOCHF(df[highcol].values, df[lowcol].values, df[closecol].values, fastk_period=fastk_period,
                            slowk_period=slowk_period, slowk_matype=slowk_matype, slowd_period=slowd_period, slowd_matype=slowd_matype)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'fastk': fastk, 'fastd': fastd})


# STOCHRSI - Stochastic Relative Strength Index
# fastk, fastd = STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)


def stochrsi(client, symbol, timeframe='6m', closecol='close', fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    '''This will return a dataframe of
    Williams' % R
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    fastk, fastd = t.STOCHF(df[closecol].values, fastk_period=fastk_period,
                            slowk_period=slowk_period, slowk_matype=slowk_matype, slowd_period=slowd_period, slowd_matype=slowd_matype)
    return pd.DataFrame({closecol: df[closecol].values, 'fastk': fastk, 'fastd': fastd})


def trix(client, symbol, timeframe='6m', col='close', period=14):
    '''This will return a dataframe of
    1-day Rate-Of-Change(ROC) of a Triple Smooth EMA
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    return pd.DataFrame({col: df[col].values, 'trix': t.TRIX(df[col].values, period)})


def ultosc(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', timeperiod1=7, timeperiod2=14, timeperiod3=28):
    '''This will return a dataframe of
    Ultimate Oscillator
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.ULTOSC(df[highcol].values, df[lowcol].values, df[closecol].values, timeperiod1=timeperiod1, timeperiod2=timeperiod2, timeperiod3=timeperiod3)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'ultosc': x})


def willr(client, symbol, timeframe='6m', highcol='high', lowcol='lowcol', closecol='close', period=14):
    '''This will return a dataframe of
    Williams' % R
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        highcol (string); column to use to calculate
        lowcol (string); column to use to calculate
        closecol (string); column to use to calculate
        period (int); period to calculate rsi across

    Returns:
        DataFrame: result
    '''
    df = client.chartDF(symbol, timeframe)
    x = t.WILLR(df[highcol].values, df[lowcol].values, df[closecol].values, period)
    return pd.DataFrame({highcol: df[highcol].values, lowcol: df[lowcol].values, closecol: df[closecol].values, 'willr': x})
