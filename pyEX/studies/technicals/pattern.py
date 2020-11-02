# -*- coding: utf-8 -*-
import talib as t
import pandas as pd


def cdl2crows(
    client,
    symbol,
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of Two crows for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDL2CROWS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 black crows for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDL3BLACKCROWS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 inside up/down for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDL3INSIDE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 line strike for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDL3LINESTRIKE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 outside for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDL3OUTSIDE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 stars in south for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDL3STARSINSOUTH(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of 3 white soldiers for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDL3WHITESOLDIERS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of abandoned baby for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLABANDONEDBABY(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of advance block for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLADVANCEBLOCK(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of belt hold for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLBELTHOLD(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of breakaway for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLBREAKAWAY(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of closing maru bozu for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLCLOSINGMARUBOZU(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of conceal baby swallow for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLCONCEALBABYSWALL(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of counterattack for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLCOUNTERATTACK(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of dark cloud cover for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLDARKCLOUDCOVER(
        df[opencol].values,
        df[highcol].values,
        df[lowcol].values,
        df[closecol].values,
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of doji for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLDOJI(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of doji star for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLDOJISTAR(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of dragonfly doji for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLDRAGONFLYDOJI(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of engulfing for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLENGULFING(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of evening doji star for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLEVENINGDOJISTAR(
        df[opencol].values,
        df[highcol].values,
        df[lowcol].values,
        df[closecol].values,
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of evening star for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLEVENINGSTAR(
        df[opencol].values,
        df[highcol].values,
        df[lowcol].values,
        df[closecol].values,
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of up.down-gap side-by-side white lines for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLGAPSIDESIDEWHITE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of gravestone doji for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLGRAVESTONEDOJI(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of hammer for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHAMMER(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of hanging man for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHANGINGMAN(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of harami for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHARAMI(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of harami cross for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHARAMICROSS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of high-wave candle for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHIGHWAVE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of hikkake pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHIKKAKE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of modified hikkake pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHIKKAKEMOD(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of homing pigeon for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLHOMINGPIGEON(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of identical three crows for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLIDENTICAL3CROWS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of in-neck pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLINNECK(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of inverted hammer for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLINVERTEDHAMMER(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of kicking for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLKICKING(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of kicking bull/bear determing by the longer marubozu for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLKICKINGBYLENGTH(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of ladder bottom for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLLADDERBOTTOM(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of long legged doji for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLLONGLEGGEDDOJI(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of long line candle for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLLONGLINE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of marubozu for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLMARUBOZU(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of matching low for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLMATCHINGLOW(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of mat hold for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLMATHOLD(
        df[opencol].values,
        df[highcol].values,
        df[lowcol].values,
        df[closecol].values,
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of morning doji star for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLMORNINGDOJISTAR(
        df[opencol].values,
        df[highcol].values,
        df[lowcol].values,
        df[closecol].values,
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
    penetration=0,
):
    """This will return a dataframe of morning star for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate
        penetration (int): penetration

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLMORNINGSTAR(
        df[opencol].values,
        df[highcol].values,
        df[lowcol].values,
        df[closecol].values,
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of on-neck pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLONNECK(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of piercing pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLPIERCING(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of rickshaw man for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLRICKSHAWMAN(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of rising/falling three methods for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLRISEFALL3METHODS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of separating lines for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLSEPARATINGLINES(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of shooting star for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLSHOOTINGSTAR(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of short line candle for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLSHORTLINE(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of spinning top for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLSPINNINGTOP(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of stalled pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLSTALLEDPATTERN(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of stick sandwich for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLSTICKSANDWICH(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of takuri dragonfly doji with very long lower shadow for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLTAKURI(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of tasuki gap for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLTASUKIGAP(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of thrusting pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLTHRUSTING(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of tristar pattern for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLTRISTAR(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of unique 3 river for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLUNIQUE3RIVER(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of upside gap two crows for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLUPSIDEGAP2CROWS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
    timeframe="6m",
    opencol="open",
    highcol="high",
    lowcol="low",
    closecol="close",
):
    """This will return a dataframe of upside/downside gap three methods for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        timeframe (string): timeframe to use, for pyEX.chart
        opencol (string): column to use to calculate
        highcol (string): column to use to calculate
        lowcol (string): column to use to calculate
        closecol (string): column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    val = t.CDLXSIDEGAP3METHODS(
        df[opencol].values, df[highcol].values, df[lowcol].values, df[closecol].values
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
