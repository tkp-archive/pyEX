# -*- coding: utf-8 -*-
from functools import wraps
from ...stocks import timeSeries, timeSeriesDF
from ...common import _expire, _UTC


@_expire(hour=8, tz=_UTC)
def _base(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeries(**kwargs)


@_expire(hour=8, tz=_UTC)
def _baseDF(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def brain30DaySentiment(symbol='', **kwargs):
    '''Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 30 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-30-day-sentiment-indicator
    '''
    return _base(id='PREMIUM_BRAIN_SENTIMENT_30_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain30DaySentimentDF(symbol='', **kwargs):
    '''Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 30 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-30-day-sentiment-indicator
    '''
    return _baseDF(id='PREMIUM_BRAIN_SENTIMENT_30_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain7DaySentiment(symbol='', **kwargs):
    '''Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 7 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-7-day-sentiment-indicator
    '''
    return _base(id='PREMIUM_BRAIN_SENTIMENT_7_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain7DaySentimentDF(symbol='', **kwargs):
    '''Brain Company’s Sentiment Indicator monitors the stock sentiment from the last 7 days of public financial news for about 3,500 US stocks. The sentiment scoring technology is based on a combination of various natural language processing techniques. The sentiment score assigned to each stock is a value ranging from -1 (most negative) to +1 (most positive) that is updated daily.
    https://iexcloud.io/docs/api/#brain-companys-7-day-sentiment-indicator
    '''
    return _baseDF(id='PREMIUM_BRAIN_SENTIMENT_7_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain21DayMLReturnRanking(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 21 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-21-day-machine-learning-estimated-return-ranking
    '''
    return _base(id='PREMIUM_BRAIN_RANKING_21_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain21DayMLReturnRankingDF(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 21 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-21-day-machine-learning-estimated-return-ranking
    '''
    return _baseDF(id='PREMIUM_BRAIN_RANKING_21_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain10DayMLReturnRanking(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-10-day-machine-learning-estimated-return-ranking
    '''
    return _base(id='PREMIUM_BRAIN_RANKING_10_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain10DayMLReturnRankingDF(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-10-day-machine-learning-estimated-return-ranking
    '''
    return _baseDF(id='PREMIUM_BRAIN_RANKING_10_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain5DayMLReturnRanking(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-5-day-machine-learning-estimated-return-ranking
    '''
    return _base(id='PREMIUM_BRAIN_RANKING_5_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain5DayMLReturnRankingDF(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-5-day-machine-learning-estimated-return-ranking
    '''
    return _baseDF(id='PREMIUM_BRAIN_RANKING_5_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain3DayMLReturnRanking(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-3-day-machine-learning-estimated-return-ranking
    '''
    return _base(id='PREMIUM_BRAIN_RANKING_3_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain3DayMLReturnRankingDF(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-3-day-machine-learning-estimated-return-ranking
    '''
    return _baseDF(id='PREMIUM_BRAIN_RANKING_3_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain2DayMLReturnRanking(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-2-day-machine-learning-estimated-return-ranking
    '''
    return _base(id='PREMIUM_BRAIN_RANKING_2_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brain2DayMLReturnRankingDF(symbol='', **kwargs):
    '''Brain Company’s Machine Learning proprietary platform is used to generate a daily stock ranking based on the predicted future returns of a universe of around 1,000 stocks over 10 days. The model implements a voting scheme of machine learning classifiers that non linearly combine a variety of features with a series of techniques aimed at mitigating the well-known overfitting problem for financial data with a low signal to noise ratio.
    https://iexcloud.io/docs/api/#brain-companys-2-day-machine-learning-estimated-return-ranking
    '''
    return _baseDF(id='PREMIUM_BRAIN_RANKING_2_DAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilingsAll(symbol='', **kwargs):
    '''Metrics about the language used in a company’s most recent annual or quarterly filings (10Ks and 10Qs). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-quarterly-and-annual
    '''
    return _base(id='PREMIUM_BRAIN_LANGUAGE_METRICS_ALL', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilingsAllDF(symbol='', **kwargs):
    '''Metrics about the language used in a company’s most recent annual or quarterly filings (10Ks and 10Qs). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-quarterly-and-annual
    '''
    return _baseDF(id='PREMIUM_BRAIN_LANGUAGE_METRICS_ALL', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilings(symbol='', **kwargs):
    '''Metrics about the language used in a company’s most recent annual filing (10Ks). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-annual-only
    '''
    return _base(id='PREMIUM_BRAIN_LANGUAGE_METRICS_10K', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilingsDF(symbol='', **kwargs):
    '''Metrics about the language used in a company’s most recent annual filing (10Ks). Includes metrics on the financial sentiment and the scores based on the prevalence of words in the statement categorized into four themes: constraining language, interesting language, litigious language, and language indicating uncertainty.
    https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-annual-only
    '''
    return _baseDF(id='PREMIUM_BRAIN_LANGUAGE_METRICS_10K', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilingsDifferenceAll(symbol='', **kwargs):
    '''Compares Brain’s sentiment and language metrics from the company’s most recent repot (annual or quarterly) to the report from last year (10Ks) or the corresponding quarter the prior year (10Qs).
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-filings-quarterly-and-annual-from-prior-period
    '''
    return _base(id='PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_ALL', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilingsDifferenceAllDF(symbol='', **kwargs):
    '''Compares Brain’s sentiment and language metrics from the company’s most recent repot (annual or quarterly) to the report from last year (10Ks) or the corresponding quarter the prior year (10Qs).
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-filings-quarterly-and-annual-from-prior-period
    '''
    return _baseDF(id='PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_ALL', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilingsDifference(symbol='', **kwargs):
    '''Compares Brain’s sentiment and language metrics from the company’s most recent annual filing (10K) to the report from last year.
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year
    '''
    return _base(id='PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_10K', symbol=symbol, **kwargs)


@wraps(timeSeries)
def brainLanguageMetricsOnCompanyFilingsDifferenceDF(symbol='', **kwargs):
    '''Compares Brain’s sentiment and language metrics from the company’s most recent annual filing (10K) to the report from last year.
    https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year
    '''
    return _baseDF(id='PREMIUM_BRAIN_LANGUAGE_DIFFERENCES_10K', symbol=symbol, **kwargs)
