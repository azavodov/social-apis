import json

from social_apis.networks.network import Network


class Twitter(Network):

    api_url = 'https://api.twitter.com'
    api_version = '1.1'
    url = f"{api_url}/{api_version}"
    quota_headers = ['x-rate-limit-reset', 'x-rate-limit-remaining', 'x-rate-limit-limit']

    def __init__(self, **params):
        super(Twitter, self).__init__(self.api_url, self.quota_headers, **params)

    def request(self, endpoint, method='GET', params=None, json_encoded=False):
        url = endpoint if endpoint.startswith('https://') else f'{self.url}/{endpoint}.json'
        return self._request(url, method=method, params=params, api_call=url, json_encoded=json_encoded)

    # Timelines
    def get_mentions_timeline(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline"""
        return self.get('statuses/mentions_timeline', params=params)

    def get_user_timeline(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline"""
        return self.get('statuses/user_timeline', params=params)

    def get_home_timeline(self, **params):
        """Docs: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-home_timeline"""
        return self.get('statuses/home_timeline', params=params)

    def retweeted_of_me(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweets_of_me"""
        return self.get('statuses/retweets_of_me', params=params)

    # Tweets
    def get_retweets(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-retweet-id """
        return self.get(f'statuses/retweets/{params.get("id")}', params=params)

    def show_status(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id"""
        return self.get(f'statuses/show/{params.get("id")}', params=params)

    def lookup_status(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-lookup"""
        return self.post('statuses/lookup', params=params)

    def destroy_status(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-destroy-id"""
        return self.post(f'statuses/destroy/{params.get("id")}')

    def update_status(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update"""
        return self.post('statuses/update', params=params)

    def retweet(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-retweet-id"""
        return self.post(f'statuses/retweet/{params.get("id")}')

    def upload_media(self, **params):
        """Docs: https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload"""
        if params and params.get('command', '') == 'STATUS':
            return self.get('https://upload.twitter.com/1.1/media/upload.json', params=params)
        return self.post('https://upload.twitter.com/1.1/media/upload.json', params=params)

    def create_metadata(self, **params):
        """Docs: https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-metadata-create"""
        params = json.dumps(params)
        return self.post("https://upload.twitter.com/1.1/media/metadata/create.json", params=params)

    def get_oembed_tweet(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed"""
        return self.get('oembed', params=params)

    def get_retweeters_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids"""
        return self.get('statuses/retweeters/ids', params=params)
    get_retweeters_ids.iter_key = 'ids'
    get_retweeters_ids.iter_field = 'cursor'
    get_retweeters_ids.iter_next = 'next_cursor_str'

    # Search
    def search(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets"""
        return self.get('search/tweets', params=params)

    # Direct Messages
    def get_direct_messages(self, **params):
        """Docs: https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events"""
        return self.get('direct_messages/events/list', params=params)

    def get_direct_message(self, **params):
        """Docs: https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/get-event"""
        return self.get('direct_messages/events/show', params=params)

    def destroy_direct_message(self, **params):
        """Docs: https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message-event"""
        return self.delete('direct_messages/events/destroy', params=params)

    def send_direct_message(self, **params):
        """Docs: https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event"""
        return self.post('direct_messages/events/new', params=params, json_encoded=True)

    # Friends & Followers
    def get_user_ids_of_blocked_retweets(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-no_retweets-ids"""
        return self.get('friendships/no_retweets/ids', params=params)

    def get_friends_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids"""
        return self.get('friends/ids', params=params)
    get_friends_ids.iter_key = 'ids'
    get_friends_ids.iter_field = 'cursor'
    get_friends_ids.iter_next = 'next_cursor_str'

    def get_followers_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids"""
        return self.get('followers/ids', params=params)
    get_followers_ids.iter_key = 'ids'
    get_followers_ids.iter_field = 'cursor'
    get_followers_ids.iter_next = 'next_cursor_str'

    def lookup_friendships(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup"""
        return self.get('friendships/lookup', params=params)

    def get_incoming_friendship_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-incoming"""
        return self.get('friendships/incoming', params=params)
    get_incoming_friendship_ids.iter_key = 'ids'
    get_incoming_friendship_ids.iter_field = 'cursor'
    get_incoming_friendship_ids.iter_next = 'next_cursor_str'

    def get_outgoing_friendship_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-outgoing"""
        return self.get('friendships/outgoing', params=params)
    get_outgoing_friendship_ids.iter_key = 'ids'
    get_outgoing_friendship_ids.iter_field = 'cursor'
    get_outgoing_friendship_ids.iter_next = 'next_cursor_str'

    def create_friendship(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create"""
        return self.post('friendships/create', params=params)

    def destroy_friendship(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy"""
        return self.post('friendships/destroy', params=params)

    def update_friendship(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/post-friendships-update"""
        return self.post('friendships/update', params=params)

    def show_friendship(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show"""
        return self.get('friendships/show', params=params)

    def get_friends_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-list"""
        return self.get('friends/list', params=params)
    get_friends_list.iter_key = 'users'
    get_friends_list.iter_field = 'cursor'
    get_friends_list.iter_next = 'next_cursor_str'

    def get_followers_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-followers-list"""
        return self.get('followers/list', params=params)
    get_followers_list.iter_key = 'users'
    get_followers_list.iter_field = 'cursor'
    get_followers_list.iter_next = 'next_cursor_str'

    # Users
    def get_account_settings(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-settings"""
        return self.get('account/settings', params=params)

    def verify_credentials(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-verify_credentials"""
        return self.get('account/verify_credentials', params=params)

    def update_account_settings(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-settings"""
        return self.post('account/settings', params=params)

    def update_delivery_service(self, **params):
        """Docs: https://dev.twitter.com/docs/api/1.1/post/account/update_delivery_device"""
        return self.post('account/update_delivery_device', params=params)

    def update_profile(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile"""
        return self.post('account/update_profile', params=params)

    def update_profile_banner_image(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_background_image"""
        return self.post('account/update_profile_banner', params=params)

    def update_profile_image(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image"""
        return self.post('account/update_profile_image', params=params)

    def list_blocks(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-blocks-list"""
        return self.get('blocks/list', params=params)
    list_blocks.iter_key = 'users'
    list_blocks.iter_field = 'cursor'
    list_blocks.iter_next = 'next_cursor_str'

    def list_block_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-blocks-ids"""
        return self.get('blocks/ids', params=params)
    list_block_ids.iter_key = 'ids'
    list_block_ids.iter_field = 'cursor'
    list_block_ids.iter_next = 'next_cursor_str'

    def create_block(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-blocks-create"""
        return self.post('blocks/create', params=params)

    def destroy_block(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-blocks-destroy"""
        return self.post('blocks/destroy', params=params)

    def lookup_user(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup"""
        return self.get('users/lookup', params=params)

    def show_user(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show"""
        return self.get('users/show', params=params)

    def search_users(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-search"""
        return self.get('users/search', params=params)

    def get_contributees(self, **params):
        """Docs: https://dev.twitter.com/docs/api/1.1/get/users/contributees"""
        return self.get('users/contributees', params=params)

    def get_contributors(self, **params):
        """Docs: https://dev.twitter.com/docs/api/1.1/get/users/contributors"""
        return self.get('users/contributors', params=params)

    def remove_profile_banner(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-remove_profile_banner"""
        return self.post('account/remove_profile_banner', params=params)

    def update_profile_background_image(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner"""
        return self.post('account/update_profile_background_image', params=params)

    def get_profile_banner_sizes(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner"""
        return self.get('users/profile_banner', params=params)

    def list_mutes(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-list"""
        return self.get('mutes/users/list', params=params)
    list_mutes.iter_key = 'users'
    list_mutes.iter_field = 'cursor'
    list_mutes.iter_next = 'next_cursor_str'

    def list_mute_ids(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/get-mutes-users-ids"""
        return self.get('mutes/users/ids', params=params)
    list_mute_ids.iter_key = 'ids'
    list_mute_ids.iter_field = 'cursor'
    list_mute_ids.iter_next = 'next_cursor_str'

    def create_mute(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create"""
        return self.post('mutes/users/create', params=params)

    def destroy_mute(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-destroy"""
        return self.post('mutes/users/destroy', params=params)

    # Suggested Users
    def get_user_suggestions_by_slug(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-suggestions-slug"""
        return self.get(f'users/suggestions/params.get("slug")', params=params)

    def get_user_suggestions(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-suggestions"""
        return self.get('users/suggestions', params=params)

    def get_user_suggestions_statuses_by_slug(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-suggestions-slug-members"""
        return self.get(f'users/suggestions/{params.get("slug")}/members', params=params)

    # Favorites
    def get_favorites(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-favorites-list"""
        return self.get('favorites/list', params=params)

    def destroy_favorite(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-favorites-destroy"""
        return self.post('favorites/destroy', params=params)

    def create_favorite(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-favorites-create"""
        return self.post('favorites/create', params=params)

    # Lists
    def show_lists(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-list"""
        return self.get('lists/list', params=params)

    def get_list_statuses(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses"""
        return self.get('lists/statuses', params=params)

    def delete_list_member(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy"""
        return self.post('lists/members/destroy', params=params)

    def get_list_memberships(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships"""
        return self.get('lists/memberships', params=params)
    get_list_memberships.iter_key = 'lists'
    get_list_memberships.iter_field = 'cursor'
    get_list_memberships.iter_next = 'next_cursor_str'

    def get_list_subscribers(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers"""
        return self.get('lists/subscribers', params=params)
    get_list_subscribers.iter_key = 'users'
    get_list_subscribers.iter_field = 'cursor'
    get_list_subscribers.iter_next = 'next_cursor_str'

    def subscribe_to_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-subscribers-create"""
        return self.post('lists/subscribers/create', params=params)

    def is_list_subscriber(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-subscribers-show"""
        return self.get('lists/subscribers/show', params=params)

    def unsubscribe_from_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-subscribers-destroy"""
        return self.post('lists/subscribers/destroy', params=params)

    def create_list_members(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create_all"""
        return self.post('lists/members/create_all', params=params)

    def is_list_member(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-members-show"""
        return self.get('lists/members/show', params=params)

    def get_list_members(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-members"""
        return self.get('lists/members', params=params)
    get_list_members.iter_key = 'users'
    get_list_members.iter_field = 'cursor'
    get_list_members.iter_next = 'next_cursor_str'

    def add_list_member(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create"""
        return self.post('lists/members/create', params=params)

    def delete_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy"""
        return self.post('lists/destroy', params=params)

    def update_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-update"""
        return self.post('lists/update', params=params)

    def create_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-create"""
        return self.post('lists/create', params=params)

    def get_specific_list(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-show"""
        return self.get('lists/show', params=params)

    def get_list_subscriptions(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-subscriptions"""
        return self.get('lists/subscriptions', params=params)
    get_list_subscriptions.iter_key = 'lists'
    get_list_subscriptions.iter_field = 'cursor'
    get_list_subscriptions.iter_next = 'next_cursor_str'

    def delete_list_members(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy_all"""
        return self.post('lists/members/destroy_all', params=params)

    def show_owned_lists(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/create-manage-lists/api-reference/get-lists-ownerships"""
        return self.get('lists/ownerships', params=params)
    show_owned_lists.iter_key = 'lists'
    show_owned_lists.iter_field = 'cursor'
    show_owned_lists.iter_next = 'next_cursor_str'

    # Saved Searches
    def get_saved_searches(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-saved_searches-list"""
        return self.get('saved_searches/list', params=params)

    def show_saved_search(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-saved_searches-show-id"""
        return self.get(f'saved_searches/show/{params.get("id")}', params=params)

    def create_saved_search(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-mutes-users-create"""
        return self.post('saved_searches/create', params=params)

    def destroy_saved_search(self, **params):
        """Docs: https://developer.twitter.com/en/docs/tweets/search/api-reference/post-saved_searches-destroy-id"""
        return self.post(f'saved_searches/destroy/{params.get("id")}', params=params)

    # Places & Geo
    def get_geo_info(self, **params):
        """Docs: https://developer.twitter.com/en/docs/geo/place-information/api-reference/get-geo-id-place_id"""
        return self.get(f'geo/id/{params.get("place_id")}', params=params)

    def reverse_geocode(self, **params):
        """Docs: https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-reverse_geocode"""
        return self.get('geo/reverse_geocode', params=params)

    def search_geo(self, **params):
        """Docs: https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search"""
        return self.get('geo/search', params=params)

    def get_similar_places(self, **params):
        """Docs: https://dev.twitter.com/docs/api/1.1/get/geo/similar_places"""
        return self.get('geo/similar_places', params=params)

    def create_place(self, **params):
        """Docs: https://dev.twitter.com/docs/api/1.1/post/geo/place"""
        return self.post('geo/place', params=params)

    # Trends
    def get_place_trends(self, **params):
        """Docs: https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place"""
        return self.get('trends/place', params=params)

    def get_available_trends(self, **params):
        """Docs: https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available"""
        return self.get('trends/available', params=params)

    def get_closest_trends(self, **params):
        """Docs: https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-closest"""
        return self.get('trends/closest', params=params)

    # Spam Reporting
    def report_spam(self, **params):
        """Docs: https://developer.twitter.com/en/docs/accounts-and-users/mute-block-report-users/api-reference/post-users-report_spam"""
        return self.post('users/report_spam', params=params)

    # Help
    def get_twitter_configuration(self, **params):
        """Docs: https://developer.twitter.com/en/docs/developer-utilities/configuration/api-reference/get-help-configuration"""
        return self.get('help/configuration', params=params)

    def get_supported_languages(self, **params):
        """Docs:https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages"""
        return self.get('help/languages', params=params)

    def get_privacy_policy(self, **params):
        """Docs: https://developer.twitter.com/en/docs/developer-utilities/privacy-policy/api-reference/get-help-privacy"""
        return self.get('help/privacy', params=params)

    def get_tos(self, **params):
        """Docs: https://developer.twitter.com/en/docs/developer-utilities/terms-of-service/api-reference/get-help-tos"""
        return self.get('help/tos', params=params)

    def get_application_rate_limit_status(self, **params):
        """Docs: https://developer.twitter.com/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status"""
        return self.get('application/rate_limit_status', params=params)
