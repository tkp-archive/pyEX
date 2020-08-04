# -*- coding: utf-8 -*-
from enum import Enum
from ..common import _strCommaSeparatedString, _streamSSE, _SSE_URL_PREFIX, _SSE_URL_PREFIX_ALL, _SSE_DEEP_URL_PREFIX, _SSE_URL_PREFIX_SANDBOX, _SSE_URL_PREFIX_ALL_SANDBOX, _SSE_DEEP_URL_PREFIX_SANDBOX, PyEXception


class DeepChannelsSSE(Enum):
    TRADINGSTATUS = 'tradingstatus'
    AUCTION = 'auction'
    OPHALTSTATUS = 'op-halt-status'
    SSR = 'ssr-status'
    SECURITYEVENT = 'security-event'
    TRADEBREAK = 'trade-breaks'
    TRADES = 'trades'
    BOOK = 'book'
    SYSTEMEVENT = 'system-event'
    ALL = 'deep'

    @staticmethod
    def options():
        return list(map(lambda c: c.value, DeepChannelsSSE))


def _runSSE(method='', symbols=None, on_data=None, token='', version=''):
    if method == '':
        raise PyEXception('method cannot be blank!')
    if symbols:
        symbols = _strCommaSeparatedString(symbols)
        if version == 'sandbox':
            return _streamSSE(_SSE_URL_PREFIX_SANDBOX.format(channel=method, symbols=symbols, token=token, version=version), on_data=on_data)
        return _streamSSE(_SSE_URL_PREFIX.format(channel=method, symbols=symbols, token=token, version=version), on_data=on_data)
    if version == 'sandbox':
        return _streamSSE(_SSE_URL_PREFIX_ALL_SANDBOX.format(channel=method, symbols=symbols, token=token, version=version), on_data=on_data)
    return _streamSSE(_SSE_URL_PREFIX_ALL.format(channel=method, symbols=symbols, token=token, version=version), on_data=on_data)


def topsSSE(symbols=None, on_data=None, token='', version=''):
    '''TOPS provides IEX’s aggregated best quoted bid and offer position in near real time for all securities on IEX’s displayed limit order book.
    TOPS is ideal for developers needing both quote and trade data.

    https://iexcloud.io/docs/api/#tops

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('tops', symbols, on_data, token, version)


def lastSSE(symbols=None, on_data=None, token='', version=''):
    '''Last provides trade data for executions on IEX. It is a near real time, intraday API that provides IEX last sale price, size and time.
    Last is ideal for developers that need a lightweight stock quote.

    https://iexcloud.io/docs/api/#last

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('last', symbols, on_data, token, version)


def deepSSE(symbols=None, channels=None, on_data=None, token='', version=''):
    '''DEEP is used to receive real-time depth of book quotations direct from IEX.
    The depth of book quotations received via DEEP provide an aggregated size of resting displayed orders at a price and side,
    and do not indicate the size or number of individual orders at any price level.
    Non-displayed orders and non-displayed portions of reserve orders are not represented in DEEP.

    DEEP also provides last trade price and size information. Trades resulting from either displayed or non-displayed orders matching on IEX will be reported. Routed executions will not be reported.

    https://iexcloud.io/docs/api/#deep

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    symbols = _strCommaSeparatedString(symbols)

    channels = channels or []
    if isinstance(channels, str):
        if channels not in DeepChannelsSSE.options():
            raise PyEXception('Channel not recognized: %s', type(channels))
        channels = [channels]
    elif isinstance(channels, DeepChannelsSSE):
        channels = [channels.value]
    elif isinstance(channels, list):
        for i, c in enumerate(channels):
            if isinstance(c, DeepChannelsSSE):
                channels[i] = c.value
            elif not isinstance(c, str) or isinstance(c, str) and c not in DeepChannelsSSE.options():
                raise PyEXception('Channel not recognized: %s', c)

    channels = _strCommaSeparatedString(channels)

    if version == 'sandbox':
        return _streamSSE(_SSE_DEEP_URL_PREFIX_SANDBOX.format(symbols=symbols, channels=channels, token=token, version=version), on_data)
    return _streamSSE(_SSE_DEEP_URL_PREFIX.format(symbols=symbols, channels=channels, token=token, version=version), on_data)


def tradesSSE(symbols=None, on_data=None, token='', version=''):
    '''Trade report messages are sent when an order on the IEX Order Book is executed in whole or in part. DEEP sends a Trade report message for every individual fill.

    https://iexcloud.io/docs/api/#deep-trades

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    symbols = _strCommaSeparatedString(symbols)
    if version == 'sandbox':
        return _streamSSE(_SSE_DEEP_URL_PREFIX_SANDBOX.format(symbols=symbols, channels='trades', token=token, version=version), on_data)
    return _streamSSE(_SSE_DEEP_URL_PREFIX.format(symbols=symbols, channels='trades', token=token, version=version), on_data)


def auctionSSE(symbols=None, on_data=None, token='', version=''):
    '''DEEP broadcasts an Auction Information Message every one second between the Lock-in Time and the auction match for Opening and Closing Auctions,
    and during the Display Only Period for IPO, Halt, and Volatility Auctions. Only IEX listed securities are eligible for IEX Auctions.

    https://iexcloud.io/docs/api/#deep-auction

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('auction', symbols, on_data, token, version)


def bookSSE(symbols=None, on_data=None, token='', version=''):
    '''Book shows IEX’s bids and asks for given symbols.

    https://iexcloud.io/docs/api/#deep-book

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('book', symbols, on_data, token, version)


def opHaltStatusSSE(symbols=None, on_data=None, token='', version=''):
    '''The Exchange may suspend trading of one or more securities on IEX for operational reasons and indicates such operational halt using the Operational halt status message.

    IEX disseminates a full pre-market spin of Operational halt status messages indicating the operational halt status of all securities.
    In the spin, IEX will send out an Operational Halt Message with “N” (Not operationally halted on IEX) for all securities that are eligible for trading at the start of the Pre-Market Session.
    If a security is absent from the dissemination, firms should assume that the security is being treated as operationally halted in the IEX Trading System at the start of the Pre-Market Session.

    After the pre-market spin, IEX will use the Operational halt status message to relay changes in operational halt status for an individual security.

    https://iexcloud.io/docs/api/#deep-operational-halt-status

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('op-halt-status', symbols, on_data, token, version)


def officialPriceSSE(symbols=None, on_data=None, token='', version=''):
    '''The Official Price message is used to disseminate the IEX Official Opening and Closing Prices.

    These messages will be provided only for IEX Listed Securities.

    https://iexcloud.io/docs/api/#deep-official-price

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('official-price', symbols, on_data, token, version)


def securityEventSSE(symbols=None, on_data=None, token='', version=''):
    '''The Security event message is used to indicate events that apply to a security. A Security event message will be sent whenever such event occurs

    https://iexcloud.io/docs/api/#deep-security-event

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('security-event', symbols, on_data, token, version)


def ssrStatusSSE(symbols=None, on_data=None, token='', version=''):
    '''In association with Rule 201 of Regulation SHO, the Short Sale Price Test Message is used to indicate when a short sale price test restriction is in effect for a security.

    IEX disseminates a full pre-market spin of Short sale price test status messages indicating the Rule 201 status of all securities. After the pre-market spin, IEX will use the Short sale price test status message in the event of an intraday status change.

    The IEX Trading System will process orders based on the latest short sale price test restriction status.

    https://iexcloud.io/docs/api/#deep-short-sale-price-test-status

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('ssr-status', symbols, on_data, token, version)


def systemEventSSE(symbols=None, on_data=None, token='', version=''):
    '''The System event message is used to indicate events that apply to the market or the data feed.

    There will be a single message disseminated per channel for each System Event type within a given trading session.

    https://iexcloud.io/docs/api/#deep-system-event

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('system-event', symbols, on_data, token, version)


def tradeBreaksSSE(symbols=None, on_data=None, token='', version=''):
    '''Trade report messages are sent when an order on the IEX Order Book is executed in whole or in part. DEEP sends a Trade report message for every individual fill.

    https://iexcloud.io/docs/api/#deep-trades

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('trade-breaks', symbols, on_data, token, version)


def tradingStatusSSE(symbols=None, on_data=None, token='', version=''):
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
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('trading-status', symbols, on_data, token, version)
