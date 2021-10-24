# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
import talib as t


def ad(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    volumecol="volume",
):
    """This will return a dataframe of Chaikin A/D Line for the given symbol across
    the given range

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
    ad = t.AD(
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
            "a/d": ad,
        }
    )


def adosc(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    volumecol="volume",
    fastperiod=3,
    slowperiod=10,
):
    """This will return a dataframe of Chaikin A/D Oscillator for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        volumecol (string): column to use to calculate
        fastperiod (int): fast period to calculate across
        slowperiod (int): slow period to calculate across
    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    adosc = t.ADOSC(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        df[volumecol].values.astype(float),
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


def obv(client, symbol, range="6m", closecol="close", volumecol="volume"):
    """This will return a dataframe of On Balance Volume for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        closecol (string): column to use to calculate
        volumecol (string): column to use to calculate
    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    obv = t.OBV(df[closecol].values.astype(float), df[volumecol].values.astype(float))
    return pd.DataFrame(
        {closecol: df[closecol].values, volumecol: df[volumecol].values, "obv": obv}
    )
