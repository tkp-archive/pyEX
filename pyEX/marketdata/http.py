# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson, _strToList, _raiseIfNotStr, _strOrDate, _reindex, _toDatetime


def tops(symbols=None, token='', version=''):
    '''TOPS provides IEX’s aggregated best quoted bid and offer position in near real time for all securities on IEX’s displayed limit order book.
    TOPS is ideal for developers needing both quote and trade data.

    https://iexcloud.io/docs/api/#tops

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops?symbols=' + ','.join(symbols) + '%2b', token, version)
    return _getJson('tops', token, version)


def topsDF(symbols=None, token='', version=''):
    '''TOPS provides IEX’s aggregated best quoted bid and offer position in near real time for all securities on IEX’s displayed limit order book.
    TOPS is ideal for developers needing both quote and trade data.

    https://iexcloud.io/docs/api/#tops

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(tops(symbols, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def last(symbols=None, token='', version=''):
    '''Last provides trade data for executions on IEX. It is a near real time, intraday API that provides IEX last sale price, size and time.
    Last is ideal for developers that need a lightweight stock quote.

    https://iexcloud.io/docs/api/#last

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops/last?symbols=' + ','.join(symbols) + '%2b', token, version)
    return _getJson('tops/last', token, version)


def lastDF(symbols=None, token='', version=''):
    '''Last provides trade data for executions on IEX. It is a near real time, intraday API that provides IEX last sale price, size and time.
    Last is ideal for developers that need a lightweight stock quote.

    https://iexcloud.io/docs/api/#last

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(last(symbols, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def deep(symbol=None, token='', version=''):
    '''DEEP is used to receive real-time depth of book quotations direct from IEX.
    The depth of book quotations received via DEEP provide an aggregated size of resting displayed orders at a price and side,
    and do not indicate the size or number of individual orders at any price level.
    Non-displayed orders and non-displayed portions of reserve orders are not represented in DEEP.

    DEEP also provides last trade price and size information. Trades resulting from either displayed or non-displayed orders matching on IEX will be reported. Routed executions will not be reported.

    https://iexcloud.io/docs/api/#deep

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep?symbols=' + symbol, token, version)
    return _getJson('deep', token, version)


def deepDF(symbol=None, token='', version=''):
    '''DEEP is used to receive real-time depth of book quotations direct from IEX.
    The depth of book quotations received via DEEP provide an aggregated size of resting displayed orders at a price and side,
    and do not indicate the size or number of individual orders at any price level.
    Non-displayed orders and non-displayed portions of reserve orders are not represented in DEEP.

    DEEP also provides last trade price and size information. Trades resulting from either displayed or non-displayed orders matching on IEX will be reported. Routed executions will not be reported.

    https://iexcloud.io/docs/api/#deep

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(deep(symbol, token, version))
    _toDatetime(df)
    return df


def auction(symbol=None, token='', version=''):
    '''DEEP broadcasts an Auction Information Message every one second between the Lock-in Time and the auction match for Opening and Closing Auctions,
    and during the Display Only Period for IPO, Halt, and Volatility Auctions. Only IEX listed securities are eligible for IEX Auctions.

    https://iexcloud.io/docs/api/#deep-auction

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/auction?symbols=' + symbol, token, version)
    return _getJson('deep/auction', token, version)


def auctionDF(symbol=None, token='', version=''):
    '''DEEP broadcasts an Auction Information Message every one second between the Lock-in Time and the auction match for Opening and Closing Auctions,
    and during the Display Only Period for IPO, Halt, and Volatility Auctions. Only IEX listed securities are eligible for IEX Auctions.

    https://iexcloud.io/docs/api/#deep-auction

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(auction(symbol, token, version))
    _toDatetime(df)
    return df


def book(symbol=None, token='', version=''):
    '''Book shows IEX’s bids and asks for given symbols.

    https://iexcloud.io/docs/api/#deep-book

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/book?symbols=' + symbol, token, version)
    return _getJson('deep/book', token, version)


def bookDF(symbol=None, token='', version=''):
    '''Book shows IEX’s bids and asks for given symbols.

    https://iexcloud.io/docs/api/#deep-book

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    x = book(symbol, token, version)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.io.json.json_normalize(data)
    _toDatetime(df)
    return df


def opHaltStatus(symbol=None, token='', version=''):
    '''The Exchange may suspend trading of one or more securities on IEX for operational reasons and indicates such operational halt using the Operational halt status message.

    IEX disseminates a full pre-market spin of Operational halt status messages indicating the operational halt status of all securities.
    In the spin, IEX will send out an Operational Halt Message with “N” (Not operationally halted on IEX) for all securities that are eligible for trading at the start of the Pre-Market Session.
    If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System at the start of the Pre-Market Session.

    After the pre-market spin, IEX will use the Operational halt status message to relay changes in operational halt status for an individual security.

    https://iexcloud.io/docs/api/#deep-operational-halt-status

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/op-halt-status?symbols=' + symbol, token, version)
    return _getJson('deep/op-halt-status', token, version)


def opHaltStatusDF(symbol=None, token='', version=''):
    '''The Exchange may suspend trading of one or more securities on IEX for operational reasons and indicates such operational halt using the Operational halt status message.

    IEX disseminates a full pre-market spin of Operational halt status messages indicating the operational halt status of all securities.
    In the spin, IEX will send out an Operational Halt Message with “N” (Not operationally halted on IEX) for all securities that are eligible for trading at the start of the Pre-Market Session.
    If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System at the start of the Pre-Market Session.

    After the pre-market spin, IEX will use the Operational halt status message to relay changes in operational halt status for an individual security.

    https://iexcloud.io/docs/api/#deep-operational-halt-status

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    x = opHaltStatus(symbol, token, version)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def officialPrice(symbol=None, token='', version=''):
    '''The Official Price message is used to disseminate the IEX Official Opening and Closing Prices.

    These messages will be provided only for IEX Listed Securities.

    https://iexcloud.io/docs/api/#deep-official-price

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/official-price?symbols=' + symbol, token, version)
    return _getJson('deep/official-price', token, version)


def officialPriceDF(symbol=None, token='', version=''):
    '''The Official Price message is used to disseminate the IEX Official Opening and Closing Prices.

    These messages will be provided only for IEX Listed Securities.

    https://iexcloud.io/docs/api/#deep-official-price

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(officialPrice(symbol, token, version))
    _toDatetime(df)
    return df


def securityEvent(symbol=None, token='', version=''):
    '''The Security event message is used to indicate events that apply to a security. A Security event message will be sent whenever such event occurs

    https://iexcloud.io/docs/api/#deep-security-event

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/security-event?symbols=' + symbol, token, version)
    return _getJson('deep/security-event', token, version)


def securityEventDF(symbol=None, token='', version=''):
    '''The Security event message is used to indicate events that apply to a security. A Security event message will be sent whenever such event occurs

    https://iexcloud.io/docs/api/#deep-security-event

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    x = securityEvent(symbol, token, version)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def ssrStatus(symbol=None, token='', version=''):
    '''In association with Rule 201 of Regulation SHO, the Short Sale Price Test Message is used to indicate when a short sale price test restriction is in effect for a security.

    IEX disseminates a full pre-market spin of Short sale price test status messages indicating the Rule 201 status of all securities.
     After the pre-market spin, IEX will use the Short sale price test status message in the event of an intraday status change.

    The IEX Trading System will process orders based on the latest short sale price test restriction status.

    https://iexcloud.io/docs/api/#deep-short-sale-price-test-status

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/ssr-status?symbols=' + symbol, token, version)
    return _getJson('deep/ssr-status', token, version)


def ssrStatusDF(symbol=None, token='', version=''):
    '''In association with Rule 201 of Regulation SHO, the Short Sale Price Test Message is used to indicate when a short sale price test restriction is in effect for a security.

    IEX disseminates a full pre-market spin of Short sale price test status messages indicating the Rule 201 status of all securities.
     After the pre-market spin, IEX will use the Short sale price test status message in the event of an intraday status change.

    The IEX Trading System will process orders based on the latest short sale price test restriction status.

    https://iexcloud.io/docs/api/#deep-short-sale-price-test-status

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    x = ssrStatus(symbol, token, version)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def systemEvent(token='', version=''):
    '''The System event message is used to indicate events that apply to the market or the data feed.

    There will be a single message disseminated per channel for each System Event type within a given trading session.

    https://iexcloud.io/docs/api/#deep-system-event

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('deep/system-event', token, version)


def systemEventDF(token='', version=''):
    '''The System event message is used to indicate events that apply to the market or the data feed.

    There will be a single message disseminated per channel for each System Event type within a given trading session.

    https://iexcloud.io/docs/api/#deep-system-event

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(systemEvent(token, version))
    _toDatetime(df)
    return df


def trades(symbol=None, token='', version=''):
    '''Trade report messages are sent when an order on the IEX Order Book is executed in whole or in part. DEEP sends a Trade report message for every individual fill.

    https://iexcloud.io/docs/api/#deep-trades

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trades?symbols=' + symbol, token, version)
    return _getJson('deep/trades', token, version)


def tradesDF(symbol=None, token='', version=''):
    '''Trade report messages are sent when an order on the IEX Order Book is executed in whole or in part. DEEP sends a Trade report message for every individual fill.

    https://iexcloud.io/docs/api/#deep-trades

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    x = trades(symbol, token, version)
    data = []
    for key in x:
        dat = x[key]
        for d in dat:
            d['symbol'] = key
            data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def tradeBreak(symbol=None, token='', version=''):
    '''Trade break messages are sent when an execution on IEX is broken on that same trading day. Trade breaks are rare and only affect applications that rely upon IEX execution based data.

    https://iexcloud.io/docs/api/#deep-trade-break


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trade-breaks?symbols=' + symbol, token, version)
    return _getJson('deep/trade-breaks', token, version)


def tradeBreakDF(symbol=None, token='', version=''):
    '''Trade break messages are sent when an execution on IEX is broken on that same trading day. Trade breaks are rare and only affect applications that rely upon IEX execution based data.

    https://iexcloud.io/docs/api/#deep-trade-break


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(tradeBreak(symbol, token, version))
    _toDatetime(df)
    return df


def tradingStatus(symbol=None, token='', version=''):
    '''The Trading status message is used to indicate the current trading status of a security.
     For IEX-listed securities, IEX acts as the primary market and has the authority to institute a trading halt or trading pause in a security due to news dissemination or regulatory reasons.
     For non-IEX-listed securities, IEX abides by any regulatory trading halts and trading pauses instituted by the primary or listing market, as applicable.

    IEX disseminates a full pre-market spin of Trading status messages indicating the trading status of all securities.
     In the spin, IEX will send out a Trading status message with “T” (Trading) for all securities that are eligible for trading at the start of the Pre-Market Session.
     If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System.


    After the pre-market spin, IEX will use the Trading status message to relay changes in trading status for an individual security. Messages will be sent when a security is:

    Halted
    Paused*
    Released into an Order Acceptance Period*
    Released for trading
    *The paused and released into an Order Acceptance Period status will be disseminated for IEX-listed securities only. Trading pauses on non-IEX-listed securities will be treated simply as a halt.

    https://iexcloud.io/docs/api/#deep-trading-status

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trading-status?symbols=' + symbol, token, version)
    return _getJson('deep/trading-status', token, version)


def tradingStatusDF(symbol=None, token='', version=''):
    '''The Trading status message is used to indicate the current trading status of a security.
     For IEX-listed securities, IEX acts as the primary market and has the authority to institute a trading halt or trading pause in a security due to news dissemination or regulatory reasons.
     For non-IEX-listed securities, IEX abides by any regulatory trading halts and trading pauses instituted by the primary or listing market, as applicable.

    IEX disseminates a full pre-market spin of Trading status messages indicating the trading status of all securities.
     In the spin, IEX will send out a Trading status message with “T” (Trading) for all securities that are eligible for trading at the start of the Pre-Market Session.
     If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System.

    After the pre-market spin, IEX will use the Trading status message to relay changes in trading status for an individual security. Messages will be sent when a security is:

    Halted
    Paused*
    Released into an Order Acceptance Period*
    Released for trading
    *The paused and released into an Order Acceptance Period status will be disseminated for IEX-listed securities only. Trading pauses on non-IEX-listed securities will be treated simply as a halt.

    https://iexcloud.io/docs/api/#deep-trading-status

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    x = tradingStatus(symbol, token, version)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def hist(date=None, token='', version=''):
    '''


    Args:
        date (datetime); Effective date
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''

    if date is None:
        return _getJson('hist', token, version)
    else:
        date = _strOrDate(date)
        return _getJson('hist?date=' + date, token, version)


def histDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#hist'''
    x = hist(date, token, version)
    data = []
    for key in x:
        dat = x[key]
        for item in dat:
            item['date'] = key
            data.append(item)
    df = pd.DataFrame(data)
    _toDatetime(df)
    _reindex(df, 'date')
    return df
