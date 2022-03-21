from social_apis.networks.network import Network


class Twitter(Network):

    api_url = 'https://api.twitter.com'
    api_version = '1.1'
    url = f"{api_url}/{api_version}"

    def __init__(self, **params):
        super(Twitter, self).__init__(self.api_url, **params)

    def get_followers_ids(self, **params):
        return self.get(f'{self.url}/followers/ids.json', params=params)
