# -*- coding: utf-8 -*-
from functools import wraps
from ...stocks import timeSeries, timeSeriesDF
from ...common import _expire, _UTC


@_expire(hour=12, tz=_UTC)
def _base(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeries(**kwargs)


@_expire(hour=12)
def _baseDF(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def kScore(symbol="", **kwargs):
    """Kavout takes in over 200 factors and signals including fundamentals, pricing, technical indicators, and alternative data, and then uses an ensemble machine learning technique to analyze and rank stocks.
    K Score is a stock rating and ranking score with values ranging from 1-to-9. A higher K Score (7-9) assigned to a stock indicates a higher probability of outperformance, whereas a lower K Score (1-3) indicates a lower probability of outperformance in the next month.
    https://iexcloud.io/docs/api/#k-score-for-us-equities

    Args:
        symbol (str): symbol to use
    """
    return _base(id="PREMIUM_KAVOUT_KSCORE", symbol=symbol, **kwargs)


@wraps(timeSeries)
def kScoreDF(symbol="", **kwargs):
    """Kavout takes in over 200 factors and signals including fundamentals, pricing, technical indicators, and alternative data, and then uses an ensemble machine learning technique to analyze and rank stocks.
    K Score is a stock rating and ranking score with values ranging from 1-to-9. A higher K Score (7-9) assigned to a stock indicates a higher probability of outperformance, whereas a lower K Score (1-3) indicates a lower probability of outperformance in the next month.
    https://iexcloud.io/docs/api/#k-score-for-us-equities

    Args:
        symbol (str): symbol to use
    """
    return _baseDF(id="PREMIUM_KAVOUT_KSCORE", symbol=symbol, **kwargs)


@wraps(timeSeries)
def kScoreChina(symbol="", **kwargs):
    """Kavout takes in over 200 factors and signals including fundamentals, pricing, technical indicators, and alternative data, and then uses an ensemble machine learning technique to analyze and rank stocks.
        K Score is a stock rating and ranking score with values ranging from 1-to-9. A higher K Score (7-9) assigned to a stock indicates a higher probability of outperformance, whereas a lower K Score (1-3) indicates a lower probability of outperformance in the next month.
        For quantitative users, overlay K Score as a signal in investment models. Mitigate risk in portfolio construction by avoiding stocks with low K scores (1-3).
        China Stock Market at a Glance
        The China A-share stock market has two exchanges – Shanghai stock exchange (SSE) and Shenzhen stock exchange (SZSE). The SSE and the SZSE are the world’s 5th largest and 8th largest stock market by market capitalization respectively.
        The most important Indices in China A-share are CSI 300, CSI 500 and CSI 800.
        CSI 300 Index consists of the 300 largest and most liquid A-share stocks, similar to the largest 500 stocks by market cap in the US.
        CSI 500 Index consists of the largest remaining 500 A-Share stocks after excluding the CSI 300 Index, similar to the largest 2,000 US stocks by market cap. CSI 500 Index reflects the overall performance of small-mid cap A-shares.
        CSI 800 Index consists of all the constituents of the CSI 300 Index and CSI 500 Index, similar to the largest 3,000 US stocks by market cap.

    https://iexcloud.io/docs/api/#k-score-for-china-a-shares

    Args:
        symbol (str): symbol to use
    """
    return _base(id="PREMIUM_KAVOUT_KSCORE_A_SHARES", symbol=symbol, **kwargs)


@wraps(timeSeries)
def kScoreChinaDF(symbol="", **kwargs):
    """Kavout takes in over 200 factors and signals including fundamentals, pricing, technical indicators, and alternative data, and then uses an ensemble machine learning technique to analyze and rank stocks.
        K Score is a stock rating and ranking score with values ranging from 1-to-9. A higher K Score (7-9) assigned to a stock indicates a higher probability of outperformance, whereas a lower K Score (1-3) indicates a lower probability of outperformance in the next month.
        For quantitative users, overlay K Score as a signal in investment models. Mitigate risk in portfolio construction by avoiding stocks with low K scores (1-3).
        China Stock Market at a Glance
        The China A-share stock market has two exchanges – Shanghai stock exchange (SSE) and Shenzhen stock exchange (SZSE). The SSE and the SZSE are the world’s 5th largest and 8th largest stock market by market capitalization respectively.
        The most important Indices in China A-share are CSI 300, CSI 500 and CSI 800.
        CSI 300 Index consists of the 300 largest and most liquid A-share stocks, similar to the largest 500 stocks by market cap in the US.
        CSI 500 Index consists of the largest remaining 500 A-Share stocks after excluding the CSI 300 Index, similar to the largest 2,000 US stocks by market cap. CSI 500 Index reflects the overall performance of small-mid cap A-shares.
        CSI 800 Index consists of all the constituents of the CSI 300 Index and CSI 500 Index, similar to the largest 3,000 US stocks by market cap.

    https://iexcloud.io/docs/api/#k-score-for-china-a-shares

    Args:
        symbol (str): symbol to use
    """
    return _baseDF(id="PREMIUM_KAVOUT_KSCORE_A_SHARES", symbol=symbol, **kwargs)
