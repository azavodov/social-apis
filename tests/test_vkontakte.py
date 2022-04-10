import os
import unittest

from social_apis.networks.vkontakte import Vkontakte


class TestVkontakte(unittest.TestCase):

    def setUp(self):
        access_token = os.environ.get("VKONTAKTE_ACCESS_TOKEN")
        self.api = Vkontakte(access_token=access_token)

    def test_get_account_counters(self):
        self.api.account_get_counters(filter="friends_recommendations")
        self.api.account_get_push_settings()

    def test_search_users(self):
        self.api.users_search(q="Иван Иванов", count=7)




