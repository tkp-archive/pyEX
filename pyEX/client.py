# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import os
import types
from functools import partial, wraps
import warnings

from .account import (
    messageBudget,
    messageBudgetAsync,
    metadata,
    metadataAsync,
    metadataDF,
    usage,
    usageAsync,
    usageDF,
    status,
    statusAsync,
    payAsYouGo,
    payAsYouGoAsync,
    getWatchlist,
    getWatchlistDF,
    createWatchlist,
    addToWatchlist,
    deleteFromWatchlist,
    deleteWatchlist,
)
from .alternative import sentiment, sentimentDF, sentimentAsync
from .commodities import (
    CommoditiesPoints,
    brent,
    brentAsync,
    brentDF,
    diesel,
    dieselAsync,
    dieselDF,
    gasmid,
    gasmidAsync,
    gasmidDF,
    gasprm,
    gasprmAsync,
    gasprmDF,
    gasreg,
    gasregAsync,
    gasregDF,
    heatoil,
    heatoilAsync,
    heatoilDF,
    jet,
    jetAsync,
    jetDF,
    natgas,
    natgasAsync,
    natgasDF,
    propane,
    propaneAsync,
    propaneDF,
    wti,
    wtiAsync,
    wtiDF,
)
from .common import PyEXception, _interval
from .cryptocurrency import (
    cryptoBook,
    cryptoBookAsync,
    cryptoBookDF,
    cryptoPrice,
    cryptoPriceAsync,
    cryptoPriceDF,
    cryptoQuote,
    cryptoQuoteAsync,
    cryptoQuoteDF,
)
from .economic import (
    EconomicPoints,
    cpi,
    cpiAsync,
    cpiDF,
    fedfunds,
    fedfundsAsync,
    fedfundsDF,
    gdp,
    gdpAsync,
    gdpDF,
    housing,
    housingAsync,
    housingDF,
    indpro,
    indproAsync,
    indproDF,
    initialClaims,
    initialClaimsAsync,
    initialClaimsDF,
    institutionalMoney,
    institutionalMoneyAsync,
    institutionalMoneyDF,
    payroll,
    payrollAsync,
    payrollDF,
    recessionProb,
    recessionProbAsync,
    recessionProbDF,
    retailMoney,
    retailMoneyAsync,
    retailMoneyDF,
    unemployment,
    unemploymentAsync,
    unemploymentDF,
    vehicles,
    vehiclesAsync,
    vehiclesDF,
)

from .files import download, files
from .futures import futures, futuresDF
from .fx import (
    convertFX,
    convertFXDF,
    historicalFX,
    historicalFXDF,
    latestFX,
    latestFXDF,
)
from .markets import markets, marketsDF
from .metadata import queryMetadata, queryMetadataDF
from .mortgage import (
    MortgagePoints,
    us5,
    us5DF,
    us15,
    us15DF,
    us30,
    us30DF,
)
from .options import optionExpirations, options, optionsDF, stockOptions, stockOptionsDF
from .points import points, pointsDF
from .platform import (
    createDataset,
    createDatasetAsync,
    deleteData,
    deleteDataAsync,
    deleteDataset,
    deleteDatasetAsync,
    listDatasets,
    listDatasetsAsync,
    listDatasetsDF,
    listJobs,
    loadData,
    loadDataAsync,
    modifyDataset,
    modifyDatasetAsync,
    modifyData,
    modifyDataAsync,
    query,
    queryAsync,
    queryDF,
    queryMeta,
    queryMetaAsync,
    queryMetaDF,
)
from .premium import (
    accountingQualityAndRiskMatrixAuditAnalytics,
    accountingQualityAndRiskMatrixAuditAnalyticsDF,
    analystDaysWallStreetHorizon,
    analystDaysWallStreetHorizonDF,
    analystRecommendationsAndPriceTargetsInvisage,
    analystRecommendationsAndPriceTargetsInvisageDF,
    analystRecommendationsRefinitiv,
    analystRecommendationsRefinitivDF,
    boardOfDirectorsMeetingWallStreetHorizon,
    boardOfDirectorsMeetingWallStreetHorizonDF,
    businessUpdatesWallStreetHorizon,
    businessUpdatesWallStreetHorizonDF,
    buybacksWallStreetHorizon,
    buybacksWallStreetHorizonDF,
    cam1ExtractAlpha,
    cam1ExtractAlphaDF,
    capitalMarketsDayWallStreetHorizon,
    capitalMarketsDayWallStreetHorizonDF,
    companyTravelWallStreetHorizon,
    companyTravelWallStreetHorizonDF,
    directorAndOfficerChangesAuditAnalytics,
    directorAndOfficerChangesAuditAnalyticsDF,
    downloadReportNewConstructs,
    downloadStockResearchReportValuEngine,
    earningsRefinitiv,
    earningsRefinitivDF,
    esgCFPBComplaintsExtractAlpha,
    esgCFPBComplaintsExtractAlphaDF,
    esgCPSCRecallsExtractAlpha,
    esgCPSCRecallsExtractAlphaDF,
    esgDOLVisaApplicationsExtractAlpha,
    esgDOLVisaApplicationsExtractAlphaDF,
    esgEPAEnforcementsExtractAlpha,
    esgEPAEnforcementsExtractAlphaDF,
    esgEPAMilestonesExtractAlpha,
    esgEPAMilestonesExtractAlphaDF,
    esgFECIndividualCampaingContributionsExtractAlpha,
    esgFECIndividualCampaingContributionsExtractAlphaDF,
    esgOSHAInspectionsExtractAlpha,
    esgOSHAInspectionsExtractAlphaDF,
    esgSenateLobbyingExtractAlpha,
    esgSenateLobbyingExtractAlphaDF,
    esgUSASpendingExtractAlpha,
    esgUSASpendingExtractAlphaDF,
    esgUSPTOPatentApplicationsExtractAlpha,
    esgUSPTOPatentApplicationsExtractAlphaDF,
    esgUSPTOPatentGrantsExtractAlpha,
    esgUSPTOPatentGrantsExtractAlphaDF,
    estimatesRefinitiv,
    estimatesRefinitivDF,
    fdaAdvisoryCommitteeMeetingsWallStreetHorizon,
    fdaAdvisoryCommitteeMeetingsWallStreetHorizonDF,
    filingDueDatesWallStreetHorizon,
    filingDueDatesWallStreetHorizonDF,
    fiscalQuarterEndWallStreetHorizon,
    fiscalQuarterEndWallStreetHorizonDF,
    fiveDayMLReturnRankingBrain,
    fiveDayMLReturnRankingBrainDF,
    forumWallStreetHorizon,
    forumWallStreetHorizonDF,
    generalConferenceWallStreetHorizon,
    generalConferenceWallStreetHorizonDF,
    holidaysWallStreetHorizon,
    holidaysWallStreetHorizonDF,
    indexChangesWallStreetHorizon,
    indexChangesWallStreetHorizonDF,
    iposWallStreetHorizon,
    iposWallStreetHorizonDF,
    kScoreChinaKavout,
    kScoreChinaKavoutDF,
    kScoreKavout,
    kScoreKavoutDF,
    languageMetricsOnCompanyFilingsAllBrain,
    languageMetricsOnCompanyFilingsAllBrainDF,
    languageMetricsOnCompanyFilingsBrain,
    languageMetricsOnCompanyFilingsBrainDF,
    languageMetricsOnCompanyFilingsDifferenceAllBrain,
    languageMetricsOnCompanyFilingsDifferenceAllBrainDF,
    languageMetricsOnCompanyFilingsDifferenceBrain,
    languageMetricsOnCompanyFilingsDifferenceBrainDF,
    legalActionsWallStreetHorizon,
    legalActionsWallStreetHorizonDF,
    mergersAndAcquisitionsWallStreetHorizon,
    mergersAndAcquisitionsWallStreetHorizonDF,
    newsCityFalcon,
    newsCityFalconDF,
    nonTimelyFilingsFraudFactors,
    nonTimelyFilingsFraudFactorsDF,
    priceDynamicsPrecisionAlpha,
    priceDynamicsPrecisionAlphaDF,
    priceTargetRefinitiv,
    priceTargetRefinitivDF,
    productEventsWallStreetHorizon,
    productEventsWallStreetHorizonDF,
    reportNewConstructs,
    researchAndDevelopmentDaysWallStreetHorizon,
    researchAndDevelopmentDaysWallStreetHorizonDF,
    sameStoreSalesWallStreetHorizon,
    sameStoreSalesWallStreetHorizonDF,
    secondaryOfferingsWallStreetHorizon,
    secondaryOfferingsWallStreetHorizonDF,
    seminarsWallStreetHorizon,
    seminarsWallStreetHorizonDF,
    sevenDaySentimentBrain,
    sevenDaySentimentBrainDF,
    shareholderMeetingsWallStreetHorizon,
    shareholderMeetingsWallStreetHorizonDF,
    socialSentimentStockTwits,
    socialSentimentStockTwitsDF,
    stockResearchReportValuEngine,
    summitMeetingsWallStreetHorizon,
    summitMeetingsWallStreetHorizonDF,
    tacticalModel1ExtractAlpha,
    tacticalModel1ExtractAlphaDF,
    tenDayMLReturnRankingBrain,
    tenDayMLReturnRankingBrainDF,
    thirtyDaySentimentBrain,
    thirtyDaySentimentBrainDF,
    threeDayMLReturnRankingBrain,
    threeDayMLReturnRankingBrainDF,
    tradeShowsWallStreetHorizon,
    tradeShowsWallStreetHorizonDF,
    twentyOneDayMLReturnRankingBrain,
    twentyOneDayMLReturnRankingBrainDF,
    twoDayMLReturnRankingBrain,
    twoDayMLReturnRankingBrainDF,
    witchingHoursWallStreetHorizon,
    witchingHoursWallStreetHorizonDF,
    workshopsWallStreetHorizon,
    workshopsWallStreetHorizonDF,
)
from .rates import (
    RatesPoints,
    cdj,
    cdjDF,
    cdnj,
    cdnjDF,
    creditcard,
    creditcardDF,
)
from .treasuries import (
    TreasuriesPoints,
    thirtyYear,
    thirtyYearDF,
    twentyYear,
    twentyYearDF,
    tenYear,
    tenYearDF,
    sevenYear,
    sevenYearDF,
    fiveYear,
    fiveYearDF,
    threeYear,
    threeYearDF,
    twoYear,
    twoYearDF,
    oneYear,
    oneYearDF,
    sixMonth,
    sixMonthDF,
    threeMonth,
    threeMonthDF,
    oneMonth,
    oneMonthDF,
)
from .refdata import (
    calendar,
    calendarDF,
    corporateActions,
    corporateActionsDF,
    cryptoSymbols,
    cryptoSymbolsDF,
    cryptoSymbolsList,
    directory,
    directoryDF,
    exchanges,
    exchangesDF,
    figi,
    figiDF,
    futuresSymbols,
    futuresSymbolsDF,
    futuresSymbolsList,
    fxSymbols,
    fxSymbolsDF,
    fxSymbolsList,
    holidays,
    holidaysDF,
    iexSymbols,
    iexSymbolsDF,
    iexSymbolsList,
    internationalExchanges,
    internationalExchangesDF,
    internationalSymbols,
    internationalSymbolsDF,
    internationalSymbolsList,
    isinLookup,
    isinLookupDF,
    mutualFundSymbols,
    mutualFundSymbolsDF,
    mutualFundSymbolsList,
    nextDayExtDate,
    nextDayExtDateDF,
    optionsSymbols,
    optionsSymbolsDF,
    optionsSymbolsList,
    otcSymbols,
    otcSymbolsDF,
    otcSymbolsList,
    refDividends,
    refDividendsDF,
    ricLookup,
    ricLookupDF,
    search,
    searchDF,
    sectors,
    sectorsDF,
    symbols,
    symbolsDF,
    symbolsList,
    tags,
    tagsDF,
)
from .rules import (
    createRule,
    deleteRule,
    lookupRule,
    ruleOutput,
    pauseRule,
    resumeRule,
    ruleInfo,
    rules,
)
from .stats import (
    daily,
    dailyDF,
    recent,
    recentDF,
    records,
    recordsDF,
    stats,
    statsDF,
    summary,
    summaryDF,
)
from .stocks import (
    advancedStats,
    advancedStatsDF,
    analystRecommendations,
    analystRecommendationsDF,
    balanceSheet,
    balanceSheetDF,
    batch,
    batchDF,
    bonusIssue,
    bonusIssueDF,
    book,
    bookDF,
    cashFlow,
    cashFlowDF,
    ceoCompensation,
    ceoCompensationDF,
    chart,
    chartDF,
    collections,
    collectionsDF,
    company,
    companyDF,
    delayedQuote,
    delayedQuoteDF,
    distribution,
    distributionDF,
    dividends,
    dividendsBasic,
    dividendsBasicDF,
    dividendsDF,
    dividendsForecast,
    dividendsForecastDF,
    earnings,
    earningsDF,
    earningsToday,
    earningsTodayDF,
    estimates,
    estimatesDF,
    financials,
    financialsDF,
    fortyF,
    fundamentals,
    fundamentalsDF,
    fundamentalValuations,
    fundamentalValuationsDF,
    fundOwnership,
    fundOwnershipDF,
    iexAuction,
    iexAuctionAsync,
    iexAuctionDF,
    iexBook,
    iexBookAsync,
    iexBookDF,
    iexDeep,
    iexDeepAsync,
    iexDeepDF,
    iexHist,
    iexHistAsync,
    iexHistDF,
    iexLast,
    iexLastAsync,
    iexLastDF,
    iexOfficialPrice,
    iexOfficialPriceAsync,
    iexOfficialPriceDF,
    iexOpHaltStatus,
    iexOpHaltStatusAsync,
    iexOpHaltStatusDF,
    iexSecurityEvent,
    iexSecurityEventAsync,
    iexSecurityEventDF,
    iexSsrStatus,
    iexSsrStatusAsync,
    iexSsrStatusDF,
    iexSystemEvent,
    iexSystemEventAsync,
    iexSystemEventDF,
    iexThreshold,
    iexThresholdDF,
    iexTops,
    iexTopsAsync,
    iexTopsDF,
    iexTradeBreak,
    iexTradeBreakAsync,
    iexTradeBreakDF,
    iexTrades,
    iexTradesAsync,
    iexTradesDF,
    iexTradingStatus,
    iexTradingStatusAsync,
    iexTradingStatusDF,
    incomeStatement,
    incomeStatementDF,
    insiderRoster,
    insiderRosterDF,
    insiderSummary,
    insiderSummaryDF,
    insiderTransactions,
    insiderTransactionsDF,
    institutionalOwnership,
    institutionalOwnershipDF,
    intraday,
    intradayDF,
    ipoToday,
    ipoTodayDF,
    ipoUpcoming,
    ipoUpcomingDF,
    keyStats,
    keyStatsDF,
    largestTrades,
    largestTradesDF,
    list,
    listDF,
    logo,
    logoNotebook,
    logoPNG,
    marketNews,
    marketNewsDF,
    marketOhlc,
    marketOhlcDF,
    marketPrevious,
    marketPreviousDF,
    marketShortInterest,
    marketShortInterestDF,
    marketVolume,
    marketVolumeDF,
    marketYesterday,
    marketYesterdayDF,
    news,
    newsDF,
    ohlc,
    ohlcDF,
    peers,
    peersDF,
    previous,
    previousDF,
    price,
    priceDF,
    priceTarget,
    priceTargetDF,
    quote,
    quoteDF,
    relevant,
    relevantDF,
    returnOfCapital,
    returnOfCapitalDF,
    rightsIssue,
    rightsIssueDF,
    rightToPurchase,
    rightToPurchaseDF,
    sectorPerformance,
    sectorPerformanceDF,
    securityReclassification,
    securityReclassificationDF,
    securitySwap,
    securitySwapDF,
    shortInterest,
    shortInterestDF,
    spinoff,
    spinoffDF,
    splits,
    splitsDF,
    splitsBasic,
    splitsBasicDF,
    spread,
    spreadDF,
    technicals,
    technicalsDF,
    tenK,
    tenQ,
    twentyF,
    upcomingDividends,
    upcomingDividendsDF,
    upcomingEarnings,
    upcomingEarningsDF,
    upcomingEvents,
    upcomingEventsDF,
    upcomingIPOs,
    upcomingIPOsDF,
    upcomingSplits,
    upcomingSplitsDF,
    volumeByVenue,
    volumeByVenueDF,
    yesterday,
    yesterdayDF,
)
from .streaming.cryptocurrency import (
    cryptoBookSSE,
    cryptoBookSSEAsync,
    cryptoEventsSSE,
    cryptoEventsSSEAsync,
    cryptoQuotesSSE,
    cryptoQuotesSSEAsync,
)
from .streaming.fx import (
    forex1MinuteSSE,
    forex1MinuteSSEAsync,
    forex1SecondSSE,
    forex1SecondSSEAsync,
    forex5SecondSSE,
    forex5SecondSSEAsync,
    fxSSE,
    fxSSEAsync,
)
from .streaming.news import newsSSE, newsSSEAsync
from .streaming.sentiment import sentimentSSE, sentimentSSEAsync
from .streaming.sse import (
    iexDeepSSE,
    iexDeepSSEAsync,
    iexLastSSE,
    iexLastSSEAsync,
    iexTopsSSE,
    iexTopsSSEAsync,
    iexTradesSSE,
    iexTradesSSEAsync,
)
from .streaming.stock import (
    stocksUS1MinuteSSE,
    stocksUS1MinuteSSEAsync,
    stocksUS1SecondSSE,
    stocksUS1SecondSSEAsync,
    stocksUS5SecondSSE,
    stocksUS5SecondSSEAsync,
    stocksUSNoUTP1MinuteSSE,
    stocksUSNoUTP1MinuteSSEAsync,
    stocksUSNoUTP1SecondSSE,
    stocksUSNoUTP1SecondSSEAsync,
    stocksUSNoUTP5SecondSSE,
    stocksUSNoUTP5SecondSSEAsync,
    stocksUSNoUTPSSE,
    stocksUSNoUTPSSEAsync,
    stocksUSSSE,
    stocksUSSSEAsync,
)

from .timeseries import (
    timeSeries,
    timeSeriesAsync,
    timeSeriesDF,
    timeSeriesInventory,
    timeSeriesInventoryAsync,
    timeSeriesInventoryDF,
)

from .studies import (
    acos,
    ad,
    add,
    adosc,
    adx,
    adxr,
    apo,
    aroon,
    aroonosc,
    asin,
    atan,
    atr,
    avgprice,
    beta,
    bollinger,
    bop,
    cci,
    cdl2crows,
    cdl3blackcrows,
    cdl3inside,
    cdl3linestrike,
    cdl3outside,
    cdl3starsinsouth,
    cdl3whitesoldiers,
    cdlabandonedbaby,
    cdladvanceblock,
    cdlbelthold,
    cdlbreakaway,
    cdlclosingmarubozu,
    cdlconcealbabyswallow,
    cdlcounterattack,
    cdldarkcloudcover,
    cdldoji,
    cdldojistar,
    cdldragonflydoji,
    cdlengulfing,
    cdleveningdojistar,
    cdleveningstar,
    cdlgapsidesidewhite,
    cdlgravestonedoji,
    cdlhammer,
    cdlhangingman,
    cdlharami,
    cdlharamicross,
    cdlhighwave,
    cdlhikkake,
    cdlhikkakemod,
    cdlhomingpigeon,
    cdlidentical3crows,
    cdlinneck,
    cdlinvertedhammer,
    cdlkicking,
    cdlkickingbylength,
    cdlladderbottom,
    cdllongleggeddoji,
    cdllongline,
    cdlmarubozu,
    cdlmatchinglow,
    cdlmathold,
    cdlmorningdojistar,
    cdlmorningstar,
    cdlonneck,
    cdlpiercing,
    cdlrickshawman,
    cdlrisefall3methods,
    cdlseparatinglines,
    cdlshootingstar,
    cdlshortline,
    cdlspinningtop,
    cdlstalledpattern,
    cdlsticksandwich,
    cdltakuri,
    cdltasukigap,
    cdlthrusting,
    cdltristar,
    cdlunique3river,
    cdlxsidegap3methods,
    ceil,
    cmo,
    correl,
    cos,
    cosh,
    dailyReturns,
    dema,
    div,
    dx,
    ema,
    exp,
    floor,
    ht_dcperiod,
    ht_dcphase,
    ht_phasor,
    ht_sine,
    ht_trendline,
    ht_trendmode,
    kama,
    linearreg,
    linearreg_angle,
    linearreg_intercept,
    linearreg_slope,
    ln,
    log10,
    macd,
    macdext,
    mama,
    mavp,
    max,
    maxindex,
    medprice,
    mfi,
    midpice,
    midpoint,
    min,
    minindex,
    minmax,
    minmaxindex,
    minus_di,
    minus_dm,
    mom,
    mult,
    natr,
    obv,
    peerCorrelation,
    peerCorrelationPlot,
    plus_di,
    plus_dm,
    ppo,
    returns,
    roc,
    rocp,
    rocr,
    rocr100,
    rsi,
    sar,
    sarext,
    sin,
    sinh,
    sma,
    sqrt,
    stddev,
    stoch,
    stochf,
    stochrsi,
    sub,
    sum,
    t3,
    tan,
    tanh,
    tema,
    trange,
    trima,
    trix,
    tsf,
    typprice,
    ultosc,
    var,
    wclprice,
    willr,
    wma,
    yieldCurve,
)

DEFAULT_API_LIMIT = 5

_INCLUDE_FUNCTIONS_PLATFORM = [
    # Platform
    ("createDataset", createDataset),
    ("createDatasetAsync", createDatasetAsync),
    ("deleteData", deleteData),
    ("deleteDataAsync", deleteDataAsync),
    ("deleteDataset", deleteDataset),
    ("deleteDatasetAsync", deleteDatasetAsync),
    ("listDatasets", listDatasets),
    ("listDatasetsAsync", listDatasetsAsync),
    ("listDatasetsDF", listDatasetsDF),
    ("listJobs", listJobs),
    ("loadData", loadData),
    ("loadDataAsync", loadDataAsync),
    ("modifyDataset", modifyDataset),
    ("modifyDatasetAsync", modifyDatasetAsync),
    ("modifyData", modifyData),
    ("modifyDataAsync", modifyDataAsync),
    ("query", query),
    ("queryAsync", queryAsync),
    ("queryDF", queryDF),
    ("queryMeta", queryMeta),
    ("queryMetaAsync", queryMetaAsync),
    ("queryMetaDF", queryMetaDF),
]

_INCLUDE_FUNCTIONS_RULES = [
    # Rules
    ("schema", lookupRule),
    ("listRules", rules),
    ("createRule", createRule),
    ("lookupRule", lookupRule),
    ("pauseRule", pauseRule),
    ("resumeRule", resumeRule),
    ("deleteRule", deleteRule),
    ("ruleInfo", ruleInfo),
    ("ruleOutput", ruleOutput),
]

_INCLUDE_FUNCTIONS_REFDATA = [
    # Refdata
    ("symbols", symbols),
    ("iexSymbols", iexSymbols),
    ("mutualFundSymbols", mutualFundSymbols),
    ("otcSymbols", otcSymbols),
    ("internationalSymbols", internationalSymbols),
    ("fxSymbols", fxSymbols),
    ("optionsSymbols", optionsSymbols),
    ("cryptoSymbols", cryptoSymbols),
    ("futuresSymbols", futuresSymbols),
    ("symbolsDF", symbolsDF),
    ("iexSymbolsDF", iexSymbolsDF),
    ("mutualFundSymbolsDF", mutualFundSymbolsDF),
    ("otcSymbolsDF", otcSymbolsDF),
    ("internationalSymbolsDF", internationalSymbolsDF),
    ("fxSymbolsDF", fxSymbolsDF),
    ("optionsSymbolsDF", optionsSymbolsDF),
    ("cryptoSymbolsDF", cryptoSymbolsDF),
    ("futuresSymbolsDF", futuresSymbolsDF),
    ("symbolsList", symbolsList),
    ("iexSymbolsList", iexSymbolsList),
    ("mutualFundSymbolsList", mutualFundSymbolsList),
    ("otcSymbolsList", otcSymbolsList),
    ("internationalSymbolsList", internationalSymbolsList),
    ("fxSymbolsList", fxSymbolsList),
    ("optionsSymbolsList", optionsSymbolsList),
    ("cryptoSymbolsList", cryptoSymbolsList),
    ("futuresSymbolsList", futuresSymbolsList),
    ("isinLookup", isinLookup),
    ("isinLookupDF", isinLookupDF),
    ("ricLookup", ricLookup),
    ("ricLookupDF", ricLookupDF),
    ("corporateActions", corporateActions),
    ("corporateActionsDF", corporateActionsDF),
    ("refDividends", refDividends),
    ("refDividendsDF", refDividendsDF),
    ("nextDayExtDate", nextDayExtDate),
    ("nextDayExtDateDF", nextDayExtDateDF),
    ("directory", directory),
    ("directoryDF", directoryDF),
    ("calendar", calendar),
    ("calendarDF", calendarDF),
    ("holidays", holidays),
    ("holidaysDF", holidaysDF),
    ("exchanges", exchanges),
    ("exchangesDF", exchangesDF),
    ("figi", figi),
    ("figiDF", figiDF),
    ("internationalExchanges", internationalExchanges),
    ("internationalExchangesDF", internationalExchangesDF),
    ("sectors", sectors),
    ("sectorsDF", sectorsDF),
    ("search", search),
    ("searchDF", searchDF),
    ("tags", tags),
    ("tagsDF", tagsDF),
    # Metadata
    # TODO move?
    ("queryMetadata", queryMetadata),
    ("queryMetadataDF", queryMetadataDF),
]

_INCLUDE_FUNCTIONS_MARKET = [
    # Markets
    ("markets", markets),
    ("marketsDF", marketsDF),
    ("marketVolume", marketVolume),
    ("marketVolumeDF", marketVolumeDF),
    ("marketShortInterest", marketShortInterest),
    ("marketShortInterestDF", marketShortInterestDF),
    ("marketNews", marketNews),
    ("marketNewsDF", marketNewsDF),
    ("marketOhlc", marketOhlc),
    ("marketOhlcDF", marketOhlcDF),
    ("marketPrevious", marketPrevious),
    ("marketPreviousDF", marketPreviousDF),
    ("marketYesterday", marketYesterday),
    ("marketYesterdayDF", marketYesterdayDF),
    ("sectorPerformance", sectorPerformance),
    ("sectorPerformanceDF", sectorPerformanceDF),
]

_INCLUDE_FUNCTIONS_STATS = [
    # Stats
    ("systemStats", stats),
    ("systemStatsDF", statsDF),
    ("recent", recent),
    ("recentDF", recentDF),
    ("records", records),
    ("recordsDF", recordsDF),
    ("summary", summary),
    ("summaryDF", summaryDF),
    ("daily", daily),
    ("dailyDF", dailyDF),
]

_INCLUDE_FUNCTIONS_STOCKS = [
    # Stocks
    ("advancedStats", advancedStats),
    ("advancedStatsDF", advancedStatsDF),
    ("analystRecommendations", analystRecommendations),
    ("analystRecommendationsDF", analystRecommendationsDF),
    ("balanceSheet", balanceSheet),
    ("balanceSheetDF", balanceSheetDF),
    ("batch", batch),
    ("batchDF", batchDF),
    ("bonusIssue", bonusIssue),
    ("bonusIssueDF", bonusIssueDF),
    ("book", book),
    ("bookDF", bookDF),
    ("cashFlow", cashFlow),
    ("cashFlowDF", cashFlowDF),
    ("ceoCompensation", ceoCompensation),
    ("ceoCompensationDF", ceoCompensationDF),
    ("chart", chart),
    ("chartDF", chartDF),
    ("company", company),
    ("companyDF", companyDF),
    ("collections", collections),
    ("collectionsDF", collectionsDF),
    ("delayedQuote", delayedQuote),
    ("delayedQuoteDF", delayedQuoteDF),
    ("distribution", distribution),
    ("distributionDF", distributionDF),
    ("dividends", dividends),
    ("dividendsBasic", dividendsBasic),
    ("dividendsDF", dividendsDF),
    ("dividendsBasicDF", dividendsBasicDF),
    ("dividendsForecast", dividendsForecast),
    ("dividendsForecastDF", dividendsForecastDF),
    ("earnings", earnings),
    ("earningsDF", earningsDF),
    ("earningsToday", earningsToday),
    ("earningsTodayDF", earningsTodayDF),
    ("spread", spread),
    ("spreadDF", spreadDF),
    ("financials", financials),
    ("financialsDF", financialsDF),
    ("fundOwnership", fundOwnership),
    ("fundOwnershipDF", fundOwnershipDF),
    ("fundamentals", fundamentals),
    ("fundamentalsDF", fundamentalsDF),
    ("fundamentalValuations", fundamentalValuations),
    ("fundamentalValuationsDF", fundamentalValuationsDF),
    ("incomeStatement", incomeStatement),
    ("incomeStatementDF", incomeStatementDF),
    ("insiderRoster", insiderRoster),
    ("insiderRosterDF", insiderRosterDF),
    ("insiderSummary", insiderSummary),
    ("insiderSummaryDF", insiderSummaryDF),
    ("insiderTransactions", insiderTransactions),
    ("insiderTransactionsDF", insiderTransactionsDF),
    ("institutionalOwnership", institutionalOwnership),
    ("institutionalOwnershipDF", institutionalOwnershipDF),
    ("intraday", intraday),
    ("intradayDF", intradayDF),
    ("ipoToday", ipoToday),
    ("ipoTodayDF", ipoTodayDF),
    ("ipoUpcoming", ipoUpcoming),
    ("ipoUpcomingDF", ipoUpcomingDF),
    ("shortInterest", shortInterest),
    ("shortInterestDF", shortInterestDF),
    ("estimates", estimates),
    ("estimatesDF", estimatesDF),
    ("keyStats", keyStats),
    ("keyStatsDF", keyStatsDF),
    ("largestTrades", largestTrades),
    ("largestTradesDF", largestTradesDF),
    ("list", list),
    ("listDF", listDF),
    ("logo", logo),
    ("logoPNG", logoPNG),
    ("logoNotebook", logoNotebook),
    ("news", news),
    ("newsDF", newsDF),
    ("ohlc", ohlc),
    ("ohlcDF", ohlcDF),
    ("optionExpirations", optionExpirations),
    ("stockOptions", stockOptions),
    ("stockOptionsDF", stockOptionsDF),
    ("peers", peers),
    ("peersDF", peersDF),
    ("previous", previous),
    ("previousDF", previousDF),
    ("yesterday", yesterday),
    ("yesterdayDF", yesterdayDF),
    ("price", price),
    ("priceDF", priceDF),
    ("priceTarget", priceTarget),
    ("priceTargetDF", priceTargetDF),
    ("quote", quote),
    ("quoteDF", quoteDF),
    ("relevant", relevant),
    ("relevantDF", relevantDF),
    ("returnOfCapital", returnOfCapital),
    ("returnOfCapitalDF", returnOfCapitalDF),
    ("rightsIssue", rightsIssue),
    ("rightsIssueDF", rightsIssueDF),
    ("rightToPurchase", rightToPurchase),
    ("rightToPurchaseDF", rightToPurchaseDF),
    ("securityReclassification", securityReclassification),
    ("securityReclassificationDF", securityReclassificationDF),
    ("securitySwap", securitySwap),
    ("securitySwapDF", securitySwapDF),
    ("spinoff", spinoff),
    ("spinoffDF", spinoffDF),
    ("splits", splits),
    ("splitsDF", splitsDF),
    ("splitsBasic", splitsBasic),
    ("splitsBasicDF", splitsBasicDF),
    ("tenQ", tenQ),
    ("tenK", tenK),
    ("twentyF", twentyF),
    ("fortyF", fortyF),
    ("technicals", technicals),
    ("technicalsDF", technicalsDF),
    ("upcomingEvents", upcomingEvents),
    ("upcomingEventsDF", upcomingEventsDF),
    ("upcomingEarnings", upcomingEarnings),
    ("upcomingEarningsDF", upcomingEarningsDF),
    ("upcomingDividends", upcomingDividends),
    ("upcomingDividendsDF", upcomingDividendsDF),
    ("upcomingSplits", upcomingSplits),
    ("upcomingSplitsDF", upcomingSplitsDF),
    ("upcomingIPOs", upcomingIPOs),
    ("upcomingIPOsDF", upcomingIPOsDF),
    ("volumeByVenue", volumeByVenue),
    ("volumeByVenueDF", volumeByVenueDF),
]

_INCLUDE_FUNCTIONS_IEX = [
    ("iexAuction", iexAuction),
    ("iexAuctionAsync", iexAuctionAsync),
    ("iexAuctionDF", iexAuctionDF),
    ("iexBook", iexBook),
    ("iexBookAsync", iexBookAsync),
    ("iexBookDF", iexBookDF),
    ("iexDeep", iexDeep),
    ("iexDeepAsync", iexDeepAsync),
    ("iexDeepDF", iexDeepDF),
    ("iexHist", iexHist),
    ("iexHistAsync", iexHistAsync),
    ("iexHistDF", iexHistDF),
    ("iexLast", iexLast),
    ("iexLastAsync", iexLastAsync),
    ("iexLastDF", iexLastDF),
    ("iexOfficialPrice", iexOfficialPrice),
    ("iexOfficialPriceAsync", iexOfficialPriceAsync),
    ("iexOfficialPriceDF", iexOfficialPriceDF),
    ("iexOpHaltStatus", iexOpHaltStatus),
    ("iexOpHaltStatusAsync", iexOpHaltStatusAsync),
    ("iexOpHaltStatusDF", iexOpHaltStatusDF),
    ("iexSecurityEvent", iexSecurityEvent),
    ("iexSecurityEventAsync", iexSecurityEventAsync),
    ("iexSecurityEventDF", iexSecurityEventDF),
    ("iexSsrStatus", iexSsrStatus),
    ("iexSsrStatusAsync", iexSsrStatusAsync),
    ("iexSsrStatusDF", iexSsrStatusDF),
    ("iexSystemEvent", iexSystemEvent),
    ("iexSystemEventAsync", iexSystemEventAsync),
    ("iexSystemEventDF", iexSystemEventDF),
    ("iexThreshold", iexThreshold),
    ("iexThresholdDF", iexThresholdDF),
    ("iexTops", iexTops),
    ("iexTopsAsync", iexTopsAsync),
    ("iexTopsDF", iexTopsDF),
    ("iexTradeBreak", iexTradeBreak),
    ("iexTradeBreakAsync", iexTradeBreakAsync),
    ("iexTradeBreakDF", iexTradeBreakDF),
    ("iexTrades", iexTrades),
    ("iexTradesAsync", iexTradesAsync),
    ("iexTradesDF", iexTradesDF),
    ("iexTradingStatus", iexTradingStatus),
    ("iexTradingStatusAsync", iexTradingStatusAsync),
    ("iexTradingStatusDF", iexTradingStatusDF),
]

_INCLUDE_FUNCTIONS_STREAMING = [
    # SSE Streaming
    ("topsSSE", iexTopsSSE),
    ("topsSSEAsync", iexTopsSSEAsync),
    ("lastSSE", iexLastSSE),
    ("lastSSEAsync", iexLastSSEAsync),
    ("deepSSE", iexDeepSSE),
    ("deepSSEAsync", iexDeepSSEAsync),
    ("tradesSSE", iexTradesSSE),
    ("tradesSSEAsync", iexTradesSSEAsync),
    # Stock SSE
    ("stocksUSNoUTPSSE", stocksUSNoUTPSSE),
    ("stocksUSNoUTPSSEAsync", stocksUSNoUTPSSEAsync),
    ("stocksUSSSE", stocksUSSSE),
    ("stocksUSSSEAsync", stocksUSSSEAsync),
    ("stocksUS1SecondSSE", stocksUS1SecondSSE),
    ("stocksUSNoUTP1SecondSSE", stocksUSNoUTP1SecondSSE),
    ("stocksUS1SecondSSEAsync", stocksUS1SecondSSEAsync),
    ("stocksUSNoUTP1SecondSSEAsync", stocksUSNoUTP1SecondSSEAsync),
    ("stocksUS5SecondSSE", stocksUS5SecondSSE),
    ("stocksUSNoUTP5SecondSSE", stocksUSNoUTP5SecondSSE),
    ("stocksUS5SecondSSEAsync", stocksUS5SecondSSEAsync),
    ("stocksUSNoUTP5SecondSSEAsync", stocksUSNoUTP5SecondSSEAsync),
    ("stocksUS1MinuteSSE", stocksUS1MinuteSSE),
    ("stocksUSNoUTP1MinuteSSE", stocksUSNoUTP1MinuteSSE),
    ("stocksUS1MinuteSSEAsync", stocksUS1MinuteSSEAsync),
    ("stocksUSNoUTP1MinuteSSEAsync", stocksUSNoUTP1MinuteSSEAsync),
    # FXSSE
    ("fxSSE", fxSSE),
    ("fxSSEAsync", fxSSEAsync),
    ("forex1SecondSSE", forex1SecondSSE),
    ("forex1SecondSSEAsync", forex1SecondSSEAsync),
    ("forex5SecondSSE", forex5SecondSSE),
    ("forex5SecondSSEAsync", forex5SecondSSEAsync),
    ("forex1MinuteSSE", forex1MinuteSSE),
    ("forex1MinuteSSEAsync", forex1MinuteSSEAsync),
    # NewsSSE
    ("newsSSE", newsSSE),
    ("newsSSEAsync", newsSSEAsync),
    # SentimentSSE
    ("sentimentSSE", sentimentSSE),
    ("sentimentSSEAsync", sentimentSSEAsync),
    # CryptoSSE
    ("cryptoBookSSE", cryptoBookSSE),
    ("cryptoBookSSEAsync", cryptoBookSSEAsync),
    ("cryptoEventsSSE", cryptoEventsSSE),
    ("cryptoEventsSSEAsync", cryptoEventsSSEAsync),
    ("cryptoQuotesSSE", cryptoQuotesSSE),
    ("cryptoQuotesSSEAsync", cryptoQuotesSSEAsync),
]

_INCLUDE_FUNCTIONS_ACCOUNT = [
    # Account
    ("messageBudget", messageBudget),
    ("messageBudgetAsync", messageBudgetAsync),
    ("metadata", metadata),
    ("metadataAsync", metadataAsync),
    ("metadataDF", metadataDF),
    ("usage", usage),
    ("usageAsync", usageAsync),
    ("usageDF", usageDF),
    ("payAsYouGo", payAsYouGo),
    ("payAsYouGoAsync", payAsYouGoAsync),
    ("status", status),
    ("statusAsync", statusAsync),
]

_INCLUDE_FUNCTIONS_ACCOUNT_WATCHLIST = [
    # Account - Watchlist
    ("get", getWatchlist),
    ("getDF", getWatchlistDF),
    ("create", createWatchlist),
    ("add", addToWatchlist),
    ("remove", deleteFromWatchlist),
    ("delete", deleteWatchlist),
]

_INCLUDE_FUNCTIONS_ALTERNATIVE = [
    # Alternative
    ("sentiment", sentiment),
    ("sentimentAsync", sentimentAsync),
    ("sentimentDF", sentimentDF),
]

_INCLUDE_FUNCTIONS_POINTS = [
    # Data Points
    ("points", points),
    ("pointsDF", pointsDF),
]


_INCLUDE_FUNCTIONS_TS = [
    ("timeSeriesInventory", timeSeriesInventory),
    ("timeSeriesInventoryAsync", timeSeriesInventoryAsync),
    ("timeSeriesInventoryDF", timeSeriesInventoryDF),
    ("timeSeries", timeSeries),
    ("timeSeriesAsync", timeSeriesAsync),
    ("timeSeriesDF", timeSeriesDF),
]

_INCLUDE_FUNCTIONS_FUTURES = [
    ("futures", futures),
    ("futuresDF", futuresDF),
]

_INCLUDE_FUNCTIONS_OPTIONS = [
    ("options", options),
    ("optionsDF", optionsDF),
]

_INCLUDE_FUNCTIONS_COMMODITIES = [
    ("brent", brent),
    ("brentAsync", brentAsync),
    ("brentDF", brentDF),
    ("diesel", diesel),
    ("dieselAsync", dieselAsync),
    ("dieselDF", dieselDF),
    ("gasmid", gasmid),
    ("gasmidAsync", gasmidAsync),
    ("gasmidDF", gasmidDF),
    ("gasprm", gasprm),
    ("gasprmAsync", gasprmAsync),
    ("gasprmDF", gasprmDF),
    ("gasreg", gasreg),
    ("gasregAsync", gasregAsync),
    ("gasregDF", gasregDF),
    ("heatoil", heatoil),
    ("heatoilAsync", heatoilAsync),
    ("heatoilDF", heatoilDF),
    ("jet", jet),
    ("jetAsync", jetAsync),
    ("jetDF", jetDF),
    ("natgas", natgas),
    ("natgasAsync", natgasAsync),
    ("natgasDF", natgasDF),
    ("propane", propane),
    ("propaneAsync", propaneAsync),
    ("propaneDF", propaneDF),
    ("wti", wti),
    ("wtiAsync", wtiAsync),
    ("wtiDF", wtiDF),
]

_INCLUDE_FUNCTIONS_RATES = [
    ("cdj", cdj),
    ("cdjDF", cdjDF),
    ("cdnj", cdnj),
    ("cdnjDF", cdnjDF),
    ("creditcard", creditcard),
    ("creditcardDF", creditcardDF),
]

_INCLUDE_FUNCTIONS_ECONOMIC = [
    ("cpi", cpi),
    ("cpiAsync", cpiAsync),
    ("cpiDF", cpiDF),
    ("fedfunds", fedfunds),
    ("fedfundsAsync", fedfundsAsync),
    ("fedfundsDF", fedfundsDF),
    ("gdp", gdp),
    ("gdpAsync", gdpAsync),
    ("gdpDF", gdpDF),
    ("housing", housing),
    ("housingAsync", housingAsync),
    ("housingDF", housingDF),
    ("indpro", indpro),
    ("indproAsync", indproAsync),
    ("indproDF", indproDF),
    ("initialClaims", initialClaims),
    ("initialClaimsAsync", initialClaimsAsync),
    ("initialClaimsDF", initialClaimsDF),
    ("institutionalMoney", institutionalMoney),
    ("institutionalMoneyAsync", institutionalMoneyAsync),
    ("institutionalMoneyDF", institutionalMoneyDF),
    ("payroll", payroll),
    ("payrollAsync", payrollAsync),
    ("payrollDF", payrollDF),
    ("recessionProb", recessionProb),
    ("recessionProbAsync", recessionProbAsync),
    ("recessionProbDF", recessionProbDF),
    ("retailMoney", retailMoney),
    ("retailMoneyAsync", retailMoneyAsync),
    ("retailMoneyDF", retailMoneyDF),
    ("unemployment", unemployment),
    ("unemploymentAsync", unemploymentAsync),
    ("unemploymentDF", unemploymentDF),
    ("vehicles", vehicles),
    ("vehiclesAsync", vehiclesAsync),
    ("vehiclesDF", vehiclesDF),
]

_INCLUDE_FUNCTIONS_MORTGAGE = [
    ("us5", us5),
    ("us5DF", us5DF),
    ("us15", us15),
    ("us15DF", us15DF),
    ("us30", us30),
    ("us30DF", us30DF),
]

_INCLUDE_FUNCTIONS_TREASURIES = [
    ("thirtyYear", thirtyYear),
    ("thirtyYearDF", thirtyYearDF),
    ("twentyYear", twentyYear),
    ("twentyYearDF", twentyYearDF),
    ("tenYear", tenYear),
    ("tenYearDF", tenYearDF),
    ("sevenYear", sevenYear),
    ("sevenYearDF", sevenYearDF),
    ("fiveYear", fiveYear),
    ("fiveYearDF", fiveYearDF),
    ("threeYear", threeYear),
    ("threeYearDF", threeYearDF),
    ("twoYear", twoYear),
    ("twoYearDF", twoYearDF),
    ("oneYear", oneYear),
    ("oneYearDF", oneYearDF),
    ("sixMonth", sixMonth),
    ("sixMonthDF", sixMonthDF),
    ("threeMonth", threeMonth),
    ("threeMonthDF", threeMonthDF),
    ("oneMonth", oneMonth),
    ("oneMonthDF", oneMonthDF),
]

_INCLUDE_FUNCTIONS_FX = [
    # FX
    ("latestFX", latestFX),
    ("latestFXDF", latestFXDF),
    ("convertFX", convertFX),
    ("convertFXDF", convertFXDF),
    ("historicalFX", historicalFX),
    ("historicalFXDF", historicalFXDF),
]

_INCLUDE_FUNCTIONS_CRYPTO = [
    # Crypto
    ("cryptoBook", cryptoBook),
    ("cryptoBookAsync", cryptoBookAsync),
    ("cryptoBookDF", cryptoBookDF),
    ("cryptoQuote", cryptoQuote),
    ("cryptoQuoteAsync", cryptoQuoteAsync),
    ("cryptoQuoteDF", cryptoQuoteDF),
    ("cryptoPrice", cryptoPrice),
    ("cryptoPriceAsync", cryptoPriceAsync),
    ("cryptoPriceDF", cryptoPriceDF),
]

_INCLUDE_FUNCTIONS = (
    _INCLUDE_FUNCTIONS_RULES
    + _INCLUDE_FUNCTIONS_REFDATA
    + _INCLUDE_FUNCTIONS_MARKET
    + _INCLUDE_FUNCTIONS_STATS
    + _INCLUDE_FUNCTIONS_STOCKS
    + _INCLUDE_FUNCTIONS_IEX
    + _INCLUDE_FUNCTIONS_STREAMING
    + _INCLUDE_FUNCTIONS_ACCOUNT
    + _INCLUDE_FUNCTIONS_ALTERNATIVE
    + _INCLUDE_FUNCTIONS_POINTS
    + _INCLUDE_FUNCTIONS_TS
    + _INCLUDE_FUNCTIONS_COMMODITIES
    + _INCLUDE_FUNCTIONS_ECONOMIC
    + _INCLUDE_FUNCTIONS_MORTGAGE
    + _INCLUDE_FUNCTIONS_RATES
    + _INCLUDE_FUNCTIONS_TREASURIES
    + _INCLUDE_FUNCTIONS_FX
    + _INCLUDE_FUNCTIONS_FUTURES
    + _INCLUDE_FUNCTIONS_OPTIONS
    + _INCLUDE_FUNCTIONS_CRYPTO
)

_INCLUDE_FILES = [
    # Files
    ("file", files),
    ("download", download),
]

_INCLUDE_FUNCTIONS_PREMIUM = [
    # Wall Street Horizon
    ("analystDays", analystDaysWallStreetHorizon),
    ("analystDaysDF", analystDaysWallStreetHorizonDF),
    ("boardOfDirectorsMeeting", boardOfDirectorsMeetingWallStreetHorizon),
    ("boardOfDirectorsMeetingDF", boardOfDirectorsMeetingWallStreetHorizonDF),
    ("businessUpdates", businessUpdatesWallStreetHorizon),
    ("businessUpdatesDF", businessUpdatesWallStreetHorizonDF),
    ("buybacks", buybacksWallStreetHorizon),
    ("buybacksDF", buybacksWallStreetHorizonDF),
    ("capitalMarketsDay", capitalMarketsDayWallStreetHorizon),
    ("capitalMarketsDayDF", capitalMarketsDayWallStreetHorizonDF),
    ("companyTravel", companyTravelWallStreetHorizon),
    ("companyTravelDF", companyTravelWallStreetHorizonDF),
    ("filingDueDates", filingDueDatesWallStreetHorizon),
    ("filingDueDatesDF", filingDueDatesWallStreetHorizonDF),
    ("fiscalQuarterEnd", fiscalQuarterEndWallStreetHorizon),
    ("fiscalQuarterEndDF", fiscalQuarterEndWallStreetHorizonDF),
    ("forum", forumWallStreetHorizon),
    ("forumDF", forumWallStreetHorizonDF),
    ("generalConference", generalConferenceWallStreetHorizon),
    ("generalConferenceDF", generalConferenceWallStreetHorizonDF),
    ("fdaAdvisoryCommitteeMeetings", fdaAdvisoryCommitteeMeetingsWallStreetHorizon),
    ("fdaAdvisoryCommitteeMeetingsDF", fdaAdvisoryCommitteeMeetingsWallStreetHorizonDF),
    ("holidays", holidaysWallStreetHorizon),
    ("holidaysDF", holidaysWallStreetHorizonDF),
    ("indexChanges", indexChangesWallStreetHorizon),
    ("indexChangesDF", indexChangesWallStreetHorizonDF),
    ("ipos", iposWallStreetHorizon),
    ("iposDF", iposWallStreetHorizonDF),
    ("legalActions", legalActionsWallStreetHorizon),
    ("legalActionsDF", legalActionsWallStreetHorizonDF),
    ("mergersAndAcquisitions", mergersAndAcquisitionsWallStreetHorizon),
    ("mergersAndAcquisitionsDF", mergersAndAcquisitionsWallStreetHorizonDF),
    ("productEvents", productEventsWallStreetHorizon),
    ("productEventsDF", productEventsWallStreetHorizonDF),
    ("researchAndDevelopmentDays", researchAndDevelopmentDaysWallStreetHorizon),
    ("researchAndDevelopmentDaysDF", researchAndDevelopmentDaysWallStreetHorizonDF),
    ("sameStoreSales", sameStoreSalesWallStreetHorizon),
    ("sameStoreSalesDF", sameStoreSalesWallStreetHorizonDF),
    ("secondaryOfferings", secondaryOfferingsWallStreetHorizon),
    ("secondaryOfferingsDF", secondaryOfferingsWallStreetHorizonDF),
    ("seminars", seminarsWallStreetHorizon),
    ("seminarsDF", seminarsWallStreetHorizonDF),
    ("shareholderMeetings", shareholderMeetingsWallStreetHorizon),
    ("shareholderMeetingsDF", shareholderMeetingsWallStreetHorizonDF),
    ("summitMeetings", summitMeetingsWallStreetHorizon),
    ("summitMeetingsDF", summitMeetingsWallStreetHorizonDF),
    ("tradeShows", tradeShowsWallStreetHorizon),
    ("tradeShowsDF", tradeShowsWallStreetHorizonDF),
    ("witchingHours", witchingHoursWallStreetHorizon),
    ("witchingHoursDF", witchingHoursWallStreetHorizonDF),
    ("workshops", workshopsWallStreetHorizon),
    ("workshopsDF", workshopsWallStreetHorizonDF),
    # Fraud Factors
    ("nonTimelyFilings", nonTimelyFilingsFraudFactors),
    ("nonTimelyFilingsDF", nonTimelyFilingsFraudFactorsDF),
    # Extract Alpha
    ("cam1", cam1ExtractAlpha),
    ("cam1DF", cam1ExtractAlphaDF),
    ("esgCFPBComplaints", esgCFPBComplaintsExtractAlpha),
    ("esgCFPBComplaintsDF", esgCFPBComplaintsExtractAlphaDF),
    ("esgCPSCRecalls", esgCPSCRecallsExtractAlpha),
    ("esgCPSCRecallsDF", esgCPSCRecallsExtractAlphaDF),
    ("esgDOLVisaApplications", esgDOLVisaApplicationsExtractAlpha),
    ("esgDOLVisaApplicationsDF", esgDOLVisaApplicationsExtractAlphaDF),
    ("esgEPAEnforcements", esgEPAEnforcementsExtractAlpha),
    ("esgEPAEnforcementsDF", esgEPAEnforcementsExtractAlphaDF),
    ("esgEPAMilestones", esgEPAMilestonesExtractAlpha),
    ("esgEPAMilestonesDF", esgEPAMilestonesExtractAlphaDF),
    (
        "esgFECIndividualCampaingContributions",
        esgFECIndividualCampaingContributionsExtractAlpha,
    ),
    (
        "esgFECIndividualCampaingContributionsDF",
        esgFECIndividualCampaingContributionsExtractAlphaDF,
    ),
    ("esgOSHAInspections", esgOSHAInspectionsExtractAlpha),
    ("esgOSHAInspectionsDF", esgOSHAInspectionsExtractAlphaDF),
    ("esgSenateLobbying", esgSenateLobbyingExtractAlpha),
    ("esgSenateLobbyingDF", esgSenateLobbyingExtractAlphaDF),
    ("esgUSASpending", esgUSASpendingExtractAlpha),
    ("esgUSASpendingDF", esgUSASpendingExtractAlphaDF),
    ("esgUSPTOPatentApplications", esgUSPTOPatentApplicationsExtractAlpha),
    ("esgUSPTOPatentApplicationsDF", esgUSPTOPatentApplicationsExtractAlphaDF),
    ("esgUSPTOPatentGrants", esgUSPTOPatentGrantsExtractAlpha),
    ("esgUSPTOPatentGrantsDF", esgUSPTOPatentGrantsExtractAlphaDF),
    ("tacticalModel1", tacticalModel1ExtractAlpha),
    ("tacticalModel1DF", tacticalModel1ExtractAlphaDF),
    # Precision Alpha
    ("precisionAlphaPriceDynamics", priceDynamicsPrecisionAlpha),
    ("precisionAlphaPriceDynamicsDF", priceDynamicsPrecisionAlphaDF),
    # BRAIN Company
    ("thirtyDaySentiment", thirtyDaySentimentBrain),
    ("thirtyDaySentimentDF", thirtyDaySentimentBrainDF),
    ("sevenDaySentiment", sevenDaySentimentBrain),
    ("sevenDaySentimentDF", sevenDaySentimentBrainDF),
    ("twentyOneDayMLReturnRanking", twentyOneDayMLReturnRankingBrain),
    ("twentyOneDayMLReturnRankingDF", twentyOneDayMLReturnRankingBrainDF),
    ("tenDayMLReturnRanking", tenDayMLReturnRankingBrain),
    ("tenDayMLReturnRankingDF", tenDayMLReturnRankingBrainDF),
    ("fiveDayMLReturnRanking", fiveDayMLReturnRankingBrain),
    ("fiveDayMLReturnRankingDF", fiveDayMLReturnRankingBrainDF),
    ("threeDayMLReturnRanking", threeDayMLReturnRankingBrain),
    ("threeDayMLReturnRankingDF", threeDayMLReturnRankingBrainDF),
    ("twoDayMLReturnRanking", twoDayMLReturnRankingBrain),
    ("twoDayMLReturnRankingDF", twoDayMLReturnRankingBrainDF),
    (
        "languageMetricsOnCompanyFilingsAll",
        languageMetricsOnCompanyFilingsAllBrain,
    ),
    (
        "languageMetricsOnCompanyFilingsAllDF",
        languageMetricsOnCompanyFilingsAllBrainDF,
    ),
    ("languageMetricsOnCompanyFilings", languageMetricsOnCompanyFilingsBrain),
    ("languageMetricsOnCompanyFilingsDF", languageMetricsOnCompanyFilingsBrainDF),
    (
        "languageMetricsOnCompanyFilingsDifferenceAll",
        languageMetricsOnCompanyFilingsDifferenceAllBrain,
    ),
    (
        "languageMetricsOnCompanyFilingsDifferenceAllDF",
        languageMetricsOnCompanyFilingsDifferenceAllBrainDF,
    ),
    (
        "languageMetricsOnCompanyFilingsDifference",
        languageMetricsOnCompanyFilingsDifferenceBrain,
    ),
    (
        "languageMetricsOnCompanyFilingsDifferenceDF",
        languageMetricsOnCompanyFilingsDifferenceBrainDF,
    ),
    # Kavout
    ("kScore", kScoreKavout),
    ("kScoreDF", kScoreKavoutDF),
    ("kScoreChina", kScoreChinaKavout),
    ("kScoreChinaDF", kScoreChinaKavoutDF),
    # Audit Analytics
    ("accountingQualityAndRiskMatrix", accountingQualityAndRiskMatrixAuditAnalytics),
    (
        "accountingQualityAndRiskMatrixDF",
        accountingQualityAndRiskMatrixAuditAnalyticsDF,
    ),
    ("directorAndOfficerChanges", directorAndOfficerChangesAuditAnalytics),
    ("directorAndOfficerChangesDF", directorAndOfficerChangesAuditAnalyticsDF),
    # Stocktwits
    ("socialSentiment", socialSentimentStockTwits),
    ("socialSentimentDF", socialSentimentStockTwitsDF),
    # Invisage
    (
        "analystRecommendationsAndPriceTargets",
        analystRecommendationsAndPriceTargetsInvisage,
    ),
    (
        "analystRecommendationsAndPriceTargetsDF",
        analystRecommendationsAndPriceTargetsInvisageDF,
    ),
    # Refinitiv
    ("analystRecommendations", analystRecommendationsRefinitiv),
    ("analystRecommendationsDF", analystRecommendationsRefinitivDF),
    ("earnings", earningsRefinitiv),
    ("earningsDF", earningsRefinitivDF),
    ("estimates", estimatesRefinitiv),
    ("estimatesDF", estimatesRefinitivDF),
    ("priceTarget", priceTargetRefinitiv),
    ("priceTargetDF", priceTargetRefinitivDF),
    # CityFalcon
    ("news", newsCityFalcon),
    ("newsDF", newsCityFalconDF),
]

_INCLUDE_PREMIUM_FILES = [
    # ValuEngine
    ("valuEngine", stockResearchReportValuEngine),
    ("valuEngineDownload", downloadStockResearchReportValuEngine),
    # New Constructs
    ("newConstructs", reportNewConstructs),
    ("newConstructsDownload", downloadReportNewConstructs),
]

_INCLUDE_POINTS_RATES = [
    ("creditcardValue", RatesPoints.CREDITCARD.value),
    ("cdnjValue", RatesPoints.CDNJ.value),
    ("cdjValue", RatesPoints.CDJ.value),
]

_INCLUDE_POINTS_COMMODITIES = [
    ("wti", CommoditiesPoints.WTI.value),
    ("brent", CommoditiesPoints.BRENT.value),
    ("natgas", CommoditiesPoints.NATGAS.value),
    ("heatoil", CommoditiesPoints.HEATOIL.value),
    ("jet", CommoditiesPoints.JET.value),
    ("diesel", CommoditiesPoints.DIESEL.value),
    ("gasreg", CommoditiesPoints.GASREG.value),
    ("gasmid", CommoditiesPoints.GASMID.value),
    ("gasprm", CommoditiesPoints.GASPRM.value),
    ("propane", CommoditiesPoints.PROPANE.value),
]


_INCLUDE_POINTS_ECONOMIC = [
    ("fedfunds", EconomicPoints.FEDFUNDS.value),
    ("gdp", EconomicPoints.GDP.value),
    ("indpro", EconomicPoints.INDPRO.value),
    ("cpi", EconomicPoints.CPI.value),
    ("payroll", EconomicPoints.PAYROLL.value),
    ("housing", EconomicPoints.HOUSING.value),
    ("unemployment", EconomicPoints.UNEMPLOYMENT.value),
    ("vehicles", EconomicPoints.VEHICLES.value),
    ("recessionProb", EconomicPoints.RECESSION_PROB.value),
    ("initialClaims", EconomicPoints.INITIALCLAIMS.value),
    ("institutionalMoney", EconomicPoints.INSTITUTIONALMONEY.value),
    ("retailMoney", EconomicPoints.RETAILMONEY.value),
]

_INCLUDE_POINTS_MORTGAGE = [
    ("us30", MortgagePoints.US30.value),
    ("us15", MortgagePoints.US15.value),
    ("us5", MortgagePoints.US5.value),
]

_INCLUDE_POINTS_TREASURIES = [
    ("thirtyYearValue", TreasuriesPoints.THIRTY.value),
    ("twentyYearValue", TreasuriesPoints.TWENTY.value),
    ("tenYearValue", TreasuriesPoints.TEN.value),
    ("sevenYearValue", TreasuriesPoints.SEVEN.value),
    ("fiveYearValue", TreasuriesPoints.FIVE.value),
    ("threeYearValue", TreasuriesPoints.THREE.value),
    ("twoYearValue", TreasuriesPoints.TWO.value),
    ("oneYearValue", TreasuriesPoints.ONE.value),
    ("sixMonthValue", TreasuriesPoints.SIXMONTH.value),
    ("threeMonthValue", TreasuriesPoints.THREEMONTH.value),
    ("oneMonthValue", TreasuriesPoints.ONEMONTH.value),
]

_INCLUDE_STUDIES = [
    ("peerCorrelation", peerCorrelation),
    ("peerCorrelationPlot", peerCorrelationPlot),
    ("returns", returns),
    ("dailyReturns", dailyReturns),
    ("yieldCurve", yieldCurve),
    # Cycle
    ("ht_dcperiod", ht_dcperiod),
    ("ht_dcphase", ht_dcphase),
    ("ht_phasor", ht_phasor),
    ("ht_sine", ht_sine),
    ("ht_trendmode", ht_trendmode),
    # Math
    ("acos", acos),
    ("asin", asin),
    ("atan", atan),
    ("ceil", ceil),
    ("cos", cos),
    ("cosh", cosh),
    ("exp", exp),
    ("floor", floor),
    ("ln", ln),
    ("log10", log10),
    ("sin", sin),
    ("sinh", sinh),
    ("sqrt", sqrt),
    ("tan", tan),
    ("tanh", tanh),
    ("add", add),
    ("div", div),
    ("max", max),
    ("maxindex", maxindex),
    ("min", min),
    ("minindex", minindex),
    ("minmax", minmax),
    ("minmaxindex", minmaxindex),
    ("mult", mult),
    ("sub", sub),
    ("sum", sum),
    # Momentum
    ("adx", adx),
    ("adxr", adxr),
    ("apo", apo),
    ("aroon", aroon),
    ("aroonosc", aroonosc),
    ("bop", bop),
    ("cci", cci),
    ("cmo", cmo),
    ("dx", dx),
    ("macd", macd),
    ("macdext", macdext),
    ("mfi", mfi),
    ("minus_di", minus_di),
    ("minus_dm", minus_dm),
    ("mom", mom),
    ("plus_di", plus_di),
    ("plus_dm", plus_dm),
    ("ppo", ppo),
    ("roc", roc),
    ("rocp", rocp),
    ("rocr", rocr),
    ("rocr100", rocr100),
    ("rsi", rsi),
    ("stoch", stoch),
    ("stochf", stochf),
    ("stochrsi", stochrsi),
    ("trix", trix),
    ("ultosc", ultosc),
    ("willr", willr),
    # Overlap
    ("bollinger", bollinger),
    ("dema", dema),
    ("ema", ema),
    ("ht_trendline", ht_trendline),
    ("kama", kama),
    ("mama", mama),
    ("mavp", mavp),
    ("midpoint", midpoint),
    ("midpice", midpice),
    ("sar", sar),
    ("sarext", sarext),
    ("sma", sma),
    ("t3", t3),
    ("tema", tema),
    ("trima", trima),
    ("wma", wma),
    # Pattern
    ("cdl2crows", cdl2crows),
    ("cdl3blackcrows", cdl3blackcrows),
    ("cdl3inside", cdl3inside),
    ("cdl3linestrike", cdl3linestrike),
    ("cdl3outside", cdl3outside),
    ("cdl3starsinsouth", cdl3starsinsouth),
    ("cdl3whitesoldiers", cdl3whitesoldiers),
    ("cdlabandonedbaby", cdlabandonedbaby),
    ("cdladvanceblock", cdladvanceblock),
    ("cdlbelthold", cdlbelthold),
    ("cdlbreakaway", cdlbreakaway),
    ("cdlclosingmarubozu", cdlclosingmarubozu),
    ("cdlconcealbabyswallow", cdlconcealbabyswallow),
    ("cdlcounterattack", cdlcounterattack),
    ("cdldarkcloudcover", cdldarkcloudcover),
    ("cdldoji", cdldoji),
    ("cdldojistar", cdldojistar),
    ("cdldragonflydoji", cdldragonflydoji),
    ("cdlengulfing", cdlengulfing),
    ("cdleveningdojistar", cdleveningdojistar),
    ("cdleveningstar", cdleveningstar),
    ("cdlgapsidesidewhite", cdlgapsidesidewhite),
    ("cdlgravestonedoji", cdlgravestonedoji),
    ("cdlhammer", cdlhammer),
    ("cdlhangingman", cdlhangingman),
    ("cdlharami", cdlharami),
    ("cdlharamicross", cdlharamicross),
    ("cdlhighwave", cdlhighwave),
    ("cdlhikkake", cdlhikkake),
    ("cdlhikkakemod", cdlhikkakemod),
    ("cdlhomingpigeon", cdlhomingpigeon),
    ("cdlidentical3crows", cdlidentical3crows),
    ("cdlinneck", cdlinneck),
    ("cdlinvertedhammer", cdlinvertedhammer),
    ("cdlkicking", cdlkicking),
    ("cdlkickingbylength", cdlkickingbylength),
    ("cdlladderbottom", cdlladderbottom),
    ("cdllongleggeddoji", cdllongleggeddoji),
    ("cdllongline", cdllongline),
    ("cdlmarubozu", cdlmarubozu),
    ("cdlmatchinglow", cdlmatchinglow),
    ("cdlmathold", cdlmathold),
    ("cdlmorningdojistar", cdlmorningdojistar),
    ("cdlmorningstar", cdlmorningstar),
    ("cdlonneck", cdlonneck),
    ("cdlpiercing", cdlpiercing),
    ("cdlrickshawman", cdlrickshawman),
    ("cdlrisefall3methods", cdlrisefall3methods),
    ("cdlseparatinglines", cdlseparatinglines),
    ("cdlshootingstar", cdlshootingstar),
    ("cdlshortline", cdlshortline),
    ("cdlspinningtop", cdlspinningtop),
    ("cdlstalledpattern", cdlstalledpattern),
    ("cdlsticksandwich", cdlsticksandwich),
    ("cdltakuri", cdltakuri),
    ("cdltasukigap", cdltasukigap),
    ("cdlthrusting", cdlthrusting),
    ("cdltristar", cdltristar),
    ("cdlunique3river", cdlunique3river),
    ("cdlxsidegap3methods", cdlxsidegap3methods),
    # Price
    ("avgprice", avgprice),
    ("medprice", medprice),
    ("typprice", typprice),
    ("wclprice", wclprice),
    # Statistic
    ("beta", beta),
    ("correl", correl),
    ("linearreg", linearreg),
    ("linearreg_angle", linearreg_angle),
    ("linearreg_intercept", linearreg_intercept),
    ("linearreg_slope", linearreg_slope),
    ("stddev", stddev),
    ("tsf", tsf),
    ("var", var),
    # Volatility
    ("atr", atr),
    ("natr", natr),
    ("trange", trange),
    # Volume
    ("ad", ad),
    ("adosc", adosc),
    ("obv", obv),
]


class Client(object):
    """IEX Cloud Client

    Client has access to all methods provided as standalone, but in an authenticated way

    Args:
        api_token (str): api token (can pickup from IEX_TOKEN environment variable)
        version (str): api version to use (defaults to v1)
                          set version to 'sandbox' to run against the IEX sandbox
        api_limit (int): cache calls in this interval
    """

    _api_limit = DEFAULT_API_LIMIT

    account = types.ModuleType("account")
    alternative = types.ModuleType("alternative")
    commodities = types.ModuleType("commodities")
    crypto = types.ModuleType("crypto")
    economic = types.ModuleType("economic")
    files = types.ModuleType("files")
    futures = types.ModuleType("futures")
    fx = types.ModuleType("fx")
    iex = types.ModuleType("iex")
    market = types.ModuleType("market")
    mortgage = types.ModuleType("market")
    options = types.ModuleType("options")
    points = types.ModuleType("points")
    platform = types.ModuleType("platform")
    premium = types.ModuleType("premium")
    premium.files = types.ModuleType("premium.files")
    rates = types.ModuleType("rates")
    refdata = types.ModuleType("refdata")
    rules = types.ModuleType("rules")
    stats = types.ModuleType("stats")
    stocks = types.ModuleType("stocks")
    streaming = types.ModuleType("streaming")
    studies = types.ModuleType("studies")
    treasuries = types.ModuleType("treasuries")
    watchlist = types.ModuleType("watchlist")

    def __init__(self, api_token=None, version="v1", api_limit=DEFAULT_API_LIMIT):
        self._token = api_token or os.environ.get("IEX_TOKEN", "")
        if not self._token:
            raise PyEXception("API Token missing or not in environment (IEX_TOKEN)")

        if version not in ("beta", "stable", "v1", "sandbox"):
            raise PyEXception("Unrecognized api version: {}".format(version))

        if self._token.startswith("T") and version != "sandbox":
            warnings.warn(
                "Using test key but attempting to connect to non-sandbox environment. Switching to sandbox"
            )
            version = "sandbox"

        self._version = version
        self._api_limit = api_limit

        # rebind
        for name, method in _INCLUDE_FUNCTIONS_ACCOUNT:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            # setattr(self.account, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_ALTERNATIVE:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.alternative, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_CRYPTO:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.crypto, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_FX:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.fx, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_FUTURES:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.futures, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_OPTIONS:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.options, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_IEX:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.iex, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_MARKET:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.market, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_POINTS:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.points, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_TS:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__

        for name, method in _INCLUDE_FUNCTIONS_COMMODITIES:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.commodities, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_ECONOMIC:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.economic, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_MORTGAGE:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.mortgage, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_RATES:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.rates, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_TREASURIES:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.treasuries, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_PLATFORM:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.platform, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_RULES:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.rules, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_REFDATA:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.refdata, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_STATS:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.stats, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_STOCKS:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.stocks, name, getattr(self, name))

        for name, method in _INCLUDE_FUNCTIONS_STREAMING:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.streaming, name, getattr(self, name))

        # rebind premium data
        for name, method in _INCLUDE_FUNCTIONS_PREMIUM:
            setattr(self.premium, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self.premium, name).__doc__ = method.__doc__

        # rebind commodities
        for name, key in _INCLUDE_POINTS_COMMODITIES:
            p = partial(self.bind, meth=points, key=key)
            p.__name__ = key
            setattr(self, name, wraps(points)(_interval(minutes=self._api_limit)(p)))
            getattr(self, name).__doc__ = points.__doc__
            setattr(
                self.commodities,
                name,
                wraps(points)(_interval(minutes=self._api_limit)(p)),
            )

        # rebind economic
        for name, key in _INCLUDE_POINTS_ECONOMIC:
            p = partial(self.bind, meth=points, key=key)
            p.__name__ = key
            setattr(self, name, wraps(points)(_interval(minutes=self._api_limit)(p)))
            getattr(self, name).__doc__ = points.__doc__
            setattr(
                self.economic,
                name,
                wraps(points)(_interval(minutes=self._api_limit)(p)),
            )

        # rebind mortgage
        for name, key in _INCLUDE_POINTS_MORTGAGE:
            p = partial(self.bind, meth=points, key=key)
            p.__name__ = key
            setattr(self, name, wraps(points)(_interval(minutes=self._api_limit)(p)))
            getattr(self, name).__doc__ = points.__doc__
            setattr(
                self.mortgage,
                name,
                wraps(points)(_interval(minutes=self._api_limit)(p)),
            )

        # rebind rates
        for name, key in _INCLUDE_POINTS_RATES:
            p = partial(self.bind, meth=points, key=key)
            p.__name__ = key
            setattr(self, name, wraps(points)(_interval(minutes=self._api_limit)(p)))
            getattr(self, name).__doc__ = points.__doc__
            setattr(
                self.rates, name, wraps(points)(_interval(minutes=self._api_limit)(p))
            )

        # rebind treasuries
        for name, key in _INCLUDE_POINTS_TREASURIES:
            p = partial(self.bind, meth=points, key=key)
            p.__name__ = key
            setattr(self, name, wraps(points)(_interval(minutes=self._api_limit)(p)))
            getattr(self, name).__doc__ = points.__doc__
            setattr(
                self.treasuries,
                name,
                wraps(points)(_interval(minutes=self._api_limit)(p)),
            )

        # rebind files
        for name, method in _INCLUDE_FILES:
            setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self, name).__doc__ = method.__doc__
            setattr(self.files, name, wraps(method)(partial(self.bind, meth=method)))
            getattr(self.files, name).__doc__ = method.__doc__

        # rebind premium files
        for name, method in _INCLUDE_PREMIUM_FILES:
            setattr(
                self.premium.files, name, wraps(method)(partial(self.bind, meth=method))
            )
            getattr(self.premium.files, name).__doc__ = method.__doc__

        # rebind studies
        for name, method in _INCLUDE_STUDIES:
            if method:
                setattr(self, name, wraps(method)(partial(self.bind, meth=method)))
                getattr(self, name).__doc__ = method.__doc__
                setattr(self.studies, name, method.__get__(self, self.__class__))

        # rebind watchlists
        for name, method in _INCLUDE_FUNCTIONS_ACCOUNT_WATCHLIST:
            setattr(
                self.watchlist, name, wraps(method)(partial(self.bind, meth=method))
            )
            getattr(self.watchlist, name).__doc__ = method.__doc__

    def bind(self, *args, **kwargs):
        meth = kwargs.pop("meth")
        if not meth:
            raise PyEXception("Must provide method!")
        return meth(token=self._token, version=self._version, *args, **kwargs)

    def account(self, *args, **kwargs):
        return self.metadata(*args, **kwargs)


#############################
# for autodoc
if os.environ.get("PYEX_AUTODOC") or os.environ.get("READTHEDOCS"):
    # rebind
    for name, method in _INCLUDE_FUNCTIONS_ACCOUNT:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        # setattr(Client.account, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_ALTERNATIVE:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.alternative, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_CRYPTO:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.crypto, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_FX:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.fx, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_FUTURES:
        setattr(Client, name, method)
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.futures, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_OPTIONS:
        setattr(Client, name, method)
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.options, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_IEX:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.iex, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_MARKET:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.market, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_POINTS:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.points, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_TS:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__

    for name, method in _INCLUDE_FUNCTIONS_COMMODITIES:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.commodities, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_ECONOMIC:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.economic, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_MORTGAGE:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.mortgage, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_RATES:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.rates, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_TREASURIES:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.treasuries, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_PLATFORM:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.platform, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_RULES:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.rules, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_REFDATA:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.refdata, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_STATS:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.stats, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_STOCKS:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.stocks, name, getattr(Client, name))

    for name, method in _INCLUDE_FUNCTIONS_STREAMING:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.streaming, name, getattr(Client, name))

    # rebind premium data
    for name, method in _INCLUDE_FUNCTIONS_PREMIUM:
        setattr(Client.premium, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client.premium, name).__doc__ = method.__doc__

    # rebind commodities
    for name, key in _INCLUDE_POINTS_COMMODITIES:
        p = partial(Client.bind, meth=points, key=key)
        p.__name__ = key
        setattr(Client, name, wraps(points)(_interval(minutes=Client._api_limit)(p)))
        getattr(Client, name).__doc__ = points.__doc__
        setattr(
            Client.commodities,
            name,
            wraps(points)(_interval(minutes=Client._api_limit)(p)),
        )

    # rebind economic
    for name, key in _INCLUDE_POINTS_ECONOMIC:
        p = partial(Client.bind, meth=points, key=key)
        p.__name__ = key
        setattr(Client, name, wraps(points)(_interval(minutes=Client._api_limit)(p)))
        getattr(Client, name).__doc__ = points.__doc__
        setattr(
            Client.economic,
            name,
            wraps(points)(_interval(minutes=Client._api_limit)(p)),
        )

    # rebind mortgage
    for name, key in _INCLUDE_POINTS_MORTGAGE:
        p = partial(Client.bind, meth=points, key=key)
        p.__name__ = key
        setattr(Client, name, wraps(points)(_interval(minutes=Client._api_limit)(p)))
        getattr(Client, name).__doc__ = points.__doc__
        setattr(
            Client.mortgage,
            name,
            wraps(points)(_interval(minutes=Client._api_limit)(p)),
        )

    # rebind rates
    for name, key in _INCLUDE_POINTS_RATES:
        p = partial(Client.bind, meth=points, key=key)
        p.__name__ = key
        setattr(Client, name, wraps(points)(_interval(minutes=Client._api_limit)(p)))
        getattr(Client, name).__doc__ = points.__doc__
        setattr(
            Client.rates, name, wraps(points)(_interval(minutes=Client._api_limit)(p))
        )

    # rebind treasuries
    for name, key in _INCLUDE_POINTS_TREASURIES:
        p = partial(Client.bind, meth=points, key=key)
        p.__name__ = key
        setattr(Client, name, wraps(points)(_interval(minutes=Client._api_limit)(p)))
        getattr(Client, name).__doc__ = points.__doc__
        setattr(
            Client.treasuries,
            name,
            wraps(points)(_interval(minutes=Client._api_limit)(p)),
        )

    # rebind files
    for name, method in _INCLUDE_FILES:
        setattr(Client, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client, name).__doc__ = method.__doc__
        setattr(Client.files, name, wraps(method)(partial(Client.bind, meth=method)))
        getattr(Client.files, name).__doc__ = method.__doc__

    # rebind premium files
    for name, method in _INCLUDE_PREMIUM_FILES:
        setattr(
            Client.premium.files, name, wraps(method)(partial(Client.bind, meth=method))
        )
        getattr(Client.premium.files, name).__doc__ = method.__doc__

    # rebind studies
    for name, method in _INCLUDE_STUDIES:
        if method:
            setattr(Client, name, method.__get__(Client, Client.__class__))
            setattr(Client.studies, name, method.__get__(Client, Client.__class__))

    # rebind watchlist
    for name, method in _INCLUDE_FUNCTIONS_ACCOUNT_WATCHLIST:
        setattr(
            Client.watchlist, name, wraps(method)(partial(Client.bind, meth=method))
        )
        getattr(Client.watchlist, name).__doc__ = method.__doc__
