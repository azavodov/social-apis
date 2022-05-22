from social_apis.networks.twitter import Twitter
from social_apis.utils.request_iterator import iterator

twitter = Twitter(access_token="tw_access_token")
results = iterator(twitter.get_followers_ids, screen_name='github')
for result in results:
    print(result)

