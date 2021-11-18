# *****************************************************************************
#
# Copyright (c) 2022, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _get


def queryMetadata(
    id="",
    key="",
    subkey="",
    provider="",
    token="",
    version="stable",
    filter="",
    format="json",  # TODO move provider up
):
    """Get inventory of available time series endpoints

    Args:
        id (str): Timeseries ID
        key (str): Timeseries Key
        subkey (str): Timeseries Subkey
        provider (str): Timeseries Data Provider
        token (str): Access token
        version (str): API version
        filter (str): https://iexcloud.io/docs/api/#filter-results
        format (str): output format
    """
    if provider:
        url = "metadata/meta"
    else:
        url = "metadata/time-series"
    if not id and key:
        id = "*"
    if id:
        url += "/{}".format(id)
        if key:
            url += "/{}".format(key)
            if subkey:
                url += "/{}".format(subkey)
    return _get(url, token=token, version=version, filter=filter, format=format)


@wraps(queryMetadata)
def queryMetadataDF(*args, **kwargs):
    return pd.DataFrame(queryMetadata(*args, **kwargs))
