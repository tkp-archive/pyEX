# -*- coding: utf-8 -*-
from functools import wraps
from ...stocks import timeSeries, timeSeriesDF
from ...common import _expire, _UTC


@_expire(hour=12, tz=_UTC)
def _base(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeries(**kwargs)


@_expire(hour=12)
def _baseDF(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def kScore(symbol='', **kwargs):
    '''Kavout takes in over 200 factors and signals including fundamentals, pricing, technical indicators, and alternative data, and then uses an ensemble machine learning technique to analyze and rank stocks.
    K Score is a stock rating and ranking score with values ranging from 1-to-9. A higher K Score (7-9) assigned to a stock indicates a higher probability of outperformance, whereas a lower K Score (1-3) indicates a lower probability of outperformance in the next month.
    https://iexcloud.io/docs/api/#k-score-for-us-equities
    '''
    return _base(id='PREMIUM_KAVOUT_KSCORE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def kScoreDF(symbol='', **kwargs):
    '''Kavout takes in over 200 factors and signals including fundamentals, pricing, technical indicators, and alternative data, and then uses an ensemble machine learning technique to analyze and rank stocks.
    K Score is a stock rating and ranking score with values ranging from 1-to-9. A higher K Score (7-9) assigned to a stock indicates a higher probability of outperformance, whereas a lower K Score (1-3) indicates a lower probability of outperformance in the next month.
    https://iexcloud.io/docs/api/#k-score-for-us-equities
    '''
    return _baseDF(id='PREMIUM_KAVOUT_KSCORE', symbol=symbol, **kwargs)
