
class SocialAPIError(Exception):

    msg = "An error occurred during the request"

    def __init__(self, msg=None, error_code=None):
        self.error_code = error_code
        if msg is not None:
            self.msg = msg
        super(SocialAPIError, self).__init__(self.msg)

    @property
    def message(self):
        return self.msg


class MethodError(SocialAPIError):
    msg = "An error occurred while calling the method. " \
          "Method does not exist, or arguments are passed incorrectly"


class IteratorError(SocialAPIError):
    msg = "An error occurred during the iteration by response"


class RateLimitError(SocialAPIError):
    msg = "Rate Limit Error occurred during the request. " \
          "Looks like you've exceeded your requests limit."

    def __init__(self, msg, error_code, quota=None):
        if quota is not None:
            msg = f'{msg} (API quota information – {quota})'
        SocialAPIError.__init__(self, msg, error_code=error_code)


class AuthError(SocialAPIError):
    msg = "Authentication error occurred during request"


class TokenError(AuthError):
    msg = "Authentication Token error occurred during request"


class ScopeError(AuthError):
    msg = "Rate limit error occurred during request"
