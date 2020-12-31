# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _expire, _getJson


@_expire(hour=8)
def sectors(token="", version="", filter=""):
    """Returns an array of sectors.

    https://iexcloud.io/docs/api/#sectors

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    return _getJson("ref-data/sectors", token, version, filter)


@wraps(sectors)
def sectorsDF(token="", version="", filter=""):
    return pd.DataFrame(sectors(token, version, filter))


@_expire(hour=8)
def tags(token="", version="", filter=""):
    """Returns an array of tags.

    https://iexcloud.io/docs/api/#tags

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    return _getJson("ref-data/tags", token, version, filter)


@wraps(tags)
def tagsDF(token="", version="", filter=""):
    return pd.DataFrame(tags(token, version, filter))
