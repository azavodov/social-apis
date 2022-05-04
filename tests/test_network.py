import unittest

from social_apis.networks.network import Network


class TestNetwork(unittest.TestCase):

    def test_default_headers_user_agent(self):
        network = Network(access_token="---", api_url="---")
        self.assertIn("User-Agent", network.client.headers)

    def test_custom_headers_user_agent(self):
        network = Network(access_token="---", api_url="---", client_args={'headers': {'User-Agent': "TEST"}})
        self.assertEqual("TEST", network.client.headers['User-Agent'])

    def test_custom_header_settings(self):
        custom_header, custom_value = 'x-limit', 'limit'
        network = Network(access_token="---", api_url="---", client_args={'headers': {custom_header: custom_value}})
        self.assertEqual(custom_value, network.client.headers[custom_header])

    def test_transparent_params_list(self):
        params, files = Network.transparent_params({'l': [1, 2, 3]})
        self.assertEqual({'l': '1,2,3'}, params)

    def test_transparent_params_string(self):
        params, files = Network.transparent_params({'s': 'test string'})
        self.assertEqual({'s': 'test string'}, params)

    def test_transparent_params_bool(self):
        params, files = Network.transparent_params({'b': True})
        self.assertEqual({'b': 'true'}, params)

    def test_transparent_params_int(self):
        params, files = Network.transparent_params({'i': 777})
        self.assertEqual({'i': 777}, params)

    def test_parse_quota_headers_without_header(self):
        network = Network(access_token="---", api_url="---")
        self.assertIsNone(network.parse_quota_headers({"quota": 'test_value'}))

    def test_parse_quota_headers_with_header(self):
        quota_header, quota_value = 'quota', 'value'
        network = Network(access_token="---", api_url="---", quota_headers=quota_header)
        quota = network.parse_quota_headers({quota_header: quota_value})
        self.assertEqual(quota, quota_value)

    def test_get_quota_headers_with_header(self):
        network = Network(access_token="---", api_url="---", quota_headers="quota")
        network.parse_quota_headers({"quota": 'test_value'})
        self.assertEqual("<< Information about quotas will be after any request to the API. >>", network.get_quota())

    def test_get_quota_without_header(self):
        network = Network(access_token="---", api_url="---")
        network.parse_quota_headers({"quota": 'test_value'})
        self.assertEqual("<< There is no information about quotas for the current network. >>", network.get_quota())




