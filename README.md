# pyEX
Python interface to IEX Api (https://iextrading.com/developer/docs/)

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



### Getting Started

![](https://raw.githubusercontent.com/timkpaine/pyEX/master/docs/img/example1.gif)


### Methods

#### Stocks

- [book](https://iextrading.com/developer/docs/#book)

    ```python3
        def book(symbol):
    ```

    ```python3
        def bookDF(symbol):
    ```

- [chart](https://iextrading.com/developer/docs/#chart)

    ```python3
        def chart(symbol, timeframe='1m', date=None):
    ```
    
    ```python3
        def chartDF(symbol, timeframe='1m'):
    ```

- [company](https://iextrading.com/developer/docs/#company)
    
    ```python3
        def company(symbol):
    ```

    ```python3
        def companyDF(symbol):
    ```

- [delayedQuote](https://iextrading.com/developer/docs/#delayed-quote)

    ```python3
        def delayedQuote(symbol):
    ```

    ```python3
        def delayedQuoteDF(symbol):
    ```

- [dividends](https://iextrading.com/developer/docs/#dividends)

    ```python3
        def dividends(symbol, timeframe='ytd'):
    ```

    ```python3
        def dividendsDF(symbol, timeframe='ytd'):
    ```

- [earnings](https://iextrading.com/developer/docs/#earnings)

    ```python3
        def earnings(symbol):
    ```

    ```python3
        def earningsDF(symbol):
    ```

- [spread](https://iextrading.com/developer/docs/#effective-spread)

    ```python3
        def spread(symbol):
    ```

    ```python3
        def spreadDF(symbol):
    ```

- [financials](https://iextrading.com/developer/docs/#financials)

    ```python3
        def financials(symbol):
    ```

    ```python3
        def financialsDF(symbol):
    ```

- [threshold](https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list)

    ```python3
        def threshold(date=None):
    ```

    ```python3
        def thresholdDF(date=None):
    ```

- [shortInterest](https://iextrading.com/developer/docs/#iex-short-interest-list)

    ```python3
        def shortInterest(symbol, date=None):
    ```

    ```python3
        def shortInterestDF(symbol, date=None):
    ```

- [marketShortInterest](https://iextrading.com/developer/docs/#iex-short-interest-list)

    ```python3
        def marketShortInterest(date=None):
    ```

    ```python3
        def marketShortInterestDF(date=None):
    ```

- [stockStats](https://iextrading.com/developer/docs/#key-stats)

    ```python3
        def stockStats(symbol):
    ```

    ```python3
        def stockStatsDF(symbol):
    ```

- [list](https://iextrading.com/developer/docs/#list)

    ```python3
        def list(option='mostactive'):
    ```

    ```python3
        def listDF(option='mostactive'):
    ```

- [logo](https://iextrading.com/developer/docs/#logo)

    ```python3
        def logo(symbol):
    ```

    ```python3
        def logoPNG(symbol):
    ```

    ```python3
        def logoNotebook(symbol):
    ```

- [news](https://iextrading.com/developer/docs/#news)

    ```python3
        def news(symbol, count=10):
    ```

    ```python3
        def newsDF(symbol, count=10):
    ```

- [marketNews](https://iextrading.com/developer/docs/#news)

    ```python3
        def marketNews(count=10):
    ```

    ```python3
        def marketNewsDF(count=10):
    ```

- [ohlc](https://iextrading.com/developer/docs/#ohlc)
    
    ```python3
        def ohlc(symbol):
    ```

    ```python3
        def ohlcDF(symbol):
    ```

- [marketOhlc](https://iextrading.com/developer/docs/#ohlc)

    ```python3
        def marketOhlc():
    ```

    ```python3
        def marketOhlcDF():
    ```

- [peers](https://iextrading.com/developer/docs/#peers)

    ```python3
        def peers(symbol):
    ```

    ```python3
        def peersDF(symbol):
    ```

- [yesterday](https://iextrading.com/developer/docs/#previous)

    ```python3
        def yesterday(symbol):
    ```

    ```python3
        def yesterdayDF(symbol):
    ```

- [marketYesterday](https://iextrading.com/developer/docs/#previous)

    ```python3
        def marketYesterday():
    ```

    ```python3
        def marketYesterdayDF():
    ```

- [price](https://iextrading.com/developer/docs/#price)
    ```python3
        def price(symbol):
    ```

    ```python3
        def priceDF(symbol):
    ```

- [quote](https://iextrading.com/developer/docs/#quote)

    ```python3
        def quote(symbol):
    ```

    ```python3
        def quoteDF(symbol):
    ```

- [relevant](https://iextrading.com/developer/docs/#relevant)

    ```python3
        def relevant(symbol):
    ```

    ```python3
        def relevantDF(symbol):
    ```

- [splits](https://iextrading.com/developer/docs/#splits)

    ```python3
        def splits(symbol, timeframe='ytd'):
    ```

    ```python3
        def splitsDF(symbol, timeframe='ytd'):
    ```

- [volumeByVenue](https://iextrading.com/developer/docs/#volume-by-venue)

    ```python3
        def volumeByVenue(symbol):
    ```

    ```python3
        def volumeByVenueDF(symbol):
    ```

#### Reference

- [symbols](https://iextrading.com/developer/docs/#symbols)

    ```python3
        def symbols():
    ```

    ```python3
        def symbolsDF():
    ```

- [corporateActions](https://iextrading.com/developer/docs/#iex-corporate-actions)
    ```python3
        def corporateActions(date=None):
    ```


    ```python3
        def corporateActionsDF(date=None):
    ```

- [dividends](https://iextrading.com/developer/docs/#iex-dividends)
    ```python3
        def dividends(date=None):
    ```

    ```python3
        def dividendsDF(date=None):
    ```

- [nextDayExtDate](https://iextrading.com/developer/docs/#iex-next-day-ex-date)
    ```python3
        def nextDayExtDate(date=None):
    ```

    ```python3
        def nextDayExtDateDF(date=None):
    ```

- [directory](https://iextrading.com/developer/docs/#iex-listed-symbol-directory)
    ```python3
        def directory(date=None):
    ```

    ```python3
        def directoryDF(date=None):
    ```


#### Market Data

#### Stats

- [stats](https://iextrading.com/developer/docs/#intraday)
    ```python3
        def stats():
    ```

    ```python3
        def statsDF():
    ```

- [recent](https://iextrading.com/developer/docs/#recent)
    ```python3
        def recent():
    ```

    ```python3
        def recentDF():
    ```

- [records](https://iextrading.com/developer/docs/#records)
    ```python3
        def records():
    ```

    ```python3
        def recordsDF():
    ```

- [summary](https://iextrading.com/developer/docs/#historical-summary)
    ```python3
        def summary(date=None):
    ```

    ```python3
        def summaryDF(date=None):
    ```

- [daily](https://iextrading.com/developer/docs/#historical-daily)
    ```python3
        def daily(date=None, last=''):
    ```

    ```python3
        def dailyDF(date=None, last=''):
    ```

#### Markets


