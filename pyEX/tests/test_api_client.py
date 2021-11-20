# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import pyEX as p

_PREEXISTING = [
    "Enum",
    "__annotations__",
    "__builtins__",
    "__cached__",
    "__call__",
    "__class__",
    "__class_getitem__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__file__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__loader__",
    "__lt__",
    "__module__",
    "__name__",
    "__ne__",
    "__new__",
    "__package__",
    "__path__",
    "__qualname__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__setstate__",
    "__sizeof__",
    "__spec__",
    "__str__",
    "__subclasshook__",
    "__wrapped__",
    "args",
    "func",
    "keywords",
]


class TestPyEXClientAPI:
    def setup(self):
        self.c = p.Client("pk_123")

    def test_all_rules(self):
        all = set(dir(self.c.rules))
        found = set(_PREEXISTING)

        for meth in (
            "schema",
            "listRules",
            "createRule",
            "lookupRule",
            "pauseRule",
            "resumeRule",
            "deleteRule",
            "ruleInfo",
            "ruleOutput",
        ):
            assert hasattr(self.c.rules, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_platform(self):
        all = set(dir(self.c.platform))
        found = set(_PREEXISTING)

        for meth in (
            "createDataset",
            "createDatasetAsync",
            "deleteData",
            "deleteDataAsync",
            "deleteDataset",
            "deleteDatasetAsync",
            "listDatasets",
            "listDatasetsAsync",
            "listDatasetsDF",
            "listJobs",
            "loadData",
            "loadDataAsync",
            "modifyDataset",
            "modifyDatasetAsync",
            "modifyData",
            "modifyDataAsync",
            "query",
            "queryAsync",
            "queryDF",
            "queryMeta",
            "queryMetaAsync",
            "queryMetaDF",
        ):
            assert hasattr(self.c.platform, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_refdata(self):
        all = set(dir(self.c.refdata))
        found = set(_PREEXISTING)

        for meth in (
            "symbols",
            "iexSymbols",
            "mutualFundSymbols",
            "otcSymbols",
            "internationalSymbols",
            "fxSymbols",
            "optionsSymbols",
            "cryptoSymbols",
            "futuresSymbols",
            "symbolsDF",
            "iexSymbolsDF",
            "mutualFundSymbolsDF",
            "otcSymbolsDF",
            "internationalSymbolsDF",
            "fxSymbolsDF",
            "optionsSymbolsDF",
            "cryptoSymbolsDF",
            "futuresSymbolsDF",
            "symbolsList",
            "iexSymbolsList",
            "mutualFundSymbolsList",
            "otcSymbolsList",
            "internationalSymbolsList",
            "fxSymbolsList",
            "optionsSymbolsList",
            "cryptoSymbolsList",
            "futuresSymbolsList",
            "isinLookup",
            "isinLookupDF",
            "ricLookup",
            "ricLookupDF",
            "corporateActions",
            "corporateActionsDF",
            "refDividends",
            "refDividendsDF",
            "nextDayExtDate",
            "nextDayExtDateDF",
            "directory",
            "directoryDF",
            "calendar",
            "calendarDF",
            "holidays",
            "holidaysDF",
            "exchanges",
            "exchangesDF",
            "figi",
            "figiDF",
            "internationalExchanges",
            "internationalExchangesDF",
            "sectors",
            "sectorsDF",
            "search",
            "searchDF",
            "tags",
            "tagsDF",
            "queryMetadata",
            "queryMetadataDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.refdata, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_markets(self):
        all = set(dir(self.c.market))
        found = set(_PREEXISTING)

        for meth in (
            "markets",
            "marketsDF",
            "marketVolume",
            "marketVolumeDF",
            "marketShortInterest",
            "marketShortInterestDF",
            "marketNews",
            "marketNewsDF",
            "marketOhlc",
            "marketOhlcDF",
            "marketPrevious",
            "marketPreviousDF",
            "marketYesterday",
            "marketYesterdayDF",
            "sectorPerformance",
            "sectorPerformanceDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.market, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_stats(self):
        all = set(dir(self.c.stats))
        found = set(_PREEXISTING)

        for meth in (
            "systemStats",
            "systemStatsDF",
            "recent",
            "recentDF",
            "records",
            "recordsDF",
            "summary",
            "summaryDF",
            "daily",
            "dailyDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.stats, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_ts(self):
        for meth in (
            "timeSeriesInventory",
            "timeSeriesInventoryAsync",
            "timeSeriesInventoryDF",
            "timeSeries",
            "timeSeriesAsync",
            "timeSeriesDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c, meth)

    def test_all_stock(self):
        all = set(dir(self.c.stocks))
        found = set(_PREEXISTING)

        for meth in (
            "advancedStats",
            "advancedStatsDF",
            "analystRecommendations",
            "analystRecommendationsDF",
            "balanceSheet",
            "balanceSheetDF",
            "batch",
            "batchDF",
            "bonusIssue",
            "bonusIssueDF",
            "book",
            "bookDF",
            "cashFlow",
            "cashFlowDF",
            "chart",
            "chartDF",
            "ceoCompensation",
            "ceoCompensationDF",
            "company",
            "companyDF",
            "collections",
            "collectionsDF",
            "delayedQuote",
            "delayedQuoteDF",
            "distribution",
            "distributionDF",
            "dividends",
            "dividendsBasic",
            "dividendsDF",
            "dividendsBasicDF",
            "dividendsForecast",
            "dividendsForecastDF",
            "earnings",
            "earningsDF",
            "earningsToday",
            "earningsTodayDF",
            "spread",
            "spreadDF",
            "financials",
            "financialsDF",
            "fortyF",
            "fundOwnership",
            "fundOwnershipDF",
            "fundamentals",
            "fundamentalsDF",
            "fundamentalValuations",
            "fundamentalValuationsDF",
            "incomeStatement",
            "incomeStatementDF",
            "insiderRoster",
            "insiderRosterDF",
            "insiderSummary",
            "insiderSummaryDF",
            "insiderTransactions",
            "insiderTransactionsDF",
            "institutionalOwnership",
            "institutionalOwnershipDF",
            "intraday",
            "intradayDF",
            "ipoToday",
            "ipoTodayDF",
            "ipoUpcoming",
            "ipoUpcomingDF",
            "shortInterest",
            "shortInterestDF",
            "estimates",
            "estimatesDF",
            "keyStats",
            "keyStatsDF",
            "largestTrades",
            "largestTradesDF",
            "list",
            "listDF",
            "logo",
            "logoPNG",
            "logoNotebook",
            "news",
            "newsDF",
            "ohlc",
            "ohlcDF",
            "optionExpirations",
            "stockOptions",
            "stockOptionsDF",
            "peers",
            "peersDF",
            "previous",
            "previousDF",
            "yesterday",
            "yesterdayDF",
            "price",
            "priceDF",
            "priceTarget",
            "priceTargetDF",
            "quote",
            "quoteDF",
            "relevant",
            "relevantDF",
            "returnOfCapital",
            "returnOfCapitalDF",
            "rightsIssue",
            "rightsIssueDF",
            "rightToPurchase",
            "rightToPurchaseDF",
            "securityReclassification",
            "securityReclassificationDF",
            "securitySwap",
            "securitySwapDF",
            "spinoff",
            "spinoffDF",
            "splits",
            "splitsDF",
            "splitsBasic",
            "splitsBasicDF",
            "tenQ",
            "tenK",
            "technicals",
            "technicalsDF",
            "twentyF",
            "upcomingEvents",
            "upcomingEventsDF",
            "upcomingEarnings",
            "upcomingEarningsDF",
            "upcomingDividends",
            "upcomingDividendsDF",
            "upcomingSplits",
            "upcomingSplitsDF",
            "upcomingIPOs",
            "upcomingIPOsDF",
            "volumeByVenue",
            "volumeByVenueDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.stocks, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_iex(self):
        all = set(dir(self.c.iex))
        found = set(_PREEXISTING)

        for meth in (
            "iexAuction",
            "iexAuctionAsync",
            "iexAuctionDF",
            "iexBook",
            "iexBookAsync",
            "iexBookDF",
            "iexDeep",
            "iexDeepAsync",
            "iexDeepDF",
            "iexHist",
            "iexHistAsync",
            "iexHistDF",
            "iexLast",
            "iexLastAsync",
            "iexLastDF",
            "iexOfficialPrice",
            "iexOfficialPriceAsync",
            "iexOfficialPriceDF",
            "iexOpHaltStatus",
            "iexOpHaltStatusAsync",
            "iexOpHaltStatusDF",
            "iexSecurityEvent",
            "iexSecurityEventAsync",
            "iexSecurityEventDF",
            "iexSsrStatus",
            "iexSsrStatusAsync",
            "iexSsrStatusDF",
            "iexSystemEvent",
            "iexSystemEventAsync",
            "iexSystemEventDF",
            "iexTops",
            "iexTopsAsync",
            "iexTopsDF",
            "iexTradeBreak",
            "iexTradeBreakAsync",
            "iexTradeBreakDF",
            "iexTrades",
            "iexTradesAsync",
            "iexTradesDF",
            "iexTradingStatus",
            "iexTradingStatusAsync",
            "iexTradingStatusDF",
            "iexThreshold",
            "iexThresholdDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.iex, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_streaming(self):
        all = set(dir(self.c.streaming))
        found = set(_PREEXISTING)

        for meth in (
            "topsSSE",
            "topsSSEAsync",
            "lastSSE",
            "lastSSEAsync",
            "deepSSE",
            "deepSSEAsync",
            "tradesSSE",
            "tradesSSEAsync",
            "stocksUSNoUTPSSE",
            "stocksUSNoUTPSSEAsync",
            "stocksUSSSE",
            "stocksUSSSEAsync",
            "stocksUS1SecondSSE",
            "stocksUSNoUTP1SecondSSE",
            "stocksUS1SecondSSEAsync",
            "stocksUSNoUTP1SecondSSEAsync",
            "stocksUS5SecondSSE",
            "stocksUSNoUTP5SecondSSE",
            "stocksUS5SecondSSEAsync",
            "stocksUSNoUTP5SecondSSEAsync",
            "stocksUS1MinuteSSE",
            "stocksUSNoUTP1MinuteSSE",
            "stocksUS1MinuteSSEAsync",
            "stocksUSNoUTP1MinuteSSEAsync",
            "fxSSE",
            "fxSSEAsync",
            "forex1SecondSSE",
            "forex1SecondSSEAsync",
            "forex5SecondSSE",
            "forex5SecondSSEAsync",
            "forex1MinuteSSE",
            "forex1MinuteSSEAsync",
            "newsSSE",
            "newsSSEAsync",
            "sentimentSSE",
            "sentimentSSEAsync",
            "cryptoBookSSE",
            "cryptoBookSSEAsync",
            "cryptoEventsSSE",
            "cryptoEventsSSEAsync",
            "cryptoQuotesSSE",
            "cryptoQuotesSSEAsync",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.streaming, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_account(self):
        for meth in (
            "messageBudget",
            "messageBudgetAsync",
            "metadata",
            "metadataAsync",
            "metadataDF",
            "usage",
            "usageAsync",
            "usageDF",
            "payAsYouGo",
            "payAsYouGoAsync",
        ):
            assert hasattr(self.c, meth)

    def test_all_alternative(self):
        all = set(dir(self.c.alternative))
        found = set(_PREEXISTING)

        for meth in (
            "sentiment",
            "sentimentAsync",
            "sentimentDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.alternative, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_points(self):
        all = set(dir(self.c.points))
        found = set(_PREEXISTING)

        for meth in ("points", "pointsDF"):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.points, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_fx(self):
        all = set(dir(self.c.fx))
        found = set(_PREEXISTING)

        for meth in (
            "latestFX",
            "latestFXDF",
            "convertFX",
            "convertFXDF",
            "historicalFX",
            "historicalFXDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.fx, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_futures(self):
        for meth in (
            "futures",
            "futuresDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.futures, meth)

    def test_all_options(self):
        for meth in (
            "options",
            "optionsDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.options, meth)

    def test_all_crypto(self):
        all = set(dir(self.c.crypto))
        found = set(_PREEXISTING)

        for meth in (
            "cryptoBook",
            "cryptoBookAsync",
            "cryptoBookDF",
            "cryptoQuote",
            "cryptoQuoteAsync",
            "cryptoQuoteDF",
            "cryptoPrice",
            "cryptoPriceAsync",
            "cryptoPriceDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.crypto, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_files(self):
        all = set(dir(self.c.files))
        found = set(_PREEXISTING)

        for meth in ("file", "download"):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.files, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_premium(self):
        all = set(dir(self.c.premium))
        found = set(_PREEXISTING)

        for meth in (
            "analystDays",
            "analystDaysDF",
            "analystRecommendationsAndPriceTargets",
            "analystRecommendationsAndPriceTargetsDF",
            "analystRecommendations",
            "analystRecommendationsDF",
            "boardOfDirectorsMeeting",
            "boardOfDirectorsMeetingDF",
            "businessUpdates",
            "businessUpdatesDF",
            "buybacks",
            "buybacksDF",
            "capitalMarketsDay",
            "capitalMarketsDayDF",
            "companyTravel",
            "companyTravelDF",
            "earnings",
            "earningsDF",
            "estimates",
            "estimatesDF",
            "files",
            "filingDueDates",
            "filingDueDatesDF",
            "fiscalQuarterEnd",
            "fiscalQuarterEndDF",
            "forum",
            "forumDF",
            "generalConference",
            "generalConferenceDF",
            "fdaAdvisoryCommitteeMeetings",
            "fdaAdvisoryCommitteeMeetingsDF",
            "holidays",
            "holidaysDF",
            "indexChanges",
            "indexChangesDF",
            "ipos",
            "iposDF",
            "legalActions",
            "legalActionsDF",
            "mergersAndAcquisitions",
            "mergersAndAcquisitionsDF",
            "news",
            "newsDF",
            "priceTarget",
            "priceTargetDF",
            "productEvents",
            "productEventsDF",
            "researchAndDevelopmentDays",
            "researchAndDevelopmentDaysDF",
            "sameStoreSales",
            "sameStoreSalesDF",
            "secondaryOfferings",
            "secondaryOfferingsDF",
            "seminars",
            "seminarsDF",
            "shareholderMeetings",
            "shareholderMeetingsDF",
            "socialSentiment",
            "socialSentimentDF",
            "summitMeetings",
            "summitMeetingsDF",
            "tradeShows",
            "tradeShowsDF",
            "witchingHours",
            "witchingHoursDF",
            "workshops",
            "workshopsDF",
            "nonTimelyFilings",
            "nonTimelyFilingsDF",
            "cam1",
            "cam1DF",
            "esgCFPBComplaints",
            "esgCFPBComplaintsDF",
            "esgCPSCRecalls",
            "esgCPSCRecallsDF",
            "esgDOLVisaApplications",
            "esgDOLVisaApplicationsDF",
            "esgEPAEnforcements",
            "esgEPAEnforcementsDF",
            "esgEPAMilestones",
            "esgEPAMilestonesDF",
            "esgFECIndividualCampaingContributions",
            "esgFECIndividualCampaingContributionsDF",
            "esgOSHAInspections",
            "esgOSHAInspectionsDF",
            "esgSenateLobbying",
            "esgSenateLobbyingDF",
            "esgUSASpending",
            "esgUSASpendingDF",
            "esgUSPTOPatentApplications",
            "esgUSPTOPatentApplicationsDF",
            "esgUSPTOPatentGrants",
            "esgUSPTOPatentGrantsDF",
            "tacticalModel1",
            "tacticalModel1DF",
            "precisionAlphaPriceDynamics",
            "precisionAlphaPriceDynamicsDF",
            "thirtyDaySentiment",
            "thirtyDaySentimentDF",
            "sevenDaySentiment",
            "sevenDaySentimentDF",
            "twentyOneDayMLReturnRanking",
            "twentyOneDayMLReturnRankingDF",
            "tenDayMLReturnRanking",
            "tenDayMLReturnRankingDF",
            "fiveDayMLReturnRanking",
            "fiveDayMLReturnRankingDF",
            "threeDayMLReturnRanking",
            "threeDayMLReturnRankingDF",
            "twoDayMLReturnRanking",
            "twoDayMLReturnRankingDF",
            "languageMetricsOnCompanyFilingsAll",
            "languageMetricsOnCompanyFilingsAllDF",
            "languageMetricsOnCompanyFilings",
            "languageMetricsOnCompanyFilingsDF",
            "languageMetricsOnCompanyFilingsDifferenceAll",
            "languageMetricsOnCompanyFilingsDifferenceAllDF",
            "languageMetricsOnCompanyFilingsDifference",
            "languageMetricsOnCompanyFilingsDifferenceDF",
            "kScore",
            "kScoreDF",
            "kScoreChina",
            "kScoreChinaDF",
            "accountingQualityAndRiskMatrix",
            "accountingQualityAndRiskMatrixDF",
            "directorAndOfficerChanges",
            "directorAndOfficerChangesDF",
        ):
            assert hasattr(self.c.premium, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_files_premium(self):
        all = set(dir(self.c.premium.files))
        found = set(_PREEXISTING)

        for meth in (
            "valuEngine",
            "valuEngineDownload",
            "newConstructs",
            "newConstructsDownload",
        ):
            assert hasattr(self.c.premium.files, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_treasuries(self):
        all = set(dir(self.c.treasuries))
        found = set(_PREEXISTING)

        for meth in (
            "thirtyYear",
            "thirtyYearValue",
            "thirtyYearDF",
            "twentyYear",
            "twentyYearValue",
            "twentyYearDF",
            "tenYear",
            "tenYearValue",
            "tenYearDF",
            "sevenYear",
            "sevenYearValue",
            "sevenYearDF",
            "fiveYear",
            "fiveYearValue",
            "fiveYearDF",
            "threeYear",
            "threeYearValue",
            "threeYearDF",
            "twoYear",
            "twoYearValue",
            "twoYearDF",
            "oneYear",
            "oneYearValue",
            "oneYearDF",
            "sixMonth",
            "sixMonthValue",
            "sixMonthDF",
            "threeMonth",
            "threeMonthValue",
            "threeMonthDF",
            "oneMonth",
            "oneMonthValue",
            "oneMonthDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.treasuries, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_commods(self):
        all = set(dir(self.c.commodities))
        found = set(_PREEXISTING)

        for meth in (
            "brent",
            "brentAsync",
            "brentDF",
            "diesel",
            "dieselAsync",
            "dieselDF",
            "gasmid",
            "gasmidAsync",
            "gasmidDF",
            "gasprm",
            "gasprmAsync",
            "gasprmDF",
            "gasreg",
            "gasregAsync",
            "gasregDF",
            "heatoil",
            "heatoilAsync",
            "heatoilDF",
            "jet",
            "jetAsync",
            "jetDF",
            "natgas",
            "natgasAsync",
            "natgasDF",
            "propane",
            "propaneAsync",
            "propaneDF",
            "wti",
            "wtiAsync",
            "wtiDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.commodities, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_economic(self):
        all = set(dir(self.c.economic))
        found = set(_PREEXISTING)

        for meth in (
            "cpi",
            "cpiAsync",
            "cpiDF",
            "fedfunds",
            "fedfundsAsync",
            "fedfundsDF",
            "gdp",
            "gdpAsync",
            "gdpDF",
            "housing",
            "housingAsync",
            "housingDF",
            "indpro",
            "indproAsync",
            "indproDF",
            "initialClaims",
            "initialClaimsAsync",
            "initialClaimsDF",
            "institutionalMoney",
            "institutionalMoneyAsync",
            "institutionalMoneyDF",
            "payroll",
            "payrollAsync",
            "payrollDF",
            "recessionProb",
            "recessionProbAsync",
            "recessionProbDF",
            "retailMoney",
            "retailMoneyAsync",
            "retailMoneyDF",
            "unemployment",
            "unemploymentAsync",
            "unemploymentDF",
            "vehicles",
            "vehiclesAsync",
            "vehiclesDF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.economic, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_rates(self):
        all = set(dir(self.c.rates))
        found = set(_PREEXISTING)

        for meth in (
            "cdj",
            "cdjDF",
            "cdjValue",
            "cdnj",
            "cdnjDF",
            "cdnjValue",
            "creditcard",
            "creditcardDF",
            "creditcardValue",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.rates, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_mortgage(self):
        all = set(dir(self.c.mortgage))
        found = set(_PREEXISTING)

        for meth in (
            "us15",
            "us15DF",
            "us30",
            "us30DF",
            "us5",
            "us5DF",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.mortgage, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_studies(self):
        all = set(dir(self.c.studies))
        found = set(_PREEXISTING)

        for meth in (
            "peerCorrelation",
            "peerCorrelationPlot",
            "yieldCurve",
            "returns",
            "dailyReturns",
            "ht_dcperiod",
            "ht_dcphase",
            "ht_phasor",
            "ht_sine",
            "ht_trendmode",
            "acos",
            "asin",
            "atan",
            "ceil",
            "cos",
            "cosh",
            "exp",
            "floor",
            "ln",
            "log10",
            "sin",
            "sinh",
            "sqrt",
            "tan",
            "tanh",
            "add",
            "div",
            "max",
            "maxindex",
            "min",
            "minindex",
            "minmax",
            "minmaxindex",
            "mult",
            "sub",
            "sum",
            "adx",
            "adxr",
            "apo",
            "aroon",
            "aroonosc",
            "bop",
            "cci",
            "cmo",
            "dx",
            "macd",
            "macdext",
            "mfi",
            "minus_di",
            "minus_dm",
            "mom",
            "plus_di",
            "plus_dm",
            "ppo",
            "roc",
            "rocp",
            "rocr",
            "rocr100",
            "rsi",
            "stoch",
            "stochf",
            "stochrsi",
            "trix",
            "ultosc",
            "willr",
            "bollinger",
            "dema",
            "ema",
            "ht_trendline",
            "kama",
            "mama",
            "mavp",
            "midpoint",
            "midpice",
            "sar",
            "sarext",
            "sma",
            "t3",
            "tema",
            "trima",
            "wma",
            "cdl2crows",
            "cdl3blackcrows",
            "cdl3inside",
            "cdl3linestrike",
            "cdl3outside",
            "cdl3starsinsouth",
            "cdl3whitesoldiers",
            "cdlabandonedbaby",
            "cdladvanceblock",
            "cdlbelthold",
            "cdlbreakaway",
            "cdlclosingmarubozu",
            "cdlconcealbabyswallow",
            "cdlcounterattack",
            "cdldarkcloudcover",
            "cdldoji",
            "cdldojistar",
            "cdldragonflydoji",
            "cdlengulfing",
            "cdleveningdojistar",
            "cdleveningstar",
            "cdlgapsidesidewhite",
            "cdlgravestonedoji",
            "cdlhammer",
            "cdlhangingman",
            "cdlharami",
            "cdlharamicross",
            "cdlhighwave",
            "cdlhikkake",
            "cdlhikkakemod",
            "cdlhomingpigeon",
            "cdlidentical3crows",
            "cdlinneck",
            "cdlinvertedhammer",
            "cdlkicking",
            "cdlkickingbylength",
            "cdlladderbottom",
            "cdllongleggeddoji",
            "cdllongline",
            "cdlmarubozu",
            "cdlmatchinglow",
            "cdlmathold",
            "cdlmorningdojistar",
            "cdlmorningstar",
            "cdlonneck",
            "cdlpiercing",
            "cdlrickshawman",
            "cdlrisefall3methods",
            "cdlseparatinglines",
            "cdlshootingstar",
            "cdlshortline",
            "cdlspinningtop",
            "cdlstalledpattern",
            "cdlsticksandwich",
            "cdltakuri",
            "cdltasukigap",
            "cdlthrusting",
            "cdltristar",
            "cdlunique3river",
            "cdlxsidegap3methods",
            "avgprice",
            "medprice",
            "typprice",
            "wclprice",
            "beta",
            "correl",
            "linearreg",
            "linearreg_angle",
            "linearreg_intercept",
            "linearreg_slope",
            "stddev",
            "tsf",
            "var",
            "atr",
            "natr",
            "trange",
            "ad",
            "adosc",
            "obv",
        ):
            assert hasattr(self.c, meth)
            assert hasattr(self.c.studies, meth)
            found.add(meth)
        assert all - found == set()

    def test_all_watchlist(self):
        all = set(dir(self.c.watchlist))
        found = set(_PREEXISTING)

        for meth in (
            "add",
            "create",
            "delete",
            "get",
            "getDF",
            "remove",
        ):
            assert hasattr(self.c.watchlist, meth)
            found.add(meth)
        assert all - found == set()
