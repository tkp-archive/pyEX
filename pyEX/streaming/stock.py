# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum
from functools import wraps

from .sse import _runSSE, _runSSEAsync


class StockSSE(Enum):
    STOCKSUSNOUTP = "stocksUSNoUTP"
    STOCKSUS = "stocksUS"
    STOCKSUS1SECOND = "stocksUS1Second"
    STOCKSUSNOUTP1SECOND = "stocksUSNoUTP1Second"
    STOCKSUS5SECOND = "stocksUS5Second"
    STOCKSUSNOUTP5SECOND = "stocksUSNoUTP5Second"
    STOCKSUS1MINUTE = "stocksUS1Minute"
    STOCKSUSNOUTP1MINUTE = "stocksUSNoUTP1Minute"

    @staticmethod
    def options():
        return list(map(lambda c: c.value, StockSSE))


def _baseSSE(
    symbols=None,
    on_data=None,
    exit=None,
    nosnapshot=False,
    token="",
    version="stable",
    name="",
):
    """https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request, if None then firehose
        on_data (function): Callback on data
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version

    """
    return _runSSE(
        name,
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    )


async def _baseSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable", name=""
):
    """https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request, if None then firehose
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version

    """
    for item in _runSSEAsync(
        name,
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    ):
        yield item


@wraps(_baseSSE)
def stocksUSNoUTPSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP",
    )


@wraps(_baseSSEAsync)
def stocksUSNoUTPSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP",
    ):
        yield item


@wraps(_baseSSE)
def stocksUSSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS",
    )


@wraps(_baseSSEAsync)
def stocksUSSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS",
    ):
        yield item


@wraps(_baseSSE)
def stocksUS1SecondSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS1Second",
    )


@wraps(_baseSSE)
def stocksUSNoUTP1SecondSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP1Second",
    )


@wraps(_baseSSEAsync)
def stocksUS1SecondSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS1Second",
    ):
        yield item


@wraps(_baseSSEAsync)
def stocksUSNoUTP1SecondSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP1Second",
    ):
        yield item


@wraps(_baseSSE)
def stocksUS5SecondSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS5Second",
    )


@wraps(_baseSSE)
def stocksUSNoUTP5SecondSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP5Second",
    )


@wraps(_baseSSEAsync)
def stocksUS5SecondSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS5Second",
    ):
        yield item


@wraps(_baseSSEAsync)
def stocksUSNoUTP5SecondSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP5Second",
    ):
        yield item


@wraps(_baseSSE)
def stocksUS1MinuteSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS1Minute",
    )


@wraps(_baseSSE)
def stocksUSNoUTP1MinuteSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return _baseSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP1Minute",
    )


@wraps(_baseSSEAsync)
def stocksUS1MinuteSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUS1Minute",
    ):
        yield item


@wraps(_baseSSEAsync)
def stocksUSNoUTP1MinuteSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in _baseSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="stocksUSNoUTP1Minute",
    ):
        yield item
