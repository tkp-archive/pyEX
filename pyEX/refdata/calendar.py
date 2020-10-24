# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _expire, _getJson, _strOrDate, _toDatetime


@_expire(hour=8)
def calendar(type='holiday', direction='next', last=1, startDate=None, token='', version='', filter=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        type (str): "holiday" or "trade"
        direction (str): "next" or "last"
        last (int): number to move in direction
        startDate (date): start date for next or last, YYYYMMDD
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if startDate:
        startDate = _strOrDate(startDate)
        return _getJson('ref-data/us/dates/{type}/{direction}/{last}/{date}'.format(type=type, direction=direction, last=last, date=startDate), token, version, filter)
    return _getJson('ref-data/us/dates/' + type + '/' + direction + '/' + str(last), token, version, filter)


@wraps(calendar)
def calendarDF(type='holiday', direction='next', last=1, startDate=None, token='', version='', filter=''):
    dat = pd.DataFrame(calendar(type, direction, last, startDate, token, version, filter))
    _toDatetime(dat)
    return dat


@_expire(hour=8)
def holidays(direction='next', last=1, startDate=None, token='', version='', filter=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        direction (str): "next" or "last"
        last (int): number to move in direction
        startDate (date): start date for next or last, YYYYMMDD
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return calendar('holiday', direction, last, startDate, token, version, filter)


@wraps(holidays)
def holidaysDF(direction='next', last=1, startDate=None, token='', version='', filter=''):
    return calendarDF('holiday', direction, last, startDate, token, version, filter)
