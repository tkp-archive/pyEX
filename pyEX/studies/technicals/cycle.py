# -*- coding: utf-8 -*-
import talib as t
import pandas as pd


def ht_dcperiod(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Dominant Cycle Period
    for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.HT_DCPERIOD(df[col].values)
    return pd.DataFrame({col: df[col].values, "ht_dcperiod": x})


def ht_dcphase(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Dominant Cycle Phase
    for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.HT_DCPHASE(df[col].values)
    return pd.DataFrame({col: df[col].values, "ht_dcphase": x})


def ht_phasor(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Phasor Components
    for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x, y = t.HT_PHASOR(df[col].values)
    return pd.DataFrame({col: df[col].values, "inphase": x, "quadrature": y})


def ht_sine(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - SineWave
    for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x, y = t.HT_SINE(df[col].values)
    return pd.DataFrame({col: df[col].values, "sine": x, "leadsine": y})


def ht_trendmode(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Trend vs Cycle Mode
    for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.HT_TRENDMODE(df[col].values)
    return pd.DataFrame({col: df[col].values, "ht_trendmode": x})
