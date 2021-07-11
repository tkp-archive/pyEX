# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from io import BytesIO

import requests
from IPython.display import Image as ImageI
from PIL import Image as ImageP

from ..common import (
    _UTC,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
)


@_expire(hour=0, tz=_UTC)
def logo(symbol, token="", version="stable", filter="", format="json"):
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
def logoPNG(symbol, token="", version="stable"):
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
def logoNotebook(symbol, token="", version="stable"):
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
