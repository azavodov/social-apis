import unittest

from social_apis.exceptions.social_api_error import AuthError
from social_apis.networks.facebook import Facebook
from social_apis.networks.twitter import Twitter
from config import tw_app_key, tw_app_secret, tw_oauth_token_secret, tw_oauth_token, fb_access_token


class TestAuth(unittest.TestCase):

    def test_oauth_1(self):
        Twitter(app_key=tw_app_key, app_secret=tw_app_secret,
                oauth_token=tw_oauth_token, oauth_token_secret=tw_oauth_token_secret)

    def test_oauth_1_without_tokens(self):
        Twitter(app_key=tw_app_key, app_secret=tw_app_secret,)

    def test_oauth_2(self):
        Facebook(access_token=fb_access_token)

    def test_oauth_2_auto_correct_version(self):
        Facebook(access_token=fb_access_token, oauth_version=1)

    def test_exceptions_during_anonim_auth(self):
        self.assertRaises(AuthError, Twitter)

    def test_oauth_version_validating(self):
        self.assertRaises(AuthError, Twitter, oauth_version=3)

    def test_oauth_1_incorrect_arguments(self):
        self.assertRaises(AuthError, Twitter, app_key="----")

    def test_oauth_1_incorrect_secret(self):
        self.assertRaises(AuthError, Twitter, app_secret="----")

    def test_oauth_2_incorrect_arguments(self):
        self.assertRaises(AuthError, Twitter, app_key="----", app_oauth_version=2)

