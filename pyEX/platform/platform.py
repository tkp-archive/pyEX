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


def listJobs(
    provider,
    type="ingest",
    jobId="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    url = "jobs/{}/{}".format(provider, type)

    if jobId:
        url += "/{}".format(jobId)

    return _get(url=url, token=token, version=version, filter=filter, format=format)


def listDatasets(
    provider="CORE", id="", token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, id=id)
    return _get(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


@wraps(listDatasets)
def listDatasetsDF(*args, **kwargs):
    return pd.DataFrame(listDatasets(*args, **kwargs))


async def listDatasetsAsync(
    provider="CORE", id="", token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, id=id)
    return await _getAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def createDataset(
    provider, id="", schema=None, token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, limit=None, basePath="datasets")

    # TODO schema validation
    return _post(
        url=base_url,
        json=schema,
        token=token,
        version=version,
        token_in_params=True,
        format=format,
    )


async def createDatasetAsync(
    provider, id="", schema=None, token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    # TODO schema validation
    return await _postAsync(
        url=base_url,
        json=schema,
        token=token,
        version=version,
        token_in_params=True,
        format=format,
    )


def loadData(
    provider,
    id,
    data,
    dataType="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")

    # data interpolation
    if not dataType:
        data, headers = _interpolateDatatype(data)
    else:
        headers = {"content-type": dataType}

    # TODO schema validation
    return _put(
        url=base_url,
        data=data,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=True,
        headers=headers,
    )


async def loadDataAsync(
    provider, id, data, token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")
    # TODO schema validation
    return await _putAsync(
        url=base_url,
        data=data,
        token=token,
        version=version,
        token_in_params=True,
        format=format,
    )


def modifyDataset(
    provider, id, schema, token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")
    return _patch(
        url=base_url,
        json=schema,
        token=token,
        version=version,
        token_in_params=True,
        format=format,
    )


async def modifyDatasetAsync(
    provider, id, schema, token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, id=id, limit=None, basePath="datasets")
    return await _patchAsync(
        url=base_url,
        json=schema,
        token=token,
        version=version,
        token_in_params=True,
        format=format,
    )


def modifyData(
    transforms=None,
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
        basePath="datasets",
        **extra_params,
    )
    return _patch(
        url=base_url,
        json=transforms,
        token=token,
        version=version,
        token_in_params=True,
        format=format,
    )


async def modifyDataAsync(
    transforms=None,
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
        basePath="datasets",
        **extra_params,
    )
    return await _patchAsync(
        url=base_url,
        json=transforms,
        token=token,
        version=version,
        token_in_params=True,
        format=format,
    )


def deleteData(
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
        basePath="datasets",
        **extra_params,
    )
    return _delete(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def deleteDataAsync(
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
        basePath="datasets",
        **extra_params,
    )
    return await _deleteAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


def deleteDataset(
    provider="CORE",
    id="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):
    base_url = _queryURL(
        provider=provider,
        id=id,
        limit=None,
        basePath="datasets",
    )
    return _delete(
        url=base_url, token=token, version=version, filter=filter, format=format
    )


async def deleteDatasetAsync(
    provider="CORE",
    id="",
    token="",
    version="stable",
    filter="",
    format="json",
    **extra_params,
):
    base_url = _queryURL(
        provider=provider,
        id=id,
        limit=None,
        basePath="datasets",
    )
    return await _deleteAsync(
        url=base_url, token=token, version=version, filter=filter, format=format
    )
