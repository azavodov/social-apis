from __future__ import generator_stop

import requests

from social_apis.authentication.auth import Auth
from social_apis.exceptions.social_api_error import SocialAPIError

from social_apis import __version__


class Network(object):

    def __init__(self, api_url, client_args=None, **params):

        self.client_args = client_args or {}
        default_headers = {'User-Agent': 'SocialAPI v' + __version__}
        if 'headers' not in self.client_args:
            self.client_args['headers'] = default_headers
        elif 'User-Agent' not in self.client_args['headers']:
            self.client_args['headers'].update(default_headers)

        self.client = requests.Session()
        self.client.auth = Auth(api_url, **params).auth

        client_args_copy = self.client_args.copy()
        for k, v in client_args_copy.items():
            if k in ('cert', 'hooks', 'max_redirects', 'proxies'):
                setattr(self.client, k, v)
                self.client_args.pop(k)

        self.client.headers.update(self.client_args.pop('headers'))

        self._last_call = None

    def _request(self, url, method='GET', params=None, api_call=None, json_encoded=False):
        method = method.lower()
        params = params or {}

        func = getattr(self.client, method)
        if isinstance(params, dict) and json_encoded is False:
            params, files = self._transparent_params(params)
        else:
            params = params
            files = list()

        requests_args = {}
        for k, v in self.client_args.items():
            if k in ('timeout', 'allow_redirects', 'stream', 'verify'):
                requests_args[k] = v

        if method == 'get' or method == 'delete':
            requests_args['params'] = params
        else:
            if json_encoded:
                data_key = 'json'
            else:
                data_key = 'data'
            requests_args.update({
                data_key: params,
                'files': files,
            })
        try:
            response = func(url, **requests_args)
        except requests.RequestException as e:
            raise SocialAPIError(str(e))
        except Exception as e:
            print(e)

        self._last_call = {
            'api_call': api_call,
            'api_error': None,
            'cookies': response.cookies,
            'headers': response.headers,
            'status_code': response.status_code,
            'url': response.url,
            'content': response.text,
        }

        content = ''
        try:
            if response.status_code == 204:
                content = response.content
            else:
                content = response.json()
        except ValueError:
            if response.content != '':
                raise SocialAPIError('Response was not valid JSON. Unable to decode.')

        return content

    def request(self, url, method='GET', params=None, json_encoded=False):
        return self._request(url, method=method, params=params, api_call=url, json_encoded=json_encoded)

    def get(self, url, params=None):
        return self.request(url, params=params)

    def post(self, url, params=None, json_encoded=False):
        return self.request(url, 'POST', params=params, json_encoded=json_encoded)

    def delete(self, url, params=None, json_encoded=False):
        return self.request(url, 'DELETE', params=params, json_encoded=json_encoded)

    @staticmethod
    def _transparent_params(_params):
        params = {}
        files = {}
        for k, v in _params.items():
            if hasattr(v, 'read') and callable(v.read):
                files[k] = v
            elif isinstance(v, bool):
                if v:
                    params[k] = 'true'
                else:
                    params[k] = 'false'
            elif isinstance(v, (str, bytes)) or isinstance(v, (int, float)):
                params[k] = v
            elif isinstance(v, list):
                try:
                    params[k] = ','.join(v)
                except TypeError:
                    params[k] = ','.join(map(str, v))
            else:
                continue
        return params, files
