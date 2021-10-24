# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
import talib as t


def ht_dcperiod(client, symbol, range="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Dominant Cycle Period
    for the given symbol across
    the given range

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        range (string); range to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.HT_DCPERIOD(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "ht_dcperiod": x})


def ht_dcphase(client, symbol, range="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Dominant Cycle Phase
    for the given symbol across
    the given range

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        range (string); range to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.HT_DCPHASE(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "ht_dcphase": x})


def ht_phasor(client, symbol, range="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Phasor Components
    for the given symbol across
    the given range

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        range (string); range to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x, y = t.HT_PHASOR(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "inphase": x, "quadrature": y})


def ht_sine(client, symbol, range="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - SineWave
    for the given symbol across
    the given range

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        range (string); range to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x, y = t.HT_SINE(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "sine": x, "leadsine": y})


def ht_trendmode(client, symbol, range="6m", col="close"):
    """This will return a dataframe of
    Hilbert Transform - Trend vs Cycle Mode
    for the given symbol across
    the given range

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        range (string); range to use, for pyEX.chart
        col (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    x = t.HT_TRENDMODE(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "ht_trendmode": x})
