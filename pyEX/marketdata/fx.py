# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum
from functools import wraps

from .sse import _runSSE, _runSSEAsync


class FXSSE(Enum):
    FOREX = "forex"
    FOREX1SECOND = "forex1Second"
    FOREX5SECOND = "forex5Second"
    FOREX1MINUTE = "forex1Minute"

    @staticmethod
    def options():
        return list(map(lambda c: c.value, FXSSE))


def fxSSE(symbols=None, on_data=None, token="", version="", name="forex"):
    """This endpoint streams real-time foreign currency exchange rates.

    https://iexcloud.io/docs/api/#forex-currencies

    Args:
        symbols (str): Tickers to request, if None then firehose
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version

    """
    return _runSSE(name, symbols, on_data, token, version)


async def fxSSEAsync(symbols=None, token="", version="", name="forex"):
    """This endpoint streams real-time foreign currency exchange rates.

    https://iexcloud.io/docs/api/#forex-currencies

    Args:
        symbols (str): Tickers to request, if None then firehose
        token (str): Access token
        version (str): API version
    """
    async for item in _runSSEAsync(name, symbols, token, version):
        yield item


@wraps(fxSSE)
def forex1SecondSSE(symbols=None, on_data=None, token="", version=""):
    return fxSSE(symbols, on_data, token, version, "forex1Second")


@wraps(fxSSEAsync)
def forex1SecondSSEAsync(symbols=None, token="", version=""):
    for item in fxSSEAsync(symbols, token, version, "forex1Second"):
        yield item


@wraps(fxSSE)
def forex5SecondSSE(symbols=None, on_data=None, token="", version=""):
    return fxSSE(symbols, on_data, token, version, "forex5Second")


@wraps(fxSSEAsync)
def forex5SecondSSEAsync(symbols=None, token="", version=""):
    for item in fxSSEAsync(symbols, token, version, "forex5Second"):
        yield item


@wraps(fxSSE)
def forex1MinuteSSE(symbols=None, on_data=None, token="", version=""):
    return fxSSE(symbols, on_data, token, version, "forex1Minute")


@wraps(fxSSEAsync)
def forex1MinuteSSEAsync(symbols=None, token="", version=""):
    for item in fxSSEAsync(symbols, token, version, "forex1Minute"):
        yield item
