# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson, _raiseIfNotStr


def figi(figi_=None, token='', version=''):
    '''Helper call to convert FIGI to IEX Cloud symbols. Note that due to licensing restrictions we are unable to return the FIGI.

    https://iexcloud.io/docs/api/#figi-mapping

    Args:
        figi_ (string); figi to lookup
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(figi_)
    return _getJson('ref-data/figi?figi={}'.format(figi_), token, version, None)


def figiDF(figi_=None, token='', version=''):
    '''Helper call to convert FIGI to IEX Cloud symbols. Note that due to licensing restrictions we are unable to return the FIGI.

    https://iexcloud.io/docs/api/#figi-mapping

    Args:
        figi_ (string); figi to lookup
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(figi(figi_, token, version))
