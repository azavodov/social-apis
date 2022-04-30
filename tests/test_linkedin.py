import unittest

from social_apis.networks.linkedin import Linkedin
from config import ld_access_token


class TestLinkedin(unittest.TestCase):

    def setUp(self):
        self.api = Linkedin(access_token=ld_access_token,
                            client_args={'headers': {'X-RestLi-Protocol-Version': '2.0.0'}})

    def test_me_endpoint(self):
        self.assertIn('id', self.api.me())

    def test_regions(self):
        places = self.api.regions(count=10)['elements']
        self.assertEqual(len(places), 10)
