# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ...common import _UTC, _expire
from ...timeseries import timeSeries, timeSeriesDF


@_expire(hour=8, tz=_UTC)
def _base(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeries(**kwargs)


@_expire(hour=8, tz=_UTC)
def _baseDF(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def thirtyDaySentimentBrain(symbol="", **kwargs):
    """Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 30 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-30-day-sentiment-indicator

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_SENTIMENT_30_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def thirtyDaySentimentBrainDF(symbol="", **kwargs):
    """Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 30 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-30-day-sentiment-indicator

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_SENTIMENT_30_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def sevenDaySentimentBrain(symbol="", **kwargs):
    """Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 7 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-7-day-sentiment-indicator

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_SENTIMENT_7_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def sevenDaySentimentBrainDF(symbol="", **kwargs):
    """Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 7 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-7-day-sentiment-indicator

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_SENTIMENT_7_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def twentyOneDayMLReturnRankingBrain(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 21 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-21-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_RANKING_21_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def twentyOneDayMLReturnRankingBrainDF(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 21 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-21-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_RANKING_21_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def tenDayMLReturnRankingBrain(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-10-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_RANKING_10_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def tenDayMLReturnRankingBrainDF(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-10-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_RANKING_10_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def fiveDayMLReturnRankingBrain(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-5-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_RANKING_5_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def fiveDayMLReturnRankingBrainDF(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-5-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_RANKING_5_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def threeDayMLReturnRankingBrain(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-3-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_RANKING_3_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def threeDayMLReturnRankingBrainDF(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-3-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_RANKING_3_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def twoDayMLReturnRankingBrain(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-2-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_RANKING_2_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def twoDayMLReturnRankingBrainDF(symbol="", **kwargs):
    """Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-2-day-machine-learning-estimated-return-ranking

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_RANKING_2_DAYS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsAllBrain(symbol="", **kwargs):
    """Metrics about the language used in a company’s most recent annual or quarterly filings (10Ks and 10Qs). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-quarterly-and-annual

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_LANGUAGE_METRICS_ALL", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsAllBrainDF(symbol="", **kwargs):
    """Metrics about the language used in a company’s most recent annual or quarterly filings (10Ks and 10Qs). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-quarterly-and-annual

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_LANGUAGE_METRICS_ALL", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsBrain(symbol="", **kwargs):
    """Metrics about the language used in a company’s most recent annual filing (10Ks). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-annual-only

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_LANGUAGE_METRICS_10K", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsBrainDF(symbol="", **kwargs):
    """Metrics about the language used in a company’s most recent annual filing (10Ks). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-annual-only

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_LANGUAGE_METRICS_10K", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsDifferenceAllBrain(symbol="", **kwargs):
    """Compares Brain’s sentiment and language metrics from the company’s most recent repot (annual or quarterly) to the report from last year (10Ks) or the corresponding quarter the prior year (10Qs).
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-filings-quarterly-and-annual-from-prior-period

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_ALL", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsDifferenceAllBrainDF(symbol="", **kwargs):
    """Compares Brain’s sentiment and language metrics from the company’s most recent repot (annual or quarterly) to the report from last year (10Ks) or the corresponding quarter the prior year (10Qs).
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-filings-quarterly-and-annual-from-prior-period

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_ALL", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsDifferenceBrain(symbol="", **kwargs):
    """Compares Brain’s sentiment and language metrics from the company’s most recent annual filing (10K) to the report from last year.
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_10K", symbol=symbol, **kwargs)


@wraps(timeSeries)
def languageMetricsOnCompanyFilingsDifferenceBrainDF(symbol="", **kwargs):
    """Compares Brain’s sentiment and language metrics from the company’s most recent annual filing (10K) to the report from last year.
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_10K", symbol=symbol, **kwargs)
