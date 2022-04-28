import unittest
from typing import Generator

from social_apis.exceptions.social_api_error import IteratorError
from social_apis.networks.facebook import Facebook
from social_apis.networks.vkontakte import Vkontakte
from config import vk_access_token, fb_access_token
from social_apis.utils.request_iterator import iterator


class TestCore(unittest.TestCase):

    def test_default_quota_header_definition(self):
        api = Facebook(access_token=fb_access_token)
        self.assertIsNotNone(api.quota_headers)

    def test_custom_quota_header_definition(self):
        custom_quota_header = "custom_quota_header"
        api = Vkontakte(access_token=vk_access_token, quota_headers=custom_quota_header)
        self.assertEqual(api.quota_headers, custom_quota_header)

    def test_iterator_returns_generator(self):
        def correct_function(): pass
        correct_function.iter_key = 'test'
        correct_function.iter_field = 'test'
        generator = iterator(correct_function)
        self.assertIsInstance(generator, Generator)

    def test_iterator_iter_key_required_property(self):
        def func_without_iter_key(): pass
        func_without_iter_key.iter_field = 'test'
        try:
            list(iterator(func_without_iter_key))
        except IteratorError:
            pass

    def test_iterator_iter_field_required_property(self):
        def func_without_iter_field(): pass
        func_without_iter_field.iter_key = 'test'
        try:
            list(iterator(func_without_iter_field))
        except IteratorError:
            pass

    def test_iterator_func_is_callable(self):
        try:
            list(iterator("string is not functions"))
        except TypeError:
            pass
