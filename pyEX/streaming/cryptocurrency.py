# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum

from .sse import _runSSE, _runSSEAsync


class CryptoSSE(Enum):
    BOOK = "cryptoBook"
    EVENTS = "cryptoEvents"
    QUOTES = "cryptoQuotes"

    @staticmethod
    def options():
        return list(map(lambda c: c.value, CryptoSSE))


def cryptoBookSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """This returns a current snapshot of the book for a specified cryptocurrency. For REST, you will receive a current snapshot of the current book for the specific cryptocurrency. For SSE Streaming, you will get a full representation of the book updated as often as the book changes. Examples of each are below:

    https://iexcloud.io/docs/api/#cryptocurrency-book

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version

    """
    return _runSSE(
        "cryptoBook",
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    )


async def cryptoBookSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """This returns a current snapshot of the book for a specified cryptocurrency. For REST, you will receive a current snapshot of the current book for the specific cryptocurrency. For SSE Streaming, you will get a full representation of the book updated as often as the book changes. Examples of each are below:

    https://iexcloud.io/docs/api/#cryptocurrency-book

    Args:
        symbols (str): Tickers to request
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version
    """
    async for item in _runSSEAsync(
        "cryptoBook",
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    ):
        yield item


def cryptoEventsSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """This returns a streaming list of event updates such as new and canceled orders.

    https://iexcloud.io/docs/api/#cryptocurrency-events

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version

    """
    return _runSSE(
        "cryptoEvents",
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    )


async def cryptoEventsSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """This returns a streaming list of event updates such as new and canceled orders.

    https://iexcloud.io/docs/api/#cryptocurrency-events

    Args:
        symbols (str): Tickers to request
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version
    """
    async for item in _runSSEAsync(
        "cryptoEvents",
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    ):
        yield item


def cryptoQuotesSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """This returns the quote for a specified cryptocurrency. Quotes are available via REST and SSE Streaming.

    https://iexcloud.io/docs/api/#cryptocurrency-quote

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version

    """
    return _runSSE(
        "cryptoQuotes",
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    )


async def cryptoQuotesSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """This returns the quote for a specified cryptocurrency. Quotes are available via REST and SSE Streaming.

    https://iexcloud.io/docs/api/#cryptocurrency-quote

    Args:
        symbols (str): Tickers to request
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version
    """
    async for item in _runSSEAsync(
        "cryptoQuotes",
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    ):
        yield item
