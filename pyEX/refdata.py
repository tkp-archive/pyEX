import pandas as pd
from deprecation import deprecated
from .common import _getJson, _strOrDate, _reindex, _toDatetime


def exchanges(token='', version=''):
    '''Returns an array of U.S. exchanges.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('ref-data/market/us/exchanges', token, version)


def exchangesDF(token='', version=''):
    '''Returns an array of U.S. exchanges.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(exchanges())


def calendar(type='holiday', direction='next', last=1, startDate=None, token='', version=''):
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

    Returns:
        dict: result
    '''
    if startDate:
        startDate = _strOrDate(startDate)
        return _getJson('ref-data/us/dates/{type}/{direction}/{last}/{date}'.format(type=type, direction=direction, last=last, date=startDate), token, version)
    return _getJson('ref-data/us/dates/' + type + '/' + direction + '/' + str(last), token, version)


def calendarDF(type='holiday', direction='next', last=1, startDate=None, token='', version=''):
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

    Returns:
        dict: result
    '''
    dat = pd.DataFrame(calendar(type, direction, last, startDate, token, version))
    _toDatetime(dat)
    return dat


def holidays(direction='next', last=1, startDate=None, token='', version=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        direction (string); "next" or "last"
        last (int); number to move in direction
        startDate (date); start date for next or last, YYYYMMDD
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return calendar('holiday', direction, last, startDate, token, version)


def holidaysDF(direction='next', last=1, startDate=None, token='', version=''):
    '''This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        direction (string); "next" or "last"
        last (int); number to move in direction
        startDate (date); start date for next or last, YYYYMMDD
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return calendarDF('holiday', direction, last, startDate, token, version)


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


def mutualFundSymbols(token='', version=''):
    '''This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('ref-data/mutual-fund/symbols', token, version)


def otcSymbols(token='', version=''):
    '''This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('ref-data/otc/symbols', token, version)


def internationalSymbols(region='', exchange='', token='', version=''):
    '''This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (string); region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (string): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if region:
        return _getJson('ref-data/region/{region}/symbols'.format(region=region), token, version)
    elif exchange:
        return _getJson('ref-data/exchange/{exchange}/exchange'.format(exchange=exchange), token, version)
    return _getJson('ref-data/region/us/symbols', token, version)


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


def mutualFundSymbolsDF(token='', version=''):
    '''This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(mutualFundSymbols(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def otcSymbolsDF(token='', version=''):
    '''This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(otcSymbols(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def internationalSymbolsDF(region='', exchange='', token='', version=''):
    '''This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (string); region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (string): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(internationalSymbols(region, exchange, token, version))
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


def mutualFundSymbolsList(token='', version=''):
    '''This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        List: result
    '''
    return mutualFundSymbolsDF(token, version).index.tolist()


def otcSymbolsList(token='', version=''):
    '''This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        list: result
    '''
    return otcSymbolsDF(token, version).index.tolist()


def internationalSymbolsList(region='', exchange='', token='', version=''):
    '''This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (string); region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (string): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (string); Access token
        version (string); API version

    Returns:
        list: result
    '''
    return internationalSymbolsDF(region, exchange, token, version).index.tolist()


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
