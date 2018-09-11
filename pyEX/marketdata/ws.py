from enum import Enum
from datetime import datetime
from ..common import _getJson, _strToList, _raiseIfNotStr, _stream, _wsURL, PyEXception


class DeepChannels(Enum):
    TRADINGSTATUS = 'tradingstatus'
    AUCTION = 'auction'
    OPHALTSTATUS = 'ophaltstatus'
    SSR = 'ssr'
    SECURITYEVENT = 'securityevent'
    TRADEBREAK = 'tradebreak'
    TRADES = 'trades'
    BOOK = 'book'
    SYSTEMEVENT = 'systemevent'
    ALL = 'deep'

    @staticmethod
    def options():
        return list(map(lambda c: c.value, DeepChannels))


def topsWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#tops'''
    symbols = _strToList(symbols)
    if symbols:
        sendinit = ('subscribe', ','.join(symbols))
        return _stream(_wsURL('tops'), sendinit, on_data)
    return _stream(_wsURL('tops'), on_data=on_data)


def lastWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#last'''
    symbols = _strToList(symbols)
    if symbols:
        sendinit = ('subscribe', ','.join(symbols))
        return _stream(_wsURL('last'), sendinit, on_data)
    return _stream(_wsURL('last'), on_data=on_data)


def deepWS(symbols=None, channels=None, on_data=None):
    '''https://iextrading.com/developer/docs/#deep'''
    symbols = _strToList(symbols)

    channels = channels or []
    if isinstance(channels, str):
        if channels not in DeepChannels.options():
            raise PyEXception('Channel not recognized: %s', type(channels))
        channels = [channels]
    elif isinstance(channels, DeepChannels):
        channels = [channels.value]
    elif isinstance(channels, list):
        for i, c in enumerate(channels):
            if isinstance(c, DeepChannels):
                channels[i] = c.value
            elif not isinstance(c, str) or isinstance(c, str) and c not in DeepChannels.options():
                raise PyEXception('Channel not recognized: %s', c)

    sendinit = ({'symbols': symbols, 'channels': channels},)
    return _stream(_wsURL('deep'), sendinit, on_data)


def bookWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#book51'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['book']},)
    return _stream(_wsURL('deep'), sendinit, on_data)


def tradesWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#trades'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['trades']},)
    return _stream(_wsURL('deep'), sendinit, on_data)


def systemEventWS(on_data=None):
    '''https://iextrading.com/developer/docs/#system-event'''
    sendinit = ({'channels': ['systemevent']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)


def tradingStatusWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#trading-status'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['tradingstatus']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)


def opHaltStatusWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#operational-halt-status'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['ophaltstatus']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)


def ssrStatusWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#short-sale-price-test-status'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['ssr']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)


def securityEventWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#security-event'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['securityevent']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)


def tradeBreakWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#trade-break'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['tradebreaks']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)


def auctionWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#auction'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['auction']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)


def officialPriceWS(symbols=None, on_data=None):
    '''https://iextrading.com/developer/docs/#official-price'''
    symbols = _strToList(symbols)
    sendinit = ({'symbols': symbols, 'channels': ['official-price']},)
    return _stream(_wsURL('/deep'), sendinit, on_data)
