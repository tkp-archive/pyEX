# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _getJson, _raiseIfNotStr


def figi(figi_=None, token="", version=""):
    """Helper call to convert FIGI to IEX Cloud symbols. Note that due to licensing restrictions we are unable to return the FIGI.

    https://iexcloud.io/docs/api/#figi-mapping

    Args:
        figi_ (str): figi to lookup
        token (str): Access token
        version (str): API version

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(figi_)
    return _getJson("ref-data/figi?figi={}".format(figi_), token, version, None)


@wraps(figi)
def figiDF(figi_=None, token="", version=""):
    return pd.DataFrame(figi(figi_, token, version))
