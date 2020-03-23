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
def precisionAlphaPriceDynamics(symbol='', **kwargs):
    '''Precision Alpha performs an unbiased non-equilibrium market analysis on six months of closing price data for all NASDAQ and NYSE listed equities, every day after market close. Precision Alpha calculates scientifically and exactly: market emotion, power, resistance, noise/efficiency, and next day probabilities
    https://iexcloud.io/docs/api/#precision-alpha-price-dynamics
    '''
    return _base(id='PREMIUM_PRECISION_ALPHA_PRICE_DYNAMICS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def precisionAlphaPriceDynamicsDF(symbol='', **kwargs):
    '''Precision Alpha performs an unbiased non-equilibrium market analysis on six months of closing price data for all NASDAQ and NYSE listed equities, every day after market close. Precision Alpha calculates scientifically and exactly: market emotion, power, resistance, noise/efficiency, and next day probabilities
    https://iexcloud.io/docs/api/#precision-alpha-price-dynamics
    '''
    return _baseDF(id='PREMIUM_PRECISION_ALPHA_PRICE_DYNAMICS', symbol=symbol, **kwargs)
