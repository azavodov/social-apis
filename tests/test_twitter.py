import unittest

from social_apis.networks.twitter import Twitter
from config import tw_app_key, tw_app_secret, tw_oauth_token_secret, tw_oauth_token


class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.api = Twitter(app_key=tw_app_key, app_secret=tw_app_secret,
                           oauth_token=tw_oauth_token, oauth_token_secret=tw_oauth_token_secret)

    def test_get_mentions_timeline(self):
        self.api.get_mentions_timeline()

    def test_get_user_timeline(self):
        self.api.get_user_timeline()
        self.api.get_user_timeline(screen_name='twitter')

    def test_retweeted_of_me(self):
        self.api.retweeted_of_me()

    def test_get_retweets(self):
        self.api.get_retweets(id="99530515043983360")

    def test_search(self):
        self.api.search(q='twitter')

    def test_get_followers_ids(self):
        self.api.get_followers_ids(screen_name="github")

    def test_get_privacy_policy(self):
        self.api.retweeted_of_me()

    def test_get_application_rate_limit_status(self):
        self.api.get_application_rate_limit_status()

    def test_quota_parsing(self):
        self.api.retweeted_of_me()
        self.assertIsNotNone(self.api.get_quota())

