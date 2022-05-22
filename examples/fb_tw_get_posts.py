from social_apis.exceptions.social_api_error import SocialAPIError
from social_apis.networks.facebook import Facebook
from social_apis.networks.twitter_v2 import Twitter2

try:

    post = Facebook(access_token="<<fb_token>>").get_post(post_id="<<post_id>>")
    tweets = Twitter2(access_token="<<tw_token>>").get_tweets(user_id="<<user_id>>")

except SocialAPIError as e:
    print(e)
