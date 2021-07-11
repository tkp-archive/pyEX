# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import (
    _get,
    _getAsync,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _strOrDate,
    _strToList,
    _toDatetime,
    json_normalize,
)


def iexThreshold(date=None, token="", version="stable", filter="", format="json"):
    """The following are IEX-listed securities that have an aggregate fail to deliver position for five consecutive settlement days at a registered clearing agency, totaling 10,000 shares or more and equal to at least 0.5% of the issuer’s total shares outstanding (i.e., “threshold securities”).
    The report data will be published to the IEX website daily at 8:30 p.m. ET with data for that trading day.

    https://iexcloud.io/docs/api/#listed-regulation-sho-threshold-securities-list-in-dev

    Args:
        date (datetime): Effective Datetime
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if date:
        date = _strOrDate(date)
        return _get(
            "stock/market/threshold-securities/" + date,
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "stock/market/threshold-securities",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(iexThreshold)
def iexThresholdDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(iexThreshold(*args, **kwargs)))


def iexTops(symbols=None, token="", version="stable", format="json"):
    """TOPS provides IEX’s aggregated best quoted bid and offer position in near real time for all securities on IEX’s displayed limit order book.
    TOPS is ideal for developers needing both quote and trade data.

    https://iexcloud.io/docs/api/#tops

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    symbols = _strToList(symbols)
    if symbols:
        return _get(
            "tops?symbols=" + _quoteSymbols(",".join(symbols)),
            token=token,
            version=version,
            format=format,
        )
    return _get("tops", token=token, version=version, format=format)


@wraps(iexTops)
async def iexTopsAsync(symbols=None, token="", version="stable", format="json"):
    symbols = _strToList(symbols)
    if symbols:
        return await _getAsync(
            "tops?symbols=" + _quoteSymbols(",".join(symbols)),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync("tops", token=token, version=version, format=format)


@wraps(iexTops)
def iexTopsDF(*args, **kwargs):
    return _reindex(_toDatetime(json_normalize(iexTops(*args, **kwargs))), "symbol")


def iexLast(symbols=None, token="", version="stable", format="json"):
    """Last provides trade data for executions on IEX. It is a near real time, intraday API that provides IEX last sale price, size and time.
    Last is ideal for developers that need a lightweight stock quote.

    https://iexcloud.io/docs/api/#last

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    symbols = _strToList(symbols)
    if symbols:
        return _get(
            "tops/last?symbols=" + _quoteSymbols(",".join(symbols)),
            token=token,
            version=version,
            format=format,
        )
    return _get("tops/last", token=token, version=version, format=format)


@wraps(iexLast)
async def iexLastAsync(symbols=None, token="", version="stable", format="json"):
    symbols = _strToList(symbols)
    if symbols:
        return await _getAsync(
            "tops/last?symbols=" + _quoteSymbols(",".join(symbols)),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync("tops/last", token=token, version=version, format=format)


@wraps(iexLast)
def iexLastDF(*args, **kwargs):
    return _reindex(_toDatetime(json_normalize(iexLast(*args, **kwargs))), "symbol")


def iexDeep(symbol=None, token="", version="stable", format="json"):
    """DEEP is used to receive real-time depth of book quotations direct from IEX.
    The depth of book quotations received via DEEP provide an aggregated size of resting displayed orders at a price and side,
    and do not indicate the size or number of individual orders at any price level.
    Non-displayed orders and non-displayed portions of reserve orders are not represented in DEEP.

    DEEP also provides last trade price and size information. Trades resulting from either displayed or non-displayed orders matching on IEX will be reported. Routed executions will not be reported.

    https://iexcloud.io/docs/api/#deep

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep", token=token, version=version, format=format)


@wraps(iexDeep)
async def iexDeepAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync("deep", token=token, version=version, format=format)


@wraps(iexDeep)
def iexDeepDF(*args, **kwargs):
    return _toDatetime(json_normalize(iexDeep(*args, **kwargs)))


def iexAuction(symbol=None, token="", version="stable", format="json"):
    """DEEP broadcasts an Auction Information Message every one second between the Lock-in Time and the auction match for Opening and Closing Auctions,
    and during the Display Only Period for IPO, Halt, and Volatility Auctions. Only IEX listed securities are eligible for IEX Auctions.

    https://iexcloud.io/docs/api/#deep-auction

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/auction?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/auction", token=token, version=version, format=format)


@wraps(iexAuction)
async def iexAuctionAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/auction?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync("deep/auction", token=token, version=version, format=format)


@wraps(iexAuction)
def iexAuctionDF(*args, **kwargs):
    return _toDatetime(json_normalize(iexAuction(*args, **kwargs)))


def iexBook(symbol=None, token="", version="stable", format="json"):
    """Book shows IEX’s bids and asks for given symbols.

    https://iexcloud.io/docs/api/#deep-book

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/book?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/book", token=token, version=version, format=format)


@wraps(iexBook)
async def iexBookAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/book?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync("deep/book", token=token, version=version, format=format)


@wraps(iexBook)
def iexBookDF(*args, **kwargs):
    x = iexBook(*args, **kwargs)
    data = []
    for key in x:
        d = x[key]
        d["symbol"] = key
        data.append(d)
    return _toDatetime(json_normalize(data))


def iexOpHaltStatus(symbol=None, token="", version="stable", format="json"):
    """The Exchange may suspend trading of one or more securities on IEX for operational reasons and indicates such operational halt using the Operational halt status message.

    IEX disseminates a full pre-market spin of Operational halt status messages indicating the operational halt status of all securities.
    In the spin, IEX will send out an Operational Halt Message with “N” (Not operationally halted on IEX) for all securities that are eligible for trading at the start of the Pre-Market Session.
    If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System at the start of the Pre-Market Session.

    After the pre-market spin, IEX will use the Operational halt status message to relay changes in operational halt status for an individual security.

    https://iexcloud.io/docs/api/#deep-operational-halt-status

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/op-halt-status?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/op-halt-status", token=token, version=version, format=format)


@wraps(iexOpHaltStatus)
async def iexOpHaltStatusAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/op-halt-status?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync(
        "deep/op-halt-status", token=token, version=version, format=format
    )


@wraps(iexOpHaltStatus)
def iexOpHaltStatusDF(*args, **kwargs):
    x = iexOpHaltStatus(*args, **kwargs)
    data = []
    for key in x:
        d = x[key]
        d["symbol"] = key
        data.append(d)
    return _toDatetime(pd.DataFrame(data))


def iexOfficialPrice(symbol=None, token="", version="stable", format="json"):
    """The Official Price message is used to disseminate the IEX Official Opening and Closing Prices.

    These messages will be provided only for IEX Listed Securities.

    https://iexcloud.io/docs/api/#deep-official-price

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/official-price?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/official-price", token=token, version=version, format=format)


@wraps(iexOfficialPrice)
async def iexOfficialPriceAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/official-price?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync(
        "deep/official-price", token=token, version=version, format=format
    )


@wraps(iexOfficialPrice)
def iexOfficialPriceDF(*args, **kwargs):
    return _toDatetime(json_normalize(iexOfficialPrice(*args, **kwargs)))


def iexSecurityEvent(symbol=None, token="", version="stable", format="json"):
    """The Security event message is used to indicate events that apply to a security. A Security event message will be sent whenever such event occurs

    https://iexcloud.io/docs/api/#deep-security-event

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/security-event?symbols=" + symbol,
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/security-event", token=token, version=version, format=format)


@wraps(iexSecurityEvent)
async def iexSecurityEventAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/security-event?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync(
        "deep/security-event", token=token, version=version, format=format
    )


@wraps(iexSecurityEvent)
def iexSecurityEventDF(*args, **kwargs):
    x = iexSecurityEvent(*args, **kwargs)
    data = []
    for key in x:
        d = x[key]
        d["symbol"] = key
        data.append(d)
    return _toDatetime(pd.DataFrame(data))


def iexSsrStatus(symbol=None, token="", version="stable", format="json"):
    """In association with Rule 201 of Regulation SHO, the Short Sale Price Test Message is used to indicate when a short sale price test restriction is in effect for a security.

    IEX disseminates a full pre-market spin of Short sale price test status messages indicating the Rule 201 status of all securities.
     After the pre-market spin, IEX will use the Short sale price test status message in the event of an intraday status change.

    The IEX Trading System will process orders based on the latest short sale price test restriction status.

    https://iexcloud.io/docs/api/#deep-short-sale-price-test-status

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/ssr-status?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/ssr-status", token=token, version=version, format=format)


@wraps(iexSsrStatus)
async def iexSsrStatusAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/ssr-status?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync(
        "deep/ssr-status", token=token, version=version, format=format
    )


@wraps(iexSsrStatus)
def iexSsrStatusDF(*args, **kwargs):
    x = iexSsrStatus(*args, **kwargs)
    data = []
    for key in x:
        d = x[key]
        d["symbol"] = key
        data.append(d)
    return _toDatetime(pd.DataFrame(data))


def iexSystemEvent(token="", version="stable", format="json"):
    """The System event message is used to indicate events that apply to the market or the data feed.

    There will be a single message disseminated per channel for each System Event type within a given trading session.

    https://iexcloud.io/docs/api/#deep-system-event

    Args:
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    return _get("deep/system-event", token=token, version=version, format=format)


@wraps(iexSystemEvent)
async def iexSystemEventAsync(token="", version="stable", format="json"):
    return await _getAsync(
        "deep/system-event", token=token, version=version, format=format
    )


@wraps(iexSystemEvent)
def iexSystemEventDF(*args, **kwargs):
    return _toDatetime(json_normalize(iexSystemEvent(*args, **kwargs)))


def iexTrades(symbol=None, token="", version="stable", format="json"):
    """Trade report messages are sent when an order on the IEX Order Book is executed in whole or in part. DEEP sends a Trade report message for every individual fill.

    https://iexcloud.io/docs/api/#deep-trades

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/trades?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/trades", token=token, version=version, format=format)


@wraps(iexTrades)
async def iexTradesAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/trades?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync("deep/trades", token=token, version=version, format=format)


@wraps(iexTrades)
def iexTradesDF(*args, **kwargs):
    x = iexTrades(*args, **kwargs)
    data = []
    for key in x:
        dat = x[key]
        for d in dat:
            d["symbol"] = key
            data.append(d)
    return _toDatetime(pd.DataFrame(data))


def iexTradeBreak(symbol=None, token="", version="stable", format="json"):
    """Trade break messages are sent when an execution on IEX is broken on that same trading day. Trade breaks are rare and only affect applications that rely upon IEX execution based data.

    https://iexcloud.io/docs/api/#deep-trade-break


    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/trade-breaks?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/trade-breaks", token=token, version=version, format=format)


@wraps(iexTradeBreak)
async def iexTradeBreakAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/trade-breaks?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _getAsync(
        "deep/trade-breaks", token=token, version=version, format=format
    )


@wraps(iexTradeBreak)
def iexTradeBreakDF(*args, **kwargs):
    return _toDatetime(json_normalize(iexTradeBreak(*args, **kwargs)))


def iexTradingStatus(symbol=None, token="", version="stable", format="json"):
    """The Trading status message is used to indicate the current trading status of a security.
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
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    if symbol:
        return _get(
            "deep/trading-status?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return _get("deep/trading-status", token=token, version=version, format=format)


@wraps(iexTradingStatus)
async def iexTradingStatusAsync(symbol=None, token="", version="stable", format="json"):
    _raiseIfNotStr(symbol)
    if symbol:
        return await _getAsync(
            "deep/trading-status?symbols=" + _quoteSymbols(symbol),
            token=token,
            version=version,
            format=format,
        )
    return await _get(
        "deep/trading-status", token=token, version=version, format=format
    )


@wraps(iexTradingStatus)
def iexTradingStatusDF(*args, **kwargs):
    x = iexTradingStatus(*args, **kwargs)
    data = []
    for key in x:
        d = x[key]
        d["symbol"] = key
        data.append(d)
    return _toDatetime(pd.DataFrame(data))


def iexHist(date=None, token="", version="stable", format="json"):
    """
    Args:
        date (datetime): Effective date
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict: result
    """

    if date is None:
        return _get("hist", token=token, version=version, format=format)
    else:
        date = _strOrDate(date)
        return _get("hist?date=" + date, token=token, version=version, format=format)


@wraps(iexHist)
async def iexHistAsync(date=None, token="", version="stable", format="json"):
    if date is None:
        return await _get("hist", token=token, version=version, format=format)
    else:
        date = _strOrDate(date)
        return await _getAsync(
            "hist?date=" + date, token=token, version=version, format=format
        )


@wraps(iexHist)
def iexHistDF(*args, **kwargs):
    x = iexHist(*args, **kwargs)
    data = []
    for key in x:
        dat = x[key]
        for item in dat:
            item["date"] = key
            data.append(item)
    return _reindex(_toDatetime(pd.DataFrame(data)), "date")
