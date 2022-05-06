import unittest

from social_apis.networks.vkontakte import Vkontakte
from config import vk_access_token


class TestVkontakte(unittest.TestCase):

    def setUp(self):
        self.api = Vkontakte(access_token=vk_access_token)

    def test_get_account_counters(self):
        self.api.account_get_counters(filter="friends_recommendations")

    def test_account_get_push_settings(self):
        self.api.account_get_push_settings()

    def test_users_search(self):
        self.api.users_search(q="Иван Иванов", count=7)

    def test_database_get_countries(self):
        self.api.database_get_countries(count=7)

    def test_database_get_regions(self):
        self.api.database_get_regions(country_id='1', count=5)

    def test_database_get_cities(self):
        self.api.database_get_cities(country_id='1')

    def test_database_get_universities(self):
        self.api.database_get_universities(city_id='1', count=7)

    def test_database_get_faculties(self):
        self.api.database_get_faculties(university_id='1', count=3)

    def test_database_get_chairs(self):
        self.api.database_get_chairs(faculty_id='1', count=5)

    def test_database_get_sc(self):
        self.api.database_get_schools(city_id='1', count=5)

    def test_database_get_school_classes(self):
        self.api.database_get_school_classes(school_id='1', count=1)
