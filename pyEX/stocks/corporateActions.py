# -*- coding: utf-8 -*-
from functools import wraps
import pandas as pd
from ..common import _getJson, _raiseIfNotStr


def bonusIssue(symbol='', refid='', token='', version='', filter=''):
    '''Bonus Issue Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#bonus-issue

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_bonus/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_bonus/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_bonus', token, version, filter)


@wraps(bonusIssue)
def bonusIssueDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(bonusIssue(symbol, refid, token, version, filter))


def distribution(symbol='', refid='', token='', version='', filter=''):
    '''Distribution Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#distribution

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_distribution/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_distribution/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_distribution', token, version, filter)


@wraps(distribution)
def distributionDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(distribution(symbol, refid, token, version, filter))


def returnOfCapital(symbol='', refid='', token='', version='', filter=''):
    '''Return of capital up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#return-of-capital

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_return_of_capital/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_return_of_capital/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_return_of_capital', token, version, filter)


@wraps(returnOfCapital)
def returnOfCapitalDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(returnOfCapital(symbol, refid, token, version, filter))


def rightsIssue(symbol='', refid='', token='', version='', filter=''):
    '''Rights issue up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#rights-issue

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_rights/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_rights/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_rights', token, version, filter)


@wraps(rightsIssue)
def rightsIssueDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(rightsIssue(symbol, refid, token, version, filter))


def rightToPurchase(symbol='', refid='', token='', version='', filter=''):
    '''Right to purchase up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#right-to-purchase

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_right_to_purchase/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_right_to_purchase/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_right_to_purchase', token, version, filter)


@wraps(rightToPurchase)
def rightToPurchaseDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(rightToPurchase(symbol, refid, token, version, filter))


def securityReclassification(symbol='', refid='', token='', version='', filter=''):
    '''Security reclassification up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-reclassification

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_security_reclassification/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_security_reclassification/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_security_reclassification', token, version, filter)


@wraps(securityReclassification)
def securityReclassificationDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(securityReclassification(symbol, refid, token, version, filter))


def securitySwap(symbol='', refid='', token='', version='', filter=''):
    '''Security Swap up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#security-swap

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_security_swap/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_security_swap/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_security_swap', token, version, filter)


@wraps(securitySwap)
def securitySwapDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(securitySwap(symbol, refid, token, version, filter))


def spinoff(symbol='', refid='', token='', version='', filter=''):
    '''Security spinoff up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#spinoff

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_spinoff/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_spinoff/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_spinoff', token, version, filter)


@wraps(spinoff)
def spinoffDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(spinoff(symbol, refid, token, version, filter))


def splits(symbol='', refid='', token='', version='', filter=''):
    '''Security splits up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#splits

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if refid and symbol:
        return _getJson('time-series/advanced_splits/{}/{}'.format(symbol, refid), token, version, filter)
    elif symbol:
        return _getJson('time-series/advanced_splits/{}'.format(symbol), token, version, filter)
    return _getJson('time-series/advanced_splits', token, version, filter)


@wraps(splits)
def splitsDF(symbol='', refid='', token='', version='', filter=''):
    return pd.DataFrame(splits(symbol, refid, token, version, filter))
