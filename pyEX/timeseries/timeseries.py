# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ..common import (
    PyEXception,
    _dateRange,
    _get,
    _getAsync,
    _quoteSymbols,
    _strOrDate,
    _toDatetime,
    json_normalize,
)


def timeSeriesInventory(token="", version="stable", filter="", format="json"):
    """Get inventory of available time series endpoints
    Returns:
        result (dict)
    """
    return _get(
        "time-series/", token=token, version=version, filter=filter, format=format
    )


@wraps(timeSeriesInventory)
def timeSeriesInventoryDF(*args, **kwargs):
    return json_normalize(timeSeriesInventory(*args, **kwargs))


@wraps(timeSeriesInventory)
async def timeSeriesInventoryAsync(
    token="", version="stable", filter="", format="json"
):
    return await _getAsync(
        "time-series/", token=token, version=version, filter=filter, format=format
    )


def _timeSeriesURL(
    id="",
    key="",
    subkey="",
    range=None,
    calendar=False,
    limit=1,
    offset=0,
    subattribute="",
    dateField=None,
    from_=None,
    to_=None,
    on=None,
    last=0,
    first=0,
    sort="",
    interval=None,
    overrideBase="",
    **extra_params,
):
    base_url = "{}/{}".format(overrideBase or "time-series", id)
    if key:
        base_url += "/{}".format(_quoteSymbols(key))
    if subkey:
        base_url += "/{}".format(_quoteSymbols(subkey))
    base_url += "?"

    if range:
        base_url += "range={}&".format(_dateRange(range))

    if calendar:
        base_url += "calendar={}&".format(str(calendar))

    if not last and (not from_ or not to_):
        base_url += "limit={}&".format(str(limit))

    if offset > 0:
        base_url += "offset={}&".format(offset)

    if subattribute:
        if isinstance(subattribute, dict):
            # dict mapping key to required equal value, e.g. {"A": 1} -> A|1
            subattribute = ",".join(
                "{}|{}".format(key, value) for key, value in subattribute.items()
            )
        elif isinstance(subattribute, list):
            # list of tuples mapping key to required equal value, e.g. [("A", "=", 1), ("B", "!=", 2)] -> A|1,B~2
            subattribute = ",".join(
                "{}{}{}".format(v1, "|" if v2.upper() == "=" else "~", v3)
                for v1, v2, v3 in subattribute
            )
        base_url += "subattribute={}&".format(subattribute)

    if dateField:
        base_url += "dateField={}&".format(dateField)

    if from_:
        base_url += "from={}&".format(_strOrDate(from_))

    if to_:
        base_url += "to={}&".format(_strOrDate(to_))

    if on:
        base_url += "on={}&".format(_strOrDate(on))

    if last:
        base_url += "last={}&".format(str(last))

    if first:
        base_url += "first={}&".format(str(first))

    if sort:
        if sort.lower() not in (
            "asc",
            "desc",
        ):
            raise PyEXception("Sort must be in (asc, desc), got: {}".format(sort))
        base_url += "sort={}&".format(sort)

    if interval:
        base_url += "interval={}&".format(int(interval))

    if extra_params:
        base_url += "&".join("{}={}".format(k, v) for k, v in extra_params.items())

    return base_url


def timeSeries(
    id="",
    key="",
    subkey="",
    range=None,
    calendar=False,
    limit=1,
    subattribute="",
    dateField=None,
    from_=None,
    to_=None,
    on=None,
    last=0,
    first=0,
    sort="",
    interval=None,
    token="",
    version="stable",
    filter="",
    format="json",
    overrideBase="",
    **extra_params,
):
    """Time series is the most common type of data available, and consists of a collection of data points over a period of time. Time series data is indexed by a single date field, and can be retrieved by any portion of time.

    https://iexcloud.io/docs/api/#time-series

    Args:
        id (str): ID used to identify a time series dataset.
        key (str): Key used to identify data within a dataset. A common example is a symbol such as AAPL.
        subkey (str): The optional subkey can used to further refine data for a particular key if available.
        range (str): Returns data for a given range. Supported ranges described below.
        calendar (bool): Used in conjunction with range to return data in the future.
        limit (int): Limits the number of results returned. Defaults to 1.
        subattribute (str,list): Allows you to query time series by any field in the result set. All time series data is stored by ID, then key, then subkey. If you want to query by any other field in the data, you can use subattribute.
                            For example, news may be stored as /news/{symbol}/{newsId}, and the result data returns the keys id, symbol, date, sector, hasPaywall
                            By default you can only query by symbol or id. Maybe you want to query all news where the sector is Technology. Your query would be:
                            /time-series/news?subattribute=source|WSJ
                            The syntax is subattribute={keyName}|{value} or {keyName}~{value}. Both the key name and the value are case sensitive. A pipe symbol `|` is used to represent ‘equal to’ and the tilde `~` is used to represent "not equal to".
        dateField (str or datetime): All time series data is stored by a single date field, and that field is used for any range or date parameters. You may want to query time series data by a different date in the result set. To change the date field used by range queries, pass the case sensitive field name with this parameter.
                                     For example, corporate buy back data may be stored by announce date, but also contains an end date which you’d rather query by. To query by end date you would use dateField=endDate&range=last-week
        from_ (str or datetime): Returns data on or after the given from date. Format YYYY-MM-DD
        to_ (str or datetime): Returns data on or before the given to date. Format YYYY-MM-DD
        on (str or datetime): Returns data on the given date. Format YYYY-MM-DD
        last (int): Returns the latest n number of records in the series
        first (int): Returns the first n number of records in the series
        sort (str): Order of results
        interval (int): interval to use
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result

    Date Ranges:
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | today        | Returns data for today                                                                                                                     |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | yesterday    | Returns data for yesterday                                                                                                                 |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | ytd          | Returns data for the current year                                                                                                          |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | last-week    | Returns data for Sunday-Saturday last week                                                                                                 |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | last-month   | Returns data for the last month                                                                                                            |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | last-quarter | Returns data for the last quarter                                                                                                          |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | d            | Use the short hand d to return a number of days. Example: 2d returns 2 days. If calendar=true, data is returned from today forward.        |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | w            | Use the short hand w to return a number of weeks. Example: 2w returns 2 weeks. If calendar=true, data is returned from today forward.      |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | m            | Use the short hand m to return a number of months. Example: 2m returns 2 months. If calendar=true, data is returned from today forward.    |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | q            | Use the short hand q to return a number of quarters. Example: 2q returns 2 quarters. If calendar=true, data is returned from today forward.|
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | y            | Use the short hand y to return a number of years. Example: 2y returns 2 years. If calendar=true, data is returned from today forward.      |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | tomorrow     | Calendar data for tomorrow. Requires calendar=true                                                                                         |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | this-week    | Calendar data for Sunday-Saturday this week. Requires calendar=true                                                                        |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | this-month   | Calendar data for current month. Requires calendar=true                                                                                    |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | this-quarter | Calendar data for current quarter. Requires calendar=true                                                                                  |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | next-week    | Calendar data for Sunday-Saturday next week. Requires calendar=true                                                                        |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | next-month   | Calendar data for next month. Requires calendar=true                                                                                       |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | next-quarter | Calendar data for next quarter. Requires calendar=true                                                                                     |
        +--------------+--------------------------------------------------------------------------------------------------------------------------------------------+
    """
    if not id:
        return timeSeriesInventory(
            token=token, version=version, filter=filter, format=format
        )

    base_url = _timeSeriesURL(
        id=id,
        key=key,
        subkey=subkey,
        range=range,
        calendar=calendar,
        limit=limit,
        subattribute=subattribute,
        dateField=dateField,
        from_=from_,
        to_=to_,
        on=on,
        last=last,
        first=first,
        sort=sort,
        interval=interval,
        overrideBase=overrideBase,
        **extra_params,
    )
    return _get(base_url, token=token, version=version, filter=filter, format=format)


@wraps(timeSeries)
def timeSeriesDF(*args, **kwargs):
    return _toDatetime(
        json_normalize(timeSeries(*args, **kwargs)),
        reformatcols=["datetime", "date", "updated"],
    )


@wraps(timeSeries)
async def timeSeriesAsync(
    id="",
    key="",
    subkey="",
    range=None,
    calendar=False,
    limit=1,
    subattribute="",
    dateField=None,
    from_=None,
    to_=None,
    on=None,
    last=0,
    first=0,
    sort="",
    interval=None,
    token="",
    version="stable",
    filter="",
    format="json",
    overrideBase="",
    **extra_params,
):
    if not id:
        return await timeSeriesInventoryAsync(
            token=token, version=version, filter=filter, format=format
        )

    base_url = _timeSeriesURL(
        id=id,
        key=key,
        subkey=subkey,
        range=range,
        calendar=calendar,
        limit=limit,
        subattribute=subattribute,
        dateField=dateField,
        from_=from_,
        to_=to_,
        on=on,
        last=last,
        first=first,
        sort=sort,
        interval=interval,
        overrideBase=overrideBase,
        **extra_params,
    )
    return await _getAsync(
        base_url, token=token, version=version, filter=filter, format=format
    )
