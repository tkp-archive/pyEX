# pyEX
Python interface to IEX Cloud (https://iexcloud.io/docs/api/)

[![Build Status](https://dev.azure.com/tpaine154/pyEX/_apis/build/status/timkpaine.pyEX?branchName=main)](https://dev.azure.com/tpaine154/pyEX/_build/latest?definitionId=3&branchName=main)
[![Coverage](https://img.shields.io/azure-devops/coverage/tpaine154/pyEX/3/main)](https://img.shields.io/azure-devops/coverage/tpaine154/pyEX/3)
[![License](https://img.shields.io/github/license/timkpaine/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![PyPI](https://img.shields.io/pypi/v/pyEX.svg)](https://pypi.python.org/pypi/pyEX/)
[![Docs](https://readthedocs.org/projects/pyex/badge/?version=latest)](https://pyex.readthedocs.io/en/latest/?badge=latest)

## Referral
Please subscribe to IEX Cloud using [my referral code](https://iexcloud.io/s/6332a3c3 ).

# Getting Started
## Install
Install from pip

`pip install pyEX`

of from source

`python setup.py install`

### Extensions
- `pyEX[async]`: `asyncio` integration for streaming APIs
- `pyEX[studies]`: Technical indicators and other calculations

## Demos + Docs
- [Demo Notebook - IEX Cloud](https://github.com/timkpaine/pyEX/blob/main/examples/all.ipynb)
- [Streaming Notebook - IEX Cloud](https://github.com/timkpaine/pyEX/blob/main/examples/sse.ipynb)
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
- [pyEX-studies](https://github.com/timkpaine/pyEX/tree/main/pyEX/studies): pyEX integration with TA-Lib and other libraries, for technical analysis and other metrics on top of the IEX data
- [pyEX-caching](https://github.com/timkpaine/pyEX-caching): persistent, queryable caching for pyEX function calls. Minimize your spend and maximize your performance
- [pyEX-zipline](https://github.com/timkpaine/pyEX-zipline): [Zipline](https://github.com/quantopian/zipline) integration for IEX data

## Demo
![](https://raw.githubusercontent.com/timkpaine/pyEX/main/docs/img/example1.gif)

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


###  Full API
Please see the [readthedocs](https://pyEX.readthedocs.io) for a full API spec

![](https://raw.githubusercontent.com/timkpaine/pyEX/main/docs/img/rtd.png)

Currently, the following methods are implemented:

### Data Points
- [points](https://iexcloud.io/docs/api/#data-points)
- [pointsDF](https://iexcloud.io/docs/api/#data-points)

### Markets
- markets
- marketsDF

### Account
- [messageBudget](https://iexcloud.io/docs/api/#message-budget)
- [metadata](https://iexcloud.io/docs/api/#metadata)
- [metadataDF](https://iexcloud.io/docs/api/#metadata)
- [payAsYouGo](https://iexcloud.io/docs/api/#pay-as-you-go)
- [usage](https://iexcloud.io/docs/api/#usage)
- [usageDF](https://iexcloud.io/docs/api/#usage)



### Stocks
#### Stock Prices
- [book](https://iexcloud.io/docs/api/#book)
- [bookDF](https://iexcloud.io/docs/api/#book)
- [chart](https://iexcloud.io/docs/api/#charts)
- [chartDF](https://iexcloud.io/docs/api/#charts)
- [delayedQuote](https://iexcloud.io/docs/api/#delayed-quote)
- [delayedQuoteDF](https://iexcloud.io/docs/api/#delayed-quote)
- [intraday](https://iexcloud.io/docs/api/#intraday-prices)
- [intradayDF](https://iexcloud.io/docs/api/#intraday-prices)
- [largestTrades](https://iexcloud.io/docs/api/#largest-trades)
- [largestTradesDF](https://iexcloud.io/docs/api/#largest-trades)
- [ohlc](https://iexcloud.io/docs/api/#open-close-price)
- [ohlcDF](https://iexcloud.io/docs/api/#open-close-price)
- [marketOhlc](https://iexcloud.io/docs/api/#open-close-price)
- [marketOhlcDF](https://iexcloud.io/docs/api/#open-close-price)
- [yesterday (previous day price)](https://iexcloud.io/docs/api/#previous-day-price)
- [yesterdayDF (previous day price)](https://iexcloud.io/docs/api/#previous-day-price)
- [marketYesterday](https://iexcloud.io/docs/api/#previous-day-price)
- [marketYesterdayDF](https://iexcloud.io/docs/api/#previous-day-price)
- [price](https://iexcloud.io/docs/api/#price-only)
- [priceDF](https://iexcloud.io/docs/api/#price-only)
- [quote](https://iexcloud.io/docs/api/#quote)
- [quoteDF](https://iexcloud.io/docs/api/#quote)
- [volumeByVenue](https://iexcloud.io/docs/api/#volume-by-venue)
- [volumeByVenueDF](https://iexcloud.io/docs/api/#volume-by-venue)

#### Stock Profiles
- [company](https://iexcloud.io/docs/api/#company)
- [companyDF](https://iexcloud.io/docs/api/#company)
- [insiderRoster](https://iexcloud.io/docs/api/#insider-roster)
- [insiderRosterDF](https://iexcloud.io/docs/api/#insider-roster)
- [insiderSummary](https://iexcloud.io/docs/api/#insider-summary)
- [insiderSummaryDF](https://iexcloud.io/docs/api/#insider-summary)
- [insiderTransactions](https://iexcloud.io/docs/api/#insider-transactions)
- [insiderTransactionsDF](https://iexcloud.io/docs/api/#insider-transactions)
- [logo](https://iexcloud.io/docs/api/#logo)
- [logoPNG](https://iexcloud.io/docs/api/#logo)
- [logoNotebook](https://iexcloud.io/docs/api/#logo)
- [peers](https://iexcloud.io/docs/api/#peer-groups)
- [peersDF](https://iexcloud.io/docs/api/#peer-groups)


#### Stock Fundamentals
- [balanceSheet](https://iexcloud.io/docs/api/#balance-sheet)
- [balanceSheetDF](https://iexcloud.io/docs/api/#balance-sheet)
- [cashFlow](https://iexcloud.io/docs/api/#cash-flow)
- [cashFlowDF](https://iexcloud.io/docs/api/#cash-flow)
- [dividendsBasic](https://iexcloud.io/docs/api/#dividends-basic)
- [dividendsBasicDF](https://iexcloud.io/docs/api/#dividends-basic)
- [earnings](https://iexcloud.io/docs/api/#earnings)
- [earningsDF](https://iexcloud.io/docs/api/#earnings)
- [financials](https://iexcloud.io/docs/api/#financials)
- [financialsDF](https://iexcloud.io/docs/api/#financials)
- [incomeStatement](https://iexcloud.io/docs/api/#income-statement)
- [incomeStatementDF](https://iexcloud.io/docs/api/#income-statement)
- [tenQ](https://iexcloud.io/docs/api/#financials-as-reported)
- [tenK](https://iexcloud.io/docs/api/#financials-as-reported)
- [stockSplits](https://iexcloud.io/docs/api/#splits-basic)
- [stockSplitsDF](https://iexcloud.io/docs/api/#splits-basic)


#### Stock Research
- [advancedStats](https://iexcloud.io/docs/api/#advanced-stats)
- [advancedStatsDF](https://iexcloud.io/docs/api/#advanced-stats)
- [analystRecommendations](https://iexcloud.io/docs/api/#analyst-recommendations)
- [analystRecommendationsDF](https://iexcloud.io/docs/api/#analyst-recommendations)
- [estimates](https://iexcloud.io/docs/api/#estimates)
- [estimatesDF](https://iexcloud.io/docs/api/#estimates)
- [fundOwnership](https://iexcloud.io/docs/api/#fund-ownership)
- [fundOwnershipDF](https://iexcloud.io/docs/api/#fund-ownership)
- [institutionalOwnership](https://iexcloud.io/docs/api/#institutional-ownership)
- [institutionalOwnershipDF](https://iexcloud.io/docs/api/#institutional-ownership)
- [keyStats](https://iexcloud.io/docs/api/#key-stats)
- [keyStatsDF](https://iexcloud.io/docs/api/#key-stats)
- [priceTarget](https://iexcloud.io/docs/api/#price-target)
- [priceTargetDF](https://iexcloud.io/docs/api/#price-target)
- [technicals](https://iexcloud.io/docs/api/#technical-indicators)
- [technicalsDF](https://iexcloud.io/docs/api/#technical-indicators)


#### Corporate Actions
- [bonusIssue](https://iexcloud.io/docs/api/#bonus-issue)
- [bonusIssueDF](https://iexcloud.io/docs/api/#bonus-issue)
- [distribution](https://iexcloud.io/docs/api/#distribution)
- [distributionDF](https://iexcloud.io/docs/api/#distribution)
- [dividends](https://iexcloud.io/docs/api/#dividends)
- [dividendsDF](https://iexcloud.io/docs/api/#dividends)
- [returnOfCapital](https://iexcloud.io/docs/api/#return-of-capital)
- [returnOfCapitalDF](https://iexcloud.io/docs/api/#return-of-capital)
- [rightsIssue](https://iexcloud.io/docs/api/#rights-issue)
- [rightsIssueDF](https://iexcloud.io/docs/api/#rights-issue)
- [rightToPurchase](https://iexcloud.io/docs/api/#right-to-purchase)
- [rightToPurchaseDF](https://iexcloud.io/docs/api/#right-to-purchase)
- [securityReclassification](https://iexcloud.io/docs/api/#security-reclassification)
- [securityReclassificationDF](https://iexcloud.io/docs/api/#security-reclassification)
- [securitySwap](https://iexcloud.io/docs/api/#security-swap)
- [securitySwapDF](https://iexcloud.io/docs/api/#security-swap)
- [spinoff](https://iexcloud.io/docs/api/#spinoff)
- [spinoffDF](https://iexcloud.io/docs/api/#spinoff)
- [splits](https://iexcloud.io/docs/api/#splits)
- [splitsDF](https://iexcloud.io/docs/api/#splits)


#### Market Info
- [collections](https://iexcloud.io/docs/api/#collections)
- [collectionsDF](https://iexcloud.io/docs/api/#collections)
- [earningsToday](https://iexcloud.io/docs/api/#earnings-today)
- [earningsTodayDF](https://iexcloud.io/docs/api/#earnings-today)
- [ipoToday](https://iexcloud.io/docs/api/#ipo-calendar)
- [ipoTodayDF](https://iexcloud.io/docs/api/#ipo-calendar)
- [ipoUpcoming](https://iexcloud.io/docs/api/#ipo-calendar)
- [ipoUpcomingDF](https://iexcloud.io/docs/api/#ipo-calendar)
- [list](https://iexcloud.io/docs/api/#list)
- [listDF](https://iexcloud.io/docs/api/#list)
- [marketVolume](https://iexcloud.io/docs/api/#market-volume-u-s)
- [marketVolumeDF](https://iexcloud.io/docs/api/#market-volume-u-s)
- [sectorPerformance](https://iexcloud.io/docs/api/#sector-performance)
- [sectorPerformanceDF](https://iexcloud.io/docs/api/#sector-performance)
- [upcomingEvents](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingEventsDF](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingEarnings](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingEarningsDF](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingDividends](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingDividendsDF](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingSplits](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingSplitsDF](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingIPOs](https://iexcloud.io/docs/api/#upcoming-events)
- [upcomingIPOsDF](https://iexcloud.io/docs/api/#upcoming-events)


#### News
- [news](https://iexcloud.io/docs/api/#news)
- [newsDF](https://iexcloud.io/docs/api/#news)
- [marketNews](https://iexcloud.io/docs/api/#news)
- [marketNewsDF](https://iexcloud.io/docs/api/#news)

#### Time Series
- [timeSeriesInventory](https://iexcloud.io/docs/api/#time-series)
- [timeSeriesInventoryDF](https://iexcloud.io/docs/api/#time-series)
- [timeSeries](https://iexcloud.io/docs/api/#time-series)
- [timeSeriesDF](https://iexcloud.io/docs/api/#time-series)

#### Bulk
- batch
- batchDF
- bulkBatch
- bulkBatchDF
- bulkMinuteBars
- bulkMinuteBarsDF

#### Old/Unknown/Deprecated
- spread
- spreadDF
- shortInterest
- shortInterestDF
- marketShortInterest
- marketShortInterestDF
- relevant
- relevantDF

### Crypto
- [cryptoBook](https://iexcloud.io/docs/api/#cryptocurrency-book)
- [cryptoBookDF](https://iexcloud.io/docs/api/#cryptocurrency-book)
- [cryptoQuote](https://iexcloud.io/docs/api/#cryptocurrency-quote)
- [cryptoQuoteDF](https://iexcloud.io/docs/api/#cryptocurrency-quote)
- [cryptoPrice](https://iexcloud.io/docs/api/#cryptocurrency-price)
- [cryptoPriceDF](https://iexcloud.io/docs/api/#cryptocurrency-price)

### FX
- [latestFX](https://iexcloud.io/docs/api/#latest-currency-rates)
- [latestFXDF](https://iexcloud.io/docs/api/#latest-currency-rates)
- [convertFX](https://iexcloud.io/docs/api/#currency-conversion)
- [convertFXDF](https://iexcloud.io/docs/api/#currency-conversion)
- [historicalFX](https://iexcloud.io/docs/api/#historical-daily)
- [historicalFXDF](https://iexcloud.io/docs/api/#historical-daily)


### EOD Options
- [optionExpirations](https://iexcloud.io/docs/api/#end-of-day-options)
- [options](https://iexcloud.io/docs/api/#end-of-day-options)
- [optionsDF](https://iexcloud.io/docs/api/#end-of-day-options)

### CEO Compensation
- [ceoCompensation](https://iexcloud.io/docs/api/#ceo-compensation)
- [ceoCompensationDF](https://iexcloud.io/docs/api/#ceo-compensation)

### Treasuries

#### Daily Treasury Rates
- [thirtyYear](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [twentyYear](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [tenYear](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [fiveYear](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [twoYear](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [oneYear](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [sixMonth](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [threeMonth](https://iexcloud.io/docs/api/#daily-treasury-rates)
- [oneMonth](https://iexcloud.io/docs/api/#daily-treasury-rates)

### Commodities
- [wti](https://iexcloud.io/docs/api/#oil-prices)
- [brent](https://iexcloud.io/docs/api/#oil-prices)
- [natgas](https://iexcloud.io/docs/api/#natural-gas-price)
- [heatoil](https://iexcloud.io/docs/api/#heating-oil-prices)
- [jet](https://iexcloud.io/docs/api/#jet-fuel-prices)
- [diesel](https://iexcloud.io/docs/api/#diesel-price)
- [gasreg](https://iexcloud.io/docs/api/#gas-prices)
- [gasmid](https://iexcloud.io/docs/api/#gas-prices)
- [gasprm](https://iexcloud.io/docs/api/#gas-prices)
- [propane](https://iexcloud.io/docs/api/#propane-prices)

### Economic Data
- [cdnj](https://iexcloud.io/docs/api/#cd-rates)
- [cdj](https://iexcloud.io/docs/api/#cd-rates)
- [cpi](https://iexcloud.io/docs/api/#consumer-price-index)
- [creditcard](https://iexcloud.io/docs/api/#credit-card-interest-rate)
- [fedfunds](https://iexcloud.io/docs/api/#federal-fund-rates)
- [gdp](https://iexcloud.io/docs/api/#real-gdp)
- [institutionalMoney](https://iexcloud.io/docs/api/#institutional-money-funds)
- [initialClaims](https://iexcloud.io/docs/api/#initial-claims)
- [indpro](https://iexcloud.io/docs/api/#industrial-production-index)
- [us30](https://iexcloud.io/docs/api/#mortgage-rates)
- [us15](https://iexcloud.io/docs/api/#mortgage-rates)
- [us5](https://iexcloud.io/docs/api/#mortgage-rates)
- [housing](https://iexcloud.io/docs/api/#total-housing-starts)
- [payroll](https://iexcloud.io/docs/api/#total-payrolls)
- [vehicles](https://iexcloud.io/docs/api/#total-vehicle-sales)
- [retailMoney](https://iexcloud.io/docs/api/#retail-money-funds)
- [unemployment](https://iexcloud.io/docs/api/#unemployment-rate)
- [recessionProb](https://iexcloud.io/docs/api/#us-recession-probabilities)

### Reference Data
- [cryptoSymbols](https://iexcloud.io/docs/api/#cryptocurrency-symbols)
- [cryptoSymbolsDF](https://iexcloud.io/docs/api/#cryptocurrency-symbols)
- [cryptoSymbolsList](https://iexcloud.io/docs/api/#cryptocurrency-symbols)
- [fxSymbols](https://iexcloud.io/docs/api/#fx-symbols)
- [fxSymbolsDF](https://iexcloud.io/docs/api/#fx-symbols)
- [fxSymbolsList](https://iexcloud.io/docs/api/#fx-symbols)
- [iexSymbols](https://iexcloud.io/docs/api/#iex-symbols)
- [iexSymbolsDF](https://iexcloud.io/docs/api/#iex-symbols)
- [iexSymbolsList](https://iexcloud.io/docs/api/#iex-symbols)
- [internationalSymbols](https://iexcloud.io/docs/api/#international-symbols)
- [internationalSymbolsDF](https://iexcloud.io/docs/api/#international-symbols)
- [internationalSymbolsList](https://iexcloud.io/docs/api/#international-symbols)
- [internationalExchanges](https://iexcloud.io/docs/api/#international-exchanges)
- [internationalExchangesDF](https://iexcloud.io/docs/api/#international-exchanges)
- [figi](https://iexcloud.io/docs/api/#figi-mapping)
- [figiDF](https://iexcloud.io/docs/api/#figi-mapping)
- [mutualFundSymbols](https://iexcloud.io/docs/api/#mutual-fund-symbols)
- [mutualFundSymbolsDF](https://iexcloud.io/docs/api/#mutual-fund-symbols)
- [mutualFundSymbolsList](https://iexcloud.io/docs/api/#mutual-fund-symbols)
- [optionsSymbols](https://iexcloud.io/docs/api/#options-symbols)
- [optionsSymbolsDF](https://iexcloud.io/docs/api/#options-symbols)
- [optionsSymbolsList](https://iexcloud.io/docs/api/#options-symbols)
- [otcSymbols](https://iexcloud.io/docs/api/#otc-symbols)
- [otcSymbolsDF](https://iexcloud.io/docs/api/#otc-symbols)
- [otcSymbolsList](https://iexcloud.io/docs/api/#otc-symbols)
- [sectors](https://iexcloud.io/docs/api/#sectors)
- [sectorsDF](https://iexcloud.io/docs/api/#sectors)
- [symbols](https://iexcloud.io/docs/api/#symbols)
- [symbolsDF](https://iexcloud.io/docs/api/#symbols)
- [symbolsList](https://iexcloud.io/docs/api/#symbols)
- [tags](https://iexcloud.io/docs/api/#tags)
- [tagsDF](https://iexcloud.io/docs/api/#tags)
- [exchanges](https://iexcloud.io/docs/api/#u-s-exchanges)
- [exchangesDF](https://iexcloud.io/docs/api/#u-s-exchanges)
- [holidays](https://iexcloud.io/docs/api/#u-s-holidays-and-trading-dates)
- [holidaysDF](https://iexcloud.io/docs/api/#u-s-holidays-and-trading-dates)

### Other Reference
- corporateActions
- corporateActionsDF
- refDividends
- refDividendsDF
- nextDayExtDate
- nextDayExtDateDF
- directory
- directoryDF
- [calendar](https://iexcloud.io/docs/api/#calendar)
- [calendarDF](https://iexcloud.io/docs/api/#calendar)

### IEX Data
#### TOPS
- [deep](https://iexcloud.io/docs/api/#deep)
- [deepAsync](https://iexcloud.io/docs/api/#deep)
- [deepDF](https://iexcloud.io/docs/api/#deep)
- [auction](https://iexcloud.io/docs/api/#deep-auction)
- [auctionAsync](https://iexcloud.io/docs/api/#deep-auction)
- [auctionDF](https://iexcloud.io/docs/api/#deep-auction)
- [bookDeep](https://iexcloud.io/docs/api/#deep-book)
- [bookDeepAsync](https://iexcloud.io/docs/api/#deep-book)
- [bookDeepDF](https://iexcloud.io/docs/api/#deep-book)
- [opHaltStatus](https://iexcloud.io/docs/api/#deep-operational-halt-status)
- [opHaltStatusAsync](https://iexcloud.io/docs/api/#deep-operational-halt-status)
- [opHaltStatusDF](https://iexcloud.io/docs/api/#deep-operational-halt-status)
- [officialPrice](https://iexcloud.io/docs/api/#deep-official-price)
- [officialPriceAsync](https://iexcloud.io/docs/api/#deep-official-price)
- [officialPriceDF](https://iexcloud.io/docs/api/#deep-official-price)
- [securityEvent](https://iexcloud.io/docs/api/#deep-security-event)
- [securityEventAsync](https://iexcloud.io/docs/api/#deep-security-event)
- [securityEventDF](https://iexcloud.io/docs/api/#deep-security-event)
- [ssrStatus](https://iexcloud.io/docs/api/#deep-short-sale-price-test-status)
- [ssrStatusAsync](https://iexcloud.io/docs/api/#deep-short-sale-price-test-status)
- [ssrStatusDF](https://iexcloud.io/docs/api/#deep-short-sale-price-test-status)
- [systemEvent](https://iexcloud.io/docs/api/#deep-system-event)
- [systemEventAsync](https://iexcloud.io/docs/api/#deep-system-event)
- [systemEventDF](https://iexcloud.io/docs/api/#deep-system-event)
- [trades](https://iexcloud.io/docs/api/#deep-trades)
- [tradesAsync](https://iexcloud.io/docs/api/#deep-trades)
- [tradesDF](https://iexcloud.io/docs/api/#deep-trades)
- [tradeBreak](https://iexcloud.io/docs/api/#deep-trade-break)
- [tradeBreakAsync](https://iexcloud.io/docs/api/#deep-trade-break)
- [tradeBreakDF](https://iexcloud.io/docs/api/#deep-trade-break)
- [tradingStatus](https://iexcloud.io/docs/api/#deep-trading-status)
- [tradingStatusAsync](https://iexcloud.io/docs/api/#deep-trading-status)
- [tradingStatusDF](https://iexcloud.io/docs/api/#deep-trading-status)
- [last](https://iexcloud.io/docs/api/#last)
- [lastAsync](https://iexcloud.io/docs/api/#last)
- [lastDF](https://iexcloud.io/docs/api/#last)
- [threshold](https://iexcloud.io/docs/api/#listed-regulation-sho-threshold-securities-list-in-dev)
- [thresholdDF](https://iexcloud.io/docs/api/#listed-regulation-sho-threshold-securities-list-in-dev)
- [tops](https://iexcloud.io/docs/api/#tops)
- [topsAsync](https://iexcloud.io/docs/api/#tops)
- [topsDF](https://iexcloud.io/docs/api/#tops)

#### Stats
- daily
- dailyDF
- summary
- summaryDF
- systemStats
- systemStatsDF
- recent
- recentDF
- records
- recordsDF

### Alternative
- crypto
- cryptoDF
- sentiment
- sentimentDF

## Streaming Data

### SSE Streaming
- [topsSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [topsSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [lastSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [lastSSEASync](https://iexcloud.io/docs/api/#sse-streaming)
- [deepSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [deepSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [tradesSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [tradesSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [auctionSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [auctionSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [bookSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [bookSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [opHaltStatusSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [opHaltStatusSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [officialPriceSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [officialPriceSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [securityEventSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [securityEventSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [ssrStatusSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [ssrStatusSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [systemEventSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [systemEventSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [tradeBreaksSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [tradeBreaksSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)
- [tradingStatusSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [tradingStatusSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)

### Stocks
- [stocksUSNoUTPSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUSNoUTPSSEsync](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUSSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUSSSEsync](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUS1SecondSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUS1SecondSSEsync](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUS5SecondSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUS5SecondSSEsync](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUS1MinuteSSE](https://iexcloud.io/docs/api/#sse-streaming)
- [stocksUS1MinuteSSEAsync](https://iexcloud.io/docs/api/#sse-streaming)

### News
- [newsSSE](https://iexcloud.io/docs/api/#streaming-news)
- [newsSSEAsync](https://iexcloud.io/docs/api/#streaming-news)

### Sentiment
- sentimentSSE
- sentimentSSEAsync

### FX
- fxSSE
- fxSSEAsync

### Crypto
- cryptoBookSSE
- cryptoBookSSEAsync
- cryptoEventsSSE
- cryptoEventsSSEAsync
- cryptoQuotesSSE
- cryptoQuotesSSEAsync

## Premium Data
### Wall Street Horizon
- [analystDays](https://iexcloud.io/docs/api/#analyst-days)
- [analystDaysDF](https://iexcloud.io/docs/api/#analyst-days)
- [boardOfDirectorsMeeting](https://iexcloud.io/docs/api/#board-of-directors-meeting)
- [boardOfDirectorsMeetingDF](https://iexcloud.io/docs/api/#board-of-directors-meeting)
- [businessUpdates](https://iexcloud.io/docs/api/#business-updates)
- [businessUpdatesDF](https://iexcloud.io/docs/api/#business-updates)
- [buybacks](https://iexcloud.io/docs/api/#buybacks)
- [buybacksDF](https://iexcloud.io/docs/api/#buybacks)
- [capitalMarketsDay](https://iexcloud.io/docs/api/#capital-markets-day)
- [capitalMarketsDayDF](https://iexcloud.io/docs/api/#capital-markets-day)
- [companyTravel](https://iexcloud.io/docs/api/#company-travel)
- [companyTravelDF](https://iexcloud.io/docs/api/#company-travel)
- [filingDueDates](https://iexcloud.io/docs/api/#filing-due-dates)
- [filingDueDatesDF](https://iexcloud.io/docs/api/#filing-due-dates)
- [fiscalQuarterEnd](https://iexcloud.io/docs/api/#fiscal-quarter-end)
- [fiscalQuarterEndDF](https://iexcloud.io/docs/api/#fiscal-quarter-end)
- [forum](https://iexcloud.io/docs/api/#forum)
- [forumDF](https://iexcloud.io/docs/api/#forum)
- [generalConference](https://iexcloud.io/docs/api/#general-conference)
- [generalConferenceDF](https://iexcloud.io/docs/api/#general-conference)
- [fdaAdvisoryCommitteeMeetings](https://iexcloud.io/docs/api/#fda-advisory-committee-meetings)
- [fdaAdvisoryCommitteeMeetingsDF](https://iexcloud.io/docs/api/#fda-advisory-committee-meetings)
- [holidaysWSH](https://iexcloud.io/docs/api/#holidays)
- [holidaysWSHDF](https://iexcloud.io/docs/api/#holidays)
- [indexChanges](https://iexcloud.io/docs/api/#index-changes)
- [indexChangesDF](https://iexcloud.io/docs/api/#index-changes)
- [iposWSH](https://iexcloud.io/docs/api/#ipos)
- [iposWSHDF](https://iexcloud.io/docs/api/#ipos)
- [legalActions](https://iexcloud.io/docs/api/#legal-actions)
- [legalActionsDF](https://iexcloud.io/docs/api/#legal-actions)
- [mergersAndAcquisitions](https://iexcloud.io/docs/api/#mergers-acquisitions)
- [mergersAndAcquisitionsDF](https://iexcloud.io/docs/api/#mergers-acquisitions)
- [productEventsDF](https://iexcloud.io/docs/api/#product-events)
- [productEvents](https://iexcloud.io/docs/api/#product-events)
- [researchAndDevelopmentDays](https://iexcloud.io/docs/api/#research-and-development-days)
- [researchAndDevelopmentDaysDF](https://iexcloud.io/docs/api/#research-and-development-days)
- [sameStoreSales](https://iexcloud.io/docs/api/#same-store-sales)
- [sameStoreSalesDF](https://iexcloud.io/docs/api/#same-store-sales)
- [secondaryOfferings](https://iexcloud.io/docs/api/#secondary-offerings)
- [secondaryOfferingsDF](https://iexcloud.io/docs/api/#secondary-offerings)
- [seminars](https://iexcloud.io/docs/api/#seminars)
- [seminarsDF](https://iexcloud.io/docs/api/#seminars)
- [shareholderMeetings](https://iexcloud.io/docs/api/#shareholder-meetings)
- [shareholderMeetingsDF](https://iexcloud.io/docs/api/#shareholder-meetings)
- [summitMeetings](https://iexcloud.io/docs/api/#summit-meetings)
- [summitMeetingsDF](https://iexcloud.io/docs/api/#summit-meetings)
- [tradeShows](https://iexcloud.io/docs/api/#trade-shows)
- [tradeShowsDF](https://iexcloud.io/docs/api/#trade-shows)
- [witchingHours](https://iexcloud.io/docs/api/#witching-hours)
- [witchingHoursDF](https://iexcloud.io/docs/api/#witching-hours)
- [workshops](https://iexcloud.io/docs/api/#workshops)
- [workshopsDF](https://iexcloud.io/docs/api/#workshops)

### Fraud Factors
- [similarityIndex](https://iexcloud.io/docs/api/#similiarity-index)
- [similarityIndexDF](https://iexcloud.io/docs/api/#similiarity-index)
- [nonTimelyFilings](https://iexcloud.io/docs/api/#non-timely-filings)
- [nonTimelyFilingsDF](https://iexcloud.io/docs/api/#non-timely-filings)

### Extract Alpha
- [cam1](https://iexcloud.io/docs/api/#cross-asset-model-1)
- [cam1DF](https://iexcloud.io/docs/api/#cross-asset-model-1)
- [esgCFPBComplaints](https://iexcloud.io/docs/api/#esg-cfpb-complaints)
- [esgCFPBComplaintsDF](https://iexcloud.io/docs/api/#esg-cfpb-complaints)
- [esgCPSCRecalls](https://iexcloud.io/docs/api/#esg-cpsc-recalls)
- [esgCPSCRecallsDF](https://iexcloud.io/docs/api/#esg-cpsc-recalls)
- [esgDOLVisaApplications](https://iexcloud.io/docs/api/#esg-dol-visa-applications)
- [esgDOLVisaApplicationsDF](https://iexcloud.io/docs/api/#esg-dol-visa-applications)
- [esgEPAEnforcements](https://iexcloud.io/docs/api/#esg-epa-enforcements)
- [esgEPAEnforcementsDF](https://iexcloud.io/docs/api/#esg-epa-enforcements)
- [esgEPAMilestones](https://iexcloud.io/docs/api/#esg-epa-milestones)
- [esgEPAMilestonesDF](https://iexcloud.io/docs/api/#esg-epa-milestones)
- [esgFECIndividualCampaingContributions](https://iexcloud.io/docs/api/#esg-fec-individual-campaign-contributions)
- [esgFECIndividualCampaingContributionsDF](https://iexcloud.io/docs/api/#esg-fec-individual-campaign-contributions)
- [esgOSHAInspections](https://iexcloud.io/docs/api/#esg-osha-inspections)
- [esgOSHAInspectionsDF](https://iexcloud.io/docs/api/#esg-osha-inspections)
- [esgSenateLobbying](https://iexcloud.io/docs/api/#esg-senate-lobbying)
- [esgSenateLobbyingDF](https://iexcloud.io/docs/api/#esg-senate-lobbying)
- [esgUSASpending](https://iexcloud.io/docs/api/#esg-usa-spending)
- [esgUSASpendingDF](https://iexcloud.io/docs/api/#esg-usa-spending)
- [esgUSPTOPatentApplications](https://iexcloud.io/docs/api/#esg-uspto-patent-applications)
- [esgUSPTOPatentApplicationsDF](https://iexcloud.io/docs/api/#esg-uspto-patent-applications)
- [esgUSPTOPatentGrants](https://iexcloud.io/docs/api/#esg-uspto-patent-grants)
- [esgUSPTOPatentGrantsDF](https://iexcloud.io/docs/api/#esg-uspto-patent-grants)
- [tacticalModel1](https://iexcloud.io/docs/api/#tactical-model-1)
- [tacticalModel1DF](https://iexcloud.io/docs/api/#tactical-model-1)

### Precision Alpha
- [precisionAlphaPriceDynamics](https://iexcloud.io/docs/api/#precision-alpha-price-dynamics)
- [precisionAlphaPriceDynamicsDF](https://iexcloud.io/docs/api/#precision-alpha-price-dynamics)

### BRAIN Company
- [brain30DaySentiment](https://iexcloud.io/docs/api/#brain-companys-30-day-sentiment-indicator)
- [brain30DaySentimentDF](https://iexcloud.io/docs/api/#brain-companys-30-day-sentiment-indicator)
- [brain7DaySentiment](https://iexcloud.io/docs/api/#brain-companys-7-day-sentiment-indicator)
- [brain7DaySentimentDF](https://iexcloud.io/docs/api/#brain-companys-7-day-sentiment-indicator)
- [brain21DayMLReturnRanking](https://iexcloud.io/docs/api/#brain-companys-21-day-machine-learning-estimated-return-ranking)
- [brain21DayMLReturnRankingDF](https://iexcloud.io/docs/api/#brain-companys-21-day-machine-learning-estimated-return-ranking)
- [brain10DayMLReturnRanking](https://iexcloud.io/docs/api/#brain-companys-10-day-machine-learning-estimated-return-ranking)
- [brain10DayMLReturnRankingDF](https://iexcloud.io/docs/api/#brain-companys-10-day-machine-learning-estimated-return-ranking)
- [brain5DayMLReturnRanking](https://iexcloud.io/docs/api/#brain-companys-5-day-machine-learning-estimated-return-ranking)
- [brain5DayMLReturnRankingDF](https://iexcloud.io/docs/api/#brain-companys-5-day-machine-learning-estimated-return-ranking)
- [brain3DayMLReturnRanking](https://iexcloud.io/docs/api/#brain-companys-3-day-machine-learning-estimated-return-ranking)
- [brain3DayMLReturnRankingDF](https://iexcloud.io/docs/api/#brain-companys-3-day-machine-learning-estimated-return-ranking)
- [brain2DayMLReturnRanking](https://iexcloud.io/docs/api/#brain-companys-2-day-machine-learning-estimated-return-ranking)
- [brain2DayMLReturnRankingDF](https://iexcloud.io/docs/api/#brain-companys-2-day-machine-learning-estimated-return-ranking)
- [brainLanguageMetricsOnCompanyFilingsAll](https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-quarterly-and-annual)
- [brainLanguageMetricsOnCompanyFilingsAllDF](https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-quarterly-and-annual)
- [brainLanguageMetricsOnCompanyFilings](https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-annual-only)
- [brainLanguageMetricsOnCompanyFilingsDF](https://iexcloud.io/docs/api/#brain-companys-language-metrics-on-company-filings-annual-only)
- [brainLanguageMetricsOnCompanyFilingsDifferenceAll](https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year)
- [brainLanguageMetricsOnCompanyFilingsDifferenceAllDF](https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year)
- [brainLanguageMetricsOnCompanyFilingsDifference](https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year)
- [brainLanguageMetricsOnCompanyFilingsDifferenceDF](https://iexcloud.io/docs/api/#brain-companys-differences-in-language-metrics-on-company-annual-filings-from-prior-year)

### Kavout
- [kScore](https://iexcloud.io/docs/api/#k-score-for-us-equities)
- [kScoreDF](https://iexcloud.io/docs/api/#k-score-for-us-equities)
- [kScoreChina](https://iexcloud.io/docs/api/#k-score-for-china-a-shares)
- [kScoreChinaDF](https://iexcloud.io/docs/api/#k-score-for-china-a-shares)

### Audit Analytics
- [accountingQualityAndRiskMatrix](https://iexcloud.io/docs/api/#audit-analytics-accounting-quality-and-risk-matrix)
- [accountingQualityAndRiskMatrixDF](https://iexcloud.io/docs/api/#audit-analytics-accounting-quality-and-risk-matrix)
- [directorAndOfficerChanges](https://iexcloud.io/docs/api/#audit-analytics-director-and-officer-changes)
- [directorAndOfficerChangesDF](https://iexcloud.io/docs/api/#audit-analytics-director-and-officer-changes)

### ValuEngine
- [valuEngineStockResearchReport](https://iexcloud.io/docs/api/#valuengine-stock-research-report)

### StockTwits Sentiment
- [socialSentiment](https://iexcloud.io/docs/api/#social-sentiment)
- [socialSentimentDF](https://iexcloud.io/docs/api/#social-sentiment)


## Studies
Available via `pyEX[studies]`.


### Studies
- peerCorrelation

### Technicals
These are built on [TA-lib](https://ta-lib.org). Note that these are different from the technicals available via IEX Cloud's `technicals` endpoint.


#### Cycle
- ht_dcperiod: Hilbert Transform - Dominant Cycle Period
- ht_dcphase: Hilbert Transform - Dominant Cycle Phase
- ht_phasor: Hilbert Transform - Phasor Components
- ht_sine: Hilbert Transform - SineWave
- ht_trendmode: Hilbert Transform - Trend vs Cycle Mode

#### Math
- acos: Vector Trigonometric ACos
- asin: Vector Trigonometric ASin
- atan: Vector Trigonometric ATan
- ceil: Vector Ceil
- cos: Vector Trigonometric Cos
- cosh: Vector Trigonometric Cosh
- exp: Vector Arithmetic Exp
- floor: Vector floor
- ln: Vector Log natural
- log10: Vector Log10
- sin: Vector Trigonometric Sin
- sinh: Vector Trigonometric Sinh
- sqrt: Vector Square Root
- tan: Vector Trigonometric Tan
- tanh: Vector Trigonometric Tanh
- add: Vector Arithmetic Add
- div: Vector Arithmetic Div
- max: Highest value over a specified period
- maxindex: Index of highest value over a specified period
- min: Lowest value over a specified period
- minindex: Index of lowest value over a specified period
- minmax: Lowest and highest values over a specified period
- minmaxindex: Index of lowest and highest values over a specified period
- mult: Vector Arithmetic Mult
- sub: Vector Arithmetic Subtraction
- sum: Summation

#### Momentum
- adx: Average Directional Movement Index
- adxr: Average Directional Movement Index Rating
- apo: Absolute Price Oscillator
- aroon: Aroon
- aroonosc: Aroon Oscillator
- bop: Balance Of Power
- cci: Commodity Channel Index
- cmo: Chande Momentum Oscillator
- dx: Directional Movement Index
- macd: Moving Average Convergence/Divergence
- macdext: MACD with controllable MA type
- mfi: Money Flow Index
- minus_di: Minus Directional Indicator
- minus_dm: Minus Directional Movement
- mom: Momentum
- plus_di: Plus Directional Indicator
- plus_dm: Plus Directional Movement
- ppo: Percentage Price Oscillator
- roc: Rate of change : ((price/prevPrice)-1)*100
- rocp: Rate of change Percentage: (price-prevPrice)/prevPrice
- rocr: Rate of change ratio: (price/prevPrice)
- rocr100: Rate of change ratio 100 scale: (price/prevPrice)*100
- rsi: Relative Strength Index
- stoch: Stochastic
- stochf: Stochastic Fast
- stochrsi: Stochastic Relative Strength Index
- trix: 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
- ultosc: Ultimate Oscillator
- willr: Williams' %R

#### Overlap
- bollinger: Bollinger Bands
- dema: Double Exponential Moving Average
- ema: Exponential Moving Aberage
- ht_trendline: Hilbert Transform - Instantaneous Trendline
- kama: Kaufman Adaptive Moving Average
- mama: MESA Adaptive Moving Average
- mavp: Moving average with variable period
- midpoint: Midpoint over period
- midpice: Midpoint price over period
- sar: Parabolic SAR
- sarext: Parabolic SAR - Extended
- sma: Moving Average
- t3: Triple Exponential Moving Average (T3)
- tema: Triple Exponential Moving Average
- trima: Triangular Moving Average
- wma: Weighted Moving Average

#### Pattern
- cdl2crows: Two Crows
- cdl3blackcrows: Three Black Crows
- cdl3inside: Three Inside Up/Down
- cdl3linestrike: Three-Line Strike
- cdl3outside: Three Outside Up/Down
- cdl3starsinsouth: Three Stars In The South
- cdl3whitesoldiers: Three Advancing White Soldiers
- cdlabandonedbaby: Abandoned Baby
- cdladvanceblock: Advance Block
- cdlbelthold: Belt-hold
- cdlbreakaway: Breakaway
- cdlclosingmarubozu: Closing Marubozu
- cdlconcealbabyswall: Concealing Baby Swallow
- cdlcounterattack: Counterattack
- cdldarkcloudcover: Dark Cloud Cover
- cdldoji: Doji
- cdldojistar: Doji Star
- cdldragonflydoji: Dragonfly Doji
- cdlengulfing: Engulfing Pattern
- cdleveningdojistar: Evening Doji Star
- cdleveningstar: Evening Star
- cdlgapsidesidewhite: Up/Down-gap side-by-side white lines
- cdlgravestonedoji: Gravestone Doji
- cdlhammer: Hammer
- cdlhangingman: Hanging Man
- cdlharami: Harami Pattern
- cdlharamicross: Harami Cross Pattern
- cdlhighwave: High-Wave Candle
- cdlhikkake: Hikkake Pattern
- cdlhikkakemod: Modified Hikkake Pattern
- cdlhomingpigeon: Homing Pigeon
- cdlidentical3crows: Identical Three Crows
- cdlinneck: In-Neck Pattern
- cdlinvertedhammer: Inverted Hammer
- cdlkicking: Kicking
- cdlkickingbylength: Kicking - bull/bear determined by the longer marubozu
- cdlladderbottom: Ladder Bottom
- cdllongleggeddoji: Long Legged Doji
- cdllongline: Long Line Candle
- cdlmarubozu: Marubozu
- cdlmatchinglow: Matching Low
- cdlmathold: Mat Hold
- cdlmorningdojistar: Morning Doji Star
- cdlmorningstar: Morning Star
- cdlonneck: On-Neck Pattern
- cdlpiercing: Piercing Pattern
- cdlrickshawman: Rickshaw Man
- cdlrisefall3methods: Rising/Falling Three Methods
- cdlseparatinglines: Separating Lines
- cdlshootingstar: Shooting Star
- cdlshortline: Short Line Candle
- cdlspinningtop: Spinning Top
- cdlstalledpattern: Stalled Pattern
- cdlsticksandwich: Stick Sandwich
- cdltakuri: Takuri (Dragonfly Doji with very long lower shadow)
- cdltasukigap: Tasuki Gap
- cdlthrusting: Thrusting Pattern
- cdltristar: Tristar Pattern
- cdlunique3river: Unique 3 River
- cdlupsidegap2crows: Upside Gap Two Crows
- cdlxsidegap3methods: Upside/Downside Gap Three Methods

#### Price
- avgprice: Average Price
- medprice: Median Price
- typprice: Typical Price
- wclprice: Weighted Close Price

#### Statistic
- beta: Beta
- correl: Pearson's Correlation Coefficient (r)
- linearreg: Linear Regression
- linearreg_angle: Linear Regression Angle
- linearreg_intercept: Linear Regression Intercept
- linearreg_slope: Linear Regression Slope
- stddev: Standard Deviation
- tsf: Time Series Forecast
- var: Variance
#### Volatility
- atr: Average True Range
- natr: Normalized Average True Range
- trange: True Range

#### Volume
- ad: Chaikin A/D Line
- adosc: Chaikin A/D Oscillator
- obv: On Balance Volume

## Attribution
- [Powered by IEX Cloud](https://iexcloud.io)
- Data provided for free by [IEX](https://iextrading.com/developer).
- [IEX terms of service](https://iextrading.com/api-exhibit-a)
