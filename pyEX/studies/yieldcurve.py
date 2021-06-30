# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import pandas as pd
from datetime import datetime, timedelta

_curves = {
    "DGS1MO": "1 Month",
    "DGS3MO": "3 Month",
    "DGS6MO": "6 Month",
    "DGS1": "1 Year",
    "DGS2": "2 Year",
    "DGS3": "3 Year",
    "DGS5": "5 Year",
    "DGS7": "7 Year",
    "DGS10": "10 Year",
    "DGS20": "20 Year",
    "DGS30": "30 Year",
}


def yieldCurve(
    client, curves=None, from_=None, to_=None, wide_or_tall="wide"
):
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
        wide_or_tall (str): Build dataframe wide or tall (default: `tall`).
                If set to `"tall"`, returned dataframe will look like:
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
    if wide_or_tall.lower() not in ("wide", "tall"):
        from pyEX import PyEXception
        raise PyEXception(
            "Unrecognized value for `wide_or_tall`: {}".format(wide_or_tall)
        )
    to_ = to_ or datetime.today().strftime("%Y%m%d")
    from_ = from_ or (datetime.strptime(to_, "%Y%m%d") - timedelta(days=30)).strftime("%Y%m%d")

    # wide - columns in DF
    if wide_or_tall == "wide":
        dfs = pd.DataFrame()
        for curve in _curves.keys():
            df = client.timeSeriesDF(
                "TREASURY", curve, from_=from_, to_=to_, filter="date,value"
            )

            # TODO fix bad/missing data since can't do this
            df = df[df["value"] > 0]
            df.set_index("date", inplace=True)
            dfs[_curves[curve]] = df["value"]

        return dfs

    # tall - values in rows
    dfs = []
    for curve in _curves.keys():
        df = client.timeSeriesDF(
            "TREASURY", curve, from_=from_, to_=to_, filter="date,value,key"
        )
        # TODO fix bad/missing data since can't do this
        df = df[df["value"] > 0]
        df.set_index("date", inplace=True)
        dfs.append(df)
    return pd.concat(dfs)
