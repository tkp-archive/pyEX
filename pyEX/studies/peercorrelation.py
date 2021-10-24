# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#


def peerCorrelation(client, symbol, range="6m"):
    """This will return a dataframe of peer correlations for the given symbol across
    the given range

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    peers = client.peers(symbol)
    rets = client.batchDF(peers + [symbol], "chart", range)["chart"]
    ret = rets.pivot(columns="symbol", values="changePercent").corr()
    ret.index.name = "symbol"
    ret.columns = ret.columns.tolist()
    return ret


def peerCorrelationPlot(client, symbol, range="6m"):
    """This will plot a dataframe of peer correlations for the given symbol across
    the given range

    Note: this function requires the use of `seaborn.heatmap`

    Args:
        client (pyEX.Client): Client
        symbol (string): Ticker
        range (string): range to use, for pyEX.chart

    Returns:
        DataFrame: result
    """
    import seaborn as sns

    return sns.heatmap(peerCorrelation)
