# <a href="https://pyEX.readthedocs.io"><img src="https://raw.githubusercontent.com/iexcloud/pyEX/main/docs/img/icon.png" width="300"></a>

Python interface to [IEX Cloud](https://iexcloud.io/docs/api/)

[![Build Status](https://github.com/iexcloud/pyEX/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/iexcloud/pyEX/actions?query=workflow%3A%22Build+Status%22)
[![Coverage](https://codecov.io/gh/iexcloud/pyEX/branch/main/graph/badge.svg?token=ag2j2TV2wE)](https://codecov.io/gh/iexcloud/pyEX)
[![License](https://img.shields.io/github/license/iexcloud/pyEX.svg)](https://github.com/iexcloud/pyEX)
[![PyPI](https://img.shields.io/pypi/v/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![Docs](https://readthedocs.org/projects/pyex/badge/?version=latest)](https://pyex.readthedocs.io/en/latest/?badge=latest)

## Referral

Please subscribe to IEX Cloud using [this referral code](https://iexcloud.io/s/6332a3c3 ).

# Getting Started

## Install

Install from pip

`pip install pyEX`

or from source

`python setup.py install`

### Extensions

- `pyEX[async]`: `asyncio` integration for streaming APIs
- `pyEX[studies]`: Technical indicators and other calculations

## Demos + Docs

- [Demo Notebook - IEX Cloud](https://github.com/iexcloud/pyEX/blob/main/examples/all.ipynb)
- [Streaming Notebook - IEX Cloud](https://github.com/iexcloud/pyEX/blob/main/examples/sse.ipynb)
- [Read The Docs!](https://pyEX.readthedocs.io)

## Overview

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
    symbol (str); Ticker to request
    timeframe (str); Timeframe to request e.g. 1m
    date (datetime): date, if requesting intraday
    token (str); Access token
    version (str); API version
    filter (str); filters: https://iexcloud.io/docs/api/#filter-results

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
    api_token (str): api token (can pickup from IEX_TOKEN environment variable)
    version (str): api version to use (defaults to v1)
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

- [pyEX-studies](https://github.com/iexcloud/pyEX/tree/main/pyEX/studies): pyEX integration with TA-Lib and other libraries, for technical analysis and other metrics on top of the IEX data
- [pyEX-caching](https://github.com/timkpaine/pyEX-caching): persistent, queryable caching for pyEX function calls. Minimize your spend and maximize your performance
- [pyEX-zipline](https://github.com/timkpaine/pyEX-zipline): [Zipline](https://github.com/quantopian/zipline) integration for IEX data

## Demo

![](https://raw.githubusercontent.com/iexcloud/pyEX/main/docs/img/example1.gif)

## Rules Engine

`pyEX` implements methods for interacting with the [Rules Engine](https://iexcloud.io/docs/api/#rules-engine-beta).

```python
rule = {
        'conditions': [['changePercent','>',500],
                       ['latestPrice','>',100000]],
        'outputs': [{'frequency': 60,
                     'method': 'email',
                     'to': 'your_email@domain'
                    }]
        }

c.createRule(rule, 'MyTestRule', 'AAPL', 'all')  # returns {"id": <ruleID>, "weight": 2}

c.rules()  # list all rules
c.ruleInfo("<ruleID>")
c.ruleOutput("<ruleID>")
c.pauseRule("<ruleID>")
c.resumeRule("<ruleID>")
c.deleteRule("<ruleID>")
```

We also provide helper classes in python for constructing rules such that they abide by the rules schema (dictated in the `schema()` helper function)

## Methods

- [schema](https://iexcloud.io/docs/api/#rules-schema)
- [lookup](https://iexcloud.io/docs/api/#lookup-values)
- [create](https://iexcloud.io/docs/api/#creating-a-rule)
- [pause](https://iexcloud.io/docs/api/#pause-and-resume)
- [resume](https://iexcloud.io/docs/api/#pause-and-resume)
- [edit](https://iexcloud.io/docs/api/#edit-an-existing-rule)
- [rule (get info)](https://iexcloud.io/docs/api/#delete-a-rule)
- [rules (list all)](https://iexcloud.io/docs/api/#list-all-rules)
- [output](https://iexcloud.io/docs/api/#get-log-output)

## Data

`pyEX` provides wrappers around both static and SSE streaming data. For most static data endpoints, we provide both JSON and DataFrame return functions. For market data endpoints, we provide async wrappers as well using `aiohttp` (to install the dependencies,  `pip install pyEX[async]`).

DataFrame functions will have the suffix `DF`, and async functions will have the suffix `Async`.

SSE streaming data can either be used with callbacks:

`newsSSE('AAPL', on_data=my_function_todo_on_data)`

or via async generators (after installing `pyEX[async]`):

`async for data in newsSSE('AAPL'):`

### Full API

Please see the [readthedocs](https://pyEX.readthedocs.io) for a full API spec. Implemented methods are provided in [CATALOG.md](CATALOG.md).

![](https://raw.githubusercontent.com/iexcloud/pyEX/main/docs/img/rtd.png)

All methods share a common naming convention. If the API method is called [technicals](https://iexcloud.io/docs/api/#technical-indicators), there will be `technicals` and `technicalsDF` methods on the client. Additionally, most methods are provided in a scope, e.g. [wti](https://iexcloud.io/docs/api/#oil-prices) is available as `client.wti` and `client.commodities.wti`, [analystDays](https://iexcloud.io/docs/api/#analyst-days) from Wall Street Horizon is available as `client.premium.analystDays`, etc.

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This software is licensed under the Apache 2.0 license. See the
[LICENSE](LICENSE) and [AUTHORS](AUTHORS) files for details.
