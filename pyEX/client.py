# -*- coding: utf-8 -*-
import os
from functools import partial, wraps
from .common import PyEXception, _interval, _getJson, _USAGE_TYPES
from .alternative import crypto, cryptoDF, \
    sentiment, sentimentDF, \
    ceoCompensation, ceoCompensationDF
from .commodities import CommoditiesPoints
from .cryptocurrency import cryptoBook, cryptoBookDF, cryptoPrice, cryptoPriceDF, cryptoQuote, cryptoQuoteDF
from .economic import EconomicPoints
from .fx import latestFX, latestFXDF, convertFX, convertFXDF, historicalFX, historicalFXDF
from .markets import markets, marketsDF
from .marketdata.cryptocurrency import cryptoBookSSE, cryptoEventsSSE, cryptoQuotesSSE
from .marketdata.fx import fxSSE
from .marketdata.sse import topsSSE, lastSSE, deepSSE, tradesSSE
from .marketdata.http import tops, topsDF, \
    last, lastDF, \
    deep, deepDF, \
    trades, tradesDF, \
    auction, auctionDF, \
    book as deepBook, bookDF as deepBookDF, \
    opHaltStatus, opHaltStatusDF, \
    officialPrice, officialPriceDF, \
    securityEvent, securityEventDF, \
    ssrStatus, ssrStatusDF, \
    systemEvent, systemEventDF, \
    tradeBreak, tradeBreakDF, \
    tradingStatus, tradingStatusDF
from .points import points, pointsDF
from .premium import (accountingQualityAndRiskMatrix, accountingQualityAndRiskMatrixDF,
                      analystDays, analystDaysDF,
                      boardOfDirectorsMeeting, boardOfDirectorsMeetingDF,
                      brain30DaySentiment, brain30DaySentimentDF,
                      brain7DaySentiment, brain7DaySentimentDF,
                      brain21DayMLReturnRanking, brain21DayMLReturnRankingDF,
                      brain10DayMLReturnRanking, brain10DayMLReturnRankingDF,
                      brain5DayMLReturnRanking, brain5DayMLReturnRankingDF,
                      brain3DayMLReturnRanking, brain3DayMLReturnRankingDF,
                      brain2DayMLReturnRanking, brain2DayMLReturnRankingDF,
                      brainLanguageMetricsOnCompanyFilingsAll, brainLanguageMetricsOnCompanyFilingsAllDF,
                      brainLanguageMetricsOnCompanyFilings, brainLanguageMetricsOnCompanyFilingsDF,
                      brainLanguageMetricsOnCompanyFilingsDifferenceAll, brainLanguageMetricsOnCompanyFilingsDifferenceAllDF,
                      brainLanguageMetricsOnCompanyFilingsDifference, brainLanguageMetricsOnCompanyFilingsDifferenceDF,
                      businessUpdates, businessUpdatesDF,
                      buybacks, buybacksDF,
                      cam1, cam1DF,
                      capitalMarketsDay, capitalMarketsDayDF,
                      companyTravel, companyTravelDF,
                      directorAndOfficerChanges, directorAndOfficerChangesDF,
                      esgCFPBComplaints, esgCFPBComplaintsDF,
                      esgCPSCRecalls, esgCPSCRecallsDF,
                      esgDOLVisaApplications, esgDOLVisaApplicationsDF,
                      esgEPAEnforcements, esgEPAEnforcementsDF,
                      esgEPAMilestones, esgEPAMilestonesDF,
                      esgFECIndividualCampaingContributions, esgFECIndividualCampaingContributionsDF,
                      esgOSHAInspections, esgOSHAInspectionsDF,
                      esgSenateLobbying, esgSenateLobbyingDF,
                      esgUSASpending, esgUSASpendingDF,
                      esgUSPTOPatentApplications, esgUSPTOPatentApplicationsDF,
                      esgUSPTOPatentGrants, esgUSPTOPatentGrantsDF,
                      fdaAdvisoryCommitteeMeetings, fdaAdvisoryCommitteeMeetingsDF,
                      filingDueDates, filingDueDatesDF,
                      fiscalQuarterEnd, fiscalQuarterEndDF,
                      forum, forumDF,
                      generalConference, generalConferenceDF,
                      holidaysWSH, holidaysWSHDF,
                      indexChanges, indexChangesDF,
                      iposWSH, iposWSHDF,
                      kScore, kScoreDF,
                      legalActions, legalActionsDF,
                      mergersAndAcquisitions, mergersAndAcquisitionsDF,
                      nonTimelyFilings, nonTimelyFilingsDF,
                      precisionAlphaPriceDynamics, precisionAlphaPriceDynamicsDF,
                      productEventsDF, productEvents,
                      researchAndDevelopmentDays, researchAndDevelopmentDaysDF,
                      sameStoreSales, sameStoreSalesDF,
                      secondaryOfferings, secondaryOfferingsDF,
                      seminars, seminarsDF,
                      shareholderMeetings, shareholderMeetingsDF,
                      similarityIndex, similarityIndexDF,
                      summitMeetings, summitMeetingsDF,
                      tacticalModel1, tacticalModel1DF,
                      tradeShows, tradeShowsDF,
                      witchingHours, witchingHoursDF,
                      valuEngineStockResearchReport,
                      workshops, workshopsDF)
from .rates import RatesPoints
from .refdata import symbols, iexSymbols, mutualFundSymbols, otcSymbols, internationalSymbols, fxSymbols, optionsSymbols, \
    symbolsDF, iexSymbolsDF, mutualFundSymbolsDF, otcSymbolsDF, internationalSymbolsDF, fxSymbolsDF, optionsSymbolsDF, \
    symbolsList, iexSymbolsList, mutualFundSymbolsList, otcSymbolsList, internationalSymbolsList, fxSymbolsList, optionsSymbolsList, \
    corporateActions, corporateActionsDF, \
    refDividends, refDividendsDF, \
    nextDayExtDate, nextDayExtDateDF, \
    directory, directoryDF, \
    calendar, calendarDF, holidays, holidaysDF, \
    exchanges, exchangesDF, \
    internationalExchanges, internationalExchangesDF, \
    sectors, sectorsDF, \
    tags, tagsDF
from .stats import stats, statsDF, \
    recent, recentDF, \
    records, recordsDF, \
    summary, summaryDF, \
    daily, dailyDF
from .stocks import advancedStats, advancedStatsDF, \
    analystRecommendations, analystRecommendationsDF, \
    balanceSheet, balanceSheetDF, \
    batch, batchDF, bulkBatch, bulkBatchDF, \
    book, bookDF, \
    bonusIssue, bonusIssueDF, \
    bulkMinuteBars, bulkMinuteBarsDF, \
    cashFlow, cashFlowDF, \
    chart, chartDF, \
    company, companyDF, \
    collections, collectionsDF, \
    delayedQuote, delayedQuoteDF, \
    distribution, distributionDF, \
    dividends, dividendsDF, \
    earnings, earningsDF, \
    earningsToday, earningsTodayDF, \
    estimates, estimatesDF, \
    financials, financialsDF, \
    fundOwnership, fundOwnershipDF, \
    incomeStatement, incomeStatementDF, \
    insiderRoster, insiderRosterDF, \
    insiderSummary, insiderSummaryDF, \
    insiderTransactions, insiderTransactionsDF, \
    institutionalOwnership, institutionalOwnershipDF, \
    intraday, intradayDF, \
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
    returnOfCapital, returnOfCapitalDF, \
    rightsIssue, rightsIssueDF, \
    rightToPurchase, rightToPurchaseDF, \
    sectorPerformance, sectorPerformanceDF, \
    securityReclassification, securityReclassificationDF, \
    securitySwap, securitySwapDF, \
    shortInterest, shortInterestDF, \
    splits, splitsDF, \
    spinoff, spinoffDF, \
    spread, spreadDF, \
    stockSplits, stockSplitsDF, \
    tenQ, tenK, \
    threshold, thresholdDF, \
    timeSeriesInventory, timeSeries, \
    timeSeriesInventoryDF, timeSeriesDF, \
    upcomingEvents, upcomingEventsDF, \
    upcomingEarnings, upcomingEarningsDF, \
    upcomingDividends, upcomingDividendsDF, \
    upcomingSplits, upcomingSplitsDF, \
    upcomingIPOs, upcomingIPOsDF, \
    volumeByVenue, volumeByVenueDF, \
    yesterday, yesterdayDF
from .options import optionExpirations, options, optionsDF

try:
    from .studies import peerCorrelation, bollinger, dema, ema, sar, sma

except ImportError:
    peerCorrelation = None
    bollinger = None
    dema = None
    ema = None
    sar = None
    sma = None

DEFAULT_API_LIMIT = 5

_INCLUDE_FUNCTIONS = [
    # Refdata
    ('symbols', symbols),
    ('iexSymbols', iexSymbols),
    ('mutualFundSymbols', mutualFundSymbols),
    ('otcSymbols', otcSymbols),
    ('internationalSymbols', internationalSymbols),
    ('fxSymbols', fxSymbols),
    ('optionsSymbols', optionsSymbols),
    ('symbolsDF', symbolsDF),
    ('iexSymbolsDF', iexSymbolsDF),
    ('mutualFundSymbolsDF', mutualFundSymbolsDF),
    ('otcSymbolsDF', otcSymbolsDF),
    ('internationalSymbolsDF', internationalSymbolsDF),
    ('fxSymbolsDF', fxSymbolsDF),
    ('optionsSymbolsDF', optionsSymbolsDF),
    ('symbolsList', symbolsList),
    ('iexSymbolsList', iexSymbolsList),
    ('mutualFundSymbolsList', mutualFundSymbolsList),
    ('otcSymbolsList', otcSymbolsList),
    ('internationalSymbolsList', internationalSymbolsList),
    ('fxSymbolsList', fxSymbolsList),
    ('optionsSymbolsList', optionsSymbolsList),
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
    ('internationalExchanges', internationalExchanges),
    ('internationalExchangesDF', internationalExchangesDF),
    ('sectors', sectors),
    ('sectorsDF', sectorsDF),
    ('tags', tags),
    ('tagsDF', tagsDF),
    # Markets
    ('markets', markets),
    ('marketsDF', marketsDF),
    # Stats
    ('systemStats', stats),
    ('systemStatsDF', statsDF),
    ('recent', recent),
    ('recentDF', recentDF),
    ('records', records),
    ('recordsDF', recordsDF),
    ('summary', summary),
    ('summaryDF', summaryDF),
    ('daily', daily),
    ('dailyDF', dailyDF),
    # Stocks
    ('advancedStats', advancedStats),
    ('advancedStatsDF', advancedStatsDF),
    ('analystRecommendations', analystRecommendations),
    ('analystRecommendationsDF', analystRecommendationsDF),
    ('balanceSheet', balanceSheet),
    ('balanceSheetDF', balanceSheetDF),
    ('batch', batch),
    ('batchDF', batchDF),
    ('bonusIssue', bonusIssue),
    ('bonusIssueDF', bonusIssueDF),
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
    ('distribution', distribution),
    ('distributionDF', distributionDF),
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
    ('fundOwnership', fundOwnership),
    ('fundOwnershipDF', fundOwnershipDF),
    ('incomeStatement', incomeStatement),
    ('incomeStatementDF', incomeStatementDF),
    ('insiderRoster', insiderRoster),
    ('insiderRosterDF', insiderRosterDF),
    ('insiderSummary', insiderSummary),
    ('insiderSummaryDF', insiderSummaryDF),
    ('insiderTransactions', insiderTransactions),
    ('insiderTransactionsDF', insiderTransactionsDF),
    ('institutionalOwnership', institutionalOwnership),
    ('institutionalOwnershipDF', institutionalOwnershipDF),
    ('intraday', intraday),
    ('intradayDF', intradayDF),
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
    ('optionExpirations', optionExpirations),
    ('options', options),
    ('optionsDF', optionsDF),
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
    ('returnOfCapital', returnOfCapital),
    ('returnOfCapitalDF', returnOfCapitalDF),
    ('rightsIssue', rightsIssue),
    ('rightsIssueDF', rightsIssueDF),
    ('rightToPurchase', rightToPurchase),
    ('rightToPurchaseDF', rightToPurchaseDF),
    ('sectorPerformance', sectorPerformance),
    ('sectorPerformanceDF', sectorPerformanceDF),
    ('securityReclassification', securityReclassification),
    ('securityReclassificationDF', securityReclassificationDF),
    ('securitySwap', securitySwap),
    ('securitySwapDF', securitySwapDF),
    ('spinoff', spinoff),
    ('spinoffDF', spinoffDF),
    ('splits', splits),
    ('splitsDF', splitsDF),
    ('stockSplits', stockSplits),
    ('stockSplitsDF', stockSplitsDF),
    ('tenQ', tenQ),
    ('tenK', tenK),
    ('timeSeriesInventory', timeSeriesInventory),
    ('timeSeriesInventoryDF', timeSeriesInventoryDF),
    ('timeSeries', timeSeries),
    ('timeSeriesDF', timeSeriesDF),
    ('upcomingEvents', upcomingEvents),
    ('upcomingEventsDF', upcomingEventsDF),
    ('upcomingEarnings', upcomingEarnings),
    ('upcomingEarningsDF', upcomingEarningsDF),
    ('upcomingDividends', upcomingDividends),
    ('upcomingDividendsDF', upcomingDividendsDF),
    ('upcomingSplits', upcomingSplits),
    ('upcomingSplitsDF', upcomingSplitsDF),
    ('upcomingIPOs', upcomingIPOs),
    ('upcomingIPOsDF', upcomingIPOsDF),
    ('volumeByVenue', volumeByVenue),
    ('volumeByVenueDF', volumeByVenueDF),
    # SSE Streaming
    ('topsSSE', topsSSE),
    ('lastSSE', lastSSE),
    ('deepSSE', deepSSE),
    ('tradesSSE', tradesSSE),
    # TOPS
    ('tops', tops),
    ('topsDF', topsDF),
    ('last', last),
    ('lastDF', lastDF),
    ('deep', deep),
    ('deepDF', deepDF),
    ('auction', auction),
    ('auctionDF', auctionDF),
    ('bookDeep', deepBook),
    ('bookDeepDF', deepBookDF),
    ('officialPrice', officialPrice),
    ('officialPriceDF', officialPriceDF),
    ('opHaltStatus', opHaltStatus),
    ('opHaltStatusDF', opHaltStatusDF),
    ('securityEvent', securityEvent),
    ('securityEventDF', securityEventDF),
    ('ssrStatus', ssrStatus),
    ('ssrStatusDF', ssrStatusDF),
    ('systemEvent', systemEvent),
    ('systemEventDF', systemEventDF),
    ('trades', trades),
    ('tradesDF', tradesDF),
    ('tradeBreak', tradeBreak),
    ('tradeBreakDF', tradeBreakDF),
    ('tradingStatus', tradingStatus),
    ('tradingStatusDF', tradingStatusDF),
    # Alternative
    ('crypto', crypto),
    ('cryptoDF', cryptoDF),
    ('sentiment', sentiment),
    ('sentimentDF', sentimentDF),
    ('ceoCompensation', ceoCompensation),
    ('ceoCompensationDF', ceoCompensationDF),
    # Data Points
    ('points', points),
    ('pointsDF', pointsDF),
    # FX
    ('latestFX', latestFX),
    ('latestFXDF', latestFXDF),
    ('convertFX', convertFX),
    ('convertFXDF', convertFXDF),
    ('historicalFX', historicalFX),
    ('historicalFXDF', historicalFXDF),
    # FXSSE
    ('fxSSE', fxSSE),
    # Crypto
    ('cryptoBook', cryptoBook),
    ('cryptoBookDF', cryptoBookDF),
    ('cryptoQuote', cryptoQuote),
    ('cryptoQuoteDF', cryptoQuoteDF),
    ('cryptoPrice', cryptoPrice),
    ('cryptoPriceDF', cryptoPriceDF),
    # CryptoSSE
    ('cryptoBookSSE', cryptoBookSSE),
    ('cryptoEventsSSE', cryptoEventsSSE),
    ('cryptoQuotesSSE', cryptoQuotesSSE),
    # Premium
    #     Wall Street Horizon
    ('analystDays', analystDays),
    ('analystDaysDF', analystDaysDF),
    ('boardOfDirectorsMeeting', boardOfDirectorsMeeting),
    ('boardOfDirectorsMeetingDF', boardOfDirectorsMeetingDF),
    ('businessUpdates', businessUpdates),
    ('businessUpdatesDF', businessUpdatesDF),
    ('buybacks', buybacks),
    ('buybacksDF', buybacksDF),
    ('capitalMarketsDay', capitalMarketsDay),
    ('capitalMarketsDayDF', capitalMarketsDayDF),
    ('companyTravel', companyTravel),
    ('companyTravelDF', companyTravelDF),
    ('filingDueDates', filingDueDates),
    ('filingDueDatesDF', filingDueDatesDF),
    ('fiscalQuarterEnd', fiscalQuarterEnd),
    ('fiscalQuarterEndDF', fiscalQuarterEndDF),
    ('forum', forum),
    ('forumDF', forumDF),
    ('generalConference', generalConference),
    ('generalConferenceDF', generalConferenceDF),
    ('fdaAdvisoryCommitteeMeetings', fdaAdvisoryCommitteeMeetings),
    ('fdaAdvisoryCommitteeMeetingsDF', fdaAdvisoryCommitteeMeetingsDF),
    ('holidaysWSH', holidaysWSH),
    ('holidaysWSHDF', holidaysWSHDF),
    ('indexChanges', indexChanges),
    ('indexChangesDF', indexChangesDF),
    ('iposWSH', iposWSH),
    ('iposWSHDF', iposWSHDF),
    ('legalActions', legalActions),
    ('legalActionsDF', legalActionsDF),
    ('mergersAndAcquisitions', mergersAndAcquisitions),
    ('mergersAndAcquisitionsDF', mergersAndAcquisitionsDF),
    ('productEventsDF', productEventsDF),
    ('productEvents', productEvents),
    ('researchAndDevelopmentDays', researchAndDevelopmentDays),
    ('researchAndDevelopmentDaysDF', researchAndDevelopmentDaysDF),
    ('sameStoreSales', sameStoreSales),
    ('sameStoreSalesDF', sameStoreSalesDF),
    ('secondaryOfferings', secondaryOfferings),
    ('secondaryOfferingsDF', secondaryOfferingsDF),
    ('seminars', seminars),
    ('seminarsDF', seminarsDF),
    ('shareholderMeetings', shareholderMeetings),
    ('shareholderMeetingsDF', shareholderMeetingsDF),
    ('summitMeetings', summitMeetings),
    ('summitMeetingsDF', summitMeetingsDF),
    ('tradeShows', tradeShows),
    ('tradeShowsDF', tradeShowsDF),
    ('witchingHours', witchingHours),
    ('witchingHoursDF', witchingHoursDF),
    ('workshops', workshops),
    ('workshopsDF', workshopsDF),
    #     Fraud Factors
    ('nonTimelyFilings', nonTimelyFilings),
    ('nonTimelyFilingsDF', nonTimelyFilingsDF),
    ('similarityIndex', similarityIndex),
    ('similarityIndexDF', similarityIndexDF),
    #     Extract Alpha
    ('cam1', cam1),
    ('cam1DF', cam1DF),
    ('esgCFPBComplaints', esgCFPBComplaints),
    ('esgCFPBComplaintsDF', esgCFPBComplaintsDF),
    ('esgCPSCRecalls', esgCPSCRecalls),
    ('esgCPSCRecallsDF', esgCPSCRecallsDF),
    ('esgDOLVisaApplications', esgDOLVisaApplications),
    ('esgDOLVisaApplicationsDF', esgDOLVisaApplicationsDF),
    ('esgEPAEnforcements', esgEPAEnforcements),
    ('esgEPAEnforcementsDF', esgEPAEnforcementsDF),
    ('esgEPAMilestones', esgEPAMilestones),
    ('esgEPAMilestonesDF', esgEPAMilestonesDF),
    ('esgFECIndividualCampaingContributions', esgFECIndividualCampaingContributions),
    ('esgFECIndividualCampaingContributionsDF', esgFECIndividualCampaingContributionsDF),
    ('esgOSHAInspections', esgOSHAInspections),
    ('esgOSHAInspectionsDF', esgOSHAInspectionsDF),
    ('esgSenateLobbying', esgSenateLobbying),
    ('esgSenateLobbyingDF', esgSenateLobbyingDF),
    ('esgUSASpending', esgUSASpending),
    ('esgUSASpendingDF', esgUSASpendingDF),
    ('esgUSPTOPatentApplications', esgUSPTOPatentApplications),
    ('esgUSPTOPatentApplicationsDF', esgUSPTOPatentApplicationsDF),
    ('esgUSPTOPatentGrants', esgUSPTOPatentGrants),
    ('esgUSPTOPatentGrantsDF', esgUSPTOPatentGrantsDF),
    ('tacticalModel1', tacticalModel1),
    ('tacticalModel1DF', tacticalModel1DF),
    #     Precision Alpha
    ('precisionAlphaPriceDynamics', precisionAlphaPriceDynamics),
    ('precisionAlphaPriceDynamicsDF', precisionAlphaPriceDynamicsDF),
    #     BRAIN Company
    ('brain30DaySentiment', brain30DaySentiment),
    ('brain30DaySentimentDF', brain30DaySentimentDF),
    ('brain7DaySentiment', brain7DaySentiment),
    ('brain7DaySentimentDF', brain7DaySentimentDF),
    ('brain21DayMLReturnRanking', brain21DayMLReturnRanking),
    ('brain21DayMLReturnRankingDF', brain21DayMLReturnRankingDF),
    ('brain10DayMLReturnRanking', brain10DayMLReturnRanking),
    ('brain10DayMLReturnRankingDF', brain10DayMLReturnRankingDF),
    ('brain5DayMLReturnRanking', brain5DayMLReturnRanking),
    ('brain5DayMLReturnRankingDF', brain5DayMLReturnRankingDF),
    ('brain3DayMLReturnRanking', brain3DayMLReturnRanking),
    ('brain3DayMLReturnRankingDF', brain3DayMLReturnRankingDF),
    ('brain2DayMLReturnRanking', brain2DayMLReturnRanking),
    ('brain2DayMLReturnRankingDF', brain2DayMLReturnRankingDF),
    ('brainLanguageMetricsOnCompanyFilingsAll', brainLanguageMetricsOnCompanyFilingsAll),
    ('brainLanguageMetricsOnCompanyFilingsAllDF', brainLanguageMetricsOnCompanyFilingsAllDF),
    ('brainLanguageMetricsOnCompanyFilings', brainLanguageMetricsOnCompanyFilings),
    ('brainLanguageMetricsOnCompanyFilingsDF', brainLanguageMetricsOnCompanyFilingsDF),
    ('brainLanguageMetricsOnCompanyFilingsDifferenceAll', brainLanguageMetricsOnCompanyFilingsDifferenceAll),
    ('brainLanguageMetricsOnCompanyFilingsDifferenceAllDF', brainLanguageMetricsOnCompanyFilingsDifferenceAllDF),
    ('brainLanguageMetricsOnCompanyFilingsDifference', brainLanguageMetricsOnCompanyFilingsDifference),
    ('brainLanguageMetricsOnCompanyFilingsDifferenceDF', brainLanguageMetricsOnCompanyFilingsDifferenceDF),
    #     Kavout
    ('kScore', kScore),
    ('kScoreDF', kScoreDF),
    #     Audit Analytics
    ('accountingQualityAndRiskMatrix', accountingQualityAndRiskMatrix),
    ('accountingQualityAndRiskMatrixDF', accountingQualityAndRiskMatrixDF),
    ('directorAndOfficerChanges', directorAndOfficerChanges),
    ('directorAndOfficerChangesDF', directorAndOfficerChangesDF),
    #     ValuEngine
    ('valuEngineStockResearchReport', valuEngineStockResearchReport),
]

_INCLUDE_POINTS = [
    # Rates
    ('thirtyYear', RatesPoints.THIRTY.value),
    ('twentyYear', RatesPoints.TWENTY.value),
    ('tenYear', RatesPoints.TEN.value),
    ('fiveYear', RatesPoints.FIVE.value),
    ('twoYear', RatesPoints.TWO.value),
    ('oneYear', RatesPoints.ONE.value),
    ('sixMonth', RatesPoints.SIXMONTH.value),
    ('threeMonth', RatesPoints.THREEMONTH.value),
    ('oneMonth', RatesPoints.ONEMONTH.value),
    # Commodities
    ('wti', CommoditiesPoints.WTI.value),
    ('brent', CommoditiesPoints.BRENT.value),
    ('natgas', CommoditiesPoints.NATGAS.value),
    ('heatoil', CommoditiesPoints.HEATOIL.value),
    ('jet', CommoditiesPoints.JET.value),
    ('diesel', CommoditiesPoints.DIESEL.value),
    ('gasreg', CommoditiesPoints.GASREG.value),
    ('gasmid', CommoditiesPoints.GASMID.value),
    ('gasprm', CommoditiesPoints.GASPRM.value),
    ('propane', CommoditiesPoints.PROPANE.value),
    # Economic
    ('us30', EconomicPoints.US30.value),
    ('us15', EconomicPoints.US15.value),
    ('us5', EconomicPoints.US5.value),
    ('fedfunds', EconomicPoints.FEDFUNDS.value),
    ('creditcard', EconomicPoints.CREDITCARD.value),
    ('cdnj', EconomicPoints.CDNJ.value),
    ('cdj', EconomicPoints.CDJ.value),
    ('gdp', EconomicPoints.GDP.value),
    ('indpro', EconomicPoints.INDPRO.value),
    ('cpi', EconomicPoints.CPI.value),
    ('payroll', EconomicPoints.PAYROLL.value),
    ('housing', EconomicPoints.HOUSING.value),
    ('unemployment', EconomicPoints.UNEMPLOYMENT.value),
    ('vehicles', EconomicPoints.VEHICLES.value),
    ('recessionProb', EconomicPoints.RECESSION_PROB.value),
    ('initialClaims', EconomicPoints.INITIALCLAIMS.value),
    ('institutionalMoney', EconomicPoints.INSTITUTIONALMONEY.value),
    ('retailMoney', EconomicPoints.RETAILMONEY.value),

]

_INCLUDE_STUDIES = [
    ('peerCorrelation', peerCorrelation),
    ('bollinger', bollinger),
    ('dema', dema),
    ('ema', ema),
    ('sar', sar),
    ('sma', sma),
]


class Client(object):
    '''IEX Cloud Client

    Client has access to all methods provided as standalone, but in an authenticated way

    Args:
        api_token (string): api token (can pickup from IEX_TOKEN environment variable)
        version (string): api version to use (defaults to v1)
                          set version to 'sandbox' to run against the IEX sandbox
        api_limit (int): cache calls in this interval
    '''
    _api_limit = DEFAULT_API_LIMIT

    def __init__(self,
                 api_token=None,
                 version='v1',
                 api_limit=DEFAULT_API_LIMIT):
        self._token = api_token or os.environ.get('IEX_TOKEN', '')
        if not self._token:
            raise PyEXception('API Token missing or not in environment (IEX_TOKEN)')

        if version not in ('beta', 'v1', 'sandbox'):
            raise PyEXception('Unrecognized api version: {}'.format(version))

        if self._token.startswith('T') and version != 'sandbox':
            raise PyEXception('Using test key but attempting to connect to non-sandbox environment')

        self._version = version
        self._api_limit = api_limit

        # rebind
        for name, method in _INCLUDE_FUNCTIONS:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__

        for name, key in _INCLUDE_POINTS:
            p = partial(self.bind, meth=points, key=key)
            p.__name__ = key
            setattr(self, name, wraps(points)(_interval(minutes=self._api_limit)(p)))
            getattr(self, name).__doc__ = points.__doc__

        for name, method in _INCLUDE_STUDIES:
            if method:
                setattr(self, name, method.__get__(self, self.__class__))

    def bind(self, *args, **kwargs):
        meth = kwargs.pop('meth')
        if not meth:
            raise PyEXception('Must provide method!')
        return meth(token=self._token, version=self._version, *args, **kwargs)

    def account(self):
        return _getJson('account/metadata', self._token, self._version)

    def usage(self, type=None):
        if type:
            if type not in _USAGE_TYPES:
                raise PyEXception('type not recognized: {}'.format(type))
            return _getJson('account/usage/{type}'.format(type=type), self._token, self._version)
        return _getJson('account/usage/messages', self._token, self._version)


#############################
# for autodoc
for name, method in _INCLUDE_FUNCTIONS:
    setattr(Client, name, method)
    getattr(Client, name).__doc__ = method.__doc__

for name, key in _INCLUDE_POINTS:
    p = partial(Client.bind, meth=points, key=key)
    p.__name__ = key
    setattr(Client, name, wraps(points)(p))
    getattr(Client, name).__doc__ = points.__doc__

for name, method in _INCLUDE_STUDIES:
    if method:
        setattr(Client, name, method)
