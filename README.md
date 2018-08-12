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
[Read The Docs!](https://pyEX.readthedocs.io)
[Demo Notebook](https://github.com/timkpaine/pyEX/blob/master/all.ipynb)


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
- [tops](https://iextrading.com/developer/docs/#tops)
    
    ```python3
        def tops(symbols=None):
    ```
    
    ```python3
        def topsDF(symbols=None):
    ```
    
    ```python3
        def topsWS(symbols=None, on_data=None):
    ```

- [last](https://iextrading.com/developer/docs/#last)
    
    ```python3
        def last(symbols=None):
    ```
    
    ```python3
        def lastDF(symbols=None):
    ```
    
    ```python3
        def lastWS(symbols=None, on_data=None):
    ```

- [hist](https://iextrading.com/developer/docs/#hist)
    
    ```python3
        def hist(date=None):
    ```
    
    ```python3
        def histDF(date=None):
    ```

- [deep](https://iextrading.com/developer/docs/#deep)
    
    ```python3
        def deep(symbol=None):
    ```
    
    ```python3
        def deepDF(symbol=None):
    ```
    
    ```python3
        def deepWS(symbols=None, channels=None, on_data=None):
    ```

- [book](https://iextrading.com/developer/docs/#book55)
    
    ```python3
        def book(symbol=None):
    ```
    
    ```python3
        def bookDF(symbol=None):
    ```
    
    ```python3
        def bookWS(symbols=None, on_data=None):
    ```

- [trades](https://iextrading.com/developer/docs/#trades)
    
    ```python3
        def trades(symbol=None):
    ```
    
    ```python3
        def tradesDF(symbol=None):
    ```
    
    ```python3
        def tradesWS(symbols=None, on_data=None):
    ```

- [systemEvent](https://iextrading.com/developer/docs/#system-event)
    
    ```python3
        def systemEvent():
    ```
    
    ```python3
        def systemEventDF():
    ```
    
    ```python3
        def systemEventWS(on_data=None):
    ```

- [tradingStatus](https://iextrading.com/developer/docs/#trading-status)
    
    ```python3
        def tradingStatus(symbol=None):
    ```
    
    ```python3
        def tradingStatusDF(symbol=None):
    ```
    
    ```python3
        def tradingStatusWS(symbols=None, on_data=None):
    ```

- [opHaltStatus](https://iextrading.com/developer/docs/#operational-halt-status)
    
    ```python3
        def opHaltStatus(symbol=None):
    ```
    
    ```python3
        def opHaltStatusDF(symbol=None):
    ```
    
    ```python3
        def opHaltStatusWS(symbols=None, on_data=None):
    ```

- [ssr](https://iextrading.com/developer/docs/#short-sale-price-test-status)
    
    ```python3
        def ssrStatus(symbol=None):
    ```
    
    ```python3
        def ssrStatusDF(symbol=None):
    ```

    ```python3
        def ssrStatusWS(symbols=None, on_data=None):
    ```

- [securityEvent](https://iextrading.com/developer/docs/#security-event)

    ```python3
        def securityEvent(symbol=None):
    ```

    ```python3
        def securityEventDF(symbol=None):
    ```

    ```python3
        def securityEventWS(symbols=None, on_data=None):
    ```

- [tradeBreak](https://iextrading.com/developer/docs/#trade-break)

    ```python3
        def tradeBreak(symbol=None):
    ```

    ```python3
        def tradeBreakDF(symbol=None):
    ```

    ```python3
        def tradeBreakWS(symbols=None, on_data=None):
    ```

- [auction](https://iextrading.com/developer/docs/#auction)

    ```python3
        def auction(symbol=None):
    ```
    
    ```python3
        def auctionDF(symbol=None):
    ```
    
    ```python3
        def auctionWS(symbols=None, on_data=None):
    ```

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

- [markets](https://iextrading.com/developer/docs/#intraday)

    ```python3
        def markets():
    ```

    ```python3
        def marketsDF():
    ```

