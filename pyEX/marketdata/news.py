# -*- coding: utf-8 -*-
from .sse import _runSSE, _runSSEAsync


def newsSSE(symbols=None, on_data=None, token='', version=''):
    '''Stream news

    https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version
    '''
    return _runSSE('news-stream', symbols, on_data, token, version)


async def newsSSEAsync(symbols=None, token='', version=''):
    '''Stream news

    https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version
    '''
    async for item in _runSSEAsync('news-stream', symbols, token, version):
        yield item
