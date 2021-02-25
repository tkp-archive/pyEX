# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd
from deprecation import deprecated

from ..common import _get, _toDatetime


@deprecated(details="Deprecated: IEX Cloud status unkown")
def markets(token="", version="stable", filter="", format="json"):
    return _get("market", token=token, version=version, format=format)


@deprecated(details="Deprecated: IEX Cloud status unkown")
def marketsDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(markets(*args, **kwargs)))
