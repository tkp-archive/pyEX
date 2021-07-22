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


class FXSSE(Enum):
    FOREX = "forex"
    FOREX1SECOND = "forex1Second"
    FOREX5SECOND = "forex5Second"
    FOREX1MINUTE = "forex1Minute"

    @staticmethod
    def options():
        return list(map(lambda c: c.value, FXSSE))


def fxSSE(
    symbols=None,
    on_data=None,
    exit=None,
    nosnapshot=False,
    token="",
    version="stable",
    name="forex",
):
    """This endpoint streams real-time foreign currency exchange rates.

    https://iexcloud.io/docs/api/#forex-currencies

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


async def fxSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable", name="forex"
):
    """This endpoint streams real-time foreign currency exchange rates.

    https://iexcloud.io/docs/api/#forex-currencies

    Args:
        symbols (str): Tickers to request, if None then firehose
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version
    """
    async for item in _runSSEAsync(
        name,
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    ):
        yield item


@wraps(fxSSE)
def forex1SecondSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return fxSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="forex1Second",
    )


@wraps(fxSSEAsync)
def forex1SecondSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in fxSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="forex1Second",
    ):
        yield item


@wraps(fxSSE)
def forex5SecondSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return fxSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="forex5Second",
    )


@wraps(fxSSEAsync)
def forex5SecondSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in fxSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="forex5Second",
    ):
        yield item


@wraps(fxSSE)
def forex1MinuteSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    return fxSSE(
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="forex1Minute",
    )


@wraps(fxSSEAsync)
def forex1MinuteSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    for item in fxSSEAsync(
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
        name="forex1Minute",
    ):
        yield item
