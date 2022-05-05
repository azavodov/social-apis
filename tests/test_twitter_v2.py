import unittest

from social_apis.networks.twitter_v2 import Twitter2
from config import tw_access_token


class TestTwitter2(unittest.TestCase):

    def setUp(self):
        self.tweet_ids = ['1261326399320715264', '1278347468690915330']
        self.api = Twitter2(access_token=tw_access_token)

    def test_get_tweet(self):
        self.api.get_tweet(id=self.tweet_ids[0])

    def test_get_tweets(self):
        self.api.get_tweets(ids=self.tweet_ids)

    def test_get_compliance_jobs(self):
        self.api.get_compliance_jobs(type='tweets')

    def test_quota_parsing(self):
        self.api.get_compliance_jobs(type='tweets')
        self.assertIsNotNone(self.api.get_quota())

