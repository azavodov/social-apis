import os
import unittest

from social_apis.networks.facebook import Facebook


class TestFacebook(unittest.TestCase):

    def setUp(self):
        access_token = os.environ.get("FACEBOOK_ACCESS_TOKEN")
        self.api = Facebook(access_token=access_token)

    def testGetPost(self):
        post_id = "128562817166981_3136913512998548"
        post = self.api.get_post(post_id=post_id)
        self.assertEqual(post['id'], post_id)
