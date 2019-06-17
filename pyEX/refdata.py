import pandas as pd
from deprecation import deprecated
from .common import _getJson, _strOrDate, _reindex, _toDatetime


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


def symbols(token='', version='', filter=''):
    '''This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/symbols', token, version, filter)


def iexSymbols(token='', version='', filter=''):
    '''This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/iex/symbols', token, version, filter)


def mutualFundSymbols(token='', version='', filter=''):
    '''This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/mutual-fund/symbols', token, version, filter)


def otcSymbols(token='', version='', filter=''):
    '''This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/otc/symbols', token, version, filter)


def internationalSymbols(region='', exchange='', token='', version='', filter=''):
    '''This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (string); region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (string): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if region:
        return _getJson('ref-data/region/{region}/symbols'.format(region=region), token, version, filter)
    elif exchange:
        return _getJson('ref-data/exchange/{exchange}/exchange'.format(exchange=exchange), token, version, filter)
    return _getJson('ref-data/region/us/symbols', token, version, filter)


def fxSymbols(token='', version='', filter=''):
    '''This call returns a list of supported currencies and currency pairs.

    https://iexcloud.io/docs/api/#fx-symbols
    7am, 9am, UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/fx/symbols', token, version, filter)


def optionsSymbols(token='', version='', filter=''):
    '''This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

    https://iexcloud.io/docs/api/#options-symbols
    9:30am ET Tue-Sat

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('ref-data/options/symbols', token, version, filter)


def symbolsDF(token='', version='', filter=''):
    '''This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dataframe: result
    '''
    df = pd.DataFrame(symbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def iexSymbolsDF(token='', version='', filter=''):
    '''This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(iexSymbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def mutualFundSymbolsDF(token='', version='', filter=''):
    '''This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(mutualFundSymbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def otcSymbolsDF(token='', version='', filter=''):
    '''This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(otcSymbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def internationalSymbolsDF(region='', exchange='', token='', version='', filter=''):
    '''This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (string); region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (string): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(internationalSymbols(region, exchange, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def fxSymbolsDF(token='', version='', filter=''):
    '''This call returns a list of supported currencies and currency pairs.

    https://iexcloud.io/docs/api/#fx-symbols
    7am, 9am, UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        [DataFrame]: results
    '''
    fx = fxSymbols(token, version, filter)
    df1 = pd.DataFrame(fx['currencies'])
    df2 = pd.DataFrame(fx['pairs'])
    _reindex(df1, 'code')
    return [df1, df2]


def optionsSymbolsDF(token='', version='', filter=''):
    '''This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

    https://iexcloud.io/docs/api/#options-symbols
    9:30am ET Tue-Sat

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(optionsSymbols(token, version, filter))
    df = df.T
    df.columns = ['expirations']
    return df


def symbolsList(token='', version='', filter=''):
    '''This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        list: result
    '''
    return symbolsDF(token, version, filter).index.tolist()


def iexSymbolsList(token='', version='', filter=''):
    '''This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        list: result
    '''
    return iexSymbolsDF(token, version, filter).index.tolist()


def mutualFundSymbolsList(token='', version='', filter=''):
    '''This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        List: result
    '''
    return mutualFundSymbolsDF(token, version, filter).index.tolist()


def otcSymbolsList(token='', version='', filter=''):
    '''This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        list: result
    '''
    return otcSymbolsDF(token, version, filter).index.tolist()


def internationalSymbolsList(region='', exchange='', token='', version='', filter=''):
    '''This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (string); region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (string): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        list: result
    '''
    return internationalSymbolsDF(region, exchange, token, version, filter).index.tolist()


def fxSymbolsList(token='', version='', filter=''):
    '''This call returns a list of supported currencies and currency pairs.

    https://iexcloud.io/docs/api/#fx-symbols
    7am, 9am, UTC daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        list: result
    '''
    fx = fxSymbols(token, version, filter)
    ret = [[], []]
    for c in fx['currencies']:
        ret[0].append(c['code'])
    for p in fx['pairs']:
        ret[1].append(p['fromCurrency'] + p['toCurrency'])
    return ret


def optionsSymbolsList(token='', version='', filter=''):
    '''This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

    https://iexcloud.io/docs/api/#options-symbols
    9:30am ET Tue-Sat

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        list: result
    '''
    return optionsSymbolsDF(token, version, filter).index.tolist()


@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActions(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/corporate-actions/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/corporate-actions', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActionsDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(corporateActions(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividends(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/dividends/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/dividends', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividendsDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(dividends(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDate(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/next-day-ex-date/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/next-day-ex-date', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDateDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(nextDayExtDate(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def directory(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/symbol-directory/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/symbol-directory', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def directoryDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    df = pd.DataFrame(directory(date, token, version, filter))
    _toDatetime(df)
    return df
