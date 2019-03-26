import os
from functools import partial
from .common import PyEXception, _getJson, _USAGE_TYPES

from .refdata import symbols, iexSymbols, mutualFundSymbols, otcSymbols, internationalSymbols, \
    symbolsDF, iexSymbolsDF, mutualFundSymbolsDF, otcSymbolsDF, internationalSymbolsDF, \
    symbolsList, iexSymbolsList, mutualFundSymbolsList, otcSymbolsList, internationalSymbolsList, \
    corporateActions, corporateActionsDF, \
    dividends as refDividends, dividendsDF as refDividendsDF, \
    nextDayExtDate, nextDayExtDateDF, \
    directory, directoryDF, \
    calendar, calendarDF, holidays, holidaysDF, \
    exchanges, exchangesDF

from .markets import markets, marketsDF

from .stats import stats, statsDF, \
    recent, recentDF, \
    records, recordsDF, \
    summary, summaryDF, \
    daily, dailyDF

from .stocks import balanceSheet, balanceSheetDF, \
    batch, batchDF, bulkBatch, bulkBatchDF, \
    book, bookDF, \
    bulkMinuteBars, bulkMinuteBarsDF, \
    cashFlow, cashFlowDF, \
    chart, chartDF, \
    company, companyDF, \
    collections, collectionsDF, \
    delayedQuote, delayedQuoteDF, \
    dividends, dividendsDF, \
    earnings, earningsDF, \
    earningsToday, earningsTodayDF, \
    estimates, estimatesDF, \
    financials, financialsDF, \
    incomeStatement, incomeStatementDF, \
    ipoToday, ipoTodayDF, \
    ipoUpcoming, ipoUpcomingDF, \
    marketShortInterest, marketShortInterestDF, \
    marketVolume, marketVolumeDF, \
    keyStats, keyStatsDF, \
    largestTrades, largestTradesDF, \
    list, listDF, \
    logo, logoPNG, logoNotebook, \
    news, newsDF, marketNews, marketNewsDF, \
    ohlc, ohlcDF, marketOhlc, marketOhlcDF, \
    peers, peersDF, \
    marketYesterday, marketYesterdayDF, \
    price, priceDF, \
    priceTarget, priceTargetDF, \
    quote, quoteDF, \
    relevant, relevantDF, \
    sectorPerformance, sectorPerformanceDF, \
    shortInterest, shortInterestDF, \
    splits, splitsDF, \
    spread, spreadDF, \
    threshold, thresholdDF, \
    volumeByVenue, volumeByVenueDF, \
    yesterday, yesterdayDF

from .alternative import crypto, cryptoDF, \
    sentiment, sentimentDF

from .marketdata.sse import topsSSE, lastSSE, deepSSE, tradesSSE


_INCLUDE_FUNCTIONS = [
    # Refdata
    ('symbols', symbols),
    ('iexSymbols', iexSymbols),
    ('mutualFundSymbols', mutualFundSymbols),
    ('otcSymbols', otcSymbols),
    ('internationalSymbols', internationalSymbols),
    ('symbolsDF', symbolsDF),
    ('iexSymbolsDF', iexSymbolsDF),
    ('mutualFundSymbolsDF', mutualFundSymbolsDF),
    ('otcSymbolsDF', otcSymbolsDF),
    ('internationalSymbolsDF', internationalSymbolsDF),
    ('symbolsList', symbolsList),
    ('iexSymbolsList', iexSymbolsList),
    ('mutualFundSymbolsList', mutualFundSymbolsList),
    ('otcSymbolsList', otcSymbolsList),
    ('internationalSymbolsList', internationalSymbolsList),
    ('corporateActions', corporateActions),
    ('corporateActionsDF', corporateActionsDF),
    ('refDividends', refDividends),
    ('refDividendsDF', refDividendsDF),
    ('nextDayExtDate', nextDayExtDate),
    ('nextDayExtDateDF', nextDayExtDateDF),
    ('directory', directory),
    ('directoryDF', directoryDF),
    ('calendar', calendar),
    ('calendarDF', calendarDF),
    ('holidays', holidays),
    ('holidaysDF', holidaysDF),
    ('exchanges', exchanges),
    ('exchangesDF', exchangesDF),
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
    ('marketVolume', marketVolume),
    ('marketVolumeDF', marketVolumeDF),
    ('marketShortInterest', marketShortInterest),
    ('marketShortInterestDF', marketShortInterestDF),
    ('estimates', estimates),
    ('estimatesDF', estimatesDF),
    ('keyStats', keyStats),
    ('keyStatsDF', keyStatsDF),
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
    ('priceTarget', priceTarget),
    ('priceTargetDF', priceTargetDF),
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
    # Alternative
    ('crypto', crypto),
    ('cryptoDF', cryptoDF),
    ('sentiment', sentiment),
    ('sentimentDF', sentimentDF),
]


class Client(object):
    '''IEX Cloud Client

    Client has access to all methods provided as standalone, but in an authenticated way

    Args:
        api_token (string): api token (can pickup from IEX_TOKEN environment variable)
        verson (string): api version to use (defaults to beta)
    '''
    def __init__(self, api_token=None, version='beta'):
        self._token = api_token or os.environ.get('IEX_TOKEN', '')
        if not self._token:
            raise PyEXception('API Token missing or not in environment (IEX_TOKEN)')

        self._version = version
        for name, method in _INCLUDE_FUNCTIONS:
            setattr(self, name, partial(self.bind, meth=method))
            getattr(self, name).__doc__ = method.__doc__

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
