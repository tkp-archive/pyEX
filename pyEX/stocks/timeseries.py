# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _getJson, _dateRange, _strOrDate, _toDatetime


def timeSeriesInventory(token='', version=''):
    '''Get inventory of available time series endpoints
    Returns:
        result (dict)
    '''
    return _getJson('time-series/', token, version)


def timeSeriesInventoryDF(token='', version=''):
    '''Get inventory of available time series endpoints

    Returns:
        result (DataFrame)
    '''
    return pd.io.json.json_normalize(timeSeriesInventory(token=token, version=version))


def timeSeries(id='',
               key='',
               subkey='',
               range=None,
               calendar=False,
               limit=1,
               subattribute='',
               dateField=None,
               from_=None,
               to_=None,
               on=None,
               last=0,
               first=0,
               token='',
               version='',
               filter=''):
    '''This is a meeting where company executives provide information about the company’s performance and its future prospects.
    6am , 10am , 2pm , 6pm and 9pm daily

    https://iexcloud.io/docs/api/#time-series

    Args:
        id (str): ID used to identify a time series dataset.
        key (str): Key used to identify data within a dataset. A common example is a symbol such as AAPL.
        subkey (str): The optional subkey can used to further refine data for a particular key if available.
        range (str): Returns data for a given range. Supported ranges described below.
        calendar (bool): Used in conjunction with range to return data in the future.
        limit (int): Limits the number of results returned. Defaults to 1.
        subattribute (str): Allows you to query time series by any field in the result set. All time series data is stored by ID, then key, then subkey. If you want to query by any other field in the data, you can use subattribute.
                            For example, news may be stored as /news/{symbol}/{newsId}, and the result data returns the keys id, symbol, date, sector, hasPaywall
                            By default you can only query by symbol or id. Maybe you want to query all news where the sector is Technology. Your query would be:
                            /time-series/news?subattribute=source|WSJ
                            The syntax is subattribute={keyName}|{value}. Both the key name and the value are case sensitive. A pipe symbol is used to represent ‘equal to’.
        dateField (str or datetime): All time series data is stored by a single date field, and that field is used for any range or date parameters. You may want to query time series data by a different date in the result set. To change the date field used by range queries, pass the case sensitive field name with this parameter.
                                     For example, corporate buy back data may be stored by announce date, but also contains an end date which you’d rather query by. To query by end date you would use dateField=endDate&range=last-week
        from_ (str or datetime): Returns data on or after the given from date. Format YYYY-MM-DD
        to_ (str or datetime): Returns data on or before the given to date. Format YYYY-MM-DD
        on (str or datetime): Returns data on the given date. Format YYYY-MM-DD
        last (int): Returns the latest n number of records in the series
        first (int): Returns the first n number of records in the series
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result


    Date Ranges:
        today	Returns data for today
        yesterday	Returns data for yesterday
        ytd	Returns data for the current year
        last-week	Returns data for Sunday-Saturday last week
        last-month	Returns data for the last month
        last-quarter	Returns data for the last quarter
        d	Use the short hand d to return a number of days. Example: 2d returns 2 days.
        If calendar=true, data is returned from today forward.
        w	Use the short hand w to return a number of weeks. Example: 2w returns 2 weeks.
        If calendar=true, data is returned from today forward.
        m	Use the short hand m to return a number of months. Example: 2m returns 2 months.
        If calendar=true, data is returned from today forward.
        q	Use the short hand q to return a number of quarters. Example: 2q returns 2 quarters.
        If calendar=true, data is returned from today forward.
        y	Use the short hand y to return a number of years. Example: 2y returns 2 years.
        If calendar=true, data is returned from today forward.
        tomorrow	Calendar data for tomorrow. Requires calendar=true
        this-week	Calendar data for Sunday-Saturday this week. Requires calendar=true
        this-month	Calendar data for current month. Requires calendar=true
        this-quarter	Calendar data for current quarter. Requires calendar=true
        next-week	Calendar data for Sunday-Saturday next week. Requires calendar=true
        next-month	Calendar data for next month. Requires calendar=true
        next-quarter	Calendar data for next quarter. Requires calendar=true
    '''
    if not id:
        return timeSeriesInventory(token=token, version=version)

    base_url = 'time-series/{}'.format(id)
    if key:
        base_url += '/{}'.format(key)
    if subkey:
        base_url += '/{}'.format(subkey)
    base_url += '?'

    if range:
        range = _dateRange(range)
        base_url += 'range={}&'.format(range)

    base_url += 'calendar={}&'.format(str(calendar))
    base_url += 'limit={}&'.format(str(limit))

    if subattribute:
        base_url += 'subattribute={}&'.format(subattribute)
    if dateField:
        base_url += 'dateField={}&'.format(dateField)

    if from_:
        base_url += 'from={}&'.format(_strOrDate(from_))
    if to_:
        base_url += 'to={}&'.format(_strOrDate(to_))
    if on:
        base_url += 'on={}&'.format(_strOrDate(on))
    if last:
        base_url += 'last={}&'.format(str(last))
    if first:
        base_url += 'first={}&'.format(str(first))

    return _getJson(base_url, token, version, filter)


@wraps(timeSeries)
def timeSeriesDF(*args, **kwargs):
    df = pd.io.json.json_normalize(timeSeries(*args, **kwargs))
    _toDatetime(df)
    return df


@wraps(timeSeries)
def tenQ(symbol, **kwargs):
    kwargs.pop('id')
    kwargs.pop('key')
    kwargs.pop('subkey')
    return timeSeries(id='REPORTED_FINANCIALS', key=symbol, subkey='10-Q', **kwargs)


@wraps(timeSeries)
def tenK(symbol, **kwargs):
    kwargs.pop('id')
    kwargs.pop('key')
    kwargs.pop('subkey')
    return timeSeries(id='REPORTED_FINANCIALS', key=symbol, subkey='10-Q', **kwargs)
