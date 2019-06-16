from __future__ import print_function
import requests
try:
    import ujson as json
except ImportError:
    import json
import pandas as pd
from datetime import datetime
from socketIO_client_nexus import SocketIO, BaseNamespace
from sseclient import SSEClient
from six import string_types

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

_URL_PREFIX = 'https://api.iextrading.com/1.0/'
_URL_PREFIX2 = 'https://cloud.iexapis.com/{version}/'
_URL_PREFIX2_SANDBOX = 'https://sandbox.iexapis.com/{version}/'

_SIO_URL_PREFIX = 'https://ws-api.iextrading.com'
_SIO_PORT = 443

_SSE_URL_PREFIX = 'https://cloud-sse.iexapis.com/{version}/{channel}?symbols={symbols}&token={token}'
_SSE_URL_PREFIX_ALL = 'https://cloud-sse.iexapis.com/{version}/{channel}?token={token}'
_SSE_DEEP_URL_PREFIX = 'https://cloud-sse.iexapis.com/{version}/deep?symbols={symbols}&channels={channels}&token={token}'

_TIMEFRAME_CHART = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1d']
_TIMEFRAME_DIVSPLIT = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m']
_LIST_OPTIONS = ['mostactive', 'gainers', 'losers', 'iexvolume', 'iexpercent']
_COLLECTION_TAGS = ['sector', 'tag', 'list']

_USAGE_TYPES = ['messages', 'rules', 'rule-records', 'alerts', 'alert-records']
_PYEX_PROXIES = None

# Limit 10
_BATCH_TYPES = [
    'book',
    'chart',
    'company',
    'dividends',
    'earnings',
    'financials',
    'stats',
    'news',
    'peers',
    'splits',
    # limit 10
    'effective-spread',
    'delayed-quote',
    'largest-trades',
    'previous',
    'price',
    'quote',
    'relevant',
    'volume-by-venue',
]

_STANDARD_DATE_FIELDS = ['date',
                         'EPSReportDate',
                         'fiscalEndDate',
                         'exDate',
                         'declaredDate',
                         'paymentDate',
                         'recordDate',
                         'reportDate',
                         'datetime',
                         'expectedDate',
                         'latestTime',
                         'DailyListTimestamp',
                         'RecordUpdateTime',
                         'settlementDate',
                         'lastUpdated',
                         'processedTime',
                         'expirationDate']

_STANDARD_TIME_FIELDS = ['closeTime',
                         'close.time',
                         'delayedPriceTime',
                         'extendedPriceTime',
                         'iexLastUpdated',
                         'latestTime',
                         'openTime',
                         'open.time',
                         'processedTime',
                         'time',
                         'timestamp',
                         'lastUpdated',
                         'reportDate',
                         'report_date']


class PyEXception(Exception):
    pass


def _getJson(url, token='', version='', filter=''):
    '''for backwards compat, accepting token and version but ignoring'''
    if token:
        if version == 'sandbox':
            return _getJsonIEXCloudSandbox(url, token, version, filter)
        return _getJsonIEXCloud(url, token, version, filter)
    return _getJsonOrig(url)


def _getJsonOrig(url):
    '''internal'''
    url = _URL_PREFIX + url
    resp = requests.get(urlparse(url).geturl(), proxies=_PYEX_PROXIES)
    if resp.status_code == 200:
        return resp.json()
    raise PyEXception('Response %d - ' % resp.status_code, resp.text)


def _getJsonIEXCloud(url, token='', version='beta', filter=''):
    '''for iex cloud'''
    url = _URL_PREFIX2.format(version=version) + url
    if filter:
        url += '?filter={filter}'.format(filter=filter)
    resp = requests.get(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params={'token': token})
    if resp.status_code == 200:
        return resp.json()
    raise PyEXception('Response %d - ' % resp.status_code, resp.text)


def _getJsonIEXCloudSandbox(url, token='', version='beta'):
    '''for iex cloud'''
    url = _URL_PREFIX2_SANDBOX.format(version='beta') + url
    resp = requests.get(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params={'token': token})
    if resp.status_code == 200:
        return resp.json()
    raise PyEXception('Response %d - ' % resp.status_code, resp.text)


def _wsURL(url):
    '''internal'''
    return '/1.0/' + url


def _strToList(st):
    '''internal'''
    if isinstance(st, string_types):
        return [st]
    return st


def _strCommaSeparatedString(st):
    '''internal'''
    return ','.join(_strToList(st))


def _strOrDate(st):
    '''internal'''
    if isinstance(st, string_types):
        return st
    elif isinstance(st, datetime):
        return st.strftime('%Y%m%d')
    raise PyEXception('Not a date: %s', str(st))


def _raiseIfNotStr(s):
    '''internal'''
    if s is not None and not isinstance(s, string_types):
        raise PyEXception('Cannot use type %s' % str(type(s)))


def _tryJson(data, raw=True):
    '''internal'''
    if raw:
        return data
    try:
        return json.loads(data)
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
    '''internal'''
    cl = WSClient(url, sendinit=sendinit, on_data=on_data)
    return cl


def _streamSSE(url, on_data=print, accrue=False):
    '''internal'''
    messages = SSEClient(url)
    if accrue:
        ret = []

    for msg in messages:
        data = msg.data
        on_data(json.loads(data))
        if accrue:
            ret.append(msg)

    return ret


def _reindex(df, col):
    '''internal'''
    if col in df.columns:
        df.set_index(col, inplace=True)


def _toDatetime(df, cols=None, tcols=None):
    '''internal'''
    cols = cols if cols is not None else _STANDARD_DATE_FIELDS
    tcols = tcols if tcols is not None else _STANDARD_TIME_FIELDS

    for col in cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], infer_datetime_format=True)

    for tcol in tcols:
        if tcol in df.columns:
            df[tcol] = pd.to_datetime(df[tcol], unit='ms')


def setProxy(proxies=None):
    '''Set proxies argument for requests

    Args:
        proxies (dict): Proxies to set
    '''
    global _PYEX_PROXIES
    _PYEX_PROXIES = proxies
