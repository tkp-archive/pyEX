import requests
import pandas as pd
import ujson
from datetime import datetime
from socketIO_client_nexus import SocketIO, BaseNamespace


_URL_PREFIX = 'https://api.iextrading.com/1.0/'
_SIO_URL_PREFIX = 'https://ws-api.iextrading.com'
_SIO_PORT = 443
_TIMEFRAME_CHART = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1d']
_TIMEFRAME_DIVSPLIT = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m']
_LIST_OPTIONS = ['mostactive', 'gainers', 'losers', 'iexvolume', 'iexpercent']


def _getJson(url):
    url = _URL_PREFIX + url
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    raise PyEXception('Response %d - ' % resp.status_code, resp.text)


def _wsURL(url):
        return '/1.0/' + url


def _strToList(st):
    if isinstance(st, str):
        return [st]
    return st


def _strOrDate(st):
    if isinstance(st, str):
        return st
    elif isinstance(st, datetime):
        return st.strftime('%Y%m%d')
    raise PyEXception('Not a date: %s', str(st))


def _raiseIfNotStr(s):
    if s is not None and not isinstance(s, str):
        raise PyEXception('Cannot use type %s' % str(type(s)))


def _tryJson(data, raw=True):
    if raw:
        return data
    try:
        return ujson.loads(data)
    except ValueError:
        return data


class WSClient(object):
    def __init__(self, addr, sendinit=None, on_data=None, on_open=None, on_close=None, raw=True):
        '''
           addr: path to sio
           sendinit: tuple to emit
           on_data, on_open, on_close: functions to call
       '''
        self.addr = addr
        self.sendinit = sendinit

        on_data = on_data or print

        class Namespace(BaseNamespace):
            def on_connect(self, *data):
                if on_open:
                    on_open(_tryJson(data, raw))

            def on_disconnect(self, *data):
                if on_close:
                    on_close(_tryJson(data, raw))

            def on_message(self, data):
                on_data(_tryJson(data, raw))

        self._Namespace = Namespace

    def run(self):
        self.socketIO = SocketIO(_SIO_URL_PREFIX, _SIO_PORT)
        self.namespace = self.socketIO.define(self._Namespace, self.addr)
        if self.sendinit:
            self.namespace.emit(*self.sendinit)
        self.socketIO.wait()


def _stream(url, sendinit=None, on_data=print):
    cl = WSClient(url, sendinit=sendinit, on_data=on_data)
    return cl


class PyEXception(Exception):
    pass
