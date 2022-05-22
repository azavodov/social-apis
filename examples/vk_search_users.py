from social_apis.exceptions.social_api_error import SocialAPIError
from social_apis.networks.vkontakte import Vkontakte

try:
    vk_api = Vkontakte(access_token="<<vk_access_token>>")
    users = vk_api.users_search(q="Иван Иванов", count=7)
except SocialAPIError as e:
    print(e)

