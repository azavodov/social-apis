import unittest

from social_apis.exceptions.social_api_error import ScopeError
from social_apis.networks.facebook import Facebook
from config import fb_access_token


class TestFacebook(unittest.TestCase):

    def setUp(self):
        self.post_id = "128562817166981_3136913512998548"
        self.album_id = "3094275057497415"
        self.group_id = "270834543757117"
        self.api = Facebook(access_token=fb_access_token)

    def test_quota_parsing(self):
        self.api.get_group(self.group_id)
        self.assertIsNotNone(self.api.get_quota())

    def test_get_group(self):
        group = self.api.get_group(self.group_id)
        self.assertEqual(group['id'], self.group_id)

    def test_get_group_albums(self):
        self.assertRaises(ScopeError, self.api.get_group_albums, self.group_id)

    def test_get_post(self):
        post = self.api.get_post(post_id=self.post_id)
        self.assertEqual(post['id'], self.post_id)

    def test_get_post_attachments(self):
        response = self.api.get_post_attachments(post_id=self.post_id)
        self.assertIn('data', response)

    def test_get_post_reactions(self):
        response = self.api.get_post_reactions(post_id=self.post_id)
        self.assertIn('data', response)

    def test_get_sharedposts(self):
        response = self.api.get_post_sharedposts(post_id=self.post_id)
        self.assertIn('data', response)

    def test_get_sponsor_tags(self):
        response = self.api.get_post_sponsor_tags(post_id=self.post_id)
        self.assertIn('data', response)

    def test_get_post_to(self):
        response = self.api.get_post_to(post_id=self.post_id)
        self.assertIn('data', response)

    def test_get_post_comments(self):
        self.assertRaises(ScopeError, self.api.get_post_comments, self.post_id)
