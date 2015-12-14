"""
STUPS Zign OAuth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin
import zign.api


__version__ = '0.2'
__author__ = 'Henning Jacobs'
__licence__ = 'Apache 2.0'


class InvalidZignToken(Exception):
    def __init__(self, token_name):
        self.token_name = token_name

    def __str__(self):
        return 'invalid or expired Zign OAuth token: "{}"'.format(self.token_name)


class ZignAuth:
    def __init__(self, token_name, scopes):
        self.token_name = token_name
        self.scopes = scopes

    def __call__(self, r):
        access_token = zign.api.get_token(self.token_name, self.scopes)
        if not access_token:
            raise InvalidZignToken(self.token_name)
        r.headers['Authorization'] = 'Bearer {}'.format(access_token)
        return r


class ZignPlugin(AuthPlugin):

    name = 'Zign OAuth 2.0'
    auth_type = 'zign'
    description = ''

    def get_auth(self, username, password):
        scopes_str = password or ''
        scopes = list(filter(None, scopes_str.split(',')))
        return ZignAuth(username, scopes)
