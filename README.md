# pyEX
Python interface to IEX Api (https://iextrading.com/developer/docs/)

[![Build Status](https://travis-ci.org/timkpaine/pyEX.svg?branch=master)](https://travis-ci.org/timkpaine/pyEX)
[![Coverage](https://codecov.io/gh/timkpaine/pyEX/branch/master/graph/badge.svg)](https://codecov.io/gh/timkpaine/pyEX)
[![BCH compliance](https://bettercodehub.com/edge/badge/timkpaine/pyEX?branch=master)](https://bettercodehub.com/)
[![License](https://img.shields.io/github/license/timkpaine/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![PyPI](https://img.shields.io/pypi/v/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![Docs](https://readthedocs.org/projects/pyex/badge/?version=latest)](https://pyex.readthedocs.io/en/latest/?badge=latest)

# Getting Started

- [Read The Docs!](https://pyEX.readthedocs.io)
- [Demo Notebook - IEX](https://github.com/timkpaine/pyEX/blob/master/examples/all.ipynb)
- [Streaming Notebook - IEX](https://github.com/timkpaine/pyEX/blob/master/examples/ws.ipynb)
- [Demo Notebook - IEX Cloud](https://github.com/timkpaine/pyEX/blob/master/examples/client.ipynb)
- [Streaming Notebook - IEX Cloud](https://github.com/timkpaine/pyEX/blob/master/examples/sse.ipynb)


## Referral
Please subscribe to IEX Cloud using [my referral code](https://iexcloud.io/s/6332a3c3 ).


![](https://raw.githubusercontent.com/timkpaine/pyEX/master/docs/img/example1.gif)

## 6 Months of spy data in a dataframe in 2 lines:

```python
    # fetch spy from website, clean for some bad formatted symbols
    spy = [x for x in pandas.read_html('https://etfdailynews.com/etf/spy/', attrs={'id': 'etfs-that-own'})[0].Symbol.values.tolist() if isinstance(x, str)]

    # bulk fetch 6m of data
    pyEX.bulkBatchDF(spy, ['chart'], _range='6m')['chart']
```


## Attribution
- [Powered by IEX Cloud](https://iexcloud.io)
- Data provided for free by [IEX](https://iextrading.com/developer).
- [IEX terms of service](https://iextrading.com/api-exhibit-a)
