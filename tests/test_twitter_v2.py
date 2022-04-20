import unittest

from social_apis.networks.twitter_v2 import Twitter2
from config import tw_access_token


class TestTwitter2(unittest.TestCase):

    def setUp(self):
        self.api = Twitter2(access_token=tw_access_token)

    def test_get_tweet(self):
        self.api.get_tweet(id='1261326399320715264')

    def test_get_tweets(self):
        self.api.get_tweets(ids=['1261326399320715264', '1278347468690915330'])

    def test_get_compliance_jobs(self):
        self.api.get_compliance_jobs(type='tweets')

