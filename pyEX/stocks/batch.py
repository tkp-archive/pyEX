# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd

from ..common import (
    _BATCH_TYPES,
    _RANGE_CHART,
    PyEXception,
    _get,
    _quoteSymbols,
    json_normalize,
)
from .book import _bookToDF
from .chart import _chartToDF
from .company import _companyToDF
from .dividendsBasic import _dividendsToDF
from .earnings import _earningsToDF
from .financials import _financialsToDF
from .keyStats import _statsToDF
from .news import _newsToDF
from .peers import _peersToDF
from .splitsBasic import _splitsToDF

_MAPPING = {
    "book": _bookToDF,
    "chart": _chartToDF,
    "company": _companyToDF,
    "dividends": _dividendsToDF,
    "earnings": _earningsToDF,
    "financials": _financialsToDF,
    "stats": _statsToDF,
    "news": _newsToDF,
    "peers": _peersToDF,
    "splits": _splitsToDF,
}


def batch(
    symbols,
    fields=None,
    range_="1m",
    last=10,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Batch several data requests into one invocation. If no `fields` passed in, will default to `quote`

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (str or list): List of tickers to request
        fields (str or list): List of fields to request
        range_ (str): Date range for chart
        last (int):
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict: results in json
    """
    fields = fields or "quote"

    if not isinstance(symbols, [].__class__) and not isinstance(symbols, str):
        raise PyEXception(
            "batch expects string or list of strings for symbols argument"
        )

    if isinstance(fields, str) and "," not in fields:
        fields = [fields]
    elif isinstance(fields, str):
        fields = fields.split(",")

    for field in fields:
        if field not in _BATCH_TYPES:
            raise PyEXception("Unrecognized batch request field: {}".format(field))

    if range_ not in _RANGE_CHART:
        raise PyEXception("Range must be in %s" % str(_RANGE_CHART))

    symbols = _quoteSymbols(symbols)
    if len(symbols.split(",")) > 100:
        raise PyEXception("IEX will only handle up to 100 symbols at a time!")

    if "," not in symbols:
        route = "stock/{}/batch?types={}&range={}&last={}".format(
            symbols, ",".join(fields), range_, last
        )
    else:
        route = "stock/market/batch?symbols={}&types={}&range={}&last={}".format(
            symbols, ",".join(fields), range_, last
        )

    return _get(route, token=token, version=version, filter=filter, format=format)


def batchDF(
    symbols,
    fields=None,
    range_="1m",
    last=10,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Batch several data requests into one invocation

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list): List of tickers to request
        fields (list): List of fields to request
        range_ (str): Date range for chart
        last (int):
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        DataFrame: results in json
    """
    symbols = _quoteSymbols(symbols)
    x = batch(
        symbols,
        fields,
        range_,
        last,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )

    ret = {}

    if "," not in symbols:
        # one level json, break down
        for field in x.keys():
            ret[field] = _MAPPING.get(field, json_normalize)(x[field])
    else:
        # two level json
        for symbol in x.keys():
            for field in x[symbol].keys():
                if field not in ret:
                    ret[field] = pd.DataFrame()

                dat = x[symbol][field]
                dat = _MAPPING.get(field, json_normalize)(dat)
                dat["symbol"] = symbol

                ret[field] = pd.concat([ret[field], dat], sort=True)
    return ret
