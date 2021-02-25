# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _UTC, _expire, _get, _reindex, _toDatetime, json_normalize


@_expire(hour=8, tz=_UTC)
def symbols(token="", version="stable", filter="", format="json"):
    """This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/symbols", token=token, version=version, filter=filter, format=format
    )


@_expire(hour=8, tz=_UTC)
def iexSymbols(token="", version="stable", filter="", format="json"):
    """This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/iex/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@_expire(hour=8, tz=_UTC)
def mutualFundSymbols(token="", version="stable", filter="", format="json"):
    """This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/mutual-funds/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@_expire(hour=8, tz=_UTC)
def otcSymbols(token="", version="stable", filter="", format="json"):
    """This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/otc/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@_expire(hour=8, tz=_UTC)
def internationalSymbols(
    region="",
    exchange="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (str): region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (str): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    if region:
        return _get(
            "ref-data/region/{region}/symbols".format(region=region),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    elif exchange:
        return _get(
            "ref-data/exchange/{exchange}/symbols".format(exchange=exchange),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/region/us/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@_expire(hour=8, tz=_UTC)
def fxSymbols(token="", version="stable", filter="", format="json"):
    """This call returns a list of supported currencies and currency pairs.

    https://iexcloud.io/docs/api/#fx-symbols
    7am, 9am, UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/fx/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@_expire(hour=8, tz=_UTC)
def optionsSymbols(token="", version="stable", filter="", format="json"):
    """This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

    https://iexcloud.io/docs/api/#options-symbols
    9:30am ET Tue-Sat

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/options/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@_expire(hour=8, tz=_UTC)
def cryptoSymbols(token="", version="stable", filter="", format="json"):
    """This provides a full list of supported cryptocurrencies by IEX Cloud.

    https://iexcloud.io/docs/api/#cryptocurrency-symbols
    8am ET Tue-Sat

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/crypto/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(symbols)
def symbolsDF(*args, **kwargs):
    df = pd.DataFrame(symbols(*args, **kwargs))
    _toDatetime(df)
    _reindex(df, "symbol")
    df.sort_index(inplace=True)
    return df


@wraps(iexSymbols)
def iexSymbolsDF(*args, **kwargs):
    df = _reindex(_toDatetime(pd.DataFrame(iexSymbols(*args, **kwargs))), "symbol")
    df.sort_index(inplace=True)
    return df


@wraps(mutualFundSymbols)
def mutualFundSymbolsDF(*args, **kwargs):
    df = _reindex(
        _toDatetime(pd.DataFrame(mutualFundSymbols(*args, **kwargs))), "symbol"
    )
    df.sort_index(inplace=True)
    return df


@wraps(otcSymbols)
def otcSymbolsDF(*args, **kwargs):
    df = _reindex(_toDatetime(pd.DataFrame(otcSymbols(*args, **kwargs))), "symbol")
    df.sort_index(inplace=True)
    return df


@wraps(internationalSymbols)
def internationalSymbolsDF(*args, **kwargs):
    df = _reindex(
        _toDatetime(pd.DataFrame(internationalSymbols(*args, **kwargs))), "symbol"
    )
    df.sort_index(inplace=True)
    return df


@wraps(fxSymbols)
def fxSymbolsDF(token="", version="stable"):
    fx = fxSymbols(token, version)
    df1 = pd.DataFrame(fx["currencies"])
    df2 = pd.DataFrame(fx["pairs"])
    _reindex(df1, "code")
    df1.sort_index(inplace=True)
    df2.sort_index(inplace=True)
    return [df1, df2]


@wraps(optionsSymbols)
def optionsSymbolsDF(*args, **kwargs):
    df = json_normalize(optionsSymbols(*args, **kwargs))
    df = df.T
    df.columns = ["expirations"]
    df.sort_index(inplace=True)
    return df


@wraps(cryptoSymbols)
def cryptoSymbolsDF(*args, **kwargs):
    df = _reindex(_toDatetime(pd.DataFrame(cryptoSymbols(*args, **kwargs))), "symbol")
    df.sort_index(inplace=True)
    return df


@wraps(symbols)
def symbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in symbols(*args, **kwargs)])


@wraps(iexSymbols)
def iexSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in iexSymbols(*args, **kwargs)])


@wraps(mutualFundSymbols)
def mutualFundSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in mutualFundSymbols(*args, **kwargs)])


@wraps(otcSymbols)
def otcSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in otcSymbols(*args, **kwargs)])


@wraps(internationalSymbols)
def internationalSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in internationalSymbols(*args, **kwargs)])


@wraps(fxSymbols)
def fxSymbolsList(*args, **kwargs):
    fx = fxSymbols(*args, **kwargs)
    ret = [[], []]
    for c in fx["currencies"]:
        ret[0].append(c["code"])
    for p in fx["pairs"]:
        ret[1].append(p["fromCurrency"] + p["toCurrency"])
    return sorted(ret)


@wraps(optionsSymbols)
def optionsSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    symbols = optionsSymbols(*args, **kwargs)
    ret = []
    for ticker, dates in symbols.items():
        for date in dates:
            ret.append("{}-{}".format(ticker, date))
    return ret


@wraps(cryptoSymbols)
def cryptoSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in cryptoSymbols(*args, **kwargs)])


def isinLookup(isin, token="", version="stable", filter="", format="json"):
    """This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#isin-mapping
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        isin (str): isin to lookup
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/isin?isin={}".format(isin),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(isinLookup)
def isinLookupDF(*args, **kwargs):
    return pd.DataFrame(isinLookup(*args, **kwargs))
