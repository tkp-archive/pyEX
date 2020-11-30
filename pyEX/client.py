# -*- coding: utf-8 -*-
import os
from functools import partial, wraps
from .common import PyEXception, _interval
from .account import messageBudget, metadata, metadataDF, usage, usageDF
from .alternative import (
    crypto,
    cryptoDF,
    sentiment,
    sentimentDF,
    ceoCompensation,
    ceoCompensationDF,
)
from .commodities import CommoditiesPoints
from .cryptocurrency import (
    cryptoBook,
    cryptoBookDF,
    cryptoPrice,
    cryptoPriceDF,
    cryptoQuote,
    cryptoQuoteDF,
)
from .economic import EconomicPoints
from .fx import (
    latestFX,
    latestFXDF,
    convertFX,
    convertFXDF,
    historicalFX,
    historicalFXDF,
)
from .markets import markets, marketsDF
from .marketdata.cryptocurrency import (
    cryptoBookSSE,
    cryptoBookSSEAsync,
    cryptoEventsSSE,
    cryptoEventsSSEAsync,
    cryptoQuotesSSE,
    cryptoQuotesSSEAsync,
)
from .marketdata.fx import fxSSE, fxSSEAsync
from .marketdata.news import newsSSE, newsSSEAsync
from .marketdata.sentiment import sentimentSSE, sentimentSSEAsync
from .marketdata.sse import (
    topsSSE,
    topsSSEAsync,
    lastSSE,
    lastSSEAsync,
    deepSSE,
    deepSSEAsync,
    tradesSSE,
    tradesSSEAsync,
)
from .marketdata.stock import (
    stocksUSNoUTPSSE,
    stocksUSNoUTPSSEAsync,
    stocksUSSSE,
    stocksUSSSEAsync,
    stocksUS1SecondSSE,
    stocksUS1SecondSSEAsync,
    stocksUS5SecondSSE,
    stocksUS5SecondSSEAsync,
    stocksUS1MinuteSSE,
    stocksUS1MinuteSSEAsync,
)
from .marketdata.http import (
    tops,
    topsAsync,
    topsDF,
    last,
    lastAsync,
    lastDF,
    deep,
    deepAsync,
    deepDF,
    hist,
    histAsync,
    histDF,
    trades,
    tradesAsync,
    tradesDF,
    auction,
    auctionAsync,
    auctionDF,
    book as deepBook,
    bookAsync as deepBookAsync,
    bookDF as deepBookDF,
    opHaltStatus,
    opHaltStatusAsync,
    opHaltStatusDF,
    officialPrice,
    officialPriceAsync,
    officialPriceDF,
    securityEvent,
    securityEventAsync,
    securityEventDF,
    ssrStatus,
    ssrStatusAsync,
    ssrStatusDF,
    systemEvent,
    systemEventAsync,
    systemEventDF,
    tradeBreak,
    tradeBreakAsync,
    tradeBreakDF,
    tradingStatus,
    tradingStatusAsync,
    tradingStatusDF,
)
from .points import points, pointsDF
from .premium import (
    accountingQualityAndRiskMatrix,
    accountingQualityAndRiskMatrixDF,
    analystDays,
    analystDaysDF,
    boardOfDirectorsMeeting,
    boardOfDirectorsMeetingDF,
    brain30DaySentiment,
    brain30DaySentimentDF,
    brain7DaySentiment,
    brain7DaySentimentDF,
    brain21DayMLReturnRanking,
    brain21DayMLReturnRankingDF,
    brain10DayMLReturnRanking,
    brain10DayMLReturnRankingDF,
    brain5DayMLReturnRanking,
    brain5DayMLReturnRankingDF,
    brain3DayMLReturnRanking,
    brain3DayMLReturnRankingDF,
    brain2DayMLReturnRanking,
    brain2DayMLReturnRankingDF,
    brainLanguageMetricsOnCompanyFilingsAll,
    brainLanguageMetricsOnCompanyFilingsAllDF,
    brainLanguageMetricsOnCompanyFilings,
    brainLanguageMetricsOnCompanyFilingsDF,
    brainLanguageMetricsOnCompanyFilingsDifferenceAll,
    brainLanguageMetricsOnCompanyFilingsDifferenceAllDF,
    brainLanguageMetricsOnCompanyFilingsDifference,
    brainLanguageMetricsOnCompanyFilingsDifferenceDF,
    businessUpdates,
    businessUpdatesDF,
    buybacks,
    buybacksDF,
    cam1,
    cam1DF,
    capitalMarketsDay,
    capitalMarketsDayDF,
    companyTravel,
    companyTravelDF,
    directorAndOfficerChanges,
    directorAndOfficerChangesDF,
    esgCFPBComplaints,
    esgCFPBComplaintsDF,
    esgCPSCRecalls,
    esgCPSCRecallsDF,
    esgDOLVisaApplications,
    esgDOLVisaApplicationsDF,
    esgEPAEnforcements,
    esgEPAEnforcementsDF,
    esgEPAMilestones,
    esgEPAMilestonesDF,
    esgFECIndividualCampaingContributions,
    esgFECIndividualCampaingContributionsDF,
    esgOSHAInspections,
    esgOSHAInspectionsDF,
    esgSenateLobbying,
    esgSenateLobbyingDF,
    esgUSASpending,
    esgUSASpendingDF,
    esgUSPTOPatentApplications,
    esgUSPTOPatentApplicationsDF,
    esgUSPTOPatentGrants,
    esgUSPTOPatentGrantsDF,
    fdaAdvisoryCommitteeMeetings,
    fdaAdvisoryCommitteeMeetingsDF,
    filingDueDates,
    filingDueDatesDF,
    fiscalQuarterEnd,
    fiscalQuarterEndDF,
    forum,
    forumDF,
    generalConference,
    generalConferenceDF,
    holidaysWSH,
    holidaysWSHDF,
    indexChanges,
    indexChangesDF,
    iposWSH,
    iposWSHDF,
    kScore,
    kScoreDF,
    kScoreChina,
    kScoreChinaDF,
    legalActions,
    legalActionsDF,
    mergersAndAcquisitions,
    mergersAndAcquisitionsDF,
    nonTimelyFilings,
    nonTimelyFilingsDF,
    precisionAlphaPriceDynamics,
    precisionAlphaPriceDynamicsDF,
    productEventsDF,
    productEvents,
    researchAndDevelopmentDays,
    researchAndDevelopmentDaysDF,
    sameStoreSales,
    sameStoreSalesDF,
    secondaryOfferings,
    secondaryOfferingsDF,
    seminars,
    seminarsDF,
    shareholderMeetings,
    shareholderMeetingsDF,
    similarityIndex,
    similarityIndexDF,
    summitMeetings,
    summitMeetingsDF,
    tacticalModel1,
    tacticalModel1DF,
    tradeShows,
    tradeShowsDF,
    witchingHours,
    witchingHoursDF,
    valuEngineStockResearchReport,
    workshops,
    workshopsDF,
)
from .rates import RatesPoints
from .refdata import (
    symbols,
    symbolsDF,
    symbolsList,
    iexSymbols,
    iexSymbolsDF,
    iexSymbolsList,
    mutualFundSymbols,
    mutualFundSymbolsDF,
    mutualFundSymbolsList,
    otcSymbols,
    otcSymbolsDF,
    otcSymbolsList,
    internationalSymbols,
    internationalSymbolsDF,
    internationalSymbolsList,
    fxSymbols,
    fxSymbolsDF,
    fxSymbolsList,
    optionsSymbols,
    optionsSymbolsDF,
    optionsSymbolsList,
    cryptoSymbols,
    cryptoSymbolsDF,
    cryptoSymbolsList,
    corporateActions,
    corporateActionsDF,
    refDividends,
    refDividendsDF,
    nextDayExtDate,
    nextDayExtDateDF,
    directory,
    directoryDF,
    calendar,
    calendarDF,
    holidays,
    holidaysDF,
    exchanges,
    exchangesDF,
    figi,
    figiDF,
    internationalExchanges,
    internationalExchangesDF,
    sectors,
    sectorsDF,
    tags,
    tagsDF,
)
from .rules import (
    schema,
    create,
    lookup,
    pause,
    resume,
    delete,
    rule as ruleInfo,
    rules,
    output as ruleOutput,
)
from .stats import (
    stats,
    statsDF,
    recent,
    recentDF,
    records,
    recordsDF,
    summary,
    summaryDF,
    daily,
    dailyDF,
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
    bulkBatch,
    bulkBatchDF,
    book,
    bookDF,
    bonusIssue,
    bonusIssueDF,
    bulkMinuteBars,
    bulkMinuteBarsDF,
    cashFlow,
    cashFlowDF,
    chart,
    chartDF,
    company,
    companyDF,
    collections,
    collectionsDF,
    delayedQuote,
    delayedQuoteDF,
    distribution,
    distributionDF,
    dividends,
    dividendsDF,
    dividendsBasic,
    dividendsBasicDF,
    earnings,
    earningsDF,
    earningsToday,
    earningsTodayDF,
    estimates,
    estimatesDF,
    financials,
    financialsDF,
    fundOwnership,
    fundOwnershipDF,
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
    marketShortInterest,
    marketShortInterestDF,
    marketVolume,
    marketVolumeDF,
    keyStats,
    keyStatsDF,
    largestTrades,
    largestTradesDF,
    list,
    listDF,
    logo,
    logoPNG,
    logoNotebook,
    news,
    newsDF,
    marketNews,
    marketNewsDF,
    ohlc,
    ohlcDF,
    marketOhlc,
    marketOhlcDF,
    peers,
    peersDF,
    marketYesterday,
    marketYesterdayDF,
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
    splits,
    splitsDF,
    spinoff,
    spinoffDF,
    spread,
    spreadDF,
    stockSplits,
    stockSplitsDF,
    tenQ,
    tenK,
    threshold,
    thresholdDF,
    technicals,
    technicalsDF,
    timeSeriesInventory,
    timeSeries,
    timeSeriesInventoryDF,
    timeSeriesDF,
    upcomingEvents,
    upcomingEventsDF,
    upcomingEarnings,
    upcomingEarningsDF,
    upcomingDividends,
    upcomingDividendsDF,
    upcomingSplits,
    upcomingSplitsDF,
    upcomingIPOs,
    upcomingIPOsDF,
    volumeByVenue,
    volumeByVenueDF,
    yesterday,
    yesterdayDF,
)
from .options import optionExpirations, options, optionsDF

try:
    from .studies import (
        peerCorrelation,
        peerCorrelationPlot,
        returns,
        dailyReturns,
        # Cycle
        ht_dcperiod,
        ht_dcphase,
        ht_phasor,
        ht_sine,
        ht_trendmode,
        # Math
        acos,
        asin,
        atan,
        ceil,
        cos,
        cosh,
        exp,
        floor,
        ln,
        log10,
        sin,
        sinh,
        sqrt,
        tan,
        tanh,
        add,
        div,
        max,
        maxindex,
        min,
        minindex,
        minmax,
        minmaxindex,
        mult,
        sub,
        sum,
        # Momentum
        adx,
        adxr,
        apo,
        aroon,
        aroonosc,
        bop,
        cci,
        cmo,
        dx,
        macd,
        macdext,
        mfi,
        minus_di,
        minus_dm,
        mom,
        plus_di,
        plus_dm,
        ppo,
        roc,
        rocp,
        rocr,
        rocr100,
        rsi,
        stoch,
        stochf,
        stochrsi,
        trix,
        ultosc,
        willr,
        # Overlap
        bollinger,
        dema,
        ema,
        ht_trendline,
        kama,
        mama,
        mavp,
        midpoint,
        midpice,
        sar,
        sarext,
        sma,
        t3,
        tema,
        trima,
        wma,
        # Pattern
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
        # Price
        avgprice,
        medprice,
        typprice,
        wclprice,
        # Statistic
        beta,
        correl,
        linearreg,
        linearreg_angle,
        linearreg_intercept,
        linearreg_slope,
        stddev,
        tsf,
        var,
        # Volatility
        atr,
        natr,
        trange,
        # Volume
        ad,
        adosc,
        obv,
    )

except ImportError:
    peerCorrelation = None
    peerCorrelationPlot = None
    returns = None
    dailyReturns = None

    ht_dcperiod = None
    ht_dcphase = None
    ht_phasor = None
    ht_sine = None
    ht_trendmode = None

    acos = None
    asin = None
    atan = None
    ceil = None
    cos = None
    cosh = None
    exp = None
    floor = None
    ln = None
    log10 = None
    sin = None
    sinh = None
    sqrt = None
    tan = None
    tanh = None
    add = None
    div = None
    max = None
    maxindex = None
    min = None
    minindex = None
    minmax = None
    minmaxindex = None
    mult = None
    sub = None
    sum = None

    adx = None
    adxr = None
    apo = None
    aroon = None
    aroonosc = None
    bop = None
    cci = None
    cmo = None
    dx = None
    macd = None
    macdext = None
    mfi = None
    minus_di = None
    minus_dm = None
    mom = None
    plus_di = None
    plus_dm = None
    ppo = None
    roc = None
    rocp = None
    rocr = None
    rocr100 = None
    rsi = None
    stoch = None
    stochf = None
    stochrsi = None
    trix = None
    ultosc = None
    willr = None

    bollinger = None
    dema = None
    ema = None
    ht_trendline = None
    kama = None
    mama = None
    mavp = None
    midpoint = None
    midpice = None
    sar = None
    sarext = None
    sma = None
    t3 = None
    tema = None
    trima = None
    wma = None

    cdl2crows = None
    cdl3blackcrows = None
    cdl3inside = None
    cdl3linestrike = None
    cdl3outside = None
    cdl3starsinsouth = None
    cdl3whitesoldiers = None
    cdlabandonedbaby = None
    cdladvanceblock = None
    cdlbelthold = None
    cdlbreakaway = None
    cdlclosingmarubozu = None
    cdlconcealbabyswallow = None
    cdlcounterattack = None
    cdldarkcloudcover = None
    cdldoji = None
    cdldojistar = None
    cdldragonflydoji = None
    cdlengulfing = None
    cdleveningdojistar = None
    cdleveningstar = None
    cdlgapsidesidewhite = None
    cdlgravestonedoji = None
    cdlhammer = None
    cdlhangingman = None
    cdlharami = None
    cdlharamicross = None
    cdlhighwave = None
    cdlhikkake = None
    cdlhikkakemod = None
    cdlhomingpigeon = None
    cdlidentical3crows = None
    cdlinneck = None
    cdlinvertedhammer = None
    cdlkicking = None
    cdlkickingbylength = None
    cdlladderbottom = None
    cdllongleggeddoji = None
    cdllongline = None
    cdlmarubozu = None
    cdlmatchinglow = None
    cdlmathold = None
    cdlmorningdojistar = None
    cdlmorningstar = None
    cdlonneck = None
    cdlpiercing = None
    cdlrickshawman = None
    cdlrisefall3methods = None
    cdlseparatinglines = None
    cdlshootingstar = None
    cdlshortline = None
    cdlspinningtop = None
    cdlstalledpattern = None
    cdlsticksandwich = None
    cdltakuri = None
    cdltasukigap = None
    cdlthrusting = None
    cdltristar = None
    cdlunique3river = None
    cdlxsidegap3methods = None

    avgprice = None
    medprice = None
    typprice = None
    wclprice = None

    beta = None
    correl = None
    linearreg = None
    linearreg_angle = None
    linearreg_intercept = None
    linearreg_slope = None
    stddev = None
    tsf = None
    var = None

    atr = None
    natr = None
    trange = None

    ad = None
    adosc = None
    obv = None


DEFAULT_API_LIMIT = 5

_INCLUDE_FUNCTIONS = [
    # Rules
    ("schema", schema),
    ("rules", rules),
    ("createRule", create),
    ("lookupRule", lookup),
    ("pauseRule", pause),
    ("resumeRule", resume),
    ("deleteRule", delete),
    ("ruleInfo", ruleInfo),
    ("ruleOutput", ruleOutput),
    # Refdata
    ("symbols", symbols),
    ("iexSymbols", iexSymbols),
    ("mutualFundSymbols", mutualFundSymbols),
    ("otcSymbols", otcSymbols),
    ("internationalSymbols", internationalSymbols),
    ("fxSymbols", fxSymbols),
    ("optionsSymbols", optionsSymbols),
    ("cryptoSymbols", cryptoSymbols),
    ("symbolsDF", symbolsDF),
    ("iexSymbolsDF", iexSymbolsDF),
    ("mutualFundSymbolsDF", mutualFundSymbolsDF),
    ("otcSymbolsDF", otcSymbolsDF),
    ("internationalSymbolsDF", internationalSymbolsDF),
    ("fxSymbolsDF", fxSymbolsDF),
    ("optionsSymbolsDF", optionsSymbolsDF),
    ("cryptoSymbolsDF", cryptoSymbolsDF),
    ("symbolsList", symbolsList),
    ("iexSymbolsList", iexSymbolsList),
    ("mutualFundSymbolsList", mutualFundSymbolsList),
    ("otcSymbolsList", otcSymbolsList),
    ("internationalSymbolsList", internationalSymbolsList),
    ("fxSymbolsList", fxSymbolsList),
    ("optionsSymbolsList", optionsSymbolsList),
    ("cryptoSymbolsList", cryptoSymbolsList),
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
    ("tags", tags),
    ("tagsDF", tagsDF),
    # Markets
    ("markets", markets),
    ("marketsDF", marketsDF),
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
    ("bulkBatch", bulkBatch),
    ("bulkBatchDF", bulkBatchDF),
    ("book", book),
    ("bookDF", bookDF),
    ("cashFlow", cashFlow),
    ("cashFlowDF", cashFlowDF),
    ("chart", chart),
    ("chartDF", chartDF),
    ("bulkMinuteBars", bulkMinuteBars),
    ("bulkMinuteBarsDF", bulkMinuteBarsDF),
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
    ("threshold", threshold),
    ("thresholdDF", thresholdDF),
    ("shortInterest", shortInterest),
    ("shortInterestDF", shortInterestDF),
    ("marketVolume", marketVolume),
    ("marketVolumeDF", marketVolumeDF),
    ("marketShortInterest", marketShortInterest),
    ("marketShortInterestDF", marketShortInterestDF),
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
    ("marketNews", marketNews),
    ("marketNewsDF", marketNewsDF),
    ("ohlc", ohlc),
    ("ohlcDF", ohlcDF),
    ("marketOhlc", marketOhlc),
    ("marketOhlcDF", marketOhlcDF),
    ("optionExpirations", optionExpirations),
    ("options", options),
    ("optionsDF", optionsDF),
    ("peers", peers),
    ("peersDF", peersDF),
    ("yesterday", yesterday),
    ("yesterdayDF", yesterdayDF),
    ("marketYesterday", marketYesterday),
    ("marketYesterdayDF", marketYesterdayDF),
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
    ("sectorPerformance", sectorPerformance),
    ("sectorPerformanceDF", sectorPerformanceDF),
    ("securityReclassification", securityReclassification),
    ("securityReclassificationDF", securityReclassificationDF),
    ("securitySwap", securitySwap),
    ("securitySwapDF", securitySwapDF),
    ("spinoff", spinoff),
    ("spinoffDF", spinoffDF),
    ("splits", splits),
    ("splitsDF", splitsDF),
    ("stockSplits", stockSplits),
    ("stockSplitsDF", stockSplitsDF),
    ("tenQ", tenQ),
    ("tenK", tenK),
    ("technicals", technicals),
    ("technicalsDF", technicalsDF),
    ("timeSeriesInventory", timeSeriesInventory),
    ("timeSeriesInventoryDF", timeSeriesInventoryDF),
    ("timeSeries", timeSeries),
    ("timeSeriesDF", timeSeriesDF),
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
    # SSE Streaming
    ("topsSSE", topsSSE),
    ("topsSSEAsync", topsSSEAsync),
    ("lastSSE", lastSSE),
    ("lastSSEAsync", lastSSEAsync),
    ("deepSSE", deepSSE),
    ("deepSSEAsync", deepSSEAsync),
    ("tradesSSE", tradesSSE),
    ("tradesSSEAsync", tradesSSEAsync),
    # Stock SSE
    ("stocksUSNoUTPSSE", stocksUSNoUTPSSE),
    ("stocksUSNoUTPSSEAsync", stocksUSNoUTPSSEAsync),
    ("stocksUSSSE", stocksUSSSE),
    ("stocksUSSSEAsync", stocksUSSSEAsync),
    ("stocksUS1SecondSSE", stocksUS1SecondSSE),
    ("stocksUS1SecondSSEAsync", stocksUS1SecondSSEAsync),
    ("stocksUS5SecondSSE", stocksUS5SecondSSE),
    ("stocksUS5SecondSSEAsync", stocksUS5SecondSSEAsync),
    ("stocksUS1MinuteSSE", stocksUS1MinuteSSE),
    ("stocksUS1MinuteSSEAsync", stocksUS1MinuteSSEAsync),
    # TOPS
    ("tops", tops),
    ("topsAsync", topsAsync),
    ("topsDF", topsDF),
    ("last", last),
    ("lastAsync", lastAsync),
    ("lastDF", lastDF),
    ("deep", deep),
    ("deepAsync", deepAsync),
    ("deepDF", deepDF),
    ("hist", hist),
    ("histAsync", histAsync),
    ("histDF", histDF),
    ("auction", auction),
    ("auctionAsync", auctionAsync),
    ("auctionDF", auctionDF),
    ("bookDeep", deepBook),
    ("bookDeepAsync", deepBookAsync),
    ("bookDeepDF", deepBookDF),
    ("officialPrice", officialPrice),
    ("officialPriceAsync", officialPriceAsync),
    ("officialPriceDF", officialPriceDF),
    ("opHaltStatus", opHaltStatus),
    ("opHaltStatusAsync", opHaltStatusAsync),
    ("opHaltStatusDF", opHaltStatusDF),
    ("securityEvent", securityEvent),
    ("securityEventAsync", securityEventAsync),
    ("securityEventDF", securityEventDF),
    ("ssrStatus", ssrStatus),
    ("ssrStatusAsync", ssrStatusAsync),
    ("ssrStatusDF", ssrStatusDF),
    ("systemEvent", systemEvent),
    ("systemEventAsync", systemEventAsync),
    ("systemEventDF", systemEventDF),
    ("trades", trades),
    ("tradesAsync", tradesAsync),
    ("tradesDF", tradesDF),
    ("tradeBreak", tradeBreak),
    ("tradeBreakAsync", tradeBreakAsync),
    ("tradeBreakDF", tradeBreakDF),
    ("tradingStatus", tradingStatus),
    ("tradingStatusAsync", tradingStatusAsync),
    ("tradingStatusDF", tradingStatusDF),
    # Account
    ("messageBudget", messageBudget),
    ("metadata", metadata),
    ("metadataDF", metadataDF),
    ("usage", usage),
    ("usageDF", usageDF),
    # Alternative
    ("crypto", crypto),
    ("cryptoDF", cryptoDF),
    ("sentiment", sentiment),
    ("sentimentDF", sentimentDF),
    ("ceoCompensation", ceoCompensation),
    ("ceoCompensationDF", ceoCompensationDF),
    # Data Points
    ("points", points),
    ("pointsDF", pointsDF),
    # FX
    ("latestFX", latestFX),
    ("latestFXDF", latestFXDF),
    ("convertFX", convertFX),
    ("convertFXDF", convertFXDF),
    ("historicalFX", historicalFX),
    ("historicalFXDF", historicalFXDF),
    # FXSSE
    ("fxSSE", fxSSE),
    ("fxSSEAsync", fxSSEAsync),
    # NewsSSE
    ("newsSSE", newsSSE),
    ("newsSSEAsync", newsSSEAsync),
    # SentimentSSE
    ("sentimentSSE", sentimentSSE),
    ("sentimentSSEAsync", sentimentSSEAsync),
    # Crypto
    ("cryptoBook", cryptoBook),
    ("cryptoBookDF", cryptoBookDF),
    ("cryptoQuote", cryptoQuote),
    ("cryptoQuoteDF", cryptoQuoteDF),
    ("cryptoPrice", cryptoPrice),
    ("cryptoPriceDF", cryptoPriceDF),
    # CryptoSSE
    ("cryptoBookSSE", cryptoBookSSE),
    ("cryptoBookSSEAsync", cryptoBookSSEAsync),
    ("cryptoEventsSSE", cryptoEventsSSE),
    ("cryptoEventsSSEAsync", cryptoEventsSSEAsync),
    ("cryptoQuotesSSE", cryptoQuotesSSE),
    ("cryptoQuotesSSEAsync", cryptoQuotesSSEAsync),
    # Premium
    #     Wall Street Horizon
    ("analystDays", analystDays),
    ("analystDaysDF", analystDaysDF),
    ("boardOfDirectorsMeeting", boardOfDirectorsMeeting),
    ("boardOfDirectorsMeetingDF", boardOfDirectorsMeetingDF),
    ("businessUpdates", businessUpdates),
    ("businessUpdatesDF", businessUpdatesDF),
    ("buybacks", buybacks),
    ("buybacksDF", buybacksDF),
    ("capitalMarketsDay", capitalMarketsDay),
    ("capitalMarketsDayDF", capitalMarketsDayDF),
    ("companyTravel", companyTravel),
    ("companyTravelDF", companyTravelDF),
    ("filingDueDates", filingDueDates),
    ("filingDueDatesDF", filingDueDatesDF),
    ("fiscalQuarterEnd", fiscalQuarterEnd),
    ("fiscalQuarterEndDF", fiscalQuarterEndDF),
    ("forum", forum),
    ("forumDF", forumDF),
    ("generalConference", generalConference),
    ("generalConferenceDF", generalConferenceDF),
    ("fdaAdvisoryCommitteeMeetings", fdaAdvisoryCommitteeMeetings),
    ("fdaAdvisoryCommitteeMeetingsDF", fdaAdvisoryCommitteeMeetingsDF),
    ("holidaysWSH", holidaysWSH),
    ("holidaysWSHDF", holidaysWSHDF),
    ("indexChanges", indexChanges),
    ("indexChangesDF", indexChangesDF),
    ("iposWSH", iposWSH),
    ("iposWSHDF", iposWSHDF),
    ("legalActions", legalActions),
    ("legalActionsDF", legalActionsDF),
    ("mergersAndAcquisitions", mergersAndAcquisitions),
    ("mergersAndAcquisitionsDF", mergersAndAcquisitionsDF),
    ("productEventsDF", productEventsDF),
    ("productEvents", productEvents),
    ("researchAndDevelopmentDays", researchAndDevelopmentDays),
    ("researchAndDevelopmentDaysDF", researchAndDevelopmentDaysDF),
    ("sameStoreSales", sameStoreSales),
    ("sameStoreSalesDF", sameStoreSalesDF),
    ("secondaryOfferings", secondaryOfferings),
    ("secondaryOfferingsDF", secondaryOfferingsDF),
    ("seminars", seminars),
    ("seminarsDF", seminarsDF),
    ("shareholderMeetings", shareholderMeetings),
    ("shareholderMeetingsDF", shareholderMeetingsDF),
    ("summitMeetings", summitMeetings),
    ("summitMeetingsDF", summitMeetingsDF),
    ("tradeShows", tradeShows),
    ("tradeShowsDF", tradeShowsDF),
    ("witchingHours", witchingHours),
    ("witchingHoursDF", witchingHoursDF),
    ("workshops", workshops),
    ("workshopsDF", workshopsDF),
    #     Fraud Factors
    ("nonTimelyFilings", nonTimelyFilings),
    ("nonTimelyFilingsDF", nonTimelyFilingsDF),
    ("similarityIndex", similarityIndex),
    ("similarityIndexDF", similarityIndexDF),
    #     Extract Alpha
    ("cam1", cam1),
    ("cam1DF", cam1DF),
    ("esgCFPBComplaints", esgCFPBComplaints),
    ("esgCFPBComplaintsDF", esgCFPBComplaintsDF),
    ("esgCPSCRecalls", esgCPSCRecalls),
    ("esgCPSCRecallsDF", esgCPSCRecallsDF),
    ("esgDOLVisaApplications", esgDOLVisaApplications),
    ("esgDOLVisaApplicationsDF", esgDOLVisaApplicationsDF),
    ("esgEPAEnforcements", esgEPAEnforcements),
    ("esgEPAEnforcementsDF", esgEPAEnforcementsDF),
    ("esgEPAMilestones", esgEPAMilestones),
    ("esgEPAMilestonesDF", esgEPAMilestonesDF),
    ("esgFECIndividualCampaingContributions", esgFECIndividualCampaingContributions),
    (
        "esgFECIndividualCampaingContributionsDF",
        esgFECIndividualCampaingContributionsDF,
    ),
    ("esgOSHAInspections", esgOSHAInspections),
    ("esgOSHAInspectionsDF", esgOSHAInspectionsDF),
    ("esgSenateLobbying", esgSenateLobbying),
    ("esgSenateLobbyingDF", esgSenateLobbyingDF),
    ("esgUSASpending", esgUSASpending),
    ("esgUSASpendingDF", esgUSASpendingDF),
    ("esgUSPTOPatentApplications", esgUSPTOPatentApplications),
    ("esgUSPTOPatentApplicationsDF", esgUSPTOPatentApplicationsDF),
    ("esgUSPTOPatentGrants", esgUSPTOPatentGrants),
    ("esgUSPTOPatentGrantsDF", esgUSPTOPatentGrantsDF),
    ("tacticalModel1", tacticalModel1),
    ("tacticalModel1DF", tacticalModel1DF),
    #     Precision Alpha
    ("precisionAlphaPriceDynamics", precisionAlphaPriceDynamics),
    ("precisionAlphaPriceDynamicsDF", precisionAlphaPriceDynamicsDF),
    #     BRAIN Company
    ("brain30DaySentiment", brain30DaySentiment),
    ("brain30DaySentimentDF", brain30DaySentimentDF),
    ("brain7DaySentiment", brain7DaySentiment),
    ("brain7DaySentimentDF", brain7DaySentimentDF),
    ("brain21DayMLReturnRanking", brain21DayMLReturnRanking),
    ("brain21DayMLReturnRankingDF", brain21DayMLReturnRankingDF),
    ("brain10DayMLReturnRanking", brain10DayMLReturnRanking),
    ("brain10DayMLReturnRankingDF", brain10DayMLReturnRankingDF),
    ("brain5DayMLReturnRanking", brain5DayMLReturnRanking),
    ("brain5DayMLReturnRankingDF", brain5DayMLReturnRankingDF),
    ("brain3DayMLReturnRanking", brain3DayMLReturnRanking),
    ("brain3DayMLReturnRankingDF", brain3DayMLReturnRankingDF),
    ("brain2DayMLReturnRanking", brain2DayMLReturnRanking),
    ("brain2DayMLReturnRankingDF", brain2DayMLReturnRankingDF),
    (
        "brainLanguageMetricsOnCompanyFilingsAll",
        brainLanguageMetricsOnCompanyFilingsAll,
    ),
    (
        "brainLanguageMetricsOnCompanyFilingsAllDF",
        brainLanguageMetricsOnCompanyFilingsAllDF,
    ),
    ("brainLanguageMetricsOnCompanyFilings", brainLanguageMetricsOnCompanyFilings),
    ("brainLanguageMetricsOnCompanyFilingsDF", brainLanguageMetricsOnCompanyFilingsDF),
    (
        "brainLanguageMetricsOnCompanyFilingsDifferenceAll",
        brainLanguageMetricsOnCompanyFilingsDifferenceAll,
    ),
    (
        "brainLanguageMetricsOnCompanyFilingsDifferenceAllDF",
        brainLanguageMetricsOnCompanyFilingsDifferenceAllDF,
    ),
    (
        "brainLanguageMetricsOnCompanyFilingsDifference",
        brainLanguageMetricsOnCompanyFilingsDifference,
    ),
    (
        "brainLanguageMetricsOnCompanyFilingsDifferenceDF",
        brainLanguageMetricsOnCompanyFilingsDifferenceDF,
    ),
    #     Kavout
    ("kScore", kScore),
    ("kScoreDF", kScoreDF),
    ("kScoreChina", kScoreChina),
    ("kScoreChinaDF", kScoreChinaDF),
    #     Audit Analytics
    ("accountingQualityAndRiskMatrix", accountingQualityAndRiskMatrix),
    ("accountingQualityAndRiskMatrixDF", accountingQualityAndRiskMatrixDF),
    ("directorAndOfficerChanges", directorAndOfficerChanges),
    ("directorAndOfficerChangesDF", directorAndOfficerChangesDF),
    #     ValuEngine
    ("valuEngineStockResearchReport", valuEngineStockResearchReport),
]

_INCLUDE_POINTS = [
    # Rates
    ("thirtyYear", RatesPoints.THIRTY.value),
    ("twentyYear", RatesPoints.TWENTY.value),
    ("tenYear", RatesPoints.TEN.value),
    ("fiveYear", RatesPoints.FIVE.value),
    ("twoYear", RatesPoints.TWO.value),
    ("oneYear", RatesPoints.ONE.value),
    ("sixMonth", RatesPoints.SIXMONTH.value),
    ("threeMonth", RatesPoints.THREEMONTH.value),
    ("oneMonth", RatesPoints.ONEMONTH.value),
    # Commodities
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
    # Economic
    ("us30", EconomicPoints.US30.value),
    ("us15", EconomicPoints.US15.value),
    ("us5", EconomicPoints.US5.value),
    ("fedfunds", EconomicPoints.FEDFUNDS.value),
    ("creditcard", EconomicPoints.CREDITCARD.value),
    ("cdnj", EconomicPoints.CDNJ.value),
    ("cdj", EconomicPoints.CDJ.value),
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

_INCLUDE_STUDIES = [
    ("peerCorrelation", peerCorrelation),
    ("peerCorrelationPlot", peerCorrelationPlot),
    ("returns", returns),
    ("dailyReturns", dailyReturns),
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

    def __init__(self, api_token=None, version="v1", api_limit=DEFAULT_API_LIMIT):
        self._token = api_token or os.environ.get("IEX_TOKEN", "")
        if not self._token:
            raise PyEXception("API Token missing or not in environment (IEX_TOKEN)")

        if version not in ("beta", "stable", "v1", "sandbox"):
            raise PyEXception("Unrecognized api version: {}".format(version))

        if self._token.startswith("T") and version != "sandbox":
            raise PyEXception(
                "Using test key but attempting to connect to non-sandbox environment"
            )

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
        meth = kwargs.pop("meth")
        if not meth:
            raise PyEXception("Must provide method!")
        return meth(token=self._token, version=self._version, *args, **kwargs)

    def account(self, *args, **kwargs):
        return self.metadata(*args, **kwargs)


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
