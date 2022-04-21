from social_apis.networks.network import Network


class Twitter2(Network):

    api_url = 'https://api.twitter.com'
    api_version = '2'
    url = f"{api_url}/{api_version}"
    quota_headers = ['x-rate-limit-reset', 'x-rate-limit-remaining', 'x-rate-limit-limit']

    def __init__(self, **params):
        super(Twitter2, self).__init__(self.api_url, self.quota_headers, **params)

    # Tweets
    def get_tweet(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id"""
        return self.get(f'{self.url}/tweets/{id}', params=params)

    def get_tweets(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets"""
        return self.get(f'{self.url}/tweets', params=params)

    def search_all_tweets(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all"""
        return self.get(f'{self.url}/tweets/search/all', params=params)

    def search_recent_tweets(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent"""
        return self.get(f'{self.url}/tweets/search/recent', params=params)

    def get_all_tweets_count(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-all"""
        return self.get(f'{self.url}/tweets/counts/all', params=params)

    def get_recent_tweets_count(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent"""
        return self.get(f'{self.url}/tweets/counts/recent', params=params)

    def post_tweet(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets"""
        return self.post(f'{self.url}/tweets', params=params)

    def delete_tweet(self, id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/delete-tweets-id"""
        return self.delete(f'{self.url}/tweets/{id}')

    # Timelines
    def get_user_mentions(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-mentions"""
        return self.get(f'{self.url}/users/{id}/mentions', params=params)

    def get_user_tweets(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets"""
        return self.get(f'{self.url}/users/{id}/tweets', params=params)

    # Streams
    def search_streams(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream"""
        return self.get(f'{self.url}/search/stream', params=params)

    def search_streams_rules(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules"""
        return self.get(f'{self.url}/search/stream/rules', params=params)

    def post_search_streams_rules(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules"""
        return self.post(f'{self.url}/search/stream/rules', params=params)

    def get_tweets_sample_streams(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/api-reference/get-tweets-sample-stream"""
        return self.get(f'{self.url}/tweets/sample/stream', params=params)

    # Retweets
    def get_retweeters(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweeted_by"""
        return self.get(f'{self.url}/tweets/{id}/retweeted_by', params=params)

    def post_user_retweet(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/post-users-id-retweets"""
        return self.post(f'{self.url}users/{id}/retweets/', params=params)

    def delete_user_retweet(self, id, source_tweet_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/api-reference/get-tweets-sample-stream"""
        return self.delete(f'{self.url}users/{id}/retweets/{source_tweet_id}')

    # Quote Tweets
    def get_quoted_tweets(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/quote-tweets/api-reference/get-tweets-id-quote_tweets"""
        return self.get(f'{self.url}/tweets/{id}/quote_tweets', params=params)

    # Likes
    def get_tweet_liking_users(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-tweets-id-liking_users"""
        return self.get(f'{self.url}/tweets/{id}/liking_users', params=params)

    def get_user_liked_tweets(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-users-id-liked_tweets"""
        return self.get(f'{self.url}/users/{id}/liked_tweets', params=params)

    def like_tweet(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/post-users-id-likes"""
        return self.post(f'{self.url}/users/{id}/likes', params=params)

    def delete_like(self, id, tweet_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/quote-tweets/api-reference/get-tweets-id-quote_tweets"""
        return self.delete(f'{self.url}/users/{id}/likes/{tweet_id}')

    # Bookmarks
    def get_user_bookmarks(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/get-users-id-bookmarks"""
        return self.get(f'{self.url}/users/{id}/bookmarks', params=params)

    def post_user_bookmark(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/delete-users-id-bookmarks-tweet_id"""
        return self.post(f'{self.url}/users/{id}/bookmarks', params=params)

    def delete_user_bookmark(self, id, tweet_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/post-users-id-bookmarks"""
        return self.delete(f'{self.url}/users/{id}/bookmarks/{tweet_id}')

    # Users lookup
    def get_user(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id"""
        return self.get(f'{self.url}/users/{id}', params=params)

    def get_users(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users"""
        return self.get(f'{self.url}/users', params=params)

    def get_users_by_username(self, username, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username"""
        return self.get(f'{self.url}/users/by/username/{username}', params=params)

    def get_users_by(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by"""
        return self.get(f'{self.url}/users/by', params=params)

    def get_users_me(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-me"""
        return self.get(f'{self.url}/users/me', params=params)

    # Follows
    def get_user_following(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-following"""
        return self.get(f'{self.url}/users/{id}/following', params=params)

    def get_user_followers(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers"""
        return self.get(f'{self.url}users/{id}/followers', params=params)

    def post_following(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following"""
        return self.post(f'{self.url}/users/{id}/following', params=params)

    def delete_following(self, source_user_id, target_user_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following"""
        return self.delete(f'{self.url}/users/{source_user_id}/following/{target_user_id}')

    # Blocks
    def get_user_blocks(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/get-users-blocking"""
        return self.get(f'{self.url}/users/{id}/blocking', params=params)

    def add_user_block(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/post-users-user_id-blocking"""
        return self.post(f'{self.url}/users/{id}/blocking', params=params)

    def delete_user_block(self, source_user_id, target_user_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/delete-users-user_id-blocking"""
        return self.delete(f'{self.url}/users/{source_user_id}/blocking/{target_user_id}')

    # Mutes
    def get_user_mutes(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/get-users-muting"""
        return self.get(f'{self.url}/users/{id}/muting', params=params)

    def add_user_mute(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/post-users-user_id-muting"""
        return self.post(f'{self.url}/users/{id}/muting', params=params)

    def delete_user_mute(self, source_user_id, target_user_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting"""
        return self.delete(f'{self.url}/users/{source_user_id}/muting/{target_user_id}')

    # Spaces
    def get_space(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id"""
        return self.get(f'{self.url}/spaces/{id}', params=params)

    def get_spaces(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces"""
        return self.get(f'{self.url}/spaces', params=params)

    def get_users_by_creator_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-by-creator-ids"""
        return self.get(f'{self.url}/spaces/by/creator_ids', params=params)

    def get_space_buyers(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-buyers"""
        return self.get(f'{self.url}/spaces/{id}/buyers', params=params)

    def get_space_tweets(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-tweets"""
        return self.get(f'{self.url}/spaces/{id}/tweets', params=params)

    def search_spaces(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/spaces/search/api-reference/get-spaces-search"""
        return self.get(f'{self.url}/spaces/search', params=params)

    # List lookup
    def get_lists(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists"""
        return self.get(f'{self.url}/lists/{id}', params=params)

    def get_lists_by_owner(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists"""
        return self.get(f'{self.url}/users/{id}/owned_lists', params=params)

    # Manage lists
    def add_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/post-lists"""
        return self.post(f'{self.url}/lists', params=params)

    def delete_list(self, id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/delete-lists-id"""
        return self.delete(f'{self.url}/lists/{id}')

    def edit_list(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/put-lists-id"""
        return self.put(f'{self.url}/lists/{id}', params=params)

    # List Tweets lookup
    def get_list_tweets(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference/get-lists-id-tweets"""
        return self.get(f'{self.url}/lists/{id}/tweets', params=params)

    # List members
    def get_list_of_members(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-lists-id-members"""
        return self.get(f'{self.url}/lists/{id}/members', params=params)

    def get_user_lists_memberships(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships"""
        return self.get(f'{self.url}/users/{id}/list_memberships', params=params)

    def add_user_to_list(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/post-lists-id-members"""
        return self.post(f'{self.url}/lists/{id}/members', params=params)

    def delete_user_from_list(self, id, user_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/delete-lists-id-members-user_id"""
        return self.delete(f'{self.url}/lists/{id}/members/{user_id}')

    # List follows
    def get_list_of_follows(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/get-lists-id-followers"""
        return self.get(f'{self.url}/lists/{id}/followers', params=params)

    def get_user_follows_lists(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/get-users-id-followed_lists"""
        return self.get(f'{self.url}/users/{id}/followed_list', params=params)

    def post_user_followed_list(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/post-users-id-followed-lists"""
        return self.post(f'{self.url}/users/{id}/followed_list', params=params)

    def delete_user_followed_list(self, id, list_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/delete-users-id-followed-lists-list_id"""
        return self.delete(f'{self.url}/users/{id}/followed_list/{list_id}')

    # Pinned Lists
    def get_user_pinned_lists(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/get-users-id-pinned_lists"""
        return self.get(f'{self.url}/users/{id}/pinned_lists', params=params)

    def post_user_pinned_lists(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/post-users-id-pinned-lists"""
        return self.post(f'{self.url}/lists/{id}/pinned_lists', params=params)

    def delete_user_pinned_list(self, id, list_id):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/delete-users-id-pinned-lists-list_id"""
        return self.delete(f'{self.url}/lists/{id}/pinned_lists/{list_id}')

    # Batch compliance
    def get_compliance_job(self, id, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id"""
        return self.get(f'{self.url}/compliance/jobs/{id}', params=params)

    def get_compliance_jobs(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs"""
        return self.get(f'{self.url}/compliance/jobs', params=params)

    def post_compliance_job(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/post-compliance-jobs"""
        return self.post(f'{self.url}/compliance/jobs', params=params)
