# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
import talib as t


def cdl2crows(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of Two crows for the given symbol across
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
    val = t.CDL2CROWS(
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
            "cdl2crows": val,
        }
    )


def cdl3blackcrows(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 black crows for the given symbol across
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
    val = t.CDL3BLACKCROWS(
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
            "cdl3blackcrows": val,
        }
    )


def cdl3inside(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 inside up/down for the given symbol across
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
    val = t.CDL3INSIDE(
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
            "cdl3inside": val,
        }
    )


def cdl3linestrike(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 line strike for the given symbol across
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
    val = t.CDL3LINESTRIKE(
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
            "cdl3linestrike": val,
        }
    )


def cdl3outside(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 outside for the given symbol across
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
    val = t.CDL3OUTSIDE(
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
            "cdl3outside": val,
        }
    )


def cdl3starsinsouth(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 stars in south for the given symbol across
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
    val = t.CDL3STARSINSOUTH(
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
            "cdl3starsinsouth": val,
        }
    )


def cdl3whitesoldiers(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 white soldiers for the given symbol across
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
    val = t.CDL3WHITESOLDIERS(
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
            "cdl3whitesoldiers": val,
        }
    )


def cdlabandonedbaby(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of abandoned baby for the given symbol across
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
    val = t.CDLABANDONEDBABY(
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
            "cdlabandonedbaby": val,
        }
    )


def cdladvanceblock(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of advance block for the given symbol across
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
    val = t.CDLADVANCEBLOCK(
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
            "cdladvanceblock": val,
        }
    )


def cdlbelthold(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of belt hold for the given symbol across
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
    val = t.CDLBELTHOLD(
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
            "cdlbelthold": val,
        }
    )


def cdlbreakaway(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of breakaway for the given symbol across
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
    val = t.CDLBREAKAWAY(
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
            "cdlbreakaway": val,
        }
    )


def cdlclosingmarubozu(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of closing maru bozu for the given symbol across
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
    val = t.CDLCLOSINGMARUBOZU(
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
            "cdlclosingmarubozu": val,
        }
    )


def cdlconcealbabyswallow(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of conceal baby swallow for the given symbol across
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
    val = t.CDLCONCEALBABYSWALL(
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
            "cdlconcealbabyswallow": val,
        }
    )


def cdlcounterattack(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of counterattack for the given symbol across
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
    val = t.CDLCOUNTERATTACK(
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
            "cdlcounterattack": val,
        }
    )


def cdldarkcloudcover(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of dark cloud cover for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    val = t.CDLDARKCLOUDCOVER(
        df[opencol].values.astype(float),
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        penetration,
    )
    return pd.DataFrame(
        {
            opencol: df[opencol].values,
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "cdldarkcloudcover": val,
        }
    )


def cdldoji(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of doji for the given symbol across
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
    val = t.CDLDOJI(
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
            "cdldoji": val,
        }
    )


def cdldojistar(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of doji star for the given symbol across
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
    val = t.CDLDOJISTAR(
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
            "cdldojistar": val,
        }
    )


def cdldragonflydoji(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of dragonfly doji for the given symbol across
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
    val = t.CDLDRAGONFLYDOJI(
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
            "cdldragonflydoji": val,
        }
    )


def cdlengulfing(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of engulfing for the given symbol across
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
    val = t.CDLENGULFING(
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
            "cdlengulfing": val,
        }
    )


def cdleveningdojistar(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of evening doji star for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    val = t.CDLEVENINGDOJISTAR(
        df[opencol].values.astype(float),
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        penetration,
    )
    return pd.DataFrame(
        {
            opencol: df[opencol].values,
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "cdleveningdojistar": val,
        }
    )


def cdleveningstar(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of evening star for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    val = t.CDLEVENINGSTAR(
        df[opencol].values.astype(float),
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        penetration,
    )
    return pd.DataFrame(
        {
            opencol: df[opencol].values,
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "cdleveningstar": val,
        }
    )


def cdlgapsidesidewhite(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of up.down-gap side-by-side white lines for the given symbol across
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
    val = t.CDLGAPSIDESIDEWHITE(
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
            "cdlgapsidesidewhite": val,
        }
    )


def cdlgravestonedoji(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of gravestone doji for the given symbol across
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
    val = t.CDLGRAVESTONEDOJI(
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
            "cdlgravestonedoji": val,
        }
    )


def cdlhammer(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of hammer for the given symbol across
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
    val = t.CDLHAMMER(
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
            "cdlhammer": val,
        }
    )


def cdlhangingman(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of hanging man for the given symbol across
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
    val = t.CDLHANGINGMAN(
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
            "cdlhangingman": val,
        }
    )


def cdlharami(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of harami for the given symbol across
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
    val = t.CDLHARAMI(
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
            "cdlharami": val,
        }
    )


def cdlharamicross(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of harami cross for the given symbol across
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
    val = t.CDLHARAMICROSS(
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
            "cdlharamicross": val,
        }
    )


def cdlhighwave(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of high-wave candle for the given symbol across
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
    val = t.CDLHIGHWAVE(
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
            "cdlhighwave": val,
        }
    )


def cdlhikkake(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of hikkake pattern for the given symbol across
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
    val = t.CDLHIKKAKE(
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
            "cdlhikkake": val,
        }
    )


def cdlhikkakemod(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of modified hikkake pattern for the given symbol across
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
    val = t.CDLHIKKAKEMOD(
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
            "cdlhikkakemod": val,
        }
    )


def cdlhomingpigeon(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of homing pigeon for the given symbol across
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
    val = t.CDLHOMINGPIGEON(
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
            "cdlhomingpigeon": val,
        }
    )


def cdlidentical3crows(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of identical three crows for the given symbol across
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
    val = t.CDLIDENTICAL3CROWS(
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
            "cdlidentical3crows": val,
        }
    )


def cdlinneck(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of in-neck pattern for the given symbol across
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
    val = t.CDLINNECK(
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
            "cdlinneck": val,
        }
    )


def cdlinvertedhammer(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of inverted hammer for the given symbol across
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
    val = t.CDLINVERTEDHAMMER(
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
            "cdlinvertedhammer": val,
        }
    )


def cdlkicking(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of kicking for the given symbol across
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
    val = t.CDLKICKING(
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
            "cdlkicking": val,
        }
    )


def cdlkickingbylength(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of kicking bull/bear determing by the longer marubozu for the given symbol across
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
    val = t.CDLKICKINGBYLENGTH(
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
            "cdlkickingbylength": val,
        }
    )


def cdlladderbottom(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of ladder bottom for the given symbol across
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
    val = t.CDLLADDERBOTTOM(
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
            "cdlladderbottom": val,
        }
    )


def cdllongleggeddoji(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of long legged doji for the given symbol across
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
    val = t.CDLLONGLEGGEDDOJI(
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
            "cdllongleggeddoji": val,
        }
    )


def cdllongline(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of long line candle for the given symbol across
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
    val = t.CDLLONGLINE(
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
            "cdllongline": val,
        }
    )


def cdlmarubozu(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of marubozu for the given symbol across
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
    val = t.CDLMARUBOZU(
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
            "cdlmarubozu": val,
        }
    )


def cdlmatchinglow(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of matching low for the given symbol across
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
    val = t.CDLMATCHINGLOW(
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
            "cdlmatchinglow": val,
        }
    )


def cdlmathold(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of mat hold for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    val = t.CDLMATHOLD(
        df[opencol].values.astype(float),
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        penetration,
    )
    return pd.DataFrame(
        {
            opencol: df[opencol].values,
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "cdlmathold": val,
        }
    )


def cdlmorningdojistar(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of morning doji star for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    val = t.CDLMORNINGDOJISTAR(
        df[opencol].values.astype(float),
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        penetration,
    )
    return pd.DataFrame(
        {
            opencol: df[opencol].values,
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "cdlmorningdojistar": val,
        }
    )


def cdlmorningstar(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of morning star for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, range)
    val = t.CDLMORNINGSTAR(
        df[opencol].values.astype(float),
        df[highcol].values.astype(float),
        df[lowcol].values.astype(float),
        df[closecol].values.astype(float),
        penetration,
    )
    return pd.DataFrame(
        {
            opencol: df[opencol].values,
            highcol: df[highcol].values,
            lowcol: df[lowcol].values,
            closecol: df[closecol].values,
            "cdlmorningstar": val,
        }
    )


def cdlonneck(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of on-neck pattern for the given symbol across
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
    val = t.CDLONNECK(
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
            "cdlonneck": val,
        }
    )


def cdlpiercing(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of piercing pattern for the given symbol across
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
    val = t.CDLPIERCING(
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
            "cdlpiercing": val,
        }
    )


def cdlrickshawman(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of rickshaw man for the given symbol across
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
    val = t.CDLRICKSHAWMAN(
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
            "cdlrickshawman": val,
        }
    )


def cdlrisefall3methods(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of rising/falling three methods for the given symbol across
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
    val = t.CDLRISEFALL3METHODS(
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
            "cdlrisefall3methods": val,
        }
    )


def cdlseparatinglines(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of separating lines for the given symbol across
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
    val = t.CDLSEPARATINGLINES(
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
            "cdlseparatinglines": val,
        }
    )


def cdlshootingstar(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of shooting star for the given symbol across
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
    val = t.CDLSHOOTINGSTAR(
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
            "cdlshootingstar": val,
        }
    )


def cdlshortline(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of short line candle for the given symbol across
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
    val = t.CDLSHORTLINE(
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
            "cdlshortline": val,
        }
    )


def cdlspinningtop(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of spinning top for the given symbol across
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
    val = t.CDLSPINNINGTOP(
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
            "cdlspinningtop": val,
        }
    )


def cdlstalledpattern(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of stalled pattern for the given symbol across
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
    val = t.CDLSTALLEDPATTERN(
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
            "cdlstalledpattern": val,
        }
    )


def cdlsticksandwich(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of stick sandwich for the given symbol across
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
    val = t.CDLSTICKSANDWICH(
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
            "cdlsticksandwich": val,
        }
    )


def cdltakuri(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of takuri dragonfly doji with very long lower shadow for the given symbol across
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
    val = t.CDLTAKURI(
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
            "cdltakuri": val,
        }
    )


def cdltasukigap(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of tasuki gap for the given symbol across
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
    val = t.CDLTASUKIGAP(
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
            "cdltasukigap": val,
        }
    )


def cdlthrusting(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of thrusting pattern for the given symbol across
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
    val = t.CDLTHRUSTING(
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
            "cdlthrusting": val,
        }
    )


def cdltristar(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of tristar pattern for the given symbol across
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
    val = t.CDLTRISTAR(
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
            "cdltristar": val,
        }
    )


def cdlunique3river(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of unique 3 river for the given symbol across
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
    val = t.CDLUNIQUE3RIVER(
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
            "cdlunique3river": val,
        }
    )


def cdlupsidegap2crows(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of upside gap two crows for the given symbol across
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
    val = t.CDLUPSIDEGAP2CROWS(
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
            "cdlupsidegap2crows": val,
        }
    )


def cdlxsidegap3methods(
    client,
    symbol,
    range="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of upside/downside gap three methods for the given symbol across
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
    val = t.CDLXSIDEGAP3METHODS(
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
            "cdlxsidegap3methods": val,
        }
    )
