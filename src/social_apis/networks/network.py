from __future__ import generator_stop

import requests
from requests import Response

from social_apis.authentication.auth import Auth
from social_apis.exceptions.social_api_error import *

from social_apis import __version__


class Network(object):

    def __init__(self, api_url, quota_headers=None, client_args=None, **params):

        self.client_args = client_args or {}
        default_headers = {'User-Agent': 'SocialAPI v' + __version__}
        if 'headers' not in self.client_args:
            self.client_args['headers'] = default_headers
        elif 'User-Agent' not in self.client_args['headers']:
            self.client_args['headers'].update(default_headers)

        self.quota_headers = quota_headers

        self.client = requests.Session()
        self.client.auth = Auth(api_url, **params).auth

        client_args_copy = self.client_args.copy()
        for k, v in client_args_copy.items():
            if k in ('cert', 'hooks', 'max_redirects', 'proxies'):
                setattr(self.client, k, v)
                self.client_args.pop(k)

        self.client.headers.update(self.client_args.pop('headers'))

        self._last_call = None

    @staticmethod
    def transparent_params(_params: dict):
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

    @staticmethod
    def parse_response(response: Response):
        if response.status_code == 200:
            try:
                content = response.json()
            except ValueError:
                content = response.content
        else:
            raise SocialAPIError(f'Status code: {response.status_code}. Reason: {response.reason}')
        return content

    @staticmethod
    def get_error_message(response: Response):
        try:
            error_message = ''
            content = response.json()
            for key in ['error', 'errors', 'message', 'description']:
                if key in content:
                    error_message += f'{key}: {content[key]}; '
            if not len(error_message):
                error_message = response.text
            return error_message
        except ValueError:
            pass
        except (KeyError, IndexError):
            pass
        return 'An error occurred processing your request.'

    def process_response_error_message(self, response: Response):
        status_code = response.status_code
        if status_code > 304:
            error_message = self.get_error_message(response)
            self._last_call['api_error'] = error_message

            if status_code == 429 or 'limit' in error_message:
                raise RateLimitError(error_message, error_code=status_code, quota=self._last_call['quota'])
            elif status_code == 403 or 'forbidden' in error_message or response.reason == 'forbidden':
                raise ScopeError(error_message, error_code=status_code)
            elif status_code == 401 or 'authentication' in error_message:
                raise AuthError(error_message, error_code=status_code)

            raise SocialAPIError(error_message, error_code=status_code)

    def parse_quota_headers(self, headers: dict):
        quota = None
        if self.quota_headers is not None:
            try:
                if isinstance(self.quota_headers, list):
                    quota = '; '.join([headers.get(head) for head in self.quota_headers])
                elif isinstance(self.quota_headers, str):
                    quota = headers.get(self.quota_headers)
            except (KeyError, TypeError):
                pass
        return quota

    def get_quota(self):
        if self.quota_headers is None:
            return "<< There is no information about quotas for the current network. >>"
        if self._last_call is not None and 'quota' in self._last_call:
            return self._last_call['quota']
        else:
            return "<< Information about quotas will be after any request to the API. >>"

    def _request(self, url, method='GET', params=None, api_call=None, json_encoded=False):
        method = method.lower()
        params = params or {}

        func = getattr(self.client, method)
        if isinstance(params, dict) and json_encoded is False:
            params, files = self.transparent_params(params)
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
            raise MethodError(str(e))

        self._last_call = {
            'api_call': api_call,
            'api_error': None,
            'cookies': response.cookies,
            'headers': response.headers,
            'quota': self.parse_quota_headers(response.headers),
            'status_code': response.status_code,
            'url': response.url,
            'content': response.text,
        }

        self.process_response_error_message(response)
        content = self.parse_response(response)

        return content

    def request(self, url, method='GET', params=None, json_encoded=False):
        return self._request(url, method=method, params=params, api_call=url, json_encoded=json_encoded)

    def get(self, url, params=None):
        return self.request(url, params=params)

    def post(self, url, params=None, json_encoded=False):
        return self.request(url, 'POST', params=params, json_encoded=json_encoded)

    def put(self, url, params=None, json_encoded=False):
        return self.request(url, 'PUT', params=params, json_encoded=json_encoded)

    def delete(self, url, params=None, json_encoded=False):
        return self.request(url, 'DELETE', params=params, json_encoded=json_encoded)
