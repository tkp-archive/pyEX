# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import (
    _COLLECTION_TAGS,
    PyEXception,
    _expire,
    _get,
    _reindex,
    _toDatetime,
)


@_expire(hour=0)
def collections(
    tag,
    collectionName,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Returns an array of quote objects for a given collection type. Currently supported collection types are sector, tag, and list


    https://iexcloud.io/docs/api/#collections

    Args:
        tag (str):  Sector, Tag, or List
        collectionName (str):  Associated name for tag
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if tag not in _COLLECTION_TAGS:
        raise PyEXception("Tag must be in %s" % str(_COLLECTION_TAGS))
    return _get(
        "stock/market/collection/" + tag + "?collectionName=" + collectionName,
        token,
        version,
        filter,
    )


@wraps(collections)
def collectionsDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(collections(*args, **kwargs))), "symbol")
