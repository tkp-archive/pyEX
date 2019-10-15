# -*- coding: utf-8 -*-
from enum import Enum
from .sse import _runSSE


class FXSSE(Enum):
    FOREX = 'forex'

    @staticmethod
    def options():
        return list(map(lambda c: c.value, FXSSE))


# def _runSSE(method='', symbols=None, on_data=None, token='', version=''):


def fxSSE(symbols=None, on_data=None, token='', version=''):
    '''This endpoint streams real-time foreign currency exchange rates.

    https://iexcloud.io/docs/api/#forex-currencies

    Args:
        symbols (string); Tickers to request
        on_data (function): Callback on data
        token (string); Access token
        version (string); API version

    '''
    return _runSSE('forex', symbols, on_data, token, version)
