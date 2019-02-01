import pandas as pd
from deprecation import deprecated
from .common import _getJson, _strOrDate, _reindex, _toDatetime


def symbols(token='', version=''):
    '''This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('ref-data/symbols', token, version)


def iexSymbols(token='', version=''):
    '''This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('ref-data/iex/symbols', token, version)


def symbolsDF(token='', version=''):
    '''This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dataframe: result
    '''
    df = pd.DataFrame(symbols(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def iexSymbolsDF(token='', version=''):
    '''This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(iexSymbols(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def symbolsList(token='', version=''):
    '''This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        list: result
    '''
    return symbolsDF(token, version).index.tolist()


def iexSymbolsList(token='', version=''):
    '''This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        list: result
    '''
    return iexSymbolsDF(token, version).index.tolist()


@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActions(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/corporate-actions/' + date, token, version)
    return _getJson('ref-data/daily-list/corporate-actions', token, version)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActionsDF(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(corporateActions(date, token, version))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividends(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/dividends/' + date, token, version)
    return _getJson('ref-data/daily-list/dividends', token, version)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividendsDF(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(dividends(date, token, version))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDate(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/next-day-ex-date/' + date, token, version)
    return _getJson('ref-data/daily-list/next-day-ex-date', token, version)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDateDF(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(nextDayExtDate(date, token, version))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def directory(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/symbol-directory/' + date, token, version)
    return _getJson('ref-data/daily-list/symbol-directory', token, version)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def directoryDF(date=None, token='', version=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    df = pd.DataFrame(directory(date, token, version))
    _toDatetime(df)
    return df
