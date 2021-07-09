# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import pandas as pd
from datetime import datetime, timedelta
from pyEX.common import _expire, _UTC

_curves = {
    "DGS1MO": "oneMonthHistoryDF",
    "DGS3MO": "threeMonthHistoryDF",
    "DGS6MO": "sixMonthHistoryDF",
    "DGS1": "oneYearHistoryDF",
    "DGS2": "twoYearHistoryDF",
    "DGS3": "threeYearHistoryDF",
    "DGS5": "fiveYearHistoryDF",
    "DGS7": "sevenYearHistoryDF",
    "DGS10": "tenYearHistoryDF",
    "DGS20": "twentyYearHistoryDF",
    "DGS30": "thirtyYearHistoryDF",
}


@_expire(hour=8, tz=_UTC)
def yieldCurve(client, curves=None, from_=None, to_=None, wide_or_long="wide"):
    """This will return a dataframe of a yield curve for all treasuries over the given range.
    Note that this may cost a large number of credits

    Args:
        client (pyEX.Client): Client
        curves (list): List of curve keys to request, must be in:
                DGS1MO
                DGS3MO
                DGS6MO
                DGS1
                DGS2
                DGS3
                DGS5
                DGS7
                DGS10
                DGS20
                DGS30
        from_ (str): Starting date of curve
        to_ (to): end date of curve
        wide_or_long (str): Build dataframe wide or long (default: `wide`).
                If set to `"long"`, returned dataframe will look like:
                ```
                date       | key  | value
                2020-01-01 | DGS1 |  0.05
                2020-01-01 | DGS2 |  0.06
                ```

                If set to `"wide"`, returned dataframe will look like:
                ```
                date       | DGS1 | DGS2 | ...
                2020-01-01 | 0.05 | 0.06
                ```
    Returns:
        DataFrame: result
    """
    if wide_or_long.lower() not in ("wide", "long"):
        from pyEX import PyEXception

        raise PyEXception(
            "Unrecognized value for `wide_or_tall`: {}".format(wide_or_long)
        )

    _basecurves = curves or _curves.keys()
    to_ = to_ or datetime.today().strftime("%Y%m%d")
    from_ = from_ or (datetime.strptime(to_, "%Y%m%d") - timedelta(days=30)).strftime(
        "%Y%m%d"
    )

    # wide - columns in DF
    if wide_or_long == "wide":
        dfs = pd.DataFrame()
        for curve in _curves.keys():
            if curve not in _basecurves:
                continue
            df = getattr(client, _curves[curve])(
                from_=from_, to_=to_, filter="date,value"
            )
            # TODO fix bad/missing data since can't do this
            df = df[df["value"] > 0]
            df.set_index("date", inplace=True)
            dfs[_curves[curve]] = df["value"]

        return dfs

    # tall - values in rows
    dfs = []
    for curve in _curves.keys():
        if curve not in _basecurves:
            continue
        df = getattr(client, _curves[curve])(
            from_=from_, to_=to_, filter="date,value,key"
        )
        # TODO fix bad/missing data since can't do this
        df = df[df["value"] > 0]
        df.set_index("date", inplace=True)
        dfs.append(df)
    return pd.concat(dfs)
