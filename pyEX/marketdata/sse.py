from enum import Enum
from ..common import _strCommaSeparatedString, _streamSSE, _SSE_URL_PREFIX, _SSE_DEEP_URL_PREFIX, PyEXception


class DeepChannelsSSE(Enum):
    # TRADINGSTATUS = 'tradingstatus'
    # AUCTION = 'auction'
    # OPHALTSTATUS = 'ophaltstatus'
    # SSR = 'ssr'
    # SECURITYEVENT = 'securityevent'
    # TRADEBREAK = 'tradebreak'
    TRADES = 'trades'
    # BOOK = 'book'
    # SYSTEMEVENT = 'systemevent'
    ALL = 'deep'

    @staticmethod
    def options():
        return list(map(lambda c: c.value, DeepChannelsSSE))


def _runSSE(method='', symbols=None, on_data=None, token='', version=''):
    symbols = _strCommaSeparatedString(symbols)
    if symbols:
        return _streamSSE(_SSE_URL_PREFIX.format(channel=method, symbols=symbols, token=token, version=version), on_data=on_data)
    return _streamSSE(_SSE_URL_PREFIX.format(channel=method, symbols=symbols, token=token, version=version), on_data=on_data)


def topsSSE(symbols=None, on_data=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#tops'''
    return _runSSE('tops', symbols, on_data, token, version)


def lastSSE(symbols=None, on_data=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#last'''
    return _runSSE('last', symbols, on_data, token, version)


def deepSSE(symbols=None, channels=None, on_data=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#deep'''
    symbols = _strCommaSeparatedString(symbols)

    channels = channels or []
    if isinstance(channels, str):
        if channels not in DeepChannelsSSE.options():
            raise PyEXception('Channel not recognized: %s', type(channels))
        channels = [channels]
    elif isinstance(channels, DeepChannelsSSE):
        channels = [channels.value]
    elif isinstance(channels, list):
        for i, c in enumerate(channels):
            if isinstance(c, DeepChannelsSSE):
                channels[i] = c.value
            elif not isinstance(c, str) or isinstance(c, str) and c not in DeepChannelsSSE.options():
                raise PyEXception('Channel not recognized: %s', c)

    channels = _strCommaSeparatedString(channels)
    return _streamSSE(_SSE_DEEP_URL_PREFIX.format(symbols=symbols, channels=channels, token=token, version=version), on_data)


def tradesSSE(symbols=None, on_data=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#trades'''
    symbols = _strCommaSeparatedString(symbols)
    return _streamSSE(_SSE_DEEP_URL_PREFIX.format(symbols=symbols, channels='trades', token=token, version=version), on_data)
