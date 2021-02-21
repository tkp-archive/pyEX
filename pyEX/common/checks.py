# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from __future__ import print_function

from datetime import datetime
from urllib.parse import quote

import pandas as pd
from six import string_types

from .exception import PyEXception

_TIMEFRAME_CHART = [
    "max",
    "5y",
    "2y",
    "1y",
    "ytd",
    "6m",
    "3m",
    "1m",
    "1mm",
    "5d",
    "5dm",
    "1d",
    "dynamic",
]
_TIMEFRAME_DIVSPLIT = ["5y", "2y", "1y", "ytd", "6m", "3m", "1m", "next"]
_LIST_OPTIONS = ["mostactive", "gainers", "losers", "iexvolume", "iexpercent"]
_COLLECTION_TAGS = ["sector", "tag", "list"]
_DATE_RANGES = [
    "today",
    "yesterday",
    "ytd",
    "last-week",
    "last-month",
    "last-quarter",
    "d",
    "w",
    "m",
    "q",
    "y",
    "tomorrow",
    "this-week",
    "this-month",
    "this-quarter",
    "next-week",
    "next-month",
    "next-quarter",
]
_KEY_STATS = [
    "companyName",
    "marketcap",
    "week52high",
    "week52low",
    "week52change",
    "sharesOutstanding",
    "float",
    "avg10Volume",
    "avg30Volume",
    "day200MovingAvg",
    "day50MovingAvg",
    "employees",
    "ttmEPS",
    "ttmDividendRate",
    "dividendYield",
    "nextDividendDate",
    "exDividendDate",
    "nextEarningsDate",
    "peRatio",
    "beta",
    "maxChangePercent",
    "year5ChangePercent",
    "year2ChangePercent",
    "year1ChangePercent",
    "ytdChangePercent",
    "month6ChangePercent",
    "month3ChangePercent",
    "month1ChangePercent",
    "day30ChangePercent",
    "day5ChangePercent",
]
_USAGE_TYPES = ["messages", "rules", "rule-records", "alerts", "alert-records"]

# Limit 10
_BATCH_TYPES = [
    "book",
    "chart",
    "company",
    "dividends",
    "earnings",
    "financials",
    "stats",
    "news",
    "peers",
    "splits",
    # limit 10
    "intraday-prices",
    "effective-spread",
    "delayed-quote",
    "largest-trades",
    "previous",
    "price",
    "quote",
    "relevant",
    "volume-by-venue",
]

_STANDARD_DATE_FIELDS = [
    "consensusEndDate",
    "consensusStartDate",
    "DailyListTimestamp",
    "date",
    "datetime",
    "declaredDate",
    "EPSReportDate",
    "endDate",
    "exDate",
    "expectedDate",
    "expirationDate",
    "fiscalEndDate",
    "latestTime",
    "lastTradeDate",
    "lastUpdated",
    "paymentDate",
    "processedTime",
    "recordDate",
    "RecordUpdateTime",
    "reportDate",
    "settlementDate",
    "startDate",
]

_STANDARD_TIME_FIELDS = [
    "closeTime",
    "close.time",
    "delayedPriceTime",
    "extendedPriceTime",
    "highTime",
    "iexCloseTime",
    "iexLastUpdated",
    "iexOpenTime",
    "lastTradeTime",
    "lastUpdated",
    "latestTime",
    "latestUpdate",
    "lowTime",
    "oddLotDelayedPriceTime",
    "openTime",
    "open.time",
    "processedTime",
    "report_date",
    "reportDate",
    "time",
    "timestamp",
    "updated",
]

_INDICATORS = [
    "abs",
    "acos",
    "ad",
    "add",
    "adosc",
    "adx",
    "adxr",
    "ao",
    "apo",
    "aroon",
    "aroonosc",
    "asin",
    "atan",
    "atr",
    "avgprice",
    "bbands",
    "bop",
    "cci",
    "ceil",
    "cmo",
    "cos",
    "cosh",
    "crossany",
    "crossover",
    "cvi",
    "decay",
    "dema",
    "di",
    "div",
    "dm",
    "dpo",
    "dx",
    "edecay",
    "ema",
    "emv",
    "exp",
    "fisher",
    "floor",
    "fosc",
    "hma",
    "kama",
    "kvo",
    "lag",
    "linreg",
    "linregintercept",
    "linregslope",
    "ln",
    "log10",
    "macd",
    "marketfi",
    "mass",
    "max",
    "md",
    "medprice",
    "mfi",
    "min",
    "mom",
    "msw",
    "mul",
    "natr",
    "nvi",
    "obv",
    "ppo",
    "psar",
    "pvi",
    "qstick",
    "roc",
    "rocr",
    "round",
    "rsi",
    "sin",
    "sinh",
    "sma",
    "sqrt",
    "stddev",
    "stderr",
    "stoch",
    "stochrsi",
    "sub",
    "sum",
    "tan",
    "tanh",
    "tema",
    "todeg",
    "torad",
    "tr",
    "trima",
    "trix",
    "trunc",
    "tsf",
    "typprice",
    "ultosc",
    "var",
    "vhf",
    "vidya",
    "volatility",
    "vosc",
    "vwma",
    "wad",
    "wcprice",
    "wilders",
    "willr",
    "wma",
    "zlema",
]

_INDICATOR_RETURNS = {
    "abs": ("abs",),
    "acos": ("acos",),
    "ad": ("ad",),
    "add": ("add",),
    "adosc": ("adosc",),
    "adx": ("dx",),
    "adxr": ("dx",),
    "ao": ("ao",),
    "apo": ("apo",),
    "aroon": ("aroon_down", "aroon_up"),
    "aroonosc": ("aroonosc",),
    "asin": ("asin",),
    "atan": ("atan",),
    "atr": ("atr",),
    "avgprice": ("avgprice",),
    "bbands": ("bbands_lower", "bbands_middle", "bbands_upper"),
    "bop": ("bop",),
    "cci": ("cci",),
    "ceil": ("ceil",),
    "cmo": ("cmo",),
    "cos": ("cos",),
    "cosh": ("cosh",),
    "crossany": ("crossany",),
    "crossover": ("crossover",),
    "cvi": ("cvi",),
    "decay": ("decay",),
    "dema": ("dema",),
    "di": ("plus_di", "minus_di"),
    "div": ("div",),
    "dm": ("plus_dm", "minus_dm"),
    "dpo": ("dop",),
    "dx": ("dx",),
    "edecay": ("edecay",),
    "ema": ("ema",),
    "emv": ("emv",),
    "exp": ("exp",),
    "fisher": ("fisher", "fisher_signal"),
    "floor": ("floor",),
    "fosc": ("fosc",),
    "hma": ("hma",),
    "kama": ("kama",),
    "kvo": ("kvo",),
    "lag": ("lag",),
    "linreg": ("linreg",),
    "linregintercept": ("linregintercept",),
    "linregslope": ("linregslope",),
    "ln": ("ln",),
    "log10": ("log10",),
    "macd": ("macd", "macd_signal", "macd_histogram"),
    "marketfi": ("marketfi",),
    "mass": ("mass",),
    "max": ("max",),
    "md": ("md",),
    "medprice": ("medprice",),
    "mfi": ("mfi",),
    "min": ("min",),
    "mom": ("mom",),
    "msw": ("msw_sine", "msw_lead"),
    "mul": ("mul",),
    "natr": ("matr",),
    "nvi": ("nvi",),
    "obv": ("obv",),
    "ppo": ("ppo",),
    "psar": ("psar",),
    "pvi": ("pvi",),
    "qstick": ("qstick",),
    "roc": ("roc",),
    "rocr": ("rocr",),
    "round": ("round",),
    "rsi": ("rsi",),
    "sin": ("sin",),
    "sinh": ("sinh",),
    "sma": ("sma",),
    "sqrt": ("sqrt",),
    "stddev": ("stddev",),
    "stderr": ("stderr",),
    "stoch": ("stock_k", "stock_d"),
    "stochrsi": ("stochrsi",),
    "sub": ("sub",),
    "sum": ("sum",),
    "tan": ("tan",),
    "tanh": ("tanh",),
    "tema": ("tema",),
    "todeg": ("degrees",),
    "torad": ("radians",),
    "tr": ("tr",),
    "trima": ("trima",),
    "trix": ("trix",),
    "trunc": ("trunc",),
    "tsf": ("tsf",),
    "typprice": ("typprice",),
    "ultosc": ("ultosc",),
    "var": ("var",),
    "vhf": ("vhf",),
    "vidya": ("vidya",),
    "volatility": ("volatility",),
    "vosc": ("vosc",),
    "vwma": ("vwma",),
    "wad": ("wad",),
    "wcprice": ("wcprice",),
    "wilders": ("wilders",),
    "willr": ("willr",),
    "wma": ("wma",),
    "zlema": ("zlema",),
}


def _strToList(st):
    """internal"""
    if isinstance(st, string_types):
        return st.split(",")
    return st


def _strCommaSeparatedString(st):
    """internal"""
    return ",".join(_strToList(st))


def _strOrDate(st):
    """internal"""
    if isinstance(st, string_types):
        return st
    elif isinstance(st, datetime):
        return st.strftime("%Y%m%d")
    raise PyEXception("Not a date: %s", str(st))


def _dateRange(st):
    """internal"""
    if st not in _DATE_RANGES:
        raise PyEXception("Must be a valid date range: got {}".format(st))
    return st


def _raiseIfNotStr(s):
    """internal"""
    if s is not None and not isinstance(s, string_types):
        raise PyEXception("Cannot use type %s" % str(type(s)))


def _checkPeriodLast(per, last):
    """check if period is ok with last"""
    if per not in ("quarter", "annual"):
        raise PyEXception("Period must be in {'quarter', 'annual'}")
    if per == "quarter":
        if last < 1 or last > 12:
            raise PyEXception("Last must be in [1, 12] for period 'quarter'")
    else:
        if last < 1 or last > 4:
            raise PyEXception("Last must be in [1, 4] for period 'annual'")


def _reindex(df, col):
    """internal"""
    if isinstance(col, list):
        if all([c in df.columns for c in col]):
            df.set_index(col, inplace=True)
    else:
        if col in df.columns:
            df.set_index(col, inplace=True)
    return df


def _toDatetime(df, cols=None, tcols=None, reformatcols=None):
    """internal"""
    cols = cols or []
    tcols = tcols or []
    reformatcols = reformatcols or []

    if not isinstance(cols, list):
        cols = [cols]

    if not isinstance(tcols, list):
        tcols = [tcols]

    if not isinstance(reformatcols, list):
        reformatcols = [reformatcols]

    cols = cols + _STANDARD_DATE_FIELDS if cols is not None else _STANDARD_DATE_FIELDS
    tcols = (
        tcols + _STANDARD_TIME_FIELDS if tcols is not None else _STANDARD_TIME_FIELDS
    )

    for col in cols:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], infer_datetime_format=True)
            except BaseException:
                # skip error
                continue

    for tcol in tcols:
        if tcol in df.columns:
            try:
                df[tcol] = pd.to_datetime(df[tcol], unit="ms")
            except BaseException:
                # skip error
                continue

    for rcol in reformatcols:
        if rcol in df.columns:
            try:
                df[rcol] = pd.to_datetime(df[rcol].astype(int), unit="ms")
            except BaseException:
                # skip error
                continue
    return df


def _requireSecret(token, allowSandbox=True):
    if token.startswith("sk") or (allowSandbox and token.startswith("Tsk")):
        return
    raise PyEXception("Requires secret token!")


def _quoteSymbols(symbols):
    """urlquote a potentially comma-separate list of symbols"""
    if isinstance(symbols, list):
        # comma separated, quote separately
        return ",".join(quote(symbol, safe="") for symbol in symbols)
    # not comma separated, just quote
    return quote(symbols, safe=",")


def _timeseriesWrapper(kwargs, key=True, subkey=True):
    if key:
        if "key" in kwargs:
            raise PyEXception("Cannot pass `key` kwarg to timeseries, already used")
    if subkey:
        if "subkey" in kwargs:
            raise PyEXception("Cannot pass `subkey` kwarg to timeseries, already used")


try:
    if pd.__version__ > "1.":
        json_normalize = pd.json_normalize
    else:
        json_normalize = pd.io.json.json_normalize
except (TypeError, AttributeError):
    json_normalize = pd.io.json.json_normalize
