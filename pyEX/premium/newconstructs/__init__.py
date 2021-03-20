# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from ...common import _EST, _expire
from ...files import files, download


@_expire(hour=10, tz=_EST)
def reportNewConstructs(symbol="", date=None, token="", version="stable"):
    """Powered by the best fundamental data in the world, New Constructs’ research provides unrivalled insights into the profitability and valuation of public and private companies.Our risk/reward ratings empower clients to make more informed investing decisions based on true, not reported or distorted, earnings. Research reports for 3,000+ stocks, 400+ ETFs, and 7,000+ mutual funds.
    https://iexcloud.io/docs/api/#new-constructs-report

    Args:
        symbol (str): symbol to use
        date (str): date to access
    """
    return files(
        id="NEW_CONSTRUCTS_REPORT",
        symbol=symbol,
        date=date,
        token=token,
        version=version,
    )


@_expire(hour=10, tz=_EST)
def downloadReportNewConstructs(symbol="", date=None, token="", version="stable"):
    """Powered by the best fundamental data in the world, New Constructs’ research provides unrivalled insights into the profitability and valuation of public and private companies.Our risk/reward ratings empower clients to make more informed investing decisions based on true, not reported or distorted, earnings. Research reports for 3,000+ stocks, 400+ ETFs, and 7,000+ mutual funds.
    https://iexcloud.io/docs/api/#new-constructs-report

    Args:
        symbol (str): symbol to use
        date (str): date to access
    """
    return download(
        id="NEW_CONSTRUCTS_REPORT",
        symbol=symbol,
        date=date,
        token=token,
        version=version,
    )
