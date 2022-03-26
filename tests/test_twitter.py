import os
import unittest

from social_apis.networks.twitter import Twitter


class TestTwitter(unittest.TestCase):

    def setUp(self):
        app_key = os.environ.get("TWITTER_APP_KEY")
        app_secret = os.environ.get("TWITTER_APP_SECRET")
        oauth_token = os.environ.get("TWITTER_TOKEN")
        oauth_token_secret = os.environ.get("TWITTER_TOKEN_SECRET")
        self.api = Twitter(app_key=app_key, app_secret=app_secret,
                           oauth_token=oauth_token, oauth_token_secret=oauth_token_secret)

    def test_get_followers_ids(self):
        ids = self.api.get_followers_ids(screen_name="github")
        self.assertGreater(len(ids), 0)
