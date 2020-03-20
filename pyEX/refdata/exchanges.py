# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _getJson


@_expire(hour=8)
def exchanges(token='', version='', filter=''):
    '''Returns an array of U.S. exchanges.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/market/us/exchanges', token, version, filter)


def exchangesDF(token='', version='', filter=''):
    '''Returns an array of U.S. exchanges.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(exchanges(token, version, filter))


@_expire(hour=8)
def internationalExchanges(token='', version='', filter=''):
    '''Returns an array of exchanges.

    https://iexcloud.io/docs/api/#international-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/exchanges', token, version, filter)


def internationalExchangesDF(token='', version='', filter=''):
    '''Returns an array of U.S. exchanges.

    https://iexcloud.io/docs/api/#international-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(internationalExchanges(token, version, filter))
