# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from __future__ import print_function

import aiohttp
import asyncio
import json
import os
import os.path
import time
from random import random
from threading import Event, Thread
from urllib.parse import urlparse
import requests
from socketIO_client_nexus import BaseNamespace, SocketIO
from sseclient import SSEClient

from .exception import PyEXception, PyEXStopSSE

_URL_PREFIX = "https://api.iextrading.com/1.0/"
_URL_PREFIX_CLOUD = "https://cloud.iexapis.com/{version}/"
_URL_PREFIX_CLOUD_ORIG = _URL_PREFIX_CLOUD
_URL_PREFIX_CLOUD_SANDBOX = "https://sandbox.iexapis.com/stable/"
_URL_PREFIX_CLOUD_SANDBOX_ORIG = _URL_PREFIX_CLOUD_SANDBOX

_SIO_URL_PREFIX = "https://ws-api.iextrading.com"
_SIO_PORT = 443

_SSE_URL_PREFIX = (
    "https://cloud-sse.iexapis.com/{version}/{channel}?symbols={symbols}&token={token}"
)
_SSE_URL_PREFIX_ORIG = _SSE_URL_PREFIX
_SSE_URL_PREFIX_ALL = "https://cloud-sse.iexapis.com/{version}/{channel}?token={token}"
_SSE_URL_PREFIX_ALL_ORIG = _SSE_URL_PREFIX_ALL
_SSE_DEEP_URL_PREFIX = "https://cloud-sse.iexapis.com/{version}/deep?symbols={symbols}&channels={channels}&token={token}"
_SSE_DEEP_URL_PREFIX_ORIG = _SSE_DEEP_URL_PREFIX
_SSE_URL_PREFIX_SANDBOX = (
    "https://sandbox-sse.iexapis.com/stable/{channel}?symbols={symbols}&token={token}"
)
_SSE_URL_PREFIX_SANDBOX_ORIG = _SSE_URL_PREFIX_SANDBOX
_SSE_URL_PREFIX_ALL_SANDBOX = (
    "https://sandbox-sse.iexapis.com/stable/{channel}?token={token}"
)
_SSE_URL_PREFIX_ALL_SANDBOX_ORIG = _SSE_URL_PREFIX_ALL_SANDBOX
_SSE_DEEP_URL_PREFIX_SANDBOX = "https://sandbox-sse.iexapis.com/stable/deep?symbols={symbols}&channels={channels}&token={token}"
_SSE_DEEP_URL_PREFIX_SANDBOX_ORIG = _SSE_DEEP_URL_PREFIX_SANDBOX

_PYEX_PROXIES = None
_PYEX_DEBUG = os.environ.get("PYEX_DEBUG", "")


def _get(url, token="", version="stable", filter="", format="json"):
    """for backwards compat, accepting token and version but ignoring"""
    token = token or os.environ.get("IEX_TOKEN")
    if token:
        if version == "sandbox":
            return _getIEXCloudSandbox(
                url=url, token=token, version=version, filter=filter, format=format
            )
        return _getIEXCloud(
            url=url, token=token, version=version, filter=filter, format=format
        )
    return _getOrig(url=url)


async def _getAsync(url, token="", version="stable", filter="", format="json"):
    """for backwards compat, accepting token and version but ignoring"""
    token = token or os.environ.get("IEX_TOKEN")
    if token:
        if version == "sandbox":
            return await _getIEXCloudSandboxAsync(
                url=url, token=token, version=version, filter=filter, format=format
            )
        return await _getIEXCloudAsync(
            url=url, token=token, version=version, filter=filter, format=format
        )
    return _getOrig(url=url)


def _post(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    token_in_params=True,
    filter="",
    format="json",
    maximumValidationErrors=None,
):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _postIEXCloudSandbox(
            url=url,
            data=data,
            json=json,
            headers=headers,
            token=token,
            version=version,
            token_in_params=token_in_params,
            format=format,
            filter=filter,
            maximumValidationErrors=maximumValidationErrors,
        )
    return _postIEXCloud(
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        token_in_params=token_in_params,
        format=format,
        filter=filter,
        maximumValidationErrors=maximumValidationErrors,
    )


def _put(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    token_in_params=True,
    filter="",
    format="json",
    maximumValidationErrors=None,
):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _putIEXCloudSandbox(
            url=url,
            data=data,
            json=json,
            headers=headers,
            token=token,
            version=version,
            token_in_params=token_in_params,
            format=format,
            filter=filter,
            maximumValidationErrors=maximumValidationErrors,
        )
    return _putIEXCloud(
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        token_in_params=token_in_params,
        format=format,
        filter=filter,
        maximumValidationErrors=maximumValidationErrors,
    )


def _patch(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    token_in_params=True,
    filter="",
    format="json",
):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _patchIEXCloudSandbox(
            url=url,
            data=data,
            json=json,
            headers=headers,
            token=token,
            version=version,
            token_in_params=token_in_params,
            format=format,
            filter=filter,
        )
    return _patchIEXCloud(
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        token_in_params=token_in_params,
        format=format,
        filter=filter,
    )


def _postAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    token_in_params=True,
    filter="",
    format="json",
):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _postIEXCloudSandboxAsync(
            url=url,
            data=data,
            json=json,
            headers=headers,
            token=token,
            version=version,
            token_in_params=token_in_params,
            format=format,
            filter=filter,
        )
    return _postIEXCloudAsync(
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        token_in_params=token_in_params,
        format=format,
        filter=filter,
    )


def _putAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    token_in_params=True,
    filter="",
    format="json",
):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _putIEXCloudSandboxAsync(
            url=url,
            data=data,
            json=json,
            headers=headers,
            token=token,
            version=version,
            token_in_params=token_in_params,
            format=format,
            filter=filter,
        )
    return _putIEXCloudAsync(
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        token_in_params=token_in_params,
        format=format,
        filter=filter,
    )


def _patchAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    token_in_params=True,
    filter="",
    format="json",
):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _patchIEXCloudSandboxAsync(
            url=url,
            data=data,
            json=json,
            headers=headers,
            token=token,
            version=version,
            token_in_params=token_in_params,
            format=format,
            filter=filter,
        )
    return _patchIEXCloudAsync(
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        token_in_params=token_in_params,
        format=format,
        filter=filter,
    )


def _delete(url, token="", version="stable", filter="", format="json"):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _deleteIEXCloudSandbox(
            url=url, token=token, version=version, filter=filter, format=format
        )
    return _deleteIEXCloud(
        url=url, token=token, version=version, filter=filter, format=format
    )


def _deleteAsync(url, token="", version="stable", filter="", format="json"):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _deleteIEXCloudSandboxAsync(
            url=url, token=token, version=version, filter=filter, format=format
        )
    return _deleteIEXCloudAsync(
        url=url, token=token, version=version, filter=filter, format=format
    )


def _getOrig(url):
    raise PyEXception(
        "Old IEX API is deprecated. For a free API token, sign up at https://iexcloud.io"
    )


def _getIEXCloudBase(
    base_url, url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    url = base_url.format(version=version) + url

    params = {"token": token}

    if filter:
        params["filter"] = filter

    if format not in ("json", "binary", "schema") and isinstance(format, str):
        params["format"] = format
    elif format == "schema":
        # add schema param
        params["schema"] = True

    if _PYEX_DEBUG:
        print(urlparse(url).geturl())

    tries = 1
    resp = requests.get(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params=params)

    while resp.status_code == 429:
        resp = requests.get(
            urlparse(url).geturl(), proxies=_PYEX_PROXIES, params=params
        )
        time.sleep(random() * 0.5 * tries)
        tries += 1

    if resp.status_code == 200:
        if format == "json":
            return resp.json()
        elif format == "binary":
            return resp.content
        elif format == "schema":
            return _parseSchema(resp.json())
        return resp.text
    raise PyEXception("Response %d - " % resp.status_code, resp.text)


def _getIEXCloud(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return _getIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


async def _getIEXCloudBaseAsync(
    base_url, url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    url = base_url.format(version=version) + url
    params = {"token": token}

    if filter:
        params["filter"] = filter

    if format not in ("json", "binary"):
        params["format"] = format

    if _PYEX_DEBUG:
        print(urlparse(url).geturl())

    tries = 1

    while tries < 5:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                urlparse(url).geturl(), proxy=_PYEX_PROXIES, params=params
            ) as resp:

                if resp.status == 429:
                    tries += 1
                    await asyncio.sleep(random() * 0.5 * tries)

                elif resp.status == 200:
                    if format == "json":
                        return await resp.json()
                    elif format == "binary":
                        return await resp.read()
                    return await resp.text()
                else:
                    # break and hit the exception case
                    break
    raise PyEXception("Response %d - " % resp.status, await resp.text())


async def _getIEXCloudAsync(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return await _getIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _getIEXCloudSandbox(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return _getIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        token=token,
        version="stable",
        filter=filter,
        format=format,
    )


async def _getIEXCloudSandboxAsync(
    url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    return await _getIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        token=token,
        version="stable",
        filter=filter,
        format=format,
    )


def _pppIEXCloudBase(
    base_url,
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter=None,
    format="json",
    token_in_params=True,
    verb="post",
    maximumValidationErrors=None,
):
    """for iex cloud"""
    url = base_url.format(version=version) + url

    if token_in_params:
        params = {"token": token}
    else:
        params = {}

    if format != "json":
        params["format"] = format

    if filter:
        params["filter"] = filter

    if maximumValidationErrors:
        params["maximumValidationErrors"] = maximumValidationErrors

    if _PYEX_DEBUG:
        print(urlparse(url).geturl())

    resp = getattr(requests, verb)(
        urlparse(url).geturl(),
        data=data,
        json=json,
        headers=headers,
        proxies=_PYEX_PROXIES,
        params=params,
    )
    if resp.status_code == 200:
        if format == "json":
            return resp.json()
        return resp.text
    raise PyEXception("Response %d - " % resp.status_code, resp.text)


def _postIEXCloud(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
    maximumValidationErrors=None,
):
    return _pppIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        maximumValidationErrors=maximumValidationErrors,
        verb="post",
    )


def _putIEXCloud(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
    maximumValidationErrors=None,
):
    return _pppIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        data=data,
        headers=headers,
        json=json,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        maximumValidationErrors=maximumValidationErrors,
        verb="put",
    )


def _patchIEXCloud(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return _pppIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        verb="patch",
    )


async def _pppIEXCloudBaseAsync(
    base_url,
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
    verb="post",
):
    """for iex cloud"""
    import aiohttp

    url = base_url.format(version=version) + url

    if token_in_params:
        params = {"token": token}
    else:
        params = {}

    if format != "json":
        params["format"] = format

    if filter:
        params["filter"] = filter

    if _PYEX_DEBUG:
        print(urlparse(url).geturl())

    async with aiohttp.ClientSession(headers=headers) as session:
        async with getattr(session, verb)(
            urlparse(url).geturl(),
            data=data,
            json=json,
            proxy=_PYEX_PROXIES,
            params=params,
        ) as resp:
            if resp.status == 200:
                if format == "json":
                    return await resp.json()
                return await resp.text()
            raise PyEXception("Response %d - " % resp.status, await resp.text())


async def _postIEXCloudAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return await _pppIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        verb="post",
    )


async def _putIEXCloudAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return await _pppIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        verb="put",
    )


async def _patchIEXCloudAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return await _pppIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        verb="patch",
    )


def _postIEXCloudSandbox(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
    maximumValidationErrors=None,
):
    return _pppIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        maximumValidationErrors=maximumValidationErrors,
        verb="post",
    )


def _putIEXCloudSandbox(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
    maximumValidationErrors=None,
):
    return _pppIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        maximumValidationErrors=maximumValidationErrors,
        verb="put",
    )


def _patchIEXCloudSandbox(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return _pppIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        format=format,
        token_in_params=token_in_params,
        verb="patch",
    )


async def _postIEXCloudSandboxAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return await _pppIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        token_in_params=token_in_params,
        format=format,
        verb="post",
    )


async def _putIEXCloudSandboxAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return await _pppIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        token_in_params=token_in_params,
        format=format,
        verb="put",
    )


async def _patchIEXCloudSandboxAsync(
    url,
    data=None,
    json=None,
    headers=None,
    token="",
    version="stable",
    filter="",
    format="json",
    token_in_params=True,
):
    return await _pppIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        data=data,
        json=json,
        headers=headers,
        token=token,
        version=version,
        filter=filter,
        token_in_params=token_in_params,
        format=format,
        verb="patch",
    )


def _deleteIEXCloudBase(
    base_url, url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    url = base_url.format(version=version) + url

    params = {"token": token}

    if format != "json":
        params["format"] = format

    if _PYEX_DEBUG:
        print(urlparse(url).geturl())

    resp = requests.delete(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params=params)

    if resp.status_code == 200:
        if format == "json":
            return resp.json()
        return resp.text
    raise PyEXception("Response %d - " % resp.status_code, resp.text)


async def _deleteIEXCloudBaseAsync(
    base_url, url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    import aiohttp

    url = base_url.format(version=version) + url

    params = {"token": token}

    if format != "json":
        params["format"] = format

    async with aiohttp.ClientSession() as session:
        async with session.delete(
            urlparse(url).geturl(),
            proxy=_PYEX_PROXIES,
            params=params,
        ) as resp:
            if resp.status == 200:
                if format == "json":
                    return await resp.json()
                return resp.text()
            raise PyEXception("Response %d - " % resp.status, await resp.text())


def _deleteIEXCloud(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return _deleteIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD, url=url, token=token, version=version, format=format
    )


async def _deleteIEXCloudAsync(
    url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    return await _deleteIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD, url=url, token=token, version=version, format=format
    )


def _deleteIEXCloudSandbox(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return _deleteIEXCloudBase(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        token=token,
        version="stable",
        filter=filter,
        format=format,
    )


async def _deleteIEXCloudSandboxAsync(
    url, token="", version="stable", filte="", format="json"
):
    """for iex cloud"""
    return await _deleteIEXCloudBaseAsync(
        base_url=_URL_PREFIX_CLOUD_SANDBOX,
        url=url,
        token=token,
        version=version,
        format=format,
    )


def _wsURL(url):
    """internal"""
    return "/1.0/" + url


def _tryJson(data, raw=True):
    """internal"""
    if raw:
        return data
    try:
        return json.loads(data)
    except ValueError:
        return data


class WSClient(object):
    def __init__(
        self, addr, sendinit=None, on_data=None, on_open=None, on_close=None, raw=True
    ):
        """
        addr: path to sio
        sendinit: tuple to emit
        on_data, on_open, on_close: functions to call
        """
        self.addr = addr
        self.sendinit = sendinit

        on_data = on_data or print

        class Namespace(BaseNamespace):
            def on_connect(self, *data):
                if on_open:
                    on_open(_tryJson(data, raw))

            def on_disconnect(self, *data):
                if on_close:
                    on_close(_tryJson(data, raw))

            def on_message(self, data):
                on_data(_tryJson(data, raw))

        self._Namespace = Namespace

    def run(self):
        self.socketIO = SocketIO(_SIO_URL_PREFIX, _SIO_PORT)
        self.namespace = self.socketIO.define(self._Namespace, self.addr)
        if self.sendinit:
            self.namespace.emit(*self.sendinit)
        self.socketIO.wait()


def _stream(url, sendinit=None, on_data=print):
    """internal"""
    cl = WSClient(url, sendinit=sendinit, on_data=on_data)
    return cl


def _streamSSE(url, on_data=print, exit=None, nosnapshot=False):
    """internal"""

    if nosnapshot:
        url += "&nosnapshot=true"

    messages = SSEClient(url, proxies=_PYEX_PROXIES, headers={"keep_alive": "false"})

    def _runner(messages=messages, on_data=on_data):
        for msg in messages:
            data = msg.data

            try:
                on_data(json.loads(data))
            except PyEXStopSSE:
                # stop listening and return
                return
            except (json.JSONDecodeError,):
                continue
            except (KeyboardInterrupt,):
                raise
            except Exception:
                raise

    def _exit(messages=messages, exit=exit):
        # run runner in wrapper
        runthread = Thread(target=_runner)

        # die with parent
        runthread.daemon = True

        # start the runner
        runthread.start()

        # wait for exit event
        exit.wait()

        # kill
        killerthread = Thread(target=lambda: messages.resp.close())

        # die with parent
        killerthread.daemon = True

        # start the killer
        killerthread.start()

        return

    if isinstance(exit, Event):
        # run on thread, stop when exit set
        exitthread = Thread(target=_exit)

        # start the threads
        exitthread.start()

        # return the threads
        return exitthread
    else:
        # just call and return the function
        return _runner()


async def _streamSSEAsync(url, exit=None):
    """internal"""
    from asyncio import Event

    from aiohttp_sse_client import client as sse_client
    from aiostream.stream import merge

    async with sse_client.EventSource(url) as event_source:
        if isinstance(exit, Event):

            async def _waitExit():
                yield await exit.wait()

            waits = (_waitExit(), event_source)
        else:
            waits = (event_source,)

        try:
            async with merge(*waits).stream() as stream:
                try:
                    async for event in stream:
                        if event == True:  # noqa: E712
                            return
                        yield json.loads(event.data)
                except ConnectionError:
                    raise PyEXception("Could not connect to SSE Stream")
                except PyEXStopSSE:
                    return
                except BaseException:
                    raise
        except (json.JSONDecodeError, KeyboardInterrupt):
            raise


def setProxy(proxies=None):
    """Set proxies argument for requests

    Args:
        proxies (dict): Proxies to set
    """
    global _PYEX_PROXIES
    _PYEX_PROXIES = proxies


def overrideUrl(url="", env=""):
    """Override the default IEX Cloud url"""
    global _URL_PREFIX_CLOUD, _URL_PREFIX_CLOUD_SANDBOX, _SSE_URL_PREFIX, _SSE_URL_PREFIX_ALL, _SSE_DEEP_URL_PREFIX, _SSE_URL_PREFIX_SANDBOX, _SSE_URL_PREFIX_ALL_SANDBOX, _SSE_DEEP_URL_PREFIX_SANDBOX

    if env:
        _URL_PREFIX_CLOUD = "https://cloud.{env}.iexapis.com/{{version}}/".format(
            env=env
        )
        _URL_PREFIX_CLOUD_SANDBOX = "https://sandbox.{env}.iexapis.com/stable/".format(
            env=env
        )
        _SSE_URL_PREFIX = "https://cloud-sse.{env}.iexapis.com/{{version}}/{{channel}}?symbols={{symbols}}&token={{token}}".format(
            env=env
        )
        _SSE_URL_PREFIX_ALL = "https://cloud-sse.{env}.iexapis.com/{{version}}/{{channel}}?token={{token}}".format(
            env=env
        )
        _SSE_DEEP_URL_PREFIX = "https://cloud-sse.{env}.iexapis.com/{{version}}/deep?symbols={{symbols}}&channels={{channels}}&token={{token}}".format(
            env=env
        )
        _SSE_URL_PREFIX_SANDBOX = "https://sandbox-sse.{env}.iexapis.com/stable/{{channel}}?symbols={{symbols}}&token={{token}}".format(
            env=env
        )
        _SSE_URL_PREFIX_ALL_SANDBOX = "https://sandbox-sse.{env}.iexapis.com/stable/{{channel}}?token={{token}}".format(
            env=env
        )
        _SSE_DEEP_URL_PREFIX_SANDBOX = "https://sandbox-sse.{env}.iexapis.com/stable/deep?symbols={{symbols}}&channels={{channels}}&token={{token}}".format(
            env=env
        )
    elif url:
        _URL_PREFIX_CLOUD = url
        _URL_PREFIX_CLOUD_SANDBOX = url
        _SSE_URL_PREFIX = "{}{{channel}}?symbols={{symbols}}&token={{token}}".format(
            url
        )
        _SSE_URL_PREFIX_ALL = "{}{{channel}}?token={{token}}".format(url)
        _SSE_DEEP_URL_PREFIX = (
            "{}deep?symbols={{symbols}}&channels={{channels}}&token={{token}}".format(
                url
            )
        )
        _SSE_URL_PREFIX_SANDBOX = (
            "{}{{channel}}?symbols={{symbols}}&token={{token}}".format(url)
        )
        _SSE_URL_PREFIX_ALL_SANDBOX = "{}{{channel}}?token={{token}}".format(url)
        _SSE_DEEP_URL_PREFIX_SANDBOX = (
            "{}deep?symbols={{symbols}}&channels={{channels}}&token={{token}}".format(
                url
            )
        )
    else:
        # reset
        _URL_PREFIX_CLOUD = _URL_PREFIX_CLOUD_ORIG
        _URL_PREFIX_CLOUD_SANDBOX = _URL_PREFIX_CLOUD_SANDBOX_ORIG
        _SSE_URL_PREFIX = _SSE_URL_PREFIX_ORIG
        _SSE_URL_PREFIX_ALL = _SSE_URL_PREFIX_ALL_ORIG
        _SSE_DEEP_URL_PREFIX = _SSE_DEEP_URL_PREFIX_ORIG
        _SSE_URL_PREFIX_SANDBOX = _SSE_URL_PREFIX_SANDBOX_ORIG
        _SSE_URL_PREFIX_ALL_SANDBOX = _SSE_URL_PREFIX_ALL_SANDBOX_ORIG
        _SSE_DEEP_URL_PREFIX_SANDBOX = _SSE_DEEP_URL_PREFIX_SANDBOX_ORIG


def _parseSchema(data):
    if isinstance(data, list) and len(data) > 0:
        # take first value
        data = data[0]
    if data:
        return data
    return {}
