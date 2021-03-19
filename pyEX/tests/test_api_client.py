import pyEX as p


class TestPyEXClientAPI:
    def test_all(self):
        c = p.Client("pk_123")

        for meth in ("schema", "rules", "createRule", "lookupRule", "pauseRule", "resumeRule", "deleteRule", "ruleInfo", "ruleOutput"):
            assert hasattr(c, meth)
            assert hasattr(c.rules, meth)

        for meth in ("symbols", "iexSymbols", "mutualFundSymbols", "otcSymbols", "internationalSymbols", "fxSymbols", "optionsSymbols", "cryptoSymbols", "symbolsDF", "iexSymbolsDF", "mutualFundSymbolsDF", "otcSymbolsDF", "internationalSymbolsDF", "fxSymbolsDF", "optionsSymbolsDF", "cryptoSymbolsDF", "symbolsList", "iexSymbolsList", "mutualFundSymbolsList", "otcSymbolsList", "internationalSymbolsList", "fxSymbolsList", "optionsSymbolsList", "cryptoSymbolsList", "isinLookup", "isinLookupDF", "corporateActions", "corporateActionsDF", "refDividends", "refDividendsDF", "nextDayExtDate", "nextDayExtDateDF", "directory", "directoryDF", "calendar", "calendarDF", "holidays", "holidaysDF", "exchanges", "exchangesDF", "figi", "figiDF", "internationalExchanges", "internationalExchangesDF", "sectors", "sectorsDF", "search", "searchDF", "tags", "tagsDF"):
            assert hasattr(c, meth)
            assert hasattr(c.refdata, meth)

        for meth in ("markets", "marketsDF", "marketVolume", "marketVolumeDF", "marketShortInterest", "marketShortInterestDF", "marketNews", "marketNewsDF", "marketOhlc", "marketOhlcDF", "marketPrevious", "marketPreviousDF", "marketYesterday", "marketYesterdayDF", "sectorPerformance", "sectorPerformanceDF"):
            assert hasattr(c, meth)
            assert hasattr(c.market, meth)

        for meth in ("systemStats", "systemStatsDF", "recent", "recentDF", "records", "recordsDF", "summary", "summaryDF", "daily", "dailyDF"):
            assert hasattr(c, meth)
            assert hasattr(c.stats, meth)

        for meth in ("advancedStats", "advancedStatsDF", "analystRecommendations", "analystRecommendationsDF", "balanceSheet", "balanceSheetDF", "batch", "batchDF", "bonusIssue", "bonusIssueDF", "bulkBatch", "bulkBatchDF", "book", "bookDF", "cashFlow", "cashFlowDF", "chart", "chartDF", "bulkMinuteBars", "bulkMinuteBarsDF", "company", "companyDF", "collections", "collectionsDF", "delayedQuote", "delayedQuoteDF", "distribution", "distributionDF", "dividends", "dividendsBasic", "dividendsDF", "dividendsBasicDF", "earnings", "earningsDF", "earningsToday", "earningsTodayDF", "spread", "spreadDF", "financials", "financialsDF", "fundOwnership", "fundOwnershipDF", "fundamentals", "fundamentalsDF", "incomeStatement", "incomeStatementDF", "insiderRoster", "insiderRosterDF", "insiderSummary", "insiderSummaryDF", "insiderTransactions", "insiderTransactionsDF", "institutionalOwnership", "institutionalOwnershipDF", "intraday", "intradayDF", "ipoToday", "ipoTodayDF", "ipoUpcoming", "ipoUpcomingDF", "threshold", "thresholdDF", "shortInterest", "shortInterestDF", "estimates", "estimatesDF", "keyStats", "keyStatsDF", "largestTrades", "largestTradesDF", "list", "listDF", "logo", "logoPNG", "logoNotebook", "news", "newsDF", "ohlc", "ohlcDF", "optionExpirations", "options", "optionsDF", "peers", "peersDF", "previous", "previousDF", "yesterday", "yesterdayDF", "price", "priceDF", "priceTarget", "priceTargetDF", "quote", "quoteDF", "relevant", "relevantDF", "returnOfCapital", "returnOfCapitalDF", "rightsIssue", "rightsIssueDF", "rightToPurchase", "rightToPurchaseDF", "securityReclassification", "securityReclassificationDF", "securitySwap", "securitySwapDF", "spinoff", "spinoffDF", "splits", "splitsDF", "stockSplits", "stockSplitsDF", "tenQ", "tenK", "technicals", "technicalsDF", "timeSeriesInventory", "timeSeriesInventoryDF", "timeSeries", "timeSeriesDF", "upcomingEvents", "upcomingEventsDF", "upcomingEarnings", "upcomingEarningsDF", "upcomingDividends", "upcomingDividendsDF", "upcomingSplits", "upcomingSplitsDF", "upcomingIPOs", "upcomingIPOsDF", "volumeByVenue", "volumeByVenueDF"):
            assert hasattr(c, meth)
            assert hasattr(c.stocks, meth)

        for meth in ("iexAuction", "iexAuctionAsync", "iexAuctionDF", "iexBook", "iexBookAsync", "iexBookDF", "iexDeep", "iexDeepAsync", "iexDeepDF", "iexHist", "iexHistAsync", "iexHistDF", "iexLast", "iexLastAsync", "iexLastDF", "iexOfficialPrice", "iexOfficialPriceAsync", "iexOfficialPriceDF", "iexOpHaltStatus", "iexOpHaltStatusAsync", "iexOpHaltStatusDF", "iexSecurityEvent", "iexSecurityEventAsync", "iexSecurityEventDF", "iexSsrStatus", "iexSsrStatusAsync", "iexSsrStatusDF", "iexSystemEvent", "iexSystemEventAsync", "iexSystemEventDF", "iexTops", "iexTopsAsync", "iexTopsDF", "iexTradeBreak", "iexTradeBreakAsync", "iexTradeBreakDF", "iexTrades", "iexTradesAsync", "iexTradesDF", "iexTradingStatus", "iexTradingStatusAsync", "iexTradingStatusDF"):
            assert hasattr(c, meth)
            assert hasattr(c.iex, meth)

        for meth in ("topsSSE", "topsSSEAsync", "lastSSE", "lastSSEAsync", "deepSSE", "deepSSEAsync", "tradesSSE", "tradesSSEAsync", "stocksUSNoUTPSSE", "stocksUSNoUTPSSEAsync", "stocksUSSSE", "stocksUSSSEAsync", "stocksUS1SecondSSE", "stocksUSNoUTP1SecondSSE", "stocksUS1SecondSSEAsync", "stocksUSNoUTP1SecondSSEAsync", "stocksUS5SecondSSE", "stocksUSNoUTP5SecondSSE", "stocksUS5SecondSSEAsync", "stocksUSNoUTP5SecondSSEAsync", "stocksUS1MinuteSSE", "stocksUSNoUTP1MinuteSSE", "stocksUS1MinuteSSEAsync", "stocksUSNoUTP1MinuteSSEAsync", "fxSSE", "fxSSEAsync", "forex1SecondSSE", "forex1SecondSSEAsync", "forex5SecondSSE", "forex5SecondSSEAsync", "forex1MinuteSSE", "forex1MinuteSSEAsync", "newsSSE", "newsSSEAsync", "sentimentSSE", "sentimentSSEAsync", "cryptoBookSSE", "cryptoBookSSEAsync", "cryptoEventsSSE", "cryptoEventsSSEAsync", "cryptoQuotesSSE", "cryptoQuotesSSEAsync"):
            assert hasattr(c, meth)
            assert hasattr(c.streaming, meth)

        for meth in ("topsSSE", "topsSSEAsync", "lastSSE", "lastSSEAsync", "deepSSE", "deepSSEAsync", "tradesSSE", "tradesSSEAsync", "stocksUSNoUTPSSE", "stocksUSNoUTPSSEAsync", "stocksUSSSE", "stocksUSSSEAsync", "stocksUS1SecondSSE", "stocksUSNoUTP1SecondSSE", "stocksUS1SecondSSEAsync", "stocksUSNoUTP1SecondSSEAsync", "stocksUS5SecondSSE", "stocksUSNoUTP5SecondSSE", "stocksUS5SecondSSEAsync", "stocksUSNoUTP5SecondSSEAsync", "stocksUS1MinuteSSE", "stocksUSNoUTP1MinuteSSE", "stocksUS1MinuteSSEAsync", "stocksUSNoUTP1MinuteSSEAsync", "fxSSE", "fxSSEAsync", "forex1SecondSSE", "forex1SecondSSEAsync", "forex5SecondSSE", "forex5SecondSSEAsync", "forex1MinuteSSE", "forex1MinuteSSEAsync", "newsSSE", "newsSSEAsync", "sentimentSSE", "sentimentSSEAsync", "cryptoBookSSE", "cryptoBookSSEAsync", "cryptoEventsSSE", "cryptoEventsSSEAsync", "cryptoQuotesSSE", "cryptoQuotesSSEAsync"):
            assert hasattr(c, meth)
            assert hasattr(c.account, meth)

"messageBudget", "metadata", "metadataDF", "usage", "usageDF",

_INCLUDE_FUNCTIONS_ALTERNATIVE = [
    # Alternative
    ("sentiment", sentiment),
    ("sentimentDF", sentimentDF),
    ("ceoCompensation", ceoCompensation),
    ("ceoCompensationDF", ceoCompensationDF),
]

_INCLUDE_FUNCTIONS_POINTS = [
    # Data Points
    ("points", points),
    ("pointsDF", pointsDF),
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
    ("cryptoBookDF", cryptoBookDF),
    ("cryptoQuote", cryptoQuote),
    ("cryptoQuoteDF", cryptoQuoteDF),
    ("cryptoPrice", cryptoPrice),
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
    + _INCLUDE_FUNCTIONS_FX
    + _INCLUDE_FUNCTIONS_CRYPTO
)

_INCLUDE_FILES = [
    # Files
    ("files", files),
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
    ("similarityIndex", similarityIndexFraudFactors),
    ("similarityIndexDF", similarityIndexFraudFactorsDF),
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
]

_INCLUDE_POINTS_COMMODITIES = [
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
]

_INCLUDE_POINTS_ECONOMIC = [
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

