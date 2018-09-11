===============
Getting started
===============
.. WARNING:: pyEX is under active beta development, so interfaces and functionality may change

Overview
===============
Stocks
^^^^^^

-  `book <https://iextrading.com/developer/docs/#book>`__

   .. code:: python3

          def book(symbol):

   .. code:: python3

          def bookDF(symbol):

-  `chart <https://iextrading.com/developer/docs/#chart>`__

   .. code:: python3

          def chart(symbol, timeframe='1m', date=None):

   .. code:: python3

          def chartDF(symbol, timeframe='1m'):

-  `company <https://iextrading.com/developer/docs/#company>`__

   .. code:: python3

          def company(symbol):

   .. code:: python3

          def companyDF(symbol):


-  `collections <https://iextrading.com/developer/docs/#collections>`__

   .. code:: python3

          def collections(tag, query):

   .. code:: python3

          def collectionsDF(tag, query):

-  `delayedQuote <https://iextrading.com/developer/docs/#delayed-quote>`__

   .. code:: python3

          def delayedQuote(symbol):

   .. code:: python3

          def delayedQuoteDF(symbol):

-  `dividends <https://iextrading.com/developer/docs/#dividends>`__

   .. code:: python3

          def dividends(symbol, timeframe='ytd'):

   .. code:: python3

          def dividendsDF(symbol, timeframe='ytd'):

-  `earnings <https://iextrading.com/developer/docs/#earnings>`__

   .. code:: python3

          def earnings(symbol):

   .. code:: python3

          def earningsDF(symbol):

-  `spread <https://iextrading.com/developer/docs/#effective-spread>`__

   .. code:: python3

          def spread(symbol):

   .. code:: python3

          def spreadDF(symbol):

-  `financials <https://iextrading.com/developer/docs/#financials>`__

   .. code:: python3

          def financials(symbol):

   .. code:: python3

          def financialsDF(symbol):

-  `threshold <https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list>`__

   .. code:: python3

          def threshold(date=None):

   .. code:: python3

          def thresholdDF(date=None):

-  `shortInterest <https://iextrading.com/developer/docs/#iex-short-interest-list>`__

   .. code:: python3

          def shortInterest(symbol, date=None):

   .. code:: python3

          def shortInterestDF(symbol, date=None):

-  `marketShortInterest <https://iextrading.com/developer/docs/#iex-short-interest-list>`__

   .. code:: python3

          def marketShortInterest(date=None):

   .. code:: python3

          def marketShortInterestDF(date=None):

-  `stockStats <https://iextrading.com/developer/docs/#key-stats>`__

   .. code:: python3

          def stockStats(symbol):

   .. code:: python3

          def stockStatsDF(symbol):

-  `list <https://iextrading.com/developer/docs/#list>`__

   .. code:: python3

          def list(option='mostactive'):

   .. code:: python3

          def listDF(option='mostactive'):

-  `logo <https://iextrading.com/developer/docs/#logo>`__

   .. code:: python3

          def logo(symbol):

   .. code:: python3

          def logoPNG(symbol):

   .. code:: python3

          def logoNotebook(symbol):

-  `news <https://iextrading.com/developer/docs/#news>`__

   .. code:: python3

          def news(symbol, count=10):

   .. code:: python3

          def newsDF(symbol, count=10):

-  `marketNews <https://iextrading.com/developer/docs/#news>`__

   .. code:: python3

          def marketNews(count=10):

   .. code:: python3

          def marketNewsDF(count=10):

-  `ohlc <https://iextrading.com/developer/docs/#ohlc>`__

   .. code:: python3

          def ohlc(symbol):

   .. code:: python3

          def ohlcDF(symbol):

-  `marketOhlc <https://iextrading.com/developer/docs/#ohlc>`__

   .. code:: python3

          def marketOhlc():

   .. code:: python3

          def marketOhlcDF():

-  `peers <https://iextrading.com/developer/docs/#peers>`__

   .. code:: python3

          def peers(symbol):

   .. code:: python3

          def peersDF(symbol):

-  `yesterday <https://iextrading.com/developer/docs/#previous>`__

   .. code:: python3

          def yesterday(symbol):

   .. code:: python3

          def yesterdayDF(symbol):

-  `marketYesterday <https://iextrading.com/developer/docs/#previous>`__

   .. code:: python3

          def marketYesterday():

   .. code:: python3

          def marketYesterdayDF():

-  `price <https://iextrading.com/developer/docs/#price>`__
   ``python3       def price(symbol):``

   .. code:: python3

          def priceDF(symbol):

-  `quote <https://iextrading.com/developer/docs/#quote>`__

   .. code:: python3

          def quote(symbol):

   .. code:: python3

          def quoteDF(symbol):

-  `relevant <https://iextrading.com/developer/docs/#relevant>`__

   .. code:: python3

          def relevant(symbol):

   .. code:: python3

          def relevantDF(symbol):

-  `splits <https://iextrading.com/developer/docs/#splits>`__

   .. code:: python3

          def splits(symbol, timeframe='ytd'):

   .. code:: python3

          def splitsDF(symbol, timeframe='ytd'):

-  `volumeByVenue <https://iextrading.com/developer/docs/#volume-by-venue>`__

   .. code:: python3

          def volumeByVenue(symbol):

   .. code:: python3

          def volumeByVenueDF(symbol):

Reference
^^^^^^^^^

-  `symbols <https://iextrading.com/developer/docs/#symbols>`__

   .. code:: python3

          def symbols():

   .. code:: python3

          def symbolsDF():

-  `corporateActions <https://iextrading.com/developer/docs/#iex-corporate-actions>`__
   ``python3       def corporateActions(date=None):``

   .. code:: python3

          def corporateActionsDF(date=None):

-  `dividends <https://iextrading.com/developer/docs/#iex-dividends>`__
   ``python3       def dividends(date=None):``

   .. code:: python3

          def dividendsDF(date=None):

-  `nextDayExtDate <https://iextrading.com/developer/docs/#iex-next-day-ex-date>`__
   ``python3       def nextDayExtDate(date=None):``

   .. code:: python3

          def nextDayExtDateDF(date=None):

-  `directory <https://iextrading.com/developer/docs/#iex-listed-symbol-directory>`__
   ``python3       def directory(date=None):``

   .. code:: python3

          def directoryDF(date=None):

Market Data
^^^^^^^^^^^

-  `tops <https://iextrading.com/developer/docs/#tops>`__

   .. code:: python3

          def tops(symbols=None):

   .. code:: python3

          def topsDF(symbols=None):

   .. code:: python3

          def topsWS(symbols=None, on_data=None):

-  `last <https://iextrading.com/developer/docs/#last>`__

   .. code:: python3

          def last(symbols=None):

   .. code:: python3

          def lastDF(symbols=None):

   .. code:: python3

          def lastWS(symbols=None, on_data=None):

-  `hist <https://iextrading.com/developer/docs/#hist>`__

   .. code:: python3

          def hist(date=None):

   .. code:: python3

          def histDF(date=None):

-  `deep <https://iextrading.com/developer/docs/#deep>`__

   .. code:: python3

          def deep(symbol=None):

   .. code:: python3

          def deepDF(symbol=None):

   .. code:: python3

          def deepWS(symbols=None, channels=None, on_data=None):

-  `book <https://iextrading.com/developer/docs/#book55>`__

   .. code:: python3

          def book(symbol=None):

   .. code:: python3

          def bookDF(symbol=None):

   .. code:: python3

          def bookWS(symbols=None, on_data=None):

-  `trades <https://iextrading.com/developer/docs/#trades>`__

   .. code:: python3

          def trades(symbol=None):

   .. code:: python3

          def tradesDF(symbol=None):

   .. code:: python3

          def tradesWS(symbols=None, on_data=None):

-  `systemEvent <https://iextrading.com/developer/docs/#system-event>`__

   .. code:: python3

          def systemEvent():

   .. code:: python3

          def systemEventDF():

   .. code:: python3

          def systemEventWS(on_data=None):

-  `tradingStatus <https://iextrading.com/developer/docs/#trading-status>`__

   .. code:: python3

          def tradingStatus(symbol=None):

   .. code:: python3

          def tradingStatusDF(symbol=None):

   .. code:: python3

          def tradingStatusWS(symbols=None, on_data=None):

-  `opHaltStatus <https://iextrading.com/developer/docs/#operational-halt-status>`__

   .. code:: python3

          def opHaltStatus(symbol=None):

   .. code:: python3

          def opHaltStatusDF(symbol=None):

   .. code:: python3

          def opHaltStatusWS(symbols=None, on_data=None):

-  `ssr <https://iextrading.com/developer/docs/#short-sale-price-test-status>`__

   .. code:: python3

          def ssrStatus(symbol=None):

   .. code:: python3

          def ssrStatusDF(symbol=None):

   .. code:: python3

          def ssrStatusWS(symbols=None, on_data=None):

-  `securityEvent <https://iextrading.com/developer/docs/#security-event>`__

   .. code:: python3

          def securityEvent(symbol=None):

   .. code:: python3

          def securityEventDF(symbol=None):

   .. code:: python3

          def securityEventWS(symbols=None, on_data=None):

-  `tradeBreak <https://iextrading.com/developer/docs/#trade-break>`__

   .. code:: python3

          def tradeBreak(symbol=None):

   .. code:: python3

          def tradeBreakDF(symbol=None):

   .. code:: python3

          def tradeBreakWS(symbols=None, on_data=None):

-  `auction <https://iextrading.com/developer/docs/#auction>`__

   .. code:: python3

          def auction(symbol=None):

   .. code:: python3

          def auctionDF(symbol=None):

   .. code:: python3

          def auctionWS(symbols=None, on_data=None):

Stats
^^^^^

-  `stats <https://iextrading.com/developer/docs/#intraday>`__
   ``python3       def stats():``

   .. code:: python3

          def statsDF():

-  `recent <https://iextrading.com/developer/docs/#recent>`__
   ``python3       def recent():``

   .. code:: python3

          def recentDF():

-  `records <https://iextrading.com/developer/docs/#records>`__
   ``python3       def records():``

   .. code:: python3

          def recordsDF():

-  `summary <https://iextrading.com/developer/docs/#historical-summary>`__
   ``python3       def summary(date=None):``

   .. code:: python3

          def summaryDF(date=None):

-  `daily <https://iextrading.com/developer/docs/#historical-daily>`__
   ``python3       def daily(date=None, last=''):``

   .. code:: python3

          def dailyDF(date=None, last=''):

Markets
^^^^^^^

-  `markets <https://iextrading.com/developer/docs/#intraday>`__

   .. code:: python3

          def markets():

   .. code:: python3

          def marketsDF():
