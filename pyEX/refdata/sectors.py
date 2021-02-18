# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _expire, _get


@_expire(hour=8)
def sectors(token="", version="", filter="", format="json"):
    """Returns an array of sectors.

    https://iexcloud.io/docs/api/#sectors

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "ref-data/sectors", token=token, version=version, filter=filter, format=format
    )


@wraps(sectors)
def sectorsDF(*args, **kwargs):
    return pd.DataFrame(sectors(*args, **kwargs))


@_expire(hour=8)
def tags(token="", version="", filter="", format="json"):
    """Returns an array of tags.

    https://iexcloud.io/docs/api/#tags

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "ref-data/tags", token=token, version=version, filter=filter, format=format
    )


@wraps(tags)
def tagsDF(*args, **kwargs):
    return pd.DataFrame(tags(*args, **kwargs))
