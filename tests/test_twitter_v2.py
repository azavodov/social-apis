import os
import unittest

from social_apis.networks.twitter_v2 import Twitter2


class TestTwitter2(unittest.TestCase):

    def setUp(self):
        access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
        self.api = Twitter2(access_token=access_token)

    def test_get_tweet(self):
        self.api.get_tweet(id='1261326399320715264')

    def test_get_tweets(self):
        self.api.get_tweets(ids=['1261326399320715264', '1278347468690915330'])

    def test_get_compliance_jobs(self):
        self.api.get_compliance_jobs(type='tweets')

