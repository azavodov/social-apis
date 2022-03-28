import os
import unittest

from social_apis.networks.linkedin import Linkedin


class TestLinkedin(unittest.TestCase):

    def setUp(self):
        access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
        self.api = Linkedin(access_token=access_token)

    def testPlaces(self):
        places = self.api.regions(count=10)['elements']
        self.assertEqual(len(places), 10)
