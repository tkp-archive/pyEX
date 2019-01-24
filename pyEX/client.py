import os
from functools import partial
from .common import PyEXception, _getJson, _USAGE_TYPES
from .refdata import symbols, iexSymbols, symbolsDF, iexSymbolsDF, \
    symbolsList, iexSymbolsList, corporateActions, corporateActionsDF, dividends as refDividends, dividendsDF as refDividendsDF, nextDayExtDate, nextDayExtDateDF, directory, directoryDF
from .markets import markets, marketsDF
from .stats import stats, statsDF, recent, recentDF, records, recordsDF, summary, summaryDF, daily, dailyDF
from .stocks import balanceSheet, balanceSheetDF, batch, batchDF, bulkBatch, bulkBatchDF, book, bookDF, cashFlow, cashFlowDF, chart, chartDF, \
    bulkMinuteBars, bulkMinuteBarsDF, company, companyDF, collections, collectionsDF, crypto, cryptoDF, delayedQuote, delayedQuoteDF, dividends, dividendsDF, \
    earnings, earningsDF, earningsToday, earningsTodayDF, spread, spreadDF, financials, financialsDF, incomeStatement, incomeStatementDF, ipoToday, ipoTodayDF, \
    ipoUpcoming, ipoUpcomingDF, threshold, thresholdDF, shortInterest, shortInterestDF, marketShortInterest, marketShortInterestDF, stockStats, stockStatsDF, \
    largestTrades, largestTradesDF, list, listDF, logo, logoPNG, logoNotebook, news, newsDF, marketNews, marketNewsDF, ohlc, ohlcDF, marketOhlc, marketOhlcDF, \
    peers, peersDF, yesterday, yesterdayDF, marketYesterday, marketYesterdayDF, price, priceDF, quote, quoteDF, relevant, relevantDF, sectorPerformance, \
    sectorPerformanceDF, splits, splitsDF, volumeByVenue, volumeByVenueDF
from .marketdata.sse import topsSSE, lastSSE, deepSSE, tradesSSE


_INCLUDE_FUNCTIONS = [
    # Refdata
    ('symbols', symbols),
    ('iexSymbols', iexSymbols),
    ('symbolsDF', symbolsDF),
    ('iexSymbolsDF', iexSymbolsDF),
    ('symbolsList', symbolsList),
    ('iexSymbolsList', iexSymbolsList),
    ('corporateActions', corporateActions),
    ('corporateActionsDF', corporateActionsDF),
    ('refDividends', refDividends),
    ('refDividendsDF', refDividendsDF),
    ('nextDayExtDate', nextDayExtDate),
    ('nextDayExtDateDF', nextDayExtDateDF),
    ('directory', directory),
    ('directoryDF', directoryDF),
    # Markets
    ('markets', markets),
    ('marketsDF', marketsDF),
    # Stats
    ('stats', stats),
    ('statsDF', statsDF),
    ('recent', recent),
    ('recentDF', recentDF),
    ('records', records),
    ('recordsDF', recordsDF),
    ('summary', summary),
    ('summaryDF', summaryDF),
    ('daily', daily),
    ('dailyDF', dailyDF),
    # Stocks
    ('balanceSheet', balanceSheet),
    ('balanceSheetDF', balanceSheetDF),
    ('batch', batch),
    ('batchDF', batchDF),
    ('bulkBatch', bulkBatch),
    ('bulkBatchDF', bulkBatchDF),
    ('book', book),
    ('bookDF', bookDF),
    ('cashFlow', cashFlow),
    ('cashFlowDF', cashFlowDF),
    ('chart', chart),
    ('chartDF', chartDF),
    ('bulkMinuteBars', bulkMinuteBars),
    ('bulkMinuteBarsDF', bulkMinuteBarsDF),
    ('company', company),
    ('companyDF', companyDF),
    ('collections', collections),
    ('collectionsDF', collectionsDF),
    ('crypto', crypto),
    ('cryptoDF', cryptoDF),
    ('delayedQuote', delayedQuote),
    ('delayedQuoteDF', delayedQuoteDF),
    ('dividends', dividends),
    ('dividendsDF', dividendsDF),
    ('earnings', earnings),
    ('earningsDF', earningsDF),
    ('earningsToday', earningsToday),
    ('earningsTodayDF', earningsTodayDF),
    ('spread', spread),
    ('spreadDF', spreadDF),
    ('financials', financials),
    ('financialsDF', financialsDF),
    ('incomeStatement', incomeStatement),
    ('incomeStatementDF', incomeStatementDF),
    ('ipoToday', ipoToday),
    ('ipoTodayDF', ipoTodayDF),
    ('ipoUpcoming', ipoUpcoming),
    ('ipoUpcomingDF', ipoUpcomingDF),
    ('threshold', threshold),
    ('thresholdDF', thresholdDF),
    ('shortInterest', shortInterest),
    ('shortInterestDF', shortInterestDF),
    ('marketShortInterest', marketShortInterest),
    ('marketShortInterestDF', marketShortInterestDF),
    ('stockStats', stockStats),
    ('stockStatsDF', stockStatsDF),
    ('largestTrades', largestTrades),
    ('largestTradesDF', largestTradesDF),
    ('list', list),
    ('listDF', listDF),
    ('logo', logo),
    ('logoPNG', logoPNG),
    ('logoNotebook', logoNotebook),
    ('news', news),
    ('newsDF', newsDF),
    ('marketNews', marketNews),
    ('marketNewsDF', marketNewsDF),
    ('ohlc', ohlc),
    ('ohlcDF', ohlcDF),
    ('marketOhlc', marketOhlc),
    ('marketOhlcDF', marketOhlcDF),
    ('peers', peers),
    ('peersDF', peersDF),
    ('yesterday', yesterday),
    ('yesterdayDF', yesterdayDF),
    ('marketYesterday', marketYesterday),
    ('marketYesterdayDF', marketYesterdayDF),
    ('price', price),
    ('priceDF', priceDF),
    ('quote', quote),
    ('quoteDF', quoteDF),
    ('relevant', relevant),
    ('relevantDF', relevantDF),
    ('sectorPerformance', sectorPerformance),
    ('sectorPerformanceDF', sectorPerformanceDF),
    ('splits', splits),
    ('splitsDF', splitsDF),
    ('volumeByVenue', volumeByVenue),
    ('volumeByVenueDF', volumeByVenueDF),
    # SSE Streaming
    ('topsSSE', topsSSE),
    ('lastSSE', lastSSE),
    ('deepSSE', deepSSE),
    ('tradesSSE', tradesSSE),
]


class Client(object):
    def __init__(self, api_token=None, version='beta'):
        self._token = api_token or os.environ.get('IEX_TOKEN', '')
        if not self._token:
            raise PyEXception('API Token missing or not in environment (IEX_TOKEN)')

        self._version = version
        for name, method in _INCLUDE_FUNCTIONS:
            setattr(self, name, partial(self.bind, meth=method))

    def bind(self, *args, meth=None, **kwargs):
        return meth(token=self._token, version=self._version, *args, **kwargs)

    def account(self):
        return _getJson('account/metadata', self._token, self._version)

    def usage(self, type=None):
        if type:
            if type not in _USAGE_TYPES:
                raise PyEXception('type not recognized: {}'.format(type))
            return _getJson('account/usage/{type}'.format(type=type), self._token, self._version)
        return _getJson('account/usage/messages', self._token, self._version)
