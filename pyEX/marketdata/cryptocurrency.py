# -*- coding: utf-8 -*-
from enum import Enum
from .sse import _runSSE


class CryptoSSE(Enum):
    BOOK = 'cryptoBook'
    EVENTS = 'cryptoEvents'
    QUOTES = 'cryptoQuotes'

    @staticmethod
    def options():
        return list(map(lambda c: c.value, CryptoSSE))


# def _runSSE(method='', symbols=None, on_data=None, token='', version=''):


def cryptoBookSSE(symbols=None, on_data=None, token='', version=''):
    '''This returns a current snapshot of the book for a specified cryptocurrency. For REST, you will receive a current snapshot of the current book for the specific cryptocurrency. For SSE Streaming, you will get a full representation of the book updated as often as the book changes. Examples of each are below:

    https://iexcloud.io/docs/api/#cryptocurrency-book

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('cryptoBook', symbols, on_data, token, version)


def cryptoEventsSSE(symbols=None, on_data=None, token='', version=''):
    '''This returns a streaming list of event updates such as new and canceled orders.

    https://iexcloud.io/docs/api/#cryptocurrency-events

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('cryptoEvents', symbols, on_data, token, version)


def cryptoQuotesSSE(symbols=None, on_data=None, token='', version=''):
    '''This returns the quote for a specified cryptocurrency. Quotes are available via REST and SSE Streaming.

    https://iexcloud.io/docs/api/#cryptocurrency-quote

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('cryptoQuotes', symbols, on_data, token, version)
