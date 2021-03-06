# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from ..common import _get, _strOrDate


def files(id="", symbol="", date=None, token="", version="stable"):
    """The Files API allows users to download bulk data files, PDFs, etc.

    https://iexcloud.io/docs/api/#files

    Args:
        id (str): report ID
        symbol (str): symbol to use
        date (str): date of report to use
    """
    if id:
        if symbol and date:
            return _get(
                "files/download/{}?symbol={}&date={}".format(
                    id, symbol, _strOrDate(date)
                ),
                token=token,
                version=version,
                format="binary",
            )
        return _get("files/info/{}".format(id), token=token, version=version)

    return _get("files", token=token, version=version)


def download(id, symbol, date, token="", version="stable"):
    """The Files API allows users to download bulk data files, PDFs, etc.

    Example: c.download('VALUENGINE_REPORT', 'AAPL', '20200804')

    https://iexcloud.io/docs/api/#files

    Args:
        id (str): report ID
        symbol (str): symbol to use
        date (str): date of report to use
    """
    with open("{}-{}-{}.pdf".format(id, symbol, date), "wb") as fp:
        fp.write(files(id=id, symbol=symbol, date=date, token=token, version=version))
