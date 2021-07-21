# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from .sse import _runSSE, _runSSEAsync


def sentimentSSE(
    symbols=None, on_data=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """Stream social sentiment

    https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version
    """
    return _runSSE(
        "sentiment",
        symbols=symbols,
        on_data=on_data,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    )


async def sentimentSSEAsync(
    symbols=None, exit=None, nosnapshot=False, token="", version="stable"
):
    """Stream social sentiment

    https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        exit (Event): Trigger to exit
        token (str): Access token
        version (str): API version
    """
    async for item in _runSSEAsync(
        "sentiment",
        symbols=symbols,
        exit=exit,
        nosnapshot=nosnapshot,
        token=token,
        version=version,
    ):
        yield item
