from requests_oauthlib import OAuth1, OAuth2


class Auth:

    def __init__(self, api_url, app_key=None, app_secret=None,
                 oauth_token=None, oauth_token_secret=None, access_token=None,
                 token_type='bearer', auth_endpoint='authenticate', oauth_version=1):

        self.api_url = api_url
        self.app_key = app_key
        self.app_secret = app_secret
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.access_token = access_token

        self.request_token_url = f"{self.api_url}/oauth/request_token"
        self.access_token_url = f"{self.api_url}/oauth/access_token"
        self.authenticate_url = f"{self.api_url}/oauth/{auth_endpoint}"

        if self.access_token:
            oauth_version = 2

        self.oauth_version = oauth_version

        if oauth_version == 2:
            self.request_token_url = f"{self.api_url}/oauth2/token"

        auth = None
        if oauth_version == 1:
            if self.app_key is not None and self.app_secret is not None:
                auth = OAuth1(self.app_key, self.app_secret, self.oauth_token, self.oauth_token_secret)

        elif oauth_version == 2 and self.access_token:
            token = {
                'token_type': token_type,
                'access_token': self.access_token
            }
            auth = OAuth2(self.app_key, token=token)

        self.auth = auth
