# -*- coding: utf-8 -*-
from functools import wraps
from ...stocks import timeSeries, timeSeriesDF
from ...common import _expire, _UTC


@_expire(hour=10, minute=30, tz=_UTC)
def _base(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeries(**kwargs)


@_expire(hour=10, minute=30, tz=_UTC)
def _baseDF(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def directorAndOfficerChanges(symbol='', **kwargs):
    '''The Director & Officer Changes data set covers all SEC registrants who have disclosed a director or officer change in Item 5.02 of an 8-K or 8-K/A since August 2004. As of January 1, 2018, the dataset also includes director or officer change disclosures in 6-K & 6-K/A filings.
    https://iexcloud.io/docs/api/#audit-analytics-director-and-officer-changes
    '''
    return _base(id='PREMIUM_AUDIT_ANALYTICS_DIRECTOR_OFFICER_CHANGES', symbol=symbol, **kwargs)


@wraps(timeSeries)
def directorAndOfficerChangesDF(symbol='', **kwargs):
    '''The Director & Officer Changes data set covers all SEC registrants who have disclosed a director or officer change in Item 5.02 of an 8-K or 8-K/A since August 2004. As of January 1, 2018, the dataset also includes director or officer change disclosures in 6-K & 6-K/A filings.
    https://iexcloud.io/docs/api/#audit-analytics-director-and-officer-changes
    '''
    return _baseDF(id='PREMIUM_AUDIT_ANALYTICS_DIRECTOR_OFFICER_CHANGES', symbol=symbol, **kwargs)


@wraps(timeSeries)
def accountingQualityAndRiskMatrix(symbol='', **kwargs):
    '''AQRM is an interactive tool designed to quickly identify and understand qualitative and contextual metrics of governance and reporting quality. Red flags and events highlighted in the risk matrix can be used for screening, idea generation, portfolio monitoring, and risk management for every SEC registrant.
    https://iexcloud.io/docs/api/#audit-analytics-accounting-quality-and-risk-matrix
    '''
    return _base(id='PREMIUM_AUDIT_ANALYTICS_ACCOUNTING_QUALITY_RISK_MATRIX', symbol=symbol, **kwargs)


@wraps(timeSeries)
def accountingQualityAndRiskMatrixDF(symbol='', **kwargs):
    '''AQRM is an interactive tool designed to quickly identify and understand qualitative and contextual metrics of governance and reporting quality. Red flags and events highlighted in the risk matrix can be used for screening, idea generation, portfolio monitoring, and risk management for every SEC registrant.
    https://iexcloud.io/docs/api/#audit-analytics-accounting-quality-and-risk-matrix
    '''
    return _baseDF(id='PREMIUM_AUDIT_ANALYTICS_ACCOUNTING_QUALITY_RISK_MATRIX', symbol=symbol, **kwargs)
