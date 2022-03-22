from social_apis.networks.network import Network


class Vkontakte(Network):

    api_url = 'https://api.vk.com'
    api_version = '5.103'
    url = f"{api_url}/method"

    def __init__(self, **params):
        super(Vkontakte, self).__init__(self.api_url, **params)

    def search_users(self, **params):
        if 'v' not in params:
            params['v'] = self.api_version
        return self.get(f'{self.url}/users.search', params=params)
