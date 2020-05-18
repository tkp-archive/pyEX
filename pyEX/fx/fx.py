# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _getJson


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
def historicalFX(symbols=None, token='', version='', filter=''):
    '''This endpoint returns a daily value for the desired currency pair.

    https://iexcloud.io/docs/api/#historical-daily
    1am Mon-Sat UTC

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
            return _getJson('/fx/historical?symbols={symbols}'.format(symbols=symbols), token, version, filter)
        return _getJson('/fx/historical?symbols={symbols}'.format(symbols=','.join(symbols)), token, version, filter)
    return _getJson('/fx/historical', token, version, filter)


def historicalFXDF(symbols=None, amount=None, token='', version='', filter=''):
    '''This endpoint returns a daily value for the desired currency pair.

    https://iexcloud.io/docs/api/#historical-daily
    1am Mon-Sat UTC

    Args:
        symbols (string): comma seperated list of symbols
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:

        DataFrame: result
    '''
    return pd.DataFrame(historicalFX(symbols, token, version, filter))
