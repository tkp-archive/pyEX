# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
import talib as t


def atr(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of average true range for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): time period to calculate over

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    atr = t.ATR(
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
            "atr": atr,
        }
    )


def natr(
    client,
    symbol,
    range="6m",
    highcol="high",
    lowcol="low",
    closecol="close",
    period=14,
):
    """This will return a dataframe of normalized average true range for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        period (int): time period to calculate over

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    natr = t.NATR(
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
            "natr": natr,
        }
    )


def trange(client, symbol, range="6m", highcol="high", lowcol="low", closecol="close"):
    """This will return a dataframe of true range for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    trange = t.TRANGE(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "trange": trange,
        }
    )
