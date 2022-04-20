import unittest

from social_apis.networks.linkedin import Linkedin
from config import ld_access_token


class TestLinkedin(unittest.TestCase):

    def setUp(self):
        self.api = Linkedin(access_token=ld_access_token)

    def testPlaces(self):
        places = self.api.regions(count=10)['elements']
        self.assertEqual(len(places), 10)
