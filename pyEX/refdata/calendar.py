# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _getJson, _strOrDate, _toDatetime


@_expire(hour=8)
def calendar(type='holiday', direction='next', last=1, startDate=None, token='', version='', filter=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        type (string); "holiday" or "trade"
        direction (string); "next" or "last"
        last (int); number to move in direction
        startDate (date); start date for next or last, YYYYMMDD
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if startDate:
        startDate = _strOrDate(startDate)
        return _getJson('ref-data/us/dates/{type}/{direction}/{last}/{date}'.format(type=type, direction=direction, last=last, date=startDate), token, version, filter)
    return _getJson('ref-data/us/dates/' + type + '/' + direction + '/' + str(last), token, version, filter)


def calendarDF(type='holiday', direction='next', last=1, startDate=None, token='', version='', filter=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        type (string); "holiday" or "trade"
        direction (string); "next" or "last"
        last (int); number to move in direction
        startDate (date); start date for next or last, YYYYMMDD
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    dat = pd.DataFrame(calendar(type, direction, last, startDate, token, version, filter))
    _toDatetime(dat)
    return dat


@_expire(hour=8)
def holidays(direction='next', last=1, startDate=None, token='', version='', filter=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        direction (string); "next" or "last"
        last (int); number to move in direction
        startDate (date); start date for next or last, YYYYMMDD
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return calendar('holiday', direction, last, startDate, token, version, filter)


def holidaysDF(direction='next', last=1, startDate=None, token='', version='', filter=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        direction (string); "next" or "last"
        last (int); number to move in direction
        startDate (date); start date for next or last, YYYYMMDD
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return calendarDF('holiday', direction, last, startDate, token, version, filter)
