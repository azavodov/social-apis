
class SocialAPIError(Exception):

    msg = "An error occurred during the request"

    def __init__(self, msg=None, error_code=None, retry_after=None):
        self.error_code = error_code
        self.retry_after = retry_after
        if msg is not None:
            self.msg = msg
        super(SocialAPIError, self).__init__(self.msg)

    @property
    def message(self):
        return self.msg


class MethodError(SocialAPIError):
    msg = "An error occurred while calling the method. " \
          "Method does not exist, or arguments are passed incorrectly"


class IterationError(SocialAPIError):
    msg = "An error occurred during the iteration by response"


class RateLimitError(SocialAPIError):
    msg = "Rate Limit Error occurred during the request. " \
          "Looks like you've exceeded your requests limit."

    def __init__(self, msg, error_code, retry_after=None):
        if isinstance(retry_after, int):
            msg = f'{msg} (Retry after {retry_after} seconds)'
        SocialAPIError.__init__(self, msg, error_code=error_code)


class AuthError(SocialAPIError):
    msg = "Authentication error occurred during request"


class TokenError(AuthError):
    msg = "Authentication Token error occurred during request"


class ScopeError(AuthError):
    msg = "Rate limit error occurred during request"
