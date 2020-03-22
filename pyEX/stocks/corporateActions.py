# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson, _raiseIfNotStr


def bonusIssue(symbol='', refid='', token='', version='', filter=''):
    '''Bonus Issue Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#bonus-issue

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_bonus/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_bonus/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_bonus', token, version, filter)


def bonusIssueDF(symbol='', refid='', token='', version='', filter=''):
    '''Bonus Issue Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#bonus-issue

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(bonusIssue(symbol, refid, token, version, filter))


def distribution(symbol='', refid='', token='', version='', filter=''):
    '''Distribution Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#distribution

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_distribution/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_distribution/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_distribution', token, version, filter)


def distributionDF(symbol='', refid='', token='', version='', filter=''):
    '''Distribution Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#distribution

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(distribution(symbol, refid, token, version, filter))


def returnOfCapital(symbol='', refid='', token='', version='', filter=''):
    '''Return of capital up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#return-of-capital

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_return_of_capital/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_return_of_capital/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_return_of_capital', token, version, filter)


def returnOfCapitalDF(symbol='', refid='', token='', version='', filter=''):
    '''Return of capital up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#return-of-capital

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(returnOfCapital(symbol, refid, token, version, filter))


def rightsIssue(symbol='', refid='', token='', version='', filter=''):
    '''Rights issue up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#rights-issue

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_rights/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_rights/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_rights', token, version, filter)


def rightsIssueDF(symbol='', refid='', token='', version='', filter=''):
    '''Rights issue up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#rights-issue

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(rightsIssue(symbol, refid, token, version, filter))


def rightToPurchase(symbol='', refid='', token='', version='', filter=''):
    '''Right to purchase up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#right-to-purchase

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_right_to_purchase/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_right_to_purchase/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_right_to_purchase', token, version, filter)


def rightToPurchaseDF(symbol='', refid='', token='', version='', filter=''):
    '''Right to purchase up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#right-to-purchase

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(rightToPurchase(symbol, refid, token, version, filter))


def securityReclassification(symbol='', refid='', token='', version='', filter=''):
    '''Security reclassification up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-reclassification

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_security_reclassification/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_security_reclassification/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_security_reclassification', token, version, filter)


def securityReclassificationDF(symbol='', refid='', token='', version='', filter=''):
    '''Security reclassification up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-reclassification

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(securityReclassification(symbol, refid, token, version, filter))


def securitySwap(symbol='', refid='', token='', version='', filter=''):
    '''Security Swap up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-swap

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_security_swap/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_security_swap/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_security_swap', token, version, filter)


def securitySwapDF(symbol='', refid='', token='', version='', filter=''):
    '''Security Swap up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-swap

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(securitySwap(symbol, refid, token, version, filter))


def spinoff(symbol='', refid='', token='', version='', filter=''):
    '''Security spinoff up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#spinoff

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_spinoff/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_spinoff/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_spinoff', token, version, filter)


def spinoffDF(symbol='', refid='', token='', version='', filter=''):
    '''Security spinoff up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#spinoff

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(spinoff(symbol, refid, token, version, filter))


def splits(symbol='', refid='', token='', version='', filter=''):
    '''Security splits up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#splits

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_splits/' + symbol + '/' + refid, token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_splits/' + symbol, token, version, filter)
    return _getJson('time-series/advanced_splits', token, version, filter)


def splitsDF(symbol='', refid='', token='', version='', filter=''):
    '''Security splits up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#splits

    Args:
        symbol (string); Symbol to look up
        refid (string); Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(splits(symbol, refid, token, version, filter))
