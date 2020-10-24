# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import os.path
import pandas as pd
import pytz
import requests
import tempfile
import json
from datetime import datetime
from six import string_types
from socketIO_client_nexus import SocketIO, BaseNamespace
from sseclient import SSEClient
from temporalcache import expire, interval

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
_SSE_URL_PREFIX_SANDBOX = 'https://sandbox-sse.iexapis.com/v1/{channel}?symbols={symbols}&token={token}'
_SSE_URL_PREFIX_ALL_SANDBOX = 'https://sandbox-sse.iexapis.com/v1/{channel}?token={token}'
_SSE_DEEP_URL_PREFIX_SANDBOX = 'https://sandbox-sse.iexapis.com/v1/deep?symbols={symbols}&channels={channels}&token={token}'

_TIMEFRAME_CHART = ['max', '5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1mm', '5d', '5dm', '1d', 'dynamic']
_TIMEFRAME_DIVSPLIT = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m', 'next']
_LIST_OPTIONS = ['mostactive', 'gainers', 'losers', 'iexvolume', 'iexpercent']
_COLLECTION_TAGS = ['sector', 'tag', 'list']
_DATE_RANGES = ['today',
                'yesterday',
                'ytd',
                'last-week',
                'last-month',
                'last-quarter',
                'd',
                'w',
                'm',
                'q',
                'y',
                'tomorrow',
                'this-week',
                'this-month',
                'this-quarter',
                'next-week',
                'next-month',
                'next-quarter']
_KEY_STATS = [
    'companyName',
    'marketcap',
    'week52high',
    'week52low',
    'week52change',
    'sharesOutstanding',
    'float',
    'avg10Volume',
    'avg30Volume',
    'day200MovingAvg',
    'day50MovingAvg',
    'employees',
    'ttmEPS',
    'ttmDividendRate',
    'dividendYield',
    'nextDividendDate',
    'exDividendDate',
    'nextEarningsDate',
    'peRatio',
    'beta',
    'maxChangePercent',
    'year5ChangePercent',
    'year2ChangePercent',
    'year1ChangePercent',
    'ytdChangePercent',
    'month6ChangePercent',
    'month3ChangePercent',
    'month1ChangePercent',
    'day30ChangePercent',
    'day5ChangePercent',
]
_USAGE_TYPES = ['messages', 'rules', 'rule-records', 'alerts', 'alert-records']
_PYEX_PROXIES = None
_PYEX_CACHE_FOLDER = os.path.abspath(os.path.join(tempfile.gettempdir(), "pyEX"))
_UTC = pytz.UTC
_EST = pytz.timezone('EST')

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
                         'expirationDate',
                         'startDate',
                         'endDate']

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

_INDICATORS = [
    "abs",
    "acos",
    "ad",
    "add",
    "adosc",
    "adx",
    "adxr",
    "ao",
    "apo",
    "aroon",
    "aroonosc",
    "asin",
    "atan",
    "atr",
    "avgprice",
    "bbands",
    "bop",
    "cci",
    "ceil",
    "cmo",
    "cos",
    "cosh",
    "crossany",
    "crossover",
    "cvi",
    "decay",
    "dema",
    "di",
    "div",
    "dm",
    "dpo",
    "dx",
    "edecay",
    "ema",
    "emv",
    "exp",
    "fisher",
    "floor",
    "fosc",
    "hma",
    "kama",
    "kvo",
    "lag",
    "linreg",
    "linregintercept",
    "linregslope",
    "ln",
    "log10",
    "macd",
    "marketfi",
    "mass",
    "max",
    "md",
    "medprice",
    "mfi",
    "min",
    "mom",
    "msw",
    "mul",
    "natr",
    "nvi",
    "obv",
    "ppo",
    "psar",
    "pvi",
    "qstick",
    "roc",
    "rocr",
    "round",
    "rsi",
    "sin",
    "sinh",
    "sma",
    "sqrt",
    "stddev",
    "stderr",
    "stoch",
    "stochrsi",
    "sub",
    "sum",
    "tan",
    "tanh",
    "tema",
    "todeg",
    "torad",
    "tr",
    "trima",
    "trix",
    "trunc",
    "tsf",
    "typprice",
    "ultosc",
    "var",
    "vhf",
    "vidya",
    "volatility",
    "vosc",
    "vwma",
    "wad",
    "wcprice",
    "wilders",
    "willr",
    "wma",
    "zlema",
]

_INDICATOR_RETURNS = {
    "abs": ("abs",),
    "acos": ("acos",),
    "ad": ("ad",),
    "add": ("add",),
    "adosc": ("adosc",),
    "adx": ("dx",),
    "adxr": ("dx",),
    "ao": ("ao",),
    "apo": ("apo",),
    "aroon": ("aroon_down", "aroon_up"),
    "aroonosc": ("aroonosc",),
    "asin": ("asin",),
    "atan": ("atan",),
    "atr": ("atr",),
    "avgprice": ("avgprice",),
    "bbands": ("bbands_lower", "bbands_middle", "bbands_upper",),
    "bop": ("bop",),
    "cci": ("cci",),
    "ceil": ("ceil",),
    "cmo": ("cmo",),
    "cos": ("cos",),
    "cosh": ("cosh",),
    "crossany": ("crossany",),
    "crossover": ("crossover",),
    "cvi": ("cvi",),
    "decay": ("decay",),
    "dema": ("dema",),
    "di": ("plus_di", "minus_di",),
    "div": ("div",),
    "dm": ("plus_dm", "minus_dm",),
    "dpo": ("dop",),
    "dx": ("dx",),
    "edecay": ("edecay",),
    "ema": ("ema",),
    "emv": ("emv",),
    "exp": ("exp",),
    "fisher": ("fisher", "fisher_signal",),
    "floor": ("floor",),
    "fosc": ("fosc",),
    "hma": ("hma",),
    "kama": ("kama",),
    "kvo": ("kvo",),
    "lag": ("lag",),
    "linreg": ("linreg",),
    "linregintercept": ("linregintercept",),
    "linregslope": ("linregslope",),
    "ln": ("ln",),
    "log10": ("log10",),
    "macd": ("macd", "macd_signal", "macd_histogram",),
    "marketfi": ("marketfi",),
    "mass": ("mass",),
    "max": ("max",),
    "md": ("md",),
    "medprice": ("medprice",),
    "mfi": ("mfi",),
    "min": ("min",),
    "mom": ("mom",),
    "msw": ("msw_sine", "msw_lead",),
    "mul": ("mul",),
    "natr": ("matr",),
    "nvi": ("nvi",),
    "obv": ("obv",),
    "ppo": ("ppo",),
    "psar": ("psar",),
    "pvi": ("pvi",),
    "qstick": ("qstick",),
    "roc": ("roc",),
    "rocr": ("rocr",),
    "round": ("round",),
    "rsi": ("rsi",),
    "sin": ("sin",),
    "sinh": ("sinh",),
    "sma": ("sma",),
    "sqrt": ("sqrt",),
    "stddev": ("stddev",),
    "stderr": ("stderr",),
    "stoch": ("stock_k", "stock_d",),
    "stochrsi": ("stochrsi",),
    "sub": ("sub",),
    "sum": ("sum",),
    "tan": ("tan",),
    "tanh": ("tanh",),
    "tema": ("tema",),
    "todeg": ("degrees",),
    "torad": ("radians",),
    "tr": ("tr",),
    "trima": ("trima",),
    "trix": ("trix",),
    "trunc": ("trunc",),
    "tsf": ("tsf",),
    "typprice": ("typprice",),
    "ultosc": ("ultosc",),
    "var": ("var",),
    "vhf": ("vhf",),
    "vidya": ("vidya",),
    "volatility": ("volatility",),
    "vosc": ("vosc",),
    "vwma": ("vwma",),
    "wad": ("wad",),
    "wcprice": ("wcprice",),
    "wilders": ("wilders",),
    "willr": ("willr",),
    "wma": ("wma",),
    "zlema": ("zlema",),
}


class PyEXception(Exception):
    pass


class PyEXStopSSE(Exception):
    pass


def _getJson(url, token='', version='', filter=''):
    '''for backwards compat, accepting token and version but ignoring'''
    token = token or os.environ.get('IEX_TOKEN')
    if token:
        if version == 'sandbox':
            return _getJsonIEXCloudSandbox(url, token, version, filter)
        return _getJsonIEXCloud(url, token, version, filter)
    return _getJsonOrig(url)


async def _getJsonAsync(url, token='', version='', filter=''):
    '''for backwards compat, accepting token and version but ignoring'''
    token = token or os.environ.get('IEX_TOKEN')
    if token:
        if version == 'sandbox':
            return await _getJsonIEXCloudSandboxAsync(url, token, version, filter)
        return await _getJsonIEXCloudAsync(url, token, version, filter)
    return _getJsonOrig(url)


def _postJson(url, data=None, json=None, token='', version='', token_in_params=True):
    token = token or os.environ.get('IEX_TOKEN')
    if version == 'sandbox':
        return _postJsonIEXCloudSandbox(url, data, json, token, version, token_in_params)
    return _postJsonIEXCloud(url, data, json, token, version, token_in_params)


def _deleteJson(url, token='', version=''):
    token = token or os.environ.get('IEX_TOKEN')
    if version == 'sandbox':
        return _deleteJsonIEXCloudSandbox(url, token, version)
    return _deleteJsonIEXCloud(url, token, version)


def _getJsonOrig(url):
    raise PyEXception('Old IEX API is deprecated. For a free API token, sign up at https://iexcloud.io')


def _getJsonIEXCloudBase(base_url, url, token='', version='stable', filter=''):
    '''for iex cloud'''
    url = base_url.format(version=version) + url
    params = {'token': token}
    if filter:
        params.update({'filter': filter})
    resp = requests.get(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params=params)
    if resp.status_code == 200:
        return resp.json()
    raise PyEXception('Response %d - ' % resp.status_code, resp.text)


def _getJsonIEXCloud(url, token='', version='stable', filter=''):
    '''for iex cloud'''
    return _getJsonIEXCloudBase(_URL_PREFIX2, url, token, version, filter)


async def _getJsonIEXCloudAsyncBase(base_url, url, token='', version='stable', filter=''):
    '''for iex cloud'''
    import aiohttp
    url = _URL_PREFIX2.format(version=version) + url
    params = {'token': token}
    if filter:
        params.update({'filter': filter})
    async with aiohttp.ClientSession() as session:
        async with session.get(urlparse(url).geturl(), proxy=_PYEX_PROXIES, params=params) as resp:
            if resp.status == 200:
                return await resp.json()
            raise PyEXception('Response %d - ' % resp.status, await resp.text())


async def _getJsonIEXCloudAsync(url, token='', version='stable', filter=''):
    '''for iex cloud'''
    return await _getJsonIEXCloudAsyncBase(_URL_PREFIX2, url, token, version, filter)


def _postJsonIEXCloudBase(base_url, url, data=None, json=None, token='', version='stable', token_in_params=True):
    '''for iex cloud'''
    url = base_url.format(version=version) + url
    if token_in_params:
        params = {'token': token}
    else:
        params = {}
    resp = requests.post(urlparse(url).geturl(), data=data, json=json, proxies=_PYEX_PROXIES, params=params)
    if resp.status_code == 200:
        return resp.json()
    raise PyEXception('Response %d - ' % resp.status_code, resp.text)


def _postJsonIEXCloud(url, data=None, json=None, token='', version='stable', token_in_params=True):
    '''for iex cloud'''
    return _postJsonIEXCloudBase(_URL_PREFIX2, data, json, token, version, token_in_params)


async def _postJsonIEXCloudAsyncBase(base_url, url, data=None, json=None, token='', version='stable', filter='', token_in_params=True):
    '''for iex cloud'''
    import aiohttp
    url = base_url.format(version=version) + url
    if token_in_params:
        params = {'token': token}
    else:
        params = {}

    async with aiohttp.ClientSession() as session:
        async with session.post(urlparse(url).geturl(), data=data, json=json, proxy=_PYEX_PROXIES, params=params) as resp:
            if resp.status == 200:
                return await resp.json()
            raise PyEXception('Response %d - ' % resp.status, await resp.text())


async def _postJsonIEXCloudAsync(url, data=None, json=None, token='', version='stable', filter='', token_in_params=True):
    '''for iex cloud'''
    return await _postJsonIEXCloudAsyncBase(_URL_PREFIX2, url, data, json, token, version, filter, token_in_params)


def _deleteJsonIEXCloudBase(base_url, url, token='', version='stable'):
    '''for iex cloud'''
    url = base_url.format(version=version) + url
    params = {'token': token}
    resp = requests.delete(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params=params)
    if resp.status_code == 200:
        return resp.json()
    raise PyEXception('Response %d - ' % resp.status_code, resp.text)


def _deleteJsonIEXCloud(url, token='', version='stable'):
    '''for iex cloud'''
    return _deleteJsonIEXCloud(_URL_PREFIX2, url, token, version)


async def _deleteJsonIEXCloudAsyncBase(url, token='', version='stable'):
    '''for iex cloud'''
    import aiohttp
    url = _URL_PREFIX2.format(version=version) + url
    params = {'token': token}

    async with aiohttp.ClientSession() as session:
        async with session.delete(urlparse(url).geturl(), proxy=_PYEX_PROXIES, params=params) as resp:
            if resp.status == 200:
                return await resp.json()
            raise PyEXception('Response %d - ' % resp.status, await resp.text())


async def _deleteJsonIEXCloudAsync(url, token='', version='stable'):
    '''for iex cloud'''
    return await _deleteJsonIEXCloudAsyncBase(_URL_PREFIX2, url, token, version)


def _getJsonIEXCloudSandbox(url, token='', version='stable', filter=''):
    '''for iex cloud'''
    return _getJsonIEXCloudBase(_URL_PREFIX2_SANDBOX, url, token, 'stable', filter)


async def _getJsonIEXCloudSandboxAsync(url, token='', version='stable', filter=''):
    '''for iex cloud'''
    return await _getJsonIEXCloudAsyncBase(_URL_PREFIX2_SANDBOX, url, token, 'stable', filter)


def _postJsonIEXCloudSandbox(url, data=None, json=None, token='', version='stable', token_in_params=True):
    '''for iex cloud'''
    return _postJsonIEXCloudBase(_URL_PREFIX2_SANDBOX, url, data, json, token, 'stable', token_in_params)


def _deleteJsonIEXCloudSandbox(url, token='', version='stable'):
    '''for iex cloud'''
    return _deleteJsonIEXCloudBase(_URL_PREFIX2_SANDBOX, url, token, 'stable')


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


def _dateRange(st):
    '''internal'''
    if st not in _DATE_RANGES:
        raise PyEXception('Must be a valid date range: got {}'.format(st))
    return st


def _raiseIfNotStr(s):
    '''internal'''
    if s is not None and not isinstance(s, string_types):
        raise PyEXception('Cannot use type %s' % str(type(s)))


def _checkPeriodLast(per, last):
    '''check if period is ok with last'''
    if per not in ("quarter", "annual"):
        raise PyEXception("Period must be in {'quarter', 'annual'}")
    if per == 'quarter':
        if last < 1 or last > 12:
            raise PyEXception("Last must be in [1, 12] for period 'quarter'")
    else:
        if last < 1 or last > 4:
            raise PyEXception("Last must be in [1, 4] for period 'annual'")


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

        try:
            on_data(json.loads(data))
            if accrue:
                ret.append(msg)
        except PyEXStopSSE:
            # stop listening and return
            return ret
        except (json.JSONDecodeError, KeyboardInterrupt):
            raise
        except Exception:
            raise
    return ret


async def _streamSSEAsync(url, accrue=False):
    '''internal'''
    from aiohttp_sse_client import client as sse_client

    async with sse_client.EventSource(url) as event_source:
        try:
            async for event in event_source:
                yield json.loads(event.data)

        except (json.JSONDecodeError, KeyboardInterrupt):
            raise
        except ConnectionError:
            raise PyEXception("Could not connect to SSE Stream")
        except PyEXStopSSE:
            return
        except Exception:
            raise
    return


def _reindex(df, col):
    '''internal'''
    if isinstance(col, list):
        if all([c in df.columns for c in col]):
            df.set_index(col, inplace=True)
    else:
        if col in df.columns:
            df.set_index(col, inplace=True)


def _toDatetime(df, cols=None, tcols=None):
    '''internal'''
    cols = cols if cols is not None else _STANDARD_DATE_FIELDS
    tcols = tcols if tcols is not None else _STANDARD_TIME_FIELDS

    for col in cols:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], infer_datetime_format=True)
            except BaseException:
                # skip error
                continue

    for tcol in tcols:
        if tcol in df.columns:
            try:
                df[tcol] = pd.to_datetime(df[tcol], unit='ms')
            except BaseException:
                # skip error
                continue


def setProxy(proxies=None):
    '''Set proxies argument for requests

    Args:
        proxies (dict): Proxies to set
    '''
    global _PYEX_PROXIES
    _PYEX_PROXIES = proxies


def _expire(**temporal_args):
    if not os.path.exists(_PYEX_CACHE_FOLDER):
        os.makedirs(_PYEX_CACHE_FOLDER)

    def _wrapper(foo):
        temporal_args['persistent'] = os.path.join(_PYEX_CACHE_FOLDER, foo.__name__)
        return expire(**temporal_args)(foo)
    return _wrapper


def _interval(**temporal_args):
    if not os.path.exists(_PYEX_CACHE_FOLDER):
        os.makedirs(_PYEX_CACHE_FOLDER)

    def _wrapper(foo):
        temporal_args['persistent'] = os.path.join(_PYEX_CACHE_FOLDER, foo.__name__)
        return interval(**temporal_args)(foo)
    return _wrapper


def _requireSecret(token):
    if not token.startswith("sk"):
        raise PyEXception("Requires secret token!")
