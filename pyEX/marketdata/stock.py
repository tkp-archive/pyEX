# -*- coding: utf-8 -*-
from enum import Enum
from functools import wraps
from .sse import _runSSE, _runSSEAsync


class StockSSE(Enum):
    STOCKSUSNOUTP = 'stocksUSNoUTP'
    STOCKSUS = 'stocksUS'
    STOCKSUS1SECOND = 'stocksUS1Second'
    STOCKSUS5SECOND = 'stocksUS5Second'
    STOCKSUS1MINUTE = 'stocksUS1Minute'

    @staticmethod
    def options():
        return list(map(lambda c: c.value, StockSSE))


def _baseSSE(symbols=None, on_data=None, token='', version='', name=''):
    '''https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version

    '''
    return _runSSE(name, symbols, on_data, token, version)


async def _baseSSEAsync(symbols=None, on_data=None, token='', version='', name=''):
    '''https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version

    '''
    for item in _runSSEAsync(name, symbols, on_data, token, version):
        yield item


@wraps(_baseSSE)
def stocksUSNoUTPSSE(symbols=None, on_data=None, token='', version=''):
    return _baseSSE(symbols, on_data, token, version, 'stocksUSNoUTP')


@wraps(_baseSSEAsync)
def stocksUSNoUTPSSEAsync(symbols=None, token='', version=''):
    for item in _baseSSEAsync(symbols, token, version, 'stocksUSNoUTP'):
        yield item


@wraps(_baseSSE)
def stocksUSSSE(symbols=None, on_data=None, token='', version=''):
    return _baseSSE(symbols, on_data, token, version, 'stocksUS')


@wraps(_baseSSEAsync)
def stocksUSSSEAsync(symbols=None, token='', version=''):
    for item in _baseSSEAsync(symbols, token, version, 'stocksUS'):
        yield item


@wraps(_baseSSE)
def stocksUS1SecondSSE(symbols=None, on_data=None, token='', version=''):
    return _baseSSE(symbols, on_data, token, version, 'stocksUS1Second')


@wraps(_baseSSEAsync)
def stocksUS1SecondSSEAsync(symbols=None, token='', version=''):
    for item in _baseSSEAsync(symbols, token, version, 'stocksUS1Second'):
        yield item


@wraps(_baseSSE)
def stocksUS5SecondSSE(symbols=None, on_data=None, token='', version=''):
    return _baseSSE(symbols, on_data, token, version, 'stocksUS5Second')


@wraps(_baseSSEAsync)
def stocksUS5SecondSSEAsync(symbols=None, token='', version=''):
    for item in _baseSSEAsync(symbols, token, version, 'stocksUS5Second'):
        yield item


@wraps(_baseSSE)
def stocksUS1MinuteSSE(symbols=None, on_data=None, token='', version=''):
    return _baseSSE(symbols, on_data, token, version, 'stocksUS1Minute')


@wraps(_baseSSEAsync)
def stocksUS1MinuteSSEAsync(symbols=None, token='', version=''):
    for item in _baseSSEAsync(symbols, token, version, 'stocksUS1Minute'):
        yield item
