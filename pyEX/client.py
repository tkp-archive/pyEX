import os
from .common import PyEXception, _getJson, _USAGE_TYPES


class Client(object):
    def __init__(self, api_token=None, version='beta'):
        self._token = api_token or os.environ.get('IEX_TOKEN', '')
        if not self._token:
            raise PyEXception('API Token missing or not in environment (IEX_TOKEN)')

        self._version = version

    def account(self):
        return _getJson('account/metadata', self._token, self._version)

    def usage(self, type=None):
        if type:
            if type not in _USAGE_TYPES:
                raise PyEXception('type not recognized: {}'.format(type))
            return _getJson('account/usage/{type}'.format(type=type), self._token, self._version)
        return _getJson('account/usage/messages', self._token, self._version)
