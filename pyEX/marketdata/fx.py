# -*- coding: utf-8 -*-
from enum import Enum
from .sse import _runSSE, _runSSEAsync


class FXSSE(Enum):
    FOREX = 'forex'

    @staticmethod
    def options():
        return list(map(lambda c: c.value, FXSSE))


def fxSSE(symbols=None, on_data=None, token='', version=''):
    '''This endpoint streams real-time foreign currency exchange rates.

    https://iexcloud.io/docs/api/#forex-currencies

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version

    '''
    return _runSSE('forex', symbols, on_data, token, version)


async def fxSSEAsync(symbols=None, token='', version=''):
    '''This endpoint streams real-time foreign currency exchange rates.

    https://iexcloud.io/docs/api/#forex-currencies

    Args:
        symbols (str): Tickers to request
        token (str): Access token
        version (str): API version
    '''
    async for item in _runSSEAsync('forex', symbols, token, version):
        yield item
