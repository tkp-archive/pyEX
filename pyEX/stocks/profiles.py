# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps
from io import BytesIO

import pandas as pd
import requests
from deprecation import deprecated
from IPython.display import Image as ImageI
from PIL import Image as ImageP

from ..common import (
    _UTC,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
    json_normalize,
)


@_expire(hour=4, tz=_UTC)
def company(symbol, token="", version="", filter="", format="json"):
    """Company reference data

    https://iexcloud.io/docs/api/#company
    Updates at 4am and 5am UTC every day

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/company".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(company)
def companyDF(*args, **kwargs):
    return _reindex(_toDatetime(json_normalize(company(*args, **kwargs))), "symbol")


@_expire(hour=5, tz=_UTC)
def insiderRoster(symbol, token="", version="", filter="", format="json"):
    """Returns the top 10 insiders, with the most recent information.

    https://iexcloud.io/docs/api/#insider-roster
    Updates at 5am, 6am ET every day

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/insider-roster".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(insiderRoster)
def insiderRosterDF(*args, **kwargs):
    return _toDatetime(
        pd.DataFrame(insiderRoster(*args, **kwargs)), cols=[], tcols=["reportDate"]
    )


@_expire(hour=5, tz=_UTC)
def insiderSummary(symbol, token="", version="", filter="", format="json"):
    """Returns aggregated insiders summary data for the last 6 months.

    https://iexcloud.io/docs/api/#insider-summary
    Updates at 5am, 6am ET every day

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/insider-summary".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(insiderSummary)
def insiderSummaryDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(insiderSummary(*args, **kwargs)))


@_expire(hour=5, tz=_UTC)
def insiderTransactions(symbol, token="", version="", filter="", format="json"):
    """Returns insider transactions.

    https://iexcloud.io/docs/api/#insider-transactions
    Updates at UTC every day

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/insider-transactions".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(insiderTransactions)
def insiderTransactionsDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(insiderTransactions(*args, **kwargs)))


@_expire(hour=0, tz=_UTC)
def logo(symbol, token="", version="", filter="", format="json"):
    """This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/logo".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@_expire(hour=0, tz=_UTC)
def logoPNG(symbol, token="", version=""):
    """This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version

    Returns:
        image: result as png
    """
    _raiseIfNotStr(symbol)
    response = requests.get(
        logo(
            _quoteSymbols(symbol),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )["url"]
    )
    return ImageP.open(BytesIO(response.content))


@_expire(hour=0, tz=_UTC)
def logoNotebook(symbol, token="", version=""):
    """This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version

    Returns:
        image: result
    """
    _raiseIfNotStr(symbol)
    url = logo(_quoteSymbols(symbol), token, version)["url"]
    return ImageI(url=url)


@_expire(hour=8, tz=_UTC)
def peers(symbol, token="", version="", filter="", format="json"):
    """Peers of ticker

    https://iexcloud.io/docs/api/#peers
    8am UTC daily

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/peers".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(peers)
def peersDF(*args, **kwargs):
    df = _reindex(
        _toDatetime(pd.DataFrame(peers(*args, **kwargs), columns=["symbol"])), "symbol"
    )
    df["peer"] = df.index
    return df


@_expire(hour=8, tz=_UTC)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def relevant(symbol, token="", version="", filter="", format="json"):
    """Same as peers

    https://iexcloud.io/docs/api/#relevant
    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/relevant".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(relevant)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def relevantDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(relevant(*args, **kwargs)))
