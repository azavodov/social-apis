from social_apis.exceptions.social_api_error import SocialAPIError

TWITTER_HTTP_STATUS_CODE = {
    200: ('OK', 'Success!'),
    304: ('Not Modified', 'There was no new data to return.'),
    400: ('Bad Request', 'The request was invalid. An accompanying \
          error message will explain why. This is the status code \
          will be returned during rate limiting.'),
    401: ('Unauthorized', 'Authentication credentials were missing \
          or incorrect.'),
    403: ('Forbidden', 'The request is understood, but it has been \
          refused. An accompanying error message will explain why. \
          This code is used when requests are being denied due to \
          update limits.'),
    404: ('Not Found', 'The URI requested is invalid or the resource \
          requested, such as a user, does not exists.'),
    406: ('Not Acceptable', 'Returned by the Search API when an \
          invalid format is specified in the request.'),
    410: ('Gone', 'This resource is gone. Used to indicate that an \
          API endpoint has been turned off.'),
    422: ('Unprocessable Entity', 'Returned when an image uploaded to \
          POST account/update_profile_banner is unable to be processed.'),
    429: ('Too Many Requests', 'Returned in API v1.1 when a request cannot \
          be served due to the application\'s rate limit having been \
          exhausted for the resource.'),
    500: ('Internal Server Error', 'Something is broken. Please post to the \
          group so the Twitter team can investigate.'),
    502: ('Bad Gateway', 'Twitter is down or being upgraded.'),
    503: ('Service Unavailable', 'The Twitter servers are up, but overloaded \
          with requests. Try again later.'),
    504: ('Gateway Timeout', 'The Twitter servers are up, but the request \
          couldn\'t be serviced due to some failure within our stack. Try \
          again later.'),
}


class TwitterError(SocialAPIError):

    msg = "Error occurred during Twitter API call."

    def __init__(self, msg, error_code=None):
        self.error_code = error_code

        if error_code is not None and error_code in TWITTER_HTTP_STATUS_CODE:
            msg = f'Twitter API returned a {error_code} ({TWITTER_HTTP_STATUS_CODE[error_code][0]}), {msg}'

        super(TwitterError, self).__init__(msg)
