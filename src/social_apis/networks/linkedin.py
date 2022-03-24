from social_apis.networks.network import Network


class Linkedin(Network):

    api_url = 'https://api.linkedin.com'
    api_version = 'v2'
    url = f"{api_url}/{api_version}"

    def __init__(self, **params):
        super(Linkedin, self).__init__(self.api_url, **params)

    def me(self, **params):
        return self.get(f'{self.url}/me', params=params)

    def places(self, **params):
        return self.get(f'{self.url}/places', params=params)

    def regions(self, **params):
        return self.get(f'{self.url}/regions', params=params)

    def people_by_id(self, id, **params):
        return self.get(f'{self.url}/people/{id}', params=params)

    def people_by_ids(self, ids: list, **params):
        return self.get(f'{self.url}/people?ids={",".join(ids)}', params=params)
