import requests
import pandas as pd


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
