# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
import talib as t


def acos(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric ACos
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
    x = t.ACOS(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "acos": x})


def asin(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric ASin
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
    x = t.ASIN(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "asin": x})


def atan(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric ATan
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
    x = t.ATAN(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "atan": x})


def ceil(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Ceil
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
    x = t.CEIL(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "ceil": x})


def cos(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric Cos
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
    x = t.COS(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "cos": x})


def cosh(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric Cosh
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
    x = t.COSH(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "cosh": x})


def exp(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Arithmetic Exp
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
    x = t.EXP(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "exp": x})


def floor(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Floor
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
    x = t.FLOOR(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "floor": x})


def ln(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Log Natural
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
    x = t.LN(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "ln": x})


def log10(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Log10
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
    x = t.LOG10(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "log10": x})


def sin(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric SIN
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
    x = t.SIN(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "sin": x})


def sinh(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric Sinh
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
    x = t.SINH(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "sinh": x})


def sqrt(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Square Root
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
    x = t.SQRT(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "sqrt": x})


def tan(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric Tan
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
    x = t.TAN(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "tan": x})


def tanh(client, symbol, timeframe="6m", col="close"):
    """This will return a dataframe of
    Vector Trigonometric Tanh
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
    x = t.TANH(df[col].values.astype(float))
    return pd.DataFrame({col: df[col].values, "tanh": x})


def add(client, symbol, timeframe="6m", col1="open", col2="close"):
    """This will return a dataframe of
    Vector Arithmetic Add
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col1 (string); column to use to calculate
        col2 (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.ADD(df[col1].values.astype(float), df[col2].values.astype(float))
    return pd.DataFrame({col1: df[col1].values, col2: df[col2].values, "add": x})


def div(client, symbol, timeframe="6m", col1="open", col2="close"):
    """This will return a dataframe of
    Vector Arithmetic Div
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col1 (string); column to use to calculate
        col2 (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.DIV(df[col1].values.astype(float), df[col2].values.astype(float))
    return pd.DataFrame({col1: df[col1].values, col2: df[col2].values, "div": x})


def max(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of
    Highest value over a specified period
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    return t.MAX(df[col].values.astype(float), period)


def maxindex(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of
    Highest value over a specified period
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.MAXINDEX(df[col].values.astype(float), period)
    return x, df[col].values[x]


def min(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of
    Lowest value over a specified period
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    return t.MIN(df[col].values.astype(float), period)


def minindex(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of
    Lowest value over a specified period
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.MININDEX(df[col].values.astype(float), period)
    return x, df[col].values[x]


def minmax(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of
    Lowest and highest values over a specified period
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    return t.MINMAX(df[col].values.astype(float), period)


def minmaxindex(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of
    Indexes of lowest and highest values over a specified period
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x, y = t.MINMAXINDEX(df[col].values.astype(float), period)
    return x, df[col].values[x], y, df[col].values[y]


def mult(client, symbol, timeframe="6m", col1="open", col2="close"):
    """This will return a dataframe of
    Vector Arithmetic Add
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col1 (string); column to use to calculate
        col2 (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.MULT(df[col1].values.astype(float), df[col2].values.astype(float))
    return pd.DataFrame({col1: df[col1].values, col2: df[col2].values, "mult": x})


def sub(client, symbol, timeframe="6m", col1="open", col2="close"):
    """This will return a dataframe of
    Vector Arithmetic Add
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col1 (string); column to use to calculate
        col2 (string); column to use to calculate

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.SUB(df[col1].values.astype(float), df[col2].values.astype(float))
    return pd.DataFrame({col1: df[col1].values, col2: df[col2].values, "sub": x})


def sum(client, symbol, timeframe="6m", col="close", period=30):
    """This will return a dataframe of
    Summation
    for the given symbol across the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart
        col (string); column to use to calculate
        period (int); period

    Returns:
        DataFrame: result
    """
    df = client.chartDF(symbol, timeframe)
    x = t.SUMMATION(df[col].values.astype(float), period)
    return pd.DataFrame({col: df[col].values, "sum": x})
