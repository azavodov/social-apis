from social_apis.networks.network import Network


class Twitter2(Network):

    api_url = 'https://api.twitter.com'
    api_version = '2'
    url = f"{api_url}/{api_version}"

    def __init__(self, **params):
        super(Twitter2, self).__init__(self.api_url, **params)

    def get_tweets(self, ids, **params):
        params.update({'ids': ','.join(ids)})
        return self.get(f'{self.url}/tweets?ids={ids}', params=params)
