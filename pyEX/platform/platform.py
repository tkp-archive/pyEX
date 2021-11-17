# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ..common import (
    PyEXception,
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
    _toDatetime,
    json_normalize,
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
    overrideBase="",
    **extra_params,
):

    base_url = "query"
    
    if (provider):
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

        if not last and (not from_ or not to_):
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

        if extra_params:
            base_url += "&".join("{}={}".format(k, v) for k, v in extra_params.items())

    return base_url


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
    overrideBase="",
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
        overrideBase=overrideBase,
        **extra_params,
    )
    return _get(base_url, token=token, version=version, filter=filter, format=format)


def list(provider="CORE", id="", token="", version="stable", filter="", format="json"):
    base_url = _queryURL(provider=provider, id=id)
    return _get(base_url, token=token, version=version, filter=filter, format=format)


def create(
    provider, id="", schema=None, token="", version="stable", filter="", format="json"
):
    base_url = _queryURL(provider=provider, id=id)
    raise NotImplementedError


def upload(provider, id, data, token="", version="stable", filter="", format="json"):
    base_url = _queryURL(provider=provider, id=id)
    raise NotImplementedError


def alter(provider, id, schema, token="", version="stable", filter="", format="json"):
    base_url = _queryURL(provider=provider, id=id)
    raise NotImplementedError


def modify(
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
    overrideBase="",
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
        overrideBase=overrideBase,
        **extra_params,
    )
    raise NotImplementedError


def delete(
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
    overrideBase="",
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
        overrideBase=overrideBase,
        **extra_params,
    )
    return _delete(base_url, token=token, version=version, filter=filter, format=format)
