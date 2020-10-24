# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _getJson, _raiseIfNotStr


def figi(figi_=None, token='', version=''):
    '''Helper call to convert FIGI to IEX Cloud symbols. Note that due to licensing restrictions we are unable to return the FIGI.

    https://iexcloud.io/docs/api/#figi-mapping

    Args:
        figi_ (str): figi to lookup
        token (str): Access token
        version (str): API version

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(figi_)
    return _getJson('ref-data/figi?figi={}'.format(figi_), token, version, None)


@wraps(figi)
def figiDF(figi_=None, token='', version=''):
    return pd.DataFrame(figi(figi_, token, version))
