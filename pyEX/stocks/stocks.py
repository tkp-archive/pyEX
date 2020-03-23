# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _getJson, _raiseIfNotStr, _strOrDate, _toDatetime, _EST


def threshold(date=None, token='', version='', filter=''):
    '''The following are IEX-listed securities that have an aggregate fail to deliver position for five consecutive settlement days at a registered clearing agency, totaling 10,000 shares or more and equal to at least 0.5% of the issuer’s total shares outstanding (i.e., “threshold securities”).
    The report data will be published to the IEX website daily at 8:30 p.m. ET with data for that trading day.

    https://iexcloud.io/docs/api/#listed-regulation-sho-threshold-securities-list-in-dev

    Args:
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/threshold-securities/' + date, token, version, filter)
    return _getJson('stock/market/threshold-securities', token, version, filter)


def thresholdDF(date=None, token='', version='', filter=''):
    '''The following are IEX-listed securities that have an aggregate fail to deliver position for five consecutive settlement days at a registered clearing agency, totaling 10,000 shares or more and equal to at least 0.5% of the issuer’s total shares outstanding (i.e., “threshold securities”).
    The report data will be published to the IEX website daily at 8:30 p.m. ET with data for that trading day.

    https://iexcloud.io/docs/api/#listed-regulation-sho-threshold-securities-list-in-dev

    Args:
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(threshold(date, token, version, filter))
    _toDatetime(df)
    return df


@_expire(hour=16, tz=_EST)
def shortInterest(symbol, date=None, token='', version='', filter=''):
    '''The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        symbol (string); Ticker to request
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/short-interest/' + date, token, version, filter)
    return _getJson('stock/' + symbol + '/short-interest', token, version, filter)


def shortInterestDF(symbol, date=None, token='', version='', filter=''):
    '''The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        symbol (string); Ticker to request
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(shortInterest(symbol, date, token, version, filter))
    _toDatetime(df)
    return df
