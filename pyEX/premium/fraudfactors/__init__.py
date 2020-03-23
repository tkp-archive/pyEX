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
def similarityIndex(symbol='', **kwargs):
    '''The Similarity Index quantifies the textual differences between a given company’s annual or quarterly filings on an “as disclosed” basis. For example, a similarity score is calculated by comparing a company’s 2017 10-K with the 2016 10-K; or a company’s 2017 Q3 10-Q compared to the 2016 Q3 10-Q a year ago.
    Intuitively, firms breaking from routine phrasing and content in mandatory disclosures give clues about their future performance which eventually drive stock returns over time. This data set captures significant changes in disclosure texts in the form of low similarity scores.
    Academic research has shown that a portfolio that shorts low similarity scores and longs high similarity scores earns non-trivial and uncorrelated returns over a period of 12-18 months.
    Data available from 2001 with coverage of about 23,000 equities

    https://iexcloud.io/docs/api/#similiarity-index
    '''
    return _base(id='PREMIUM_FRAUD_FACTORS_SIMILARITY_INDEX', symbol=symbol, **kwargs)


@wraps(timeSeries)
def similarityIndexDF(symbol='', **kwargs):
    '''The Similarity Index quantifies the textual differences between a given company’s annual or quarterly filings on an “as disclosed” basis. For example, a similarity score is calculated by comparing a company’s 2017 10-K with the 2016 10-K; or a company’s 2017 Q3 10-Q compared to the 2016 Q3 10-Q a year ago.
    Intuitively, firms breaking from routine phrasing and content in mandatory disclosures give clues about their future performance which eventually drive stock returns over time. This data set captures significant changes in disclosure texts in the form of low similarity scores.
    Academic research has shown that a portfolio that shorts low similarity scores and longs high similarity scores earns non-trivial and uncorrelated returns over a period of 12-18 months.
    Data available from 2001 with coverage of about 23,000 equities

    https://iexcloud.io/docs/api/#similiarity-index
    '''
    return _baseDF(id='PREMIUM_FRAUD_FACTORS_SIMILARITY_INDEX', symbol=symbol, **kwargs)


@wraps(timeSeries)
def nonTimelyFilings(symbol='', **kwargs):
    '''The data set records the date in which a firm files a Non-Timely notification with the SEC.
    Companies regulated by the SEC are required to file a Non-Timely notification when they are unable to file their annual or quarterly disclosures on time. In most cases, the inability to file annual/quarterly disclosures on time is a red-flag and thus a valuable signal for algorithmic strategies and fundamental investing alike.
    Data available from 1994 with coverage of about 18,000 equities
    https://iexcloud.io/docs/api/#non-timely-filings
    '''
    return _base(id='PREMIUM_FRAUD_FACTORS_NON_TIMELY_FILINGS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def nonTimelyFilingsDF(symbol='', **kwargs):
    '''The data set records the date in which a firm files a Non-Timely notification with the SEC.
    Companies regulated by the SEC are required to file a Non-Timely notification when they are unable to file their annual or quarterly disclosures on time. In most cases, the inability to file annual/quarterly disclosures on time is a red-flag and thus a valuable signal for algorithmic strategies and fundamental investing alike.
    Data available from 1994 with coverage of about 18,000 equities
    https://iexcloud.io/docs/api/#non-timely-filings
    '''
    return _baseDF(id='PREMIUM_FRAUD_FACTORS_NON_TIMELY_FILINGS', symbol=symbol, **kwargs)
