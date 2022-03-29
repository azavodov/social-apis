import os
import unittest

from social_apis.networks.vkontakte import Vkontakte


class TestVkontakte(unittest.TestCase):

    def setUp(self):
        access_token = os.environ.get("VKONTAKTE_ACCESS_TOKEN")
        self.api = Vkontakte(access_token=access_token)

    def testSearchUsers(self):
        users = self.api.search_users(q="Иван Иванов")['response']['items']
        self.assertGreater(len(users), 0)

