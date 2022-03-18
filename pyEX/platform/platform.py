# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps
import json
import pandas as pd

from ..common import (
    PyEXception,
    _interpolateDatatype,
    _dateRange,
    _get,
    _getAsync,
    _patch,
    _patchAsync,
    _post,
    _postAsync,
    _put,
    _putAsync,
    _delete,
    _deleteAsync,
    _quoteSymbols,
    _strOrDate,
)


def _queryURL(
    provider="CORE",
    id="",
    key="",
    subkey="",
    date="",
    range=None,
    calendar=False,
    limit=1,
    offset=0,
    subattribute="",
    dateField=None,
    from_=None,
    to_=None,
    on=None,
    last=0,
    first=0,
    sort="",
    interval=None,
    transforms=None,
    basePath="query",
    **extra_params,
):

    base_url = basePath

    if provider:
        base_url += "/{}".format(provider)

    if provider and id:
        base_url += "/{}".format(_quoteSymbols(id))
    if provider and id and key:
        base_url += "/{}".format(_quoteSymbols(key))
    if provider and id and key and subkey:
        base_url += "/{}".format(_quoteSymbols(subkey))
    if provider and id and key and subkey and date:
        base_url += "/{}".format(_quoteSymbols(date))

    base_url += "?"

    if provider and id:
        if range:
            base_url += "range={}&".format(_dateRange(range))

        if calendar:
            base_url += "calendar={}&".format(str(calendar))

        if limit and not last and (not from_ or not to_):
            base_url += "limit={}&".format(str(limit))

        if offset > 0:
            base_url += "offset={}&".format(offset)

        if subattribute:
            if isinstance(subattribute, dict):
                # dict mapping key to required equal value, e.g. {"A": 1} -> A|1
                subattribute = ",".join(
                    "{}|{}".format(key, value) for key, value in subattribute.items()
                )
            elif isinstance(subattribute, list):
                # list of tuples mapping key to required equal value, e.g. [("A", "=", 1), ("B", "!=", 2)] -> A|1,B~2
                subattribute = ",".join(
                    "{}{}{}".format(v1, "|" if v2.upper() == "=" else "~", v3)
                    for v1, v2, v3 in subattribute
                )
            base_url += "subattribute={}&".format(subattribute)

        if dateField:
            base_url += "dateField={}&".format(dateField)

        if from_:
            base_url += "from={}&".format(_strOrDate(from_))

        if to_:
            base_url += "to={}&".format(_strOrDate(to_))

        if on:
            base_url += "on={}&".format(_strOrDate(on))

        if last:
            base_url += "last={}&".format(str(last))

        if first:
            base_url += "first={}&".format(str(first))

        if sort:
            if sort.lower() not in (
                "asc",
                "desc",
            ):
                raise PyEXception("Sort must be in (asc, desc), got: {}".format(sort))
            base_url += "sort={}&".format(sort)

        if interval:
            base_url += "interval={}&".format(int(interval))

        if transforms:
            base_url += "transforms={}&".format(json.dumps(transforms or []))

        if extra_params:
            base_url += "&".join("{}={}".format(k, v) for k, v in extra_params.items())

    return base_url


def _queryMetaUrl(provider="", id="", key="", subkey=""):
    url = "meta"
    if provider:
        url += "/{}".format(provider)
        if not id and key:
            id = "*"
        if id:
            url += "/{}".format(id)
            if key:
                url += "/{}".format(key)
                if subkey:
                    url += "/{}".format(subkey)
    return url


def _queryURLLoose(
    basePath,
    **extra_params,
):
    base_url = basePath
    base_url += "?"
    if extra_params:
        base_url += "&".join("{}={}".format(k, v) for k, v in extra_params.items())

    return base_url


def queryMeta(
    provider="",
    id="",
    key="",
    subkey="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    return _get(
        _queryMetaUrl(provider=provider, id=id, key=key, subkey=subkey),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


async def queryMetaAsync(
    provider="",
    id="",
    key="",
    subkey="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    return await _getAsync(
        _queryMetaUrl(provider=provider, id=id, key=key, subkey=subkey),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(queryMeta)
def queryMetaDF(*args, **kwargs):
    return pd.DataFrame(queryMeta(*args, **kwargs))


def query(
    provider="CORE",
    id="",
    key="",
    subkey="",
    range=None,
    calendar=False,
    limit=1,
    subattribute="",
    dateField=None,
    from_=None,
    to_=None,
    on=None,
    last=0,
    first=0,
    sort="",
    interval=None,
    token="",
    version="stable",
    filter="",
    format="json",
    transforms=None,
    **extra_params,
):
    base_url = _queryURL(
        provider=provider,
        id=id,
        key=key,
        subkey=subkey,
        range=range,
        calendar=calendar,
        limit=limit,
        subattribute=subattribute,
        dateField=dateField,
        from_=from_,
        to_=to_,
        on=on,
        last=last,
        first=first,
        sort=sort,
        interval=interval,
        transforms=transforms,
        **extra_params,
    )
    return _get(base_url, token=token, version=version, filter=filter, format=format)


@wraps(query)
def queryDF(*args, **kwargs):
    return pd.DataFrame(query(*args, **kwargs))


async def queryAsync(
    provider="CORE",
    id="",
    key="",
    subkey="",
    range=None,
    calendar=False,
    limit=1,
    subattribute="",
    dateField=None,
    from_=None,
    to_=None,
    on=None,
    last=0,
    first=0,
    sort="",
    interval=None,
    token="",
    version="stable",
    filter="",
    format="json",
    transforms=None,
    **extra_params,
):
    base_url = _queryURL(
        provider=provider,
        id=id,
        key=key,
        subkey=subkey,
        range=range,
        calendar=calendar,
        limit=limit,
        subattribute=subattribute,
        dateField=dateField,
        from_=from_,
        to_=to_,
        on=on,
        last=last,
        first=first,
        sort=sort,
        interval=interval,
        transforms=transforms,
        **extra_params,
    )
    return await _getAsync(
        base_url, token=token, version=version, filter=filter, format=format
    )


# CRUD code
# def listJobs(
#     provider,
#     type="ingest",
#     jobId="",
#     token="",
#     version="stable",
#     filter="",
#     format="json",
# ):
#     url = "jobs/{}/{}".format(provider, type)

#     if jobId:
#         url += "/{}".format(jobId)

#     return _get(url=url, token=token, version=version, filter=filter, format=format)


# def listDatasets(
#     provider="CORE", id="", token="", version="stable", filter="", format="json"
# ):
#     base_url = _queryURL(provider=provider, id=id)
#     return _get(
#         url=base_url, token=token, version=version, filter=filter, format=format
#     )


# @wraps(listDatasets)
# def listDatasetsDF(*args, **kwargs):
#     return pd.DataFrame(listDatasets(*args, **kwargs))


# async def listDatasetsAsync(
#     provider="CORE", id="", token="", version="stable", filter="", format="json"
# ):
#     base_url = _queryURL(provider=provider, id=id)
#     return await _getAsync(
#         url=base_url, token=token, version=version, filter=filter, format=format
#     )


# def createDataset(
#     provider, id="", schema=None, token="", version="stable", filter="", format="json"
# ):
#     base_url = _queryURL(provider=provider, limit=None, basePath="datasets")

#     # TODO schema validation
#     return _post(
#         url=base_url,
#         json=schema,
#         token=token,
#         version=version,
#         token_in_params=True,
#         format=format,
#     )


# async def createDatasetAsync(
#     provider, id="", schema=None, token="", version="stable", filter="", format="json"
# ):
#     base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

#     # TODO schema validation
#     return await _postAsync(
#         url=base_url,
#         json=schema,
#         token=token,
#         version=version,
#         token_in_params=True,
#         format=format,
#     )


# def loadData(
#     provider,
#     id,
#     data,
#     dataType="",
#     token="",
#     version="stable",
#     filter="",
#     format="json",
#     overwrite=False,
#     maximumValidationErrors=None,
# ):
#     base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

#     # data interpolation
#     if not dataType:
#         data, headers = _interpolateDatatype(data)
#     else:
#         headers = {"content-type": dataType}

#     # TODO schema validation
#     if overwrite:
#         return _put(
#             url=base_url,
#             data=data,
#             token=token,
#             version=version,
#             filter=filter,
#             format=format,
#             token_in_params=True,
#             headers=headers,
#             maximumValidationErrors=maximumValidationErrors,
#         )
#     else:
#         return _post(
#             url=base_url,
#             data=data,
#             token=token,
#             version=version,
#             filter=filter,
#             format=format,
#             token_in_params=True,
#             headers=headers,
#             maximumValidationErrors=maximumValidationErrors,
#         )


# async def loadDataAsync(
#     provider, id, data, token="", version="stable", filter="", format="json"
# ):
#     base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")
#     # TODO schema validation
#     return await _putAsync(
#         url=base_url,
#         data=data,
#         token=token,
#         version=version,
#         token_in_params=True,
#         format=format,
#     )


# def modifyDataset(
#     provider, id, schema, token="", version="stable", filter="", format="json"
# ):
#     base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")
#     return _patch(
#         url=base_url,
#         json=schema,
#         token=token,
#         version=version,
#         token_in_params=True,
#         format=format,
#     )


# async def modifyDatasetAsync(
#     provider, id, schema, token="", version="stable", filter="", format="json"
# ):
#     base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")
#     return await _patchAsync(
#         url=base_url,
#         json=schema,
#         token=token,
#         version=version,
#         token_in_params=True,
#         format=format,
#     )


# def modifyData(
#     transforms=None,
#     provider="CORE",
#     id="",
#     key="",
#     subkey="",
#     range=None,
#     calendar=False,
#     limit=1,
#     subattribute="",
#     dateField=None,
#     from_=None,
#     to_=None,
#     on=None,
#     last=0,
#     first=0,
#     sort="",
#     interval=None,
#     token="",
#     version="stable",
#     filter="",
#     format="json",
#     **extra_params,
# ):
#     base_url = _queryURL(
#         provider=provider,
#         id=id,
#         key=key,
#         subkey=subkey,
#         range=range,
#         calendar=calendar,
#         limit=limit,
#         subattribute=subattribute,
#         dateField=dateField,
#         from_=from_,
#         to_=to_,
#         on=on,
#         last=last,
#         first=first,
#         sort=sort,
#         interval=interval,
#         basePath="datasets",
#         **extra_params,
#     )
#     return _patch(
#         url=base_url,
#         json=transforms,
#         token=token,
#         version=version,
#         token_in_params=True,
#         format=format,
#     )


# async def modifyDataAsync(
#     transforms=None,
#     provider="CORE",
#     id="",
#     key="",
#     subkey="",
#     range=None,
#     calendar=False,
#     limit=1,
#     subattribute="",
#     dateField=None,
#     from_=None,
#     to_=None,
#     on=None,
#     last=0,
#     first=0,
#     sort="",
#     interval=None,
#     token="",
#     version="stable",
#     filter="",
#     format="json",
#     **extra_params,
# ):
#     base_url = _queryURL(
#         provider=provider,
#         id=id,
#         key=key,
#         subkey=subkey,
#         range=range,
#         calendar=calendar,
#         limit=limit,
#         subattribute=subattribute,
#         dateField=dateField,
#         from_=from_,
#         to_=to_,
#         on=on,
#         last=last,
#         first=first,
#         sort=sort,
#         interval=interval,
#         basePath="datasets",
#         **extra_params,
#     )
#     return await _patchAsync(
#         url=base_url,
#         json=transforms,
#         token=token,
#         version=version,
#         token_in_params=True,
#         format=format,
#     )


# def deleteData(
#     provider="CORE",
#     id="",
#     key="",
#     subkey="",
#     date="",
#     range=None,
#     calendar=False,
#     subattribute="",
#     dateField=None,
#     from_=None,
#     to_=None,
#     on=None,
#     last=0,
#     first=0,
#     sort="",
#     interval=None,
#     token="",
#     version="stable",
#     filter="",
#     format="json",
#     **extra_params,
# ):
#     base_url = _queryURL(
#         provider=provider,
#         id=id,
#         key=key,
#         subkey=subkey,
#         date=date,
#         range=range,
#         calendar=calendar,
#         subattribute=subattribute,
#         dateField=dateField,
#         from_=from_,
#         to_=to_,
#         on=on,
#         last=last,
#         first=first,
#         sort=sort,
#         interval=interval,
#         basePath="datasets",
#         **extra_params,
#     )
#     return _delete(
#         url=base_url, token=token, version=version, filter=filter, format=format
#     )


# async def deleteDataAsync(
#     provider="CORE",
#     id="",
#     key="",
#     subkey="",
#     date="",
#     range=None,
#     calendar=False,
#     limit=1,
#     subattribute="",
#     dateField=None,
#     from_=None,
#     to_=None,
#     on=None,
#     last=0,
#     first=0,
#     sort="",
#     interval=None,
#     token="",
#     version="stable",
#     filter="",
#     format="json",
#     **extra_params,
# ):
#     base_url = _queryURL(
#         provider=provider,
#         id=id,
#         key=key,
#         subkey=subkey,
#         date=date,
#         range=range,
#         calendar=calendar,
#         limit=limit,
#         subattribute=subattribute,
#         dateField=dateField,
#         from_=from_,
#         to_=to_,
#         on=on,
#         last=last,
#         first=first,
#         sort=sort,
#         interval=interval,
#         basePath="datasets",
#         **extra_params,
#     )
#     return await _deleteAsync(
#         url=base_url, token=token, version=version, filter=filter, format=format
#     )


# def deleteDataset(
#     provider="CORE",
#     id="",
#     token="",
#     version="stable",
#     filter="",
#     format="json",
#     **extra_params,
# ):
#     base_url = _queryURL(
#         provider=provider,
#         id=id,
#         limit=None,
#         basePath="datasets",
#     )
#     return _delete(
#         url=base_url, token=token, version=version, filter=filter, format=format
#     )


# async def deleteDatasetAsync(
#     provider="CORE",
#     id="",
#     token="",
#     version="stable",
#     filter="",
#     format="json",
#     **extra_params,
# ):
#     base_url = _queryURL(
#         provider=provider,
#         id=id,
#         limit=None,
#         basePath="datasets",
#     )
#     return await _deleteAsync(
#         url=base_url, token=token, version=version, filter=filter, format=format
#     )


def createDataJob(
    provider,
    type,
    json,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}",
    )

    headers = {"content-type": "application/json"}

    return _post(
        url=base_url,
        json=json,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


async def createDataJobAsync(
    provider,
    type,
    json,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}",
    )

    headers = {"content-type": "application/json"}

    return await _postAsync(
        url=base_url,
        json=json,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


def listDataJobs(
    provider, type, token="", version="stable", filter="", format="json", **extra_params
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}",
    )

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def listDataJobsAsync(
    provider, type, token="", version="stable", filter="", format="json", **extra_params
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}",
    )

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def queryDataJob(
    provider,
    type,
    limit=0,
    from_="",
    to_="",
    last="",
    first="",
    sort="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}/query",
        limit=limit,
        from_=from_,
        to_=to_,
        last=last,
        first=first,
        sort=sort,
    )

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def queryDataJobAsync(
    provider,
    type,
    limit=0,
    from_="",
    to_="",
    last="",
    first="",
    sort="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}/query",
        limit=limit,
        from_=from_,
        to_=to_,
        last=last,
        first=first,
        sort=sort,
    )

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def listDataJobsById(
    provider,
    type,
    id,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}/{id}",
    )

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def listDataJobsByIdAsync(
    provider,
    type,
    id,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}/{id}",
    )

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def getDataJobLogFile(
    provider,
    type,
    id,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}/{id}/invalid-records-log",
    )

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def getDataJobLogFileAsync(
    provider,
    type,
    id,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"jobs/{provider}/{type}/{id}/invalid-records-log",
    )

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def awsOnboarding(
    provider,
    arnrole="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"aws-onboarding/{provider}/configure-aws-s3",
        arnrole=arnrole,
    )

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def awsOnboardingAsync(
    provider,
    arnrole="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"aws-onboarding/{provider}/configure-aws-s3",
        arnrole=arnrole,
    )

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def getplatformswaggerjson(
    token="", version="stable", filter="", format="json", **extra_params
):

    base_url = _queryURLLoose(
        basePath="platform/swagger-json",
    )

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def getplatformswaggerjsonAsync(
    token="", version="stable", filter="", format="json", **extra_params
):

    base_url = _queryURLLoose(
        basePath="platform/swagger-json",
    )

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def listDatasets(
    provider,
    limit=0,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, limit=None, basePath="datasets")

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def listDatasetsAsync(
    provider,
    limit=0,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, limit=None, basePath="datasets")

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def getDataset(
    provider, id, token="", version="stable", filter="", format="json", **extra_params
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def getDatasetAsync(
    provider, id, token="", version="stable", filter="", format="json", **extra_params
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def registerDataset(
    provider,
    json,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, limit=None, basePath="datasets")

    headers = {"content-type": "application/json"}

    return _post(
        url=base_url,
        json=json,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


async def registerDatasetAsync(
    provider,
    json,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, limit=None, basePath="datasets")

    headers = {"content-type": "application/json"}

    return await _postAsync(
        url=base_url,
        json=json,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


def loadData(
    provider,
    id,
    data=None,
    dataType="",
    overwrite=False,
    maximumValidationErrors=None,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    if not dataType:
        data, headers = _interpolateDatatype(data)
    else:
        headers = {"content-type": dataType}

    if overwrite:
        return _put(
            url=base_url,
            data=data,
            token=token,
            version=version,
            filter=filter,
            format=format,
            token_in_params=True,
            headers=headers,
            maximumValidationErrors=maximumValidationErrors,
        )
    else:
        return _post(
            url=base_url,
            data=data,
            token=token,
            version=version,
            filter=filter,
            format=format,
            token_in_params=True,
            headers=headers,
            maximumValidationErrors=maximumValidationErrors,
        )


async def loadDataAsync(
    provider,
    id,
    data=None,
    dataType="",
    overwrite=False,
    maximumValidationErrors=None,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    if not dataType:
        data, headers = _interpolateDatatype(data)
    else:
        headers = {"content-type": dataType}

    if overwrite:
        return await _putAsync(
            url=base_url,
            data=data,
            token=token,
            version=version,
            filter=filter,
            format=format,
            token_in_params=True,
            headers=headers,
            maximumValidationErrors=maximumValidationErrors,
        )
    else:
        return await _postAsync(
            url=base_url,
            data=data,
            token=token,
            version=version,
            filter=filter,
            format=format,
            token_in_params=True,
            headers=headers,
            maximumValidationErrors=maximumValidationErrors,
        )


def modifyDataset(
    provider,
    id,
    json,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    headers = {"content-type": "application/json"}

    return _patch(
        url=base_url,
        json=json,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


async def modifyDatasetAsync(
    provider,
    id,
    json,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    headers = {"content-type": "application/json"}

    return await _patchAsync(
        url=base_url,
        json=json,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


def deleteDataset(
    provider,
    id,
    data=None,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    if not dataType:
        data, headers = _interpolateDatatype(data)
    else:
        headers = {"content-type": dataType}

    return _delete(
        url=base_url,
        data=data,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


async def deleteDatasetAsync(
    provider,
    id,
    data=None,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    if not dataType:
        data, headers = _interpolateDatatype(data)
    else:
        headers = {"content-type": dataType}

    return await _deleteAsync(
        url=base_url,
        data=data,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


def deleteData(
    provider,
    id,
    key,
    subkey="",
    date="",
    data=None,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(
        provider=provider,
        id=id,
        key=key,
        subkey=subkey,
        date=date,
        limit=None,
        basePath="datasets",
    )

    if not dataType:
        data, headers = _interpolateDatatype(data)
    else:
        headers = {"content-type": dataType}

    return _delete(
        url=base_url,
        data=data,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


async def deleteDataAsync(
    provider,
    id,
    key,
    subkey="",
    date="",
    data=None,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURL(
        provider=provider,
        id=id,
        key=key,
        subkey=subkey,
        date=date,
        limit=None,
        basePath="datasets",
    )

    if not dataType:
        data, headers = _interpolateDatatype(data)
    else:
        headers = {"content-type": dataType}

    return await _deleteAsync(
        url=base_url,
        data=data,
        token=token,
        version=version,
        filter=filter,
        format=format,
        headers=headers,
    )


def getDataSourceContent(
    provider,
    objectId,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"sample-data-source/{provider}/{objectId}",
    )

    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def getDataSourceContentAsync(
    provider,
    objectId,
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):

    base_url = _queryURLLoose(
        basePath=f"sample-data-source/{provider}/{objectId}",
    )

    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )
