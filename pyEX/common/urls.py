# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from __future__ import print_function

import json
import os
import os.path
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

_SIO_URL_PREFIX = "https://ws-api.iextrading.com"
_SIO_PORT = 443

_SSE_URL_PREFIX = (
    "https://cloud-sse.iexapis.com/{version}/{channel}?symbols={symbols}&token={token}"
)
_SSE_URL_PREFIX_ORIG = _SSE_URL_PREFIX
_SSE_URL_PREFIX_ALL = "https://cloud-sse.iexapis.com/{version}/{channel}?token={token}"
_SSE_DEEP_URL_PREFIX = "https://cloud-sse.iexapis.com/{version}/deep?symbols={symbols}&channels={channels}&token={token}"
_SSE_URL_PREFIX_SANDBOX = (
    "https://sandbox-sse.iexapis.com/stable/{channel}?symbols={symbols}&token={token}"
)
_SSE_URL_PREFIX_ALL_SANDBOX = (
    "https://sandbox-sse.iexapis.com/stable/{channel}?token={token}"
)
_SSE_DEEP_URL_PREFIX_SANDBOX = "https://sandbox-sse.iexapis.com/stable/deep?symbols={symbols}&channels={channels}&token={token}"

_PYEX_PROXIES = None


def _get(url, token="", version="stable", filter="", format="json"):
    """for backwards compat, accepting token and version but ignoring"""
    token = token or os.environ.get("IEX_TOKEN")
    if token:
        if version == "sandbox":
            return _getIEXCloudSandbox(url, token, version, filter, format)
        return _getIEXCloud(url, token, version, filter, format)
    return _getOrig(url)


async def _getAsync(url, token="", version="stable", filter="", format="json"):
    """for backwards compat, accepting token and version but ignoring"""
    token = token or os.environ.get("IEX_TOKEN")
    if token:
        if version == "sandbox":
            return await _getIEXCloudSandboxAsync(url, token, version, filter, format)
        return await _getIEXCloudAsync(url, token, version, filter, format)
    return _getOrig(url)


def _post(
    url,
    data=None,
    json=None,
    token="",
    version="stable",
    token_in_params=True,
    format="json",
):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _postIEXCloudSandbox(
            url, data, json, token, version, token_in_params, format
        )
    return _postIEXCloud(url, data, json, token, version, token_in_params, format)


def _delete(url, token="", version="stable", format="json"):
    token = token or os.environ.get("IEX_TOKEN")
    if version == "sandbox":
        return _deleteIEXCloudSandbox(url, token, version, format)
    return _deleteIEXCloud(url, token, version, format)


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

    if format != "json" and isinstance(format, str):
        params["format"] = format

    resp = requests.get(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params=params)

    if resp.status_code == 200:
        if format == "json":
            return resp.json()
        return resp.text
    raise PyEXception("Response %d - " % resp.status_code, resp.text)


def _getIEXCloud(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return _getIEXCloudBase(_URL_PREFIX_CLOUD, url, token, version, filter, format)


async def _getIEXCloudAsyncBase(
    base_url, url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    import aiohttp

    url = _URL_PREFIX_CLOUD.format(version=version) + url
    params = {"token": token}

    if filter:
        params["filter"] = filter

    if format != "json":
        params["format"] = format

    async with aiohttp.ClientSession() as session:
        async with session.get(
            urlparse(url).geturl(), proxy=_PYEX_PROXIES, params=params
        ) as resp:

            if resp.status == 200:
                if format == "json":
                    return await resp.json()
                return resp.text()
            raise PyEXception("Response %d - " % resp.status, await resp.text())


async def _getIEXCloudAsync(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return await _getIEXCloudAsyncBase(
        _URL_PREFIX_CLOUD, url, token, version, filter, format
    )


def _getIEXCloudSandbox(url, token="", version="stable", filter="", format="json"):
    """for iex cloud"""
    return _getIEXCloudBase(
        _URL_PREFIX_CLOUD_SANDBOX, url, token, "stable", filter, format
    )


async def _getIEXCloudSandboxAsync(
    url, token="", version="stable", filter="", format="json"
):
    """for iex cloud"""
    return await _getIEXCloudAsyncBase(
        _URL_PREFIX_CLOUD_SANDBOX, url, token, "stable", filter, format
    )


def _postIEXCloudBase(
    base_url,
    url,
    data=None,
    json=None,
    token="",
    version="stable",
    token_in_params=True,
    format="json",
):
    """for iex cloud"""
    url = base_url.format(version=version) + url

    if token_in_params:
        params = {"token": token}
    else:
        params = {}

    if format != "json":
        params["format"] = format

    resp = requests.post(
        urlparse(url).geturl(),
        data=data,
        json=json,
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
    token="",
    version="stable",
    token_in_params=True,
    format="json",
):
    """for iex cloud"""
    return _postIEXCloudBase(
        _URL_PREFIX_CLOUD, data, json, token, version, token_in_params, format
    )


async def _postIEXCloudAsyncBase(
    base_url,
    url,
    data=None,
    json=None,
    token="",
    version="stable",
    filter="",
    token_in_params=True,
    format="json",
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

    async with aiohttp.ClientSession() as session:
        async with session.post(
            urlparse(url).geturl(),
            data=data,
            json=json,
            proxy=_PYEX_PROXIES,
            params=params,
        ) as resp:
            if resp.status == 200:
                if format == "json":
                    return await resp.json()
                return resp.text()
            raise PyEXception("Response %d - " % resp.status, await resp.text())


async def _postIEXCloudAsync(
    url,
    data=None,
    json=None,
    token="",
    version="stable",
    filter="",
    token_in_params=True,
    format="json",
):
    """for iex cloud"""
    return await _postIEXCloudAsyncBase(
        _URL_PREFIX_CLOUD,
        url,
        data,
        json,
        token,
        version,
        filter,
        token_in_params,
        format,
    )


def _postIEXCloudSandbox(
    url,
    data=None,
    json=None,
    token="",
    version="stable",
    token_in_params=True,
    format="json",
):
    """for iex cloud"""
    return _postIEXCloudBase(
        _URL_PREFIX_CLOUD_SANDBOX,
        url,
        data,
        json,
        token,
        "stable",
        token_in_params,
        format,
    )


def _deleteIEXCloudBase(base_url, url, token="", version="stable", format="json"):
    """for iex cloud"""
    url = base_url.format(version=version) + url

    params = {"token": token}

    if format != "json":
        params["format"] = format

    resp = requests.delete(urlparse(url).geturl(), proxies=_PYEX_PROXIES, params=params)

    if resp.status_code == 200:
        if format == "json":
            return resp.json()
        return resp.text
    raise PyEXception("Response %d - " % resp.status_code, resp.text)


def _deleteIEXCloud(url, token="", version="stable", format="json"):
    """for iex cloud"""
    return _deleteIEXCloud(_URL_PREFIX_CLOUD, url, token, version, format)


async def _deleteIEXCloudAsyncBase(url, token="", version="stable", format="json"):
    """for iex cloud"""
    import aiohttp

    url = _URL_PREFIX_CLOUD.format(version=version) + url
    params = {"token": token}

    if format != "json":
        params["format"] = format

    async with aiohttp.ClientSession() as session:
        async with session.delete(
            urlparse(url).geturl(), proxy=_PYEX_PROXIES, params=params
        ) as resp:
            if resp.status == 200:
                if format == "json":
                    return await resp.json()
                return resp.text()
            raise PyEXception("Response %d - " % resp.status, await resp.text())


async def _deleteIEXCloudAsync(url, token="", version="stable", format="json"):
    """for iex cloud"""
    return await _deleteIEXCloudAsyncBase(
        _URL_PREFIX_CLOUD, url, token, version, format
    )


def _deleteIEXCloudSandbox(url, token="", version="stable", format="json"):
    """for iex cloud"""
    return _deleteIEXCloudBase(_URL_PREFIX_CLOUD_SANDBOX, url, token, "stable", format)


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


def _streamSSE(url, on_data=print, exit=None):
    """internal"""

    messages = SSEClient(url, proxies=_PYEX_PROXIES, headers={"keep_alive": "false"})

    def _runner(messages=messages, on_data=on_data):
        for msg in messages:
            data = msg.data

            try:
                on_data(json.loads(data))
            except PyEXStopSSE:
                # stop listening and return
                print("HERE3")
                return
            except (json.JSONDecodeError, KeyboardInterrupt):
                print("HERE4")
                raise
            except Exception:
                print("HERE5")
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
    global _URL_PREFIX_CLOUD
    if env:
        _URL_PREFIX_CLOUD = "https://cloud.{env}.iexapis.com/{{version}}/".format(
            env=env
        )
    elif url:
        _URL_PREFIX_CLOUD = url
    else:
        # reset
        _URL_PREFIX_CLOUD = _URL_PREFIX_CLOUD_ORIG


def overrideSSEUrl(url="", env=""):
    """Override the default IEX Cloud SSE url"""
    global _SSE_URL_PREFIX
    if env:
        _SSE_URL_PREFIX = "https://cloud-sse.{env}.iexapis.com/{{version}}/{{channel}}?symbols={{symbols}}&token={{token}}".format(
            env=env
        )
    elif url:
        _SSE_URL_PREFIX = url
    else:
        # reset
        _SSE_URL_PREFIX = _SSE_URL_PREFIX_ORIG
