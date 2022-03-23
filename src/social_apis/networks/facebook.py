from social_apis.networks.network import Network


class Facebook(Network):

    api_url = 'https://graph.facebook.com'
    api_version = 'v13.0'
    url = f"{api_url}/{api_version}"

    def __init__(self, **params):
        super(Facebook, self).__init__(self.api_url, **params)

    def search_pages(self, **params):
        return self.get(f"{self.api_url}/posts/search", params=params)

    def get_post(self, post_id, **params):
        return self.get(f"{self.url}/{post_id}", params)

    def get_post_comments(self, post_id, **params):
        return self.get(f"{self.url}/{post_id}/comments", params)
