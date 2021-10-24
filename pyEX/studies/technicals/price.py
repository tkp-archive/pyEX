# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
import talib as t


def avgprice(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of average price for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    avg = t.AVGPRICE(
        df[opencol].values.astype(float),
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
    )
    return pd.DataFrame(
        {
            opencol: df[opencol].values,
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "avgprice": avg,
        }
    )


def medprice(client, symbol, range="6m", highcol="high", lowcol="low"):
    """This will return a dataframe of median price for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    med = t.MEDPRICE(df[highcol].values.astype(float), df[lowcol].values.astype(float))
    return pd.DataFrame(
        {highcol: df[highcol].values, lowcol: df[lowcol].values, "medprice": med}
    )


def typprice(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of typical price for the given symbol across
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
    typ = t.TYPPRICE(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "typprice": typ,
        }
    )


def wclprice(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of weighted close price for the given symbol across
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
    wcl = t.WCLPRICE(
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
    )
    return pd.DataFrame(
        {
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "wclprice": wcl,
        }
    )
