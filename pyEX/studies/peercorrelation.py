# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#


def peerCorrelation(client, symbol, timeframe="6m"):
    """This will return a dataframe of peer correlations for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    peers = client.peers(symbol)
    rets = client.batchDF(peers + [symbol], "chart", timeframe)["chart"]
    ret = rets.pivot(columns="symbol", values="changePercent").corr()
    ret.index.name = "symbol"
    ret.columns = ret.columns.tolist()
    return ret


def peerCorrelationPlot(client, symbol, timeframe="6m"):
    """This will plot a dataframe of peer correlations for the given symbol across
    the given timeframe

    Args:
        client (pyEX.Client); Client
        symbol (string); Ticker
        timeframe (string); timeframe to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    import seaborn as sns

    return sns.heatmap(peerCorrelation)
