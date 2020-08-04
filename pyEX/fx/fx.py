# -*- coding: utf-8 -*-
import pandas as pd
import itertools
from ..common import _expire, _getJson, _strOrDate, _reindex


def latestFX(symbols=None, token='', version='', filter=''):
    '''This endpoint returns real-time foreign currency exchange rates data updated every 250 milliseconds.

    https://iexcloud.io/docs/api/#latest-currency-rates
    5pm Sun-4pm Fri UTC

    Args:
        symbols (string): comma seperated list of symbols
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if symbols:
        if isinstance(symbols, str):
            return _getJson('/fx/latest?symbols={symbols}'.format(symbols=symbols), token, version, filter)
        return _getJson('/fx/latest?symbols={symbols}'.format(symbols=','.join(symbols)), token, version, filter)
    return _getJson('/fx/latest', token, version, filter)


def latestFXDF(symbols=None, token='', version='', filter=''):
    '''This endpoint returns real-time foreign currency exchange rates data updated every 250 milliseconds.

    https://iexcloud.io/docs/api/#latest-currency-rates
    5pm Sun-4pm Fri UTC

    Args:
        symbols (string): comma seperated list of symbols
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:

        DataFrame: result
    '''
    return pd.DataFrame(latestFX(symbols, token, version, filter))


def convertFX(symbols=None, amount=None, token='', version='', filter=''):
    '''This endpoint performs a conversion from one currency to another for a supplied amount of the base currency. If an amount isn’t provided, the latest exchange rate will be provided and the amount will be null.

    https://iexcloud.io/docs/api/#currency-conversion
    5pm Sun-4pm Fri UTC

    Args:
        symbols (string): comma seperated list of symbols
        amount (float): amount to convert
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    amount = amount or ''
    if symbols:
        if isinstance(symbols, str):
            return _getJson('/fx/convert?symbols={symbols}&amount={amount}'.format(symbols=symbols, amount=amount), token, version, filter)
        return _getJson('/fx/convert?symbols={symbols}&amount={amount}'.format(symbols=','.join(symbols), amount=amount), token, version, filter)
    return _getJson('/fx/convert?amount={amount}'.format(amount=amount), token, version, filter)


def convertFXDF(symbols=None, amount=None, token='', version='', filter=''):
    '''This endpoint performs a conversion from one currency to another for a supplied amount of the base currency. If an amount isn’t provided, the latest exchange rate will be provided and the amount will be null.

    https://iexcloud.io/docs/api/#currency-conversion
    5pm Sun-4pm Fri UTC

    Args:
        symbols (string): comma seperated list of symbols
        amount (float): amount to convert
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:

        DataFrame: result
    '''
    return pd.DataFrame(convertFX(symbols, token, version, filter))


@_expire(hour=1)
def historicalFX(symbols=None, from_='', to_='', on='', last=0, first=0, token='', version='', filter=''):
    '''This endpoint returns a daily value for the desired currency pair.

    https://iexcloud.io/docs/api/#historical-daily
    1am Mon-Sat UTC

    Args:
        symbols (string): comma seperated list of symbols
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
    '''
    base_url = '/fx/historical?'

    if symbols:
        if isinstance(symbols, str):
            base_url += 'symbols={symbols}&'.format(symbols=symbols)
        else:
            base_url += 'symbols={symbols}&'.format(symbols=','.join(symbols))

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

    return list(itertools.chain.from_iterable(_getJson(base_url, token, version, filter)))


def historicalFXDF(symbols=None, from_='', to_='', on='', last=0, first=0, token='', version='', filter=''):
    '''This endpoint returns a daily value for the desired currency pair.

    https://iexcloud.io/docs/api/#historical-daily
    1am Mon-Sat UTC

    Args:
        symbols (string): comma seperated list of symbols
        from_ (str or datetime): Returns data on or after the given from date. Format YYYY-MM-DD
        to_ (str or datetime): Returns data on or before the given to date. Format YYYY-MM-DD
        on (str or datetime): Returns data on the given date. Format YYYY-MM-DD
        last (int): Returns the latest n number of records in the series
        first (int): Returns the first n number of records in the series
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:

        DataFrame: result
    '''
    df = pd.DataFrame(historicalFX(symbols, from_=from_, to_=to_, on=on, last=last, first=first, token=token, version=version, filter=filter))
    _reindex(df, ['date', 'symbol'])
    df.sort_index(inplace=True)
    return df
