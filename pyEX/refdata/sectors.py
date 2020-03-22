# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _getJson


@_expire(hour=8)
def sectors(token='', version='', filter=''):
    '''Returns an array of sectors.

    https://iexcloud.io/docs/api/#sectors

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/sectors', token, version, filter)


def sectorsDF(token='', version='', filter=''):
    '''Returns an array of sectors.

    https://iexcloud.io/docs/api/#sectors

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(sectors(token, version, filter))


@_expire(hour=8)
def tags(token='', version='', filter=''):
    '''Returns an array of tags.

    https://iexcloud.io/docs/api/#tags

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/tags', token, version, filter)


def tagsDF(token='', version='', filter=''):
    '''Returns an array of tags.

    https://iexcloud.io/docs/api/#tags

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(tags(token, version, filter))
