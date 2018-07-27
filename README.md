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
![](https://raw.githubusercontent.com/timkpaine/jupyterlab_templates/master/docs/img/example1.gif)


### Methods

#### Stocks

- [book](https://iextrading.com/developer/docs/#book)

    ```python3
        def book(symbol):
    ```

- [bookDF](https://iextrading.com/developer/docs/#book)
    
    ```python3
        def bookDF(symbol):
    ```

- [chart](https://iextrading.com/developer/docs/#chart)

    ```python3
        def chart(symbol, timeframe='1m', date=None):
    ```


- [chartDF](https://iextrading.com/developer/docs/#chart)
    
    ```python3
        def chartDF(symbol, timeframe='1m'):
    ```

- [company](https://iextrading.com/developer/docs/#company)
    
    ```python3
        def company(symbol):
    ```

- [companyDF](https://iextrading.com/developer/docs/#company)
    
    ```python3
        def companyDF(symbol):
    ```

- [delayedQuote](https://iextrading.com/developer/docs/#delayed-quote)

    ```python3
        def delayedQuote(symbol):
    ```

- [delayedQuoteDF](https://iextrading.com/developer/docs/#delayed-quote)
    
    ```python3
        def delayedQuoteDF(symbol):
    ```

- [dividends](https://iextrading.com/developer/docs/#dividends)

    ```python3
        def dividends(symbol, timeframe='ytd'):
    ```


- [dividendsDF](https://iextrading.com/developer/docs/#dividends)

    ```python3
        def dividendsDF(symbol, timeframe='ytd'):
    ```

- [earnings](https://iextrading.com/developer/docs/#earnings)

    ```python3
        def earnings(symbol):
    ```

- [earningsDF](https://iextrading.com/developer/docs/#earnings)
    
    ```python3
        def earningsDF(symbol):
    ```

- [spread](https://iextrading.com/developer/docs/#effective-spread)

    ```python3
        def spread(symbol):
    ```

- [spreadDF](https://iextrading.com/developer/docs/#effective-spread)

    ```python3
        def spreadDF(symbol):
    ```

- [financials](https://iextrading.com/developer/docs/#financials)

    ```python3
        def financials(symbol):
    ```

- [financialsDF](https://iextrading.com/developer/docs/#financials)

    ```python3
        def financialsDF(symbol):
    ```

- [threshold](https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list)

    ```python3
        def threshold(date=None):
    ```

- [thresholdDF](https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list)

    ```python3
        def thresholdDF(date=None):
    ```

- [shortInterest](https://iextrading.com/developer/docs/#iex-short-interest-list)

    ```python3
        def shortInterest(symbol, date=None):
    ```

- [shortInterestDF](https://iextrading.com/developer/docs/#iex-short-interest-list)

    ```python3
        def shortInterestDF(symbol, date=None):
    ```

- [marketShortInterest](https://iextrading.com/developer/docs/#iex-short-interest-list)

    ```python3
        def marketShortInterest(date=None):
    ```

- [marketShortInterestDF](https://iextrading.com/developer/docs/#iex-short-interest-list)

    ```python3
        def marketShortInterestDF(date=None):
    ```

- [stockStats](https://iextrading.com/developer/docs/#key-stats)

    ```python3
        def stockStats(symbol):
    ```

- [stockStatsDF](https://iextrading.com/developer/docs/#key-stats)
    ```python3
        def stockStatsDF(symbol):
    ```

- [list](https://iextrading.com/developer/docs/#list)

    ```python3
        def list(option='mostactive'):
    ```

- [listDF](https://iextrading.com/developer/docs/#list)

    ```python3
        def listDF(option='mostactive'):
    ```

- [logo](https://iextrading.com/developer/docs/#logo)

    ```python3
        def logo(symbol):
    ```

- [logoPNG](https://iextrading.com/developer/docs/#logo)

    ```python3
        def logoPNG(symbol):
    ```

- [logoNotebook](https://iextrading.com/developer/docs/#logo)

    ```python3
        def logoNotebook(symbol):
    ```

- [news](https://iextrading.com/developer/docs/#news)

    ```python3
        def news(symbol, count=10):
    ```

- [newsDF](https://iextrading.com/developer/docs/#news)

    ```python3
        def newsDF(symbol, count=10):
    ```

- [marketNews](https://iextrading.com/developer/docs/#news)

    ```python3
        def marketNews(count=10):
    ```

- [marketNewsDF](https://iextrading.com/developer/docs/#news)

    ```python3
        def marketNewsDF(count=10):
    ```

- [ohlc](https://iextrading.com/developer/docs/#ohlc)
    
    ```python3
        def ohlc(symbol):
    ```

- [ohlcDF](https://iextrading.com/developer/docs/#ohlc)

    ```python3
        def ohlcDF(symbol):
    ```

- [marketOhlc](https://iextrading.com/developer/docs/#ohlc)

    ```python3
        def marketOhlc():
    ```

- [marketOhlcDF](https://iextrading.com/developer/docs/#ohlc)

    ```python3
        def marketOhlcDF():
    ```

- [peers](https://iextrading.com/developer/docs/#peers)

    ```python3
        def peers(symbol):
    ```

- [peersDF](https://iextrading.com/developer/docs/#peers)

    ```python3
        def peersDF(symbol):
    ```

- [yesterday](https://iextrading.com/developer/docs/#previous)

    ```python3
        def yesterday(symbol):
    ```

- [yesterdayDF](https://iextrading.com/developer/docs/#previous)

    ```python3
        def yesterdayDF(symbol):
    ```

- [marketYesterday](https://iextrading.com/developer/docs/#previous)

    ```python3
        def marketYesterday():
    ```

- [marketYesterdayDF](https://iextrading.com/developer/docs/#previous)

    ```python3
        def marketYesterdayDF():
    ```

- [price](https://iextrading.com/developer/docs/#price)
    ```python3
        def price(symbol):
    ```

- [priceDF](https://iextrading.com/developer/docs/#price)

    ```python3
        def priceDF(symbol):
    ```

- [quote](https://iextrading.com/developer/docs/#quote)

    ```python3
        def quote(symbol):
    ```

- [quoteDF](https://iextrading.com/developer/docs/#quote)

    ```python3
        def quoteDF(symbol):
    ```

- [relevant](https://iextrading.com/developer/docs/#relevant)

    ```python3
        def relevant(symbol):
    ```

- [relevantDF](https://iextrading.com/developer/docs/#relevant)

    ```python3
        def relevantDF(symbol):
    ```

- [splits](https://iextrading.com/developer/docs/#splits)

    ```python3
        def splits(symbol, timeframe='ytd'):
    ```

- [splitsDF](https://iextrading.com/developer/docs/#splits)

    ```python3
        def splitsDF(symbol, timeframe='ytd'):
    ```

- [volumeByVenue](https://iextrading.com/developer/docs/#volume-by-venue)

    ```python3
        def volumeByVenue(symbol):
    ```

- [volumeByVenueDF](https://iextrading.com/developer/docs/#volume-by-venue)

    ```python3
        def volumeByVenueDF(symbol):
    ```
