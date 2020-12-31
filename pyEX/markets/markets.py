# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
from deprecation import deprecated

from ..common import _getJson, _toDatetime


@deprecated(details="Deprecated: IEX Cloud status unkown")
def markets(token="", version="", filter=""):
    """https://iextrading.com/developer/docs/#intraday"""
    return _getJson("market", token, version, filter)


@deprecated(details="Deprecated: IEX Cloud status unkown")
def marketsDF(token="", version="", filter=""):
    """https://iextrading.com/developer/docs/#intraday"""
    df = pd.DataFrame(markets(token, version, filter))
    _toDatetime(df)
    return df
