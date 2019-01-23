# pyEX
Python interface to IEX Api (https://iextrading.com/developer/docs/)

# Now supporting IEX Cloud

[![Build Status](https://travis-ci.org/timkpaine/pyEX.svg?branch=master)](https://travis-ci.org/timkpaine/pyEX)
[![Coverage](https://codecov.io/gh/timkpaine/pyEX/branch/master/graph/badge.svg)](https://codecov.io/gh/timkpaine/pyEX)
[![Waffle.io](https://badge.waffle.io/timkpaine/pyEX.png?label=ready&title=Ready)](https://waffle.io/timkpaine/pyEX?utm_source=badge)
[![BCH compliance](https://bettercodehub.com/edge/badge/timkpaine/pyEX?branch=master)](https://bettercodehub.com/)
[![License](https://img.shields.io/github/license/timkpaine/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![PyPI](https://img.shields.io/pypi/v/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![Docs](https://img.shields.io/readthedocs/pyEX.svg)](https://pyEX.readthedocs.io)


### Attribution
If you redistribute our API data:

- Cite IEX using the following text and link: “Data provided for free by [IEX](https://iextrading.com/developer).”
- Provide a link to https://iextrading.com/api-exhibit-a in your terms of service.
- Additionally, if you display our TOPS price data, cite “IEX Real-Time Price” near the price.

### IEX Cloud attribution
[Powered by IEX Cloud](https://iexcloud.io)


### Version 2 API
[There is a new IEX API being developed](https://github.com/iexg/IEX-API/issues/557), so all development efforts will focus on that in the near term. 

### Getting Started

- [Read The Docs!](https://pyEX.readthedocs.io)
- [Demo Notebook](https://github.com/timkpaine/pyEX/blob/master/all.ipynb)


![](https://raw.githubusercontent.com/timkpaine/pyEX/master/docs/img/example1.gif)



### 6 Months of spy data in a dataframe in 2 lines:

```python
    # fetch spy from website, clean for some bad formatted symbols
    spy = [x for x in pandas.read_html('https://etfdailynews.com/etf/spy/', attrs={'id': 'etfs-that-own'})[0].Symbol.values.tolist() if isinstance(x, str)]

    # bulk fetch 6m of data
    pyEX.bulkBatchDF(spy, ['chart'], _range='6m')['chart']
```


### Methods
[Notebook](https://github.com/timkpaine/pyEX/blob/master/all.ipynb)
