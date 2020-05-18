# pyEX
Python interface to IEX Api (https://iextrading.com/developer/docs/)

[![Build Status](https://dev.azure.com/tpaine154/pyEX/_apis/build/status/timkpaine.pyEX?branchName=master)](https://dev.azure.com/tpaine154/pyEX/_build/latest?definitionId=3&branchName=master)
[![Coverage](https://img.shields.io/azure-devops/coverage/tpaine154/pyEX/3/master)](https://img.shields.io/azure-devops/coverage/tpaine154/pyEX/3)
[![License](https://img.shields.io/github/license/timkpaine/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![PyPI](https://img.shields.io/pypi/v/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![Docs](https://readthedocs.org/projects/pyex/badge/?version=latest)](https://pyex.readthedocs.io/en/latest/?badge=latest)

## Referral
Please subscribe to IEX Cloud using [my referral code](https://iexcloud.io/s/6332a3c3 ).

# Getting Started
Install from pip

`pip install pyEX`

of from source

`python setup.py install`

- [Demo Notebook - IEX Cloud](https://github.com/timkpaine/pyEX/blob/master/examples/all.ipynb)
- [Streaming Notebook - IEX Cloud](https://github.com/timkpaine/pyEX/blob/master/examples/sse.ipynb)
- [Read The Docs!](https://pyEX.readthedocs.io)

`pyEX` supports the IEX Cloud api through 2 interfaces. The first is a simple function call, passing in the api version and token as arguments

```bash
In [1]: import pyEX as p

In [2]: p.chart?
Signature: p.chart(symbol, timeframe='1m', date=None, token='', version='', filter='')
Docstring:
Historical price/volume data, daily and intraday

https://iexcloud.io/docs/api/#historical-prices
Data Schedule
1d: -9:30-4pm ET Mon-Fri on regular market trading days
    -9:30-1pm ET on early close trading days
All others:
    -Prior trading day available after 4am ET Tue-Sat

Args:
    symbol (string); Ticker to request
    timeframe (string); Timeframe to request e.g. 1m
    date (datetime): date, if requesting intraday
    token (string); Access token
    version (string); API version
    filter (string); filters: https://iexcloud.io/docs/api/#filter-results

Returns:
    dict: result
```

For most calls, there is a convenience method that returns a dataframe as well:

```bash
In [5]: [_ for _ in dir(p) if _.endswith('DF')]
Out[5]:
['advancedStatsDF',
 'auctionDF',
 'balanceSheetDF',
 'batchDF',
 'bookDF',
 'bulkBatchDF',
 'bulkMinuteBarsDF',
 'calendarDF',
...
```

Since the token rarely changes, we have a `Client` object for convenience:

```bash
In [6]: p.Client?
Init signature: p.Client(api_token=None, version='v1', api_limit=5)
Docstring:
IEX Cloud Client

Client has access to all methods provided as standalone, but in an authenticated way

Args:
    api_token (string): api token (can pickup from IEX_TOKEN environment variable)
    version (string): api version to use (defaults to v1)
                      set version to 'sandbox' to run against the IEX sandbox
    api_limit (int): cache calls in this interval
File:           ~/Programs/projects/iex/pyEX/pyEX/client.py
Type:           type
Subclasses:
```

The client will automatically pick up the API key from the environment variable `IEX_TOKEN`, or it can be passed as an argument. To use the IEX Cloud test environment, simple set `version='sandbox'`.

```bash
In [8]: c = p.Client(version='sandbox')

In [9]: c.chartDF('AAPL').head()
Out[9]:
              open   close    high     low    volume   uOpen  uClose   uHigh    uLow   uVolume  change  changePercent   label  changeOverTime
date
2019-11-27  271.31  274.04  277.09  268.75  16994433  267.69  271.99  271.82  266.32  16811747    0.00         0.0000  Nov 27        0.000000
2019-11-29  271.30  272.19  280.00  279.20  12135259  270.90  275.02  270.00  267.10  11927464   -0.60        -0.2255  Nov 29       -0.002232
2019-12-02  279.96  265.23  276.41  267.93  23831255  279.97  266.80  281.32  269.29  24607845   -3.20        -1.1646   Dec 2       -0.013820
2019-12-03  261.54  271.05  259.96  262.09  30331487  259.87  271.34  269.02  260.71  30518449   -4.93        -1.8450   Dec 3       -0.032745
2019-12-04  272.81  273.56  271.26  267.06  17109161  267.30  262.82  274.99  270.83  17230517    2.39         0.8955   Dec 4       -0.023411
```

## Improvements over native API, other libraries, etc
- pyEX will **transparently cache requests** according to the refresh interval as defined on the IEX Cloud website (and in the docstrings), to avoid wasting credits. It can also cache to disk, or integrate with your own custom caching scheme. 
- pyEX fully implements the streaming APIs

## Other enhancements
- [pyEX-studies](https://github.com/timkpaine/pyEX-studies): pyEX integration with TA-Lib and other libraries, for technical analysis and other metrics on top of the IEX data
- [pyEX-caching](https://github.com/timkpaine/pyEX-caching): persistent, queryable caching for pyEX function calls. Minimize your spend and maximize your performance
- [pyEX-zipline](https://github.com/timkpaine/pyEX-zipline): [Zipline](https://github.com/quantopian/zipline) integration for IEX data

## Demo
![](https://raw.githubusercontent.com/timkpaine/pyEX/master/docs/img/example1.gif)

## Full API
Please see the [readthedocs](https://pyEX.readthedocs.io) for a full API spec

![](https://raw.githubusercontent.com/timkpaine/pyEX/master/docs/img/rtd.png)


## Attribution
- [Powered by IEX Cloud](https://iexcloud.io)
- Data provided for free by [IEX](https://iextrading.com/developer).
- [IEX terms of service](https://iextrading.com/api-exhibit-a)
