import requests
import pandas as pd
import websocket

_URL_PREFIX = 'https://api.iextrading.com/1.0/'
_TIMEFRAME_CHART = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1d']
_TIMEFRAME_DIVSPLIT = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m']
_LIST_OPTIONS = ['mostactive', 'gainers', 'losers', 'iexvolume', 'iexpercent']


def _getJson(url):
    url = _URL_PREFIX + url
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    raise Exception('Response %d - ' % resp.status_code, resp.text)


def _df(resp):
    df = {k: [v] for k, v in resp.items()}
    return pd.DataFrame(df)


def _strToList(st):
    if isinstance(st, str):
        return [st]
    return st


def _raiseIfNotStr(s):
    if s is not None and not isinstance(s, str):
        raise Exception('Cannot use type %s' % str(type(s)))


class WSClient(object):
    def __init__(self, addr, sendinit=None, on_data=None, on_open=None, on_close=None, on_error=None):
        self.on_data = on_data or print

        def on_message(ws, message):
            self.on_data(message)

        def on_error_default(ws, error):
            pass

        def on_close_default(ws):
            pass

        def on_open_default(ws):
            if sendinit:
                ws.send(sendinit)

        self.ws = websocket.WebSocketApp(addr,
                                         on_message=on_message,
                                         on_error=on_error if on_error else on_error_default,
                                         on_close=on_close if on_close else on_close_default)
        self.ws.on_open = on_open if on_open else on_open_default

    def run(self):
        self.ws.run_forever()


def _stream(url, sendinit=None, on_data=print):
    factory = WSClient(url, sendinit=sendinit, on_data=on_data)
    return factory
