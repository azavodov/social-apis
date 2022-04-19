from social_apis.networks.network import Network


class Vkontakte(Network):

    api_url = 'https://api.vk.com'
    api_version = '5.103'
    url = f"{api_url}/method"

    def __init__(self, **params):
        super(Vkontakte, self).__init__(self.api_url, **params)

    def request(self, endpoint, method='GET', params=None, json_encoded=False):
        if 'v' not in params:
            params['v'] = self.api_version
        url = endpoint if endpoint.startswith('https://') else f'{self.url}/{endpoint}'
        return self._request(url, method=method, params=params, api_call=url, json_encoded=json_encoded)

    # Account
    def account_ban(self, **params):
        """Docs: https://dev.vk.com/method/account.ban"""
        return self.post(f'account.ban', params=params)

    def account_change_password(self, **params):
        """Docs: https://dev.vk.com/method/account.changePassword"""
        return self.post(f'account.changePassword', params=params)

    def account_get_active_offers(self, **params):
        """Docs: https://dev.vk.com/method/account.getActiveOffers"""
        return self.post(f'account.getActiveOffers', params=params)

    def account_get_app_permissions(self, **params):
        """Docs: https://dev.vk.com/method/account.getAppPermissions"""
        return self.post(f'account.getAppPermissions', params=params)

    def account_get_banned(self, **params):
        """Docs: https://dev.vk.com/method/account.getBanned"""
        return self.post(f'account.getBanned', params=params)

    def account_get_counters(self, **params):
        """Docs: https://dev.vk.com/method/account.getCounters"""
        return self.post(f'account.getCounters', params=params)

    def account_get_info(self, **params):
        """Docs: https://dev.vk.com/method/account.getInfo"""
        return self.post(f'account.getInfo', params=params)

    def account_get_profile_info(self, **params):
        """Docs: https://dev.vk.com/method/account.getProfileInfo"""
        return self.post(f'account.getProfileInfo', params=params)

    def account_get_push_settings(self, **params):
        """Docs: https://dev.vk.com/method/account.getPushSettings"""
        return self.post(f'account.getPushSettings', params=params)

    def account_lookup_contracts(self, **params):
        """Docs: https://dev.vk.com/method/account.lookupContacts"""
        return self.post(f'account.lookupContacts', params=params)

    def account_register_device(self, **params):
        """Docs: https://dev.vk.com/method/account.registerDevice"""
        return self.post(f'account.registerDevice', params=params)

    def account_save_profile_info(self, **params):
        """Docs: https://dev.vk.com/method/account.saveProfileInfo"""
        return self.post(f'account.saveProfileInfo', params=params)

    def account_set_info(self, **params):
        """Docs: https://dev.vk.com/method/account.setInfo"""
        return self.post(f'account.setInfo', params=params)

    def account_set_name_in_menu(self, **params):
        """Docs: https://dev.vk.com/method/account.setNameInMenu"""
        return self.post(f'account.setNameInMenu', params=params)

    def account_set_offline(self, **params):
        """Docs: https://dev.vk.com/method/account.setOffline"""
        return self.post(f'account.setOffline', params=params)

    def account_set_online(self, **params):
        """Docs: https://dev.vk.com/method/account.setOnline"""
        return self.post(f'account.setOnline', params=params)

    def account_set_push_settings(self, **params):
        """Docs: https://dev.vk.com/method/account.setPushSettings"""
        return self.post(f'account.setPushSettings', params=params)

    def account_set_silence_mode(self, **params):
        """Docs: https://dev.vk.com/method/account.setSilenceMode"""
        return self.post(f'account.', params=params)

    def account_unban(self, **params):
        """Docs: https://dev.vk.com/method/account.unban"""
        return self.post(f'account.unban', params=params)

    def account_unregister_device(self, **params):
        """Docs: https://dev.vk.com/method/account.unregisterDevice"""
        return self.post(f'account.unregisterDevice', params=params)

    # Ads
    def ads_add_office_users(self, **params):
        """Docs: https://dev.vk.com/method/ads.addOfficeUsers"""
        return self.post(f'ads.addOfficeUsers', params=params)

    def ads_check_link(self, **params):
        """Docs: https://dev.vk.com/method/ads.checkLink"""
        return self.post(f'ads.checkLink', params=params)

    def ads_create_ads(self, **params):
        """Docs: https://dev.vk.com/method/ads.createAds"""
        return self.post(f'ads.createAds', params=params)

    def ads_create_campaigns(self, **params):
        """Docs: https://dev.vk.com/method/ads.createCampaigns"""
        return self.post(f'ads.createCampaigns', params=params)

    def ads_create_clients(self, **params):
        """Docs: https://dev.vk.com/method/ads.createClients"""
        return self.post(f'ads.createClients', params=params)

    def ads_create_lookalike_request(self, **params):
        """Docs: https://dev.vk.com/method/ads.createLookalikeRequest"""
        return self.post(f'ads.createLookalikeRequest', params=params)

    def ads_create_target_group(self, **params):
        """Docs: https://dev.vk.com/method/ads.createTargetGroup"""
        return self.post(f'ads.createTargetGroup', params=params)

    def ads_create_target_pixel(self, **params):
        """Docs: https://dev.vk.com/method/ads.createTargetPixel"""
        return self.post(f'ads.createTargetPixel', params=params)

    def ads_delete_ads(self, **params):
        """Docs: https://dev.vk.com/method/ads.deleteAds"""
        return self.post(f'ads.deleteAds', params=params)

    def ads_delete_campaigns(self, **params):
        """Docs: https://dev.vk.com/method/ads.deleteCampaigns"""
        return self.post(f'ads.deleteCampaigns', params=params)

    def ads_delete_clients(self, **params):
        """Docs: https://dev.vk.com/method/ads.deleteClients"""
        return self.post(f'ads.deleteClients', params=params)

    def ads_delete_target_group(self, **params):
        """Docs: https://dev.vk.com/method/ads.deleteTargetGroup"""
        return self.post(f'ads.deleteTargetGroup', params=params)

    def ads_delete_target_pixel(self, **params):
        """Docs: https://dev.vk.com/method/ads.deleteTargetPixel"""
        return self.post(f'ads.delete_target_pixel', params=params)

    def ads_get_accounts(self, **params):
        """Docs: https://dev.vk.com/method/ads.getAccounts"""
        return self.post(f'ads.get_accounts', params=params)

    def ads_get_ads(self, **params):
        """Docs: https://dev.vk.com/method/ads.getAds"""
        return self.post(f'ads.getAds', params=params)
    ads_get_ads.iter_key = 'response.items'
    ads_get_ads.iter_field = 'offset'
    ads_get_ads.iter_mode = 'offset'
    ads_get_ads.iter_next = 'response.items'

    def ads_get_ads_layout(self, **params):
        """Docs: https://dev.vk.com/method/ads.getAdsLayout"""
        return self.post(f'ads.getAdsLayout', params=params)

    def ads_get_ads_posts_reach(self, **params):
        """Docs: https://dev.vk.com/method/ads.getAdsPostsReach"""
        return self.post(f'ads.getAdsPostsReach', params=params)

    def ads_get_ads_targeting(self, **params):
        """Docs: https://dev.vk.com/method/ads.getAdsTargeting"""
        return self.post(f'ads.getAdsTargeting', params=params)

    def ads_get_budget(self, **params):
        """Docs: https://dev.vk.com/method/ads.getBudget"""
        return self.post(f'ads.getBudget', params=params)

    def ads_get_campaigns(self, **params):
        """Docs: https://dev.vk.com/method/ads.getCampaigns"""
        return self.post(f'ads.getCampaigns', params=params)
    ads_get_campaigns.iter_key = 'response.items'
    ads_get_campaigns.iter_field = 'offset'
    ads_get_campaigns.iter_mode = 'offset'
    ads_get_campaigns.iter_next = 'response.items'

    def ads_get_categories(self, **params):
        """Docs: https://dev.vk.com/method/ads.getCategories"""
        return self.post(f'ads.getCategories', params=params)
    ads_get_categories.iter_key = 'response.items'
    ads_get_categories.iter_field = 'offset'
    ads_get_categories.iter_mode = 'offset'
    ads_get_categories.iter_next = 'response.items'

    def ads_get_clients(self, **params):
        """Docs: https://dev.vk.com/method/ads.getClients"""
        return self.post(f'ads.getClients', params=params)
    ads_get_clients.iter_key = 'response.items'
    ads_get_clients.iter_field = 'offset'
    ads_get_clients.iter_mode = 'offset'
    ads_get_clients.iter_next = 'response.items'

    def ads_get_demographics(self, **params):
        """Docs: https://dev.vk.com/method/ads.getDemographics"""
        return self.post(f'ads.getDemographics', params=params)

    def ads_get_flood_stats(self, **params):
        """Docs: https://dev.vk.com/method/ads.getFloodStats"""
        return self.post(f'ads.getFloodStats', params=params)

    def ads_get_lookalike_requests(self, **params):
        """Docs: https://dev.vk.com/method/ads.getLookalikeRequests"""
        return self.post(f'ads.get_lookalike_requests', params=params)

    def ads_get_musicians(self, **params):
        """Docs: https://dev.vk.com/method/ads.getMusicians"""
        return self.post(f'ads.getMusicians', params=params)

    def ads_get_musicians_by_ids(self, **params):
        """Docs: https://dev.vk.com/method/ads.getMusiciansByIds"""
        return self.post(f'ads.getMusiciansByIds', params=params)

    def ads_get_office_users(self, **params):
        """Docs: https://dev.vk.com/method/ads.getOfficeUsers"""
        return self.post(f'ads.getOfficeUsers', params=params)

    def ads_get_posts_reach(self, **params):
        """Docs: https://dev.vk.com/method/ads.getPostsReach"""
        return self.post(f'ads.getPostsReach', params=params)

    def ads_get_rejection_reason(self, **params):
        """Docs: https://dev.vk.com/method/ads.getRejectionReason"""
        return self.post(f'ads.getRejectionReason', params=params)

    def ads_get_statistics(self, **params):
        """Docs: https://dev.vk.com/method/ads.getStatistics"""
        return self.post(f'ads.getStatistics', params=params)

    def ads_get_suggestions(self, **params):
        """Docs: https://dev.vk.com/method/ads.getSuggestions"""
        return self.post(f'ads.getSuggestions', params=params)

    def ads_get_target_groups(self, **params):
        """Docs: https://dev.vk.com/method/ads.getTargetGroups"""
        return self.post(f'ads.getTargetGroups', params=params)

    def ads_get_target_pixels(self, **params):
        """Docs: https://dev.vk.com/method/ads.getTargetPixels"""
        return self.post(f'ads.getTargetPixels', params=params)

    def ads_get_targeting_stats(self, **params):
        """Docs: https://dev.vk.com/method/ads.getTargetingStats"""
        return self.post(f'ads.getTargetingStats', params=params)

    def ads_get_upload_url(self, **params):
        """Docs: https://dev.vk.com/method/ads.getUploadURL"""
        return self.post(f'ads.getUploadURL', params=params)

    def ads_get_video_upload_url(self, **params):
        """Docs: https://dev.vk.com/method/ads.getVideoUploadURL"""
        return self.post(f'ads.getVideoUploadURL', params=params)

    def ads_import_target_contacts(self, **params):
        """Docs: https://dev.vk.com/method/ads.importTargetContacts"""
        return self.post(f'ads.importTargetContacts', params=params)

    def ads_remove_office_users(self, **params):
        """Docs: https://dev.vk.com/method/ads.removeOfficeUsers"""
        return self.post(f'ads.removeOfficeUsers', params=params)

    def ads_remove_target_contacts(self, **params):
        """Docs: https://dev.vk.com/method/ads.removeTargetContacts"""
        return self.post(f'ads.removeTargetContacts', params=params)

    def ads_save_lookalike_request_result(self, **params):
        """Docs: https://dev.vk.com/method/ads.saveLookalikeRequestResult"""
        return self.post(f'ads.saveLookalikeRequestResult', params=params)

    def ads_share_target_group(self, **params):
        """Docs: https://dev.vk.com/method/ads.shareTargetGroup"""
        return self.post(f'ads.shareTargetGroup', params=params)

    def ads_update_ads(self, **params):
        """Docs: https://dev.vk.com/method/ads.updateAds"""
        return self.post(f'ads.updateAds', params=params)

    def ads_update_campaigns(self, **params):
        """Docs: https://dev.vk.com/method/ads.updateCampaigns"""
        return self.post(f'ads.updateCampaigns', params=params)

    def ads_update_clients(self, **params):
        """Docs: https://dev.vk.com/method/ads.updateClients"""
        return self.post(f'ads.updateClients', params=params)

    def ads_update_office_users(self, **params):
        """Docs: https://dev.vk.com/method/ads.updateOfficeUsers"""
        return self.post(f'ads.updateOfficeUsers', params=params)

    def ads_update_target_group(self, **params):
        """Docs: https://dev.vk.com/method/ads.updateTargetGroup"""
        return self.post(f'ads.', params=params)

    def ads_update_target_pixel(self, **params):
        """Docs: https://dev.vk.com/method/ads.updateTargetPixel"""
        return self.post(f'ads.updateTargetPixel', params=params)

    # Database
    def database_get_chairs(self, **params):
        """Docs: https://dev.vk.com/method/database.getChairs"""
        return self.post(f'database.getChairs', params=params)
    database_get_chairs.iter_key = 'response.items'
    database_get_chairs.iter_field = 'offset'
    database_get_chairs.iter_mode = 'offset'
    database_get_chairs.iter_next = 'response.items'

    def database_get_cities(self, **params):
        """Docs: https://dev.vk.com/method/database.getCities"""
        return self.post(f'database.getCities', params=params)
    database_get_cities.iter_key = 'response.items'
    database_get_cities.iter_field = 'offset'
    database_get_cities.iter_mode = 'offset'
    database_get_cities.iter_next = 'response.items'

    def database_get_cities_by_id(self, **params):
        """Docs: https://dev.vk.com/method/database.getCitiesById"""
        return self.post(f'database.getCitiesById', params=params)
    database_get_cities_by_id.iter_key = 'response.items'
    database_get_cities_by_id.iter_field = 'offset'
    database_get_cities_by_id.iter_mode = 'offset'
    database_get_cities_by_id.iter_next = 'response.items'

    def database_get_countries(self, **params):
        """Docs: https://dev.vk.com/method/database.getCountries"""
        return self.post(f'database.getCountries', params=params)
    database_get_countries.iter_key = 'response.items'
    database_get_countries.iter_field = 'offset'
    database_get_countries.iter_mode = 'offset'
    database_get_countries.iter_next = 'response.items'

    def database_get_countries_by_id(self, **params):
        """Docs: https://dev.vk.com/method/database.getCountriesById"""
        return self.post(f'database.getCountriesById', params=params)
    database_get_countries_by_id.iter_key = 'response.items'
    database_get_countries_by_id.iter_field = 'offset'
    database_get_countries_by_id.iter_mode = 'offset'
    database_get_countries_by_id.iter_next = 'response.items'

    def database_get_faculties(self, **params):
        """Docs: https://dev.vk.com/method/database.getFaculties"""
        return self.post(f'database.getFaculties', params=params)
    database_get_faculties.iter_key = 'response.items'
    database_get_faculties.iter_field = 'offset'
    database_get_faculties.iter_mode = 'offset'
    database_get_faculties.iter_next = 'response.items'

    def database_get_metro_stations(self, **params):
        """Docs: https://dev.vk.com/method/database.getMetroStations"""
        return self.post(f'database.getMetroStations', params=params)
    database_get_metro_stations.iter_key = 'response.items'
    database_get_metro_stations.iter_field = 'offset'
    database_get_metro_stations.iter_mode = 'offset'
    database_get_metro_stations.iter_next = 'response.items'

    def database_get_metro_stations_by_id(self, **params):
        """Docs: https://dev.vk.com/method/database.getMetroStationsById"""
        return self.post(f'database.getMetroStationsById', params=params)
    database_get_metro_stations_by_id.iter_key = 'response.items'
    database_get_metro_stations_by_id.iter_field = 'offset'
    database_get_metro_stations_by_id.iter_mode = 'offset'
    database_get_metro_stations_by_id.iter_next = 'response.items'

    def database_get_regions(self, **params):
        """Docs: https://dev.vk.com/method/database.getRegions"""
        return self.post(f'database.getRegions', params=params)
    database_get_regions.iter_key = 'response.items'
    database_get_regions.iter_field = 'offset'
    database_get_regions.iter_mode = 'offset'
    database_get_regions.iter_next = 'response.items'

    def database_get_school_classes(self, **params):
        """Docs: https://dev.vk.com/method/database.getSchoolClasses"""
        return self.post(f'database.getSchoolClasses', params=params)
    database_get_school_classes.iter_key = 'response.items'
    database_get_school_classes.iter_field = 'offset'
    database_get_school_classes.iter_mode = 'offset'
    database_get_school_classes.iter_next = 'response.items'

    def database_get_schools(self, **params):
        """Docs: https://dev.vk.com/method/database.getSchools"""
        return self.post(f'database.getSchools', params=params)
    database_get_schools.iter_key = 'response.items'
    database_get_schools.iter_field = 'offset'
    database_get_schools.iter_mode = 'offset'
    database_get_schools.iter_next = 'response.items'

    def database_get_universities(self, **params):
        """Docs: https://dev.vk.com/method/database.getUniversities"""
        return self.post(f'database.getUniversities', params=params)
    database_get_universities.iter_key = 'response.items'
    database_get_universities.iter_field = 'offset'
    database_get_universities.iter_mode = 'offset'
    database_get_universities.iter_next = 'response.items'

    # Docs
    def docs_add(self, **params):
        """Docs: https://dev.vk.com/method/docs.add"""
        return self.post(f'docs.add', params=params)

    def docs_delete(self, **params):
        """Docs: https://dev.vk.com/method/docs.delete"""
        return self.post(f'docs.delete', params=params)

    def docs_edit(self, **params):
        """Docs: https://dev.vk.com/method/docs.edit"""
        return self.post(f'docs.edit', params=params)

    def docs_get(self, **params):
        """Docs: https://dev.vk.com/method/docs.get"""
        return self.post(f'docs.get', params=params)

    def docs_get_by_id(self, **params):
        """Docs: https://dev.vk.com/method/docs.getById"""
        return self.post(f'docs.getById', params=params)

    def docs_get_messages_upload_server(self, **params):
        """Docs: https://dev.vk.com/method/docs.getMessagesUploadServer"""
        return self.post(f'docs.getMessagesUploadServer', params=params)

    def docs_get_types(self, **params):
        """Docs: https://dev.vk.com/method/docs.getTypes"""
        return self.post(f'docs.getTypes', params=params)

    def docs_get_upload_server(self, **params):
        """Docs: https://dev.vk.com/method/docs.getUploadServer"""
        return self.post(f'docs.getUploadServer', params=params)

    def docs_getWallUploadServer(self, **params):
        """Docs: https://dev.vk.com/method/docs.getWallUploadServer"""
        return self.post(f'docs.getWallUploadServer', params=params)

    def docs_save(self, **params):
        """Docs: https://dev.vk.com/method/docs.save"""
        return self.post(f'docs.save', params=params)

    def docs_search(self, **params):
        """Docs: https://dev.vk.com/method/docs.search"""
        return self.post(f'docs.search', params=params)

    # Donut
    def donut_get_fiends(self, **params):
        """Docs: https://dev.vk.com/method/donut.getFriends"""
        return self.post(f'donut.getFriends', params=params)

    def donut_get_subscription(self, **params):
        """Docs: https://dev.vk.com/method/donut.getSubscription"""
        return self.post(f'donut.getSubscription', params=params)

    def donut_get_subscriptions(self, **params):
        """Docs: https://dev.vk.com/method/donut.getSubscriptions"""
        return self.post(f'donut.getSubscriptions', params=params)

    def donut_is_don(self, **params):
        """Docs: https://dev.vk.com/method/donut.isDon"""
        return self.post(f'donut.isDon', params=params)

    # Downloaded Games
    def downloaded_games_get_paid_status(self, **params):
        """Docs: https://dev.vk.com/method/downloadedGames.getPaidStatus"""
        return self.post(f'downloadedGames.getPaidStatus', params=params)

    # Friends
    def friends_add(self, **params):
        """Docs: https://dev.vk.com/method/friends.add"""
        return self.post(f'friends.add', params=params)

    def friends_add_list(self, **params):
        """Docs: https://dev.vk.com/method/friends.addList"""
        return self.post(f'friends.addList', params=params)

    def friends_are_friends(self, **params):
        """Docs: https://dev.vk.com/method/friends.areFriends"""
        return self.post(f'friends.areFriends', params=params)

    def friends_delete(self, **params):
        """Docs: https://dev.vk.com/method/friends.delete"""
        return self.post(f'friends.delete', params=params)

    def friends_delete_all_requests(self, **params):
        """Docs: https://dev.vk.com/method/friends.deleteAllRequests"""
        return self.post(f'friends.deleteAllRequests', params=params)

    def friends_delete_list(self, **params):
        """Docs: https://dev.vk.com/method/friends.deleteList"""
        return self.post(f'friends.deleteList', params=params)

    def friends_edit(self, **params):
        """Docs: https://dev.vk.com/method/friends.edit"""
        return self.post(f'friends.edit', params=params)

    def friends_edit_list(self, **params):
        """Docs: https://dev.vk.com/method/friends.editList"""
        return self.post(f'friends.editList', params=params)

    def friends_get(self, **params):
        """Docs: https://dev.vk.com/method/friends.get"""
        return self.post(f'friends.get', params=params)

    def friends_get_app_users(self, **params):
        """Docs: https://dev.vk.com/method/friends.getAppUsers"""
        return self.post(f'friends.getAppUsers', params=params)

    def friends_get_available_for_call(self, **params):
        """Docs: https://dev.vk.com/method/friends.getAvailableForCall"""
        return self.post(f'friends.getAvailableForCall', params=params)

    def friends_get_by_phones(self, **params):
        """Docs: https://dev.vk.com/method/friends.getByPhones"""
        return self.post(f'friends.getByPhones', params=params)

    def friends_get_lists(self, **params):
        """Docs: https://dev.vk.com/method/friends.getLists"""
        return self.post(f'friends.getLists', params=params)

    def friends_get_mutual(self, **params):
        """Docs: https://dev.vk.com/method/friends.getMutual"""
        return self.post(f'friends.getMutual', params=params)

    def friends_get_online(self, **params):
        """Docs: https://dev.vk.com/method/friends.getOnline"""
        return self.post(f'friends.getOnline', params=params)

    def friends_get_recent(self, **params):
        """Docs: https://dev.vk.com/method/friends.getRecent"""
        return self.post(f'friends.getRecent', params=params)

    def friends_get_requests(self, **params):
        """Docs: https://dev.vk.com/method/friends.getRequests"""
        return self.post(f'friends.getRequests', params=params)

    def friends_get_suggestions(self, **params):
        """Docs: https://dev.vk.com/method/friends.getSuggestions"""
        return self.post(f'friends.getSuggestions', params=params)

    def friends_search(self, **params):
        """Docs: https://dev.vk.com/method/friends.search"""
        return self.post(f'friends.search', params=params)

    # Gifts
    def gifts_get(self, **params):
        """Docs: https://dev.vk.com/method/gifts.get"""
        return self.post(f'gifts.get', params=params)

    # Likes
    def likes_add(self, **params):
        """Docs: https://dev.vk.com/method/likes.add"""
        return self.post(f'likes.add', params=params)

    def likes_delete(self, **params):
        """Docs: https://dev.vk.com/method/likes.delete"""
        return self.post(f'likes.delete', params=params)

    def likes_get_list(self, **params):
        """Docs: https://dev.vk.com/method/likes.getList"""
        return self.post(f'likes.get_list', params=params)

    def likes_is_liked(self, **params):
        """Docs: https://dev.vk.com/method/likes.isLiked"""
        return self.post(f'likes.isLiked', params=params)

    # Notifications
    def notifications_get(self, **params):
        """Docs: https://dev.vk.com/method/notifications.get"""
        return self.post(f'notifications.get', params=params)

    def notifications_mark_as_viewed(self, **params):
        """Docs: https://dev.vk.com/method/notifications.markAsViewed"""
        return self.post(f'notifications.markAsViewed', params=params)

    def notifications_send_message(self, **params):
        """Docs: https://dev.vk.com/method/notifications.sendMessage"""
        return self.post(f'notifications.sendMessage', params=params)

    # Pages
    def pages_clear_cache(self, **params):
        """Docs: https://dev.vk.com/method/pages.clearCache"""
        return self.post(f'pages.clearCache', params=params)

    def pages_get(self, **params):
        """Docs: https://dev.vk.com/method/pages.get"""
        return self.post(f'pages.get', params=params)

    def pages_get_history(self, **params):
        """Docs: https://dev.vk.com/method/pages.getHistory"""
        return self.post(f'pages.getHistory', params=params)

    def pages_get_titles(self, **params):
        """Docs: https://dev.vk.com/method/pages.getTitles"""
        return self.post(f'pages.getTitles', params=params)

    def pages_get_version(self, **params):
        """Docs: https://dev.vk.com/method/pages.getVersion"""
        return self.post(f'pages.getVersion', params=params)

    def pages_parse_wiki(self, **params):
        """Docs: https://dev.vk.com/method/pages.parseWiki"""
        return self.post(f'pages.parseWiki', params=params)

    def pages_preview(self, **params):
        """Docs: https://dev.vk.com/method/pages.preview"""
        return self.post(f'pages.preview', params=params)

    def pages_save(self, **params):
        """Docs: https://dev.vk.com/method/pages.save"""
        return self.post(f'pages.save', params=params)

    def pages_save_access(self, **params):
        """Docs: https://dev.vk.com/method/pages.saveAccess"""
        return self.post(f'pages.saveAccess', params=params)

    # Places
    def places_get_checkins(self, **params):
        """Docs: https://dev.vk.com/method/places.getCheckins"""
        return self.post(f'places.getCheckins', params=params)

    # Podcasts
    def podcasts_search_podcast(self, **params):
        """Docs: https://dev.vk.com/method/podcasts.searchPodcast"""
        return self.post(f'podcasts.searchPodcast', params=params)

    # Search
    def places_get_hints(self, **params):
        """Docs: https://dev.vk.com/method/search.getHints"""
        return self.post(f'search.getHints', params=params)

    # Stats
    def stats_get(self, **params):
        """Docs: https://dev.vk.com/method/stats.get"""
        return self.post(f'stats.get', params=params)

    def stats_get_post_reach(self, **params):
        """Docs: https://dev.vk.com/method/stats.getPostReach"""
        return self.post(f'stats.getPostReach', params=params)

    def stats_track_visitor(self, **params):
        """Docs: https://dev.vk.com/method/stats.trackVisitor"""
        return self.post(f'stats.trackVisitor', params=params)

    # Status
    def status_get(self, **params):
        """Docs: https://dev.vk.com/method/status.get"""
        return self.post(f'status.get', params=params)

    def status_set(self, **params):
        """Docs: https://dev.vk.com/method/status.set"""
        return self.post(f'status.set', params=params)

    # Storage
    def storage_get(self, **params):
        """Docs: https://dev.vk.com/method/storage.get"""
        return self.post(f'storage.', params=params)

    def storage_get_keys(self, **params):
        """Docs: https://dev.vk.com/method/storage.getKeys"""
        return self.post(f'storage.getKeys', params=params)

    def storage_set(self, **params):
        """Docs: https://dev.vk.com/method/storage.set"""
        return self.post(f'storage.set', params=params)

    # Users
    def users_get(self, **params):
        """Docs: https://dev.vk.com/method/users.get"""
        return self.post(f'users.get', params=params)

    def users_get_followers(self, **params):
        """Docs: https://dev.vk.com/method/users.getFollowers"""
        return self.post(f'users.getFollowers', params=params)

    def users_get_subscriptions(self, **params):
        """Docs: https://dev.vk.com/method/users.getSubscriptions"""
        return self.post(f'users.getSubscriptions', params=params)

    def users_report(self, **params):
        """Docs: https://dev.vk.com/method/users.report"""
        return self.post(f'users.report', params=params)

    def users_search(self, **params):
        """Docs: https://dev.vk.com/method/users.search"""
        return self.post(f'users.search', params=params)

    # Utils
    def utils_check_link(self, **params):
        """Docs: https://dev.vk.com/method/utils.checkLink"""
        return self.post(f'utils.checkLink', params=params)

    def utils_delete_from_last_shortened(self, **params):
        """Docs: https://dev.vk.com/method/utils.deleteFromLastShortened"""
        return self.post(f'utils.deleteFromLastShortened', params=params)

    def utils_get_last_shortened_links(self, **params):
        """Docs: https://dev.vk.com/method/utils.getLastShortenedLinks"""
        return self.post(f'utils.getLastShortenedLinks', params=params)

    def utils_get_link_stats(self, **params):
        """Docs: https://dev.vk.com/method/utils.getLinkStats"""
        return self.post(f'utils.getLinkStats', params=params)

    def utils_get_server_time(self, **params):
        """Docs: https://dev.vk.com/method/utils.getServerTime"""
        return self.post(f'utils.getServerTime', params=params)

    def utils_get_short_link(self, **params):
        """Docs: https://dev.vk.com/method/utils.getShortLink"""
        return self.post(f'utils.getShortLink', params=params)

    def utils_resolve_screen_name(self, **params):
        """Docs: https://dev.vk.com/method/utils.resolveScreenName"""
        return self.post(f'utils.resolveScreenName', params=params)

    # Wall
    def wall_check_copyright_link(self, **params):
        """Docs: https://dev.vk.com/method/wall.checkCopyrightLink"""
        return self.post(f'wall.checkCopyrightLink', params=params)

    def wall_close_comments(self, **params):
        """Docs: https://dev.vk.com/method/wall.closeComments"""
        return self.post(f'wall.closeComments', params=params)

    def wall_create_comment(self, **params):
        """Docs: https://dev.vk.com/method/wall.createComment"""
        return self.post(f'wall.createComment', params=params)

    def wall_delete(self, **params):
        """Docs: https://dev.vk.com/method/wall.delete"""
        return self.post(f'wall.delete', params=params)

    def wall_delete_comment(self, **params):
        """Docs: https://dev.vk.com/method/wall.deleteComment"""
        return self.post(f'wall.deleteComment', params=params)

    def wall_delete_like(self, **params):
        """Docs: https://dev.vk.com/method/wall.deleteLike"""
        return self.post(f'wall.deleteLike', params=params)

    def wall_edit(self, **params):
        """Docs: https://dev.vk.com/method/wall.edit"""
        return self.post(f'wall.edit', params=params)

    def wall_edit_ads_stealth(self, **params):
        """Docs: https://dev.vk.com/method/wall.editAdsStealth"""
        return self.post(f'wall.editAdsStealth', params=params)

    def wall_edit_comment(self, **params):
        """Docs: https://dev.vk.com/method/wall.editComment"""
        return self.post(f'wall.editComment', params=params)

    def wall_get(self, **params):
        """Docs: https://dev.vk.com/method/wall.get"""
        return self.post(f'wall.get', params=params)

    def wall_get_by_id(self, **params):
        """Docs: https://dev.vk.com/method/wall.getById"""
        return self.post(f'wall.getById', params=params)

    def wall_get_comment(self, **params):
        """Docs: https://dev.vk.com/method/wall.getComment"""
        return self.post(f'wall.getComment', params=params)

    def wall_get_comments(self, **params):
        """Docs: https://dev.vk.com/method/wall.getComments"""
        return self.post(f'wall.getComments', params=params)

    def wall_get_likes(self, **params):
        """Docs: https://dev.vk.com/method/wall.getLikes"""
        return self.post(f'wall.getLikes', params=params)

    def wall_get_photo_upload_server(self, **params):
        """Docs: https://dev.vk.com/method/wall.getPhotoUploadServer"""
        return self.post(f'wall.getPhotoUploadServer', params=params)

    def wall_get_reposts(self, **params):
        """Docs: https://dev.vk.com/method/wall.getReposts"""
        return self.post(f'wall.getReposts', params=params)
    wall_get_reposts.iter_key = 'response.items'
    wall_get_reposts.iter_field = 'offset'
    wall_get_reposts.iter_mode = 'offset'
    wall_get_reposts.iter_next = 'response.items'

    def wall_open_comments(self, **params):
        """Docs: https://dev.vk.com/method/wall.openComments"""
        return self.post(f'wall.openComments', params=params)

    def wall_pin(self, **params):
        """Docs: https://dev.vk.com/method/wall.pin"""
        return self.post(f'wall.pin', params=params)

    def wall_post(self, **params):
        """Docs: https://dev.vk.com/method/wall.post"""
        return self.post(f'wall.post', params=params)

    def wall_post_ads_stealth(self, **params):
        """Docs: https://dev.vk.com/method/wall.postAdsStealth"""
        return self.post(f'wall.postAdsStealth', params=params)

    def wall_report_comment(self, **params):
        """Docs: https://dev.vk.com/method/wall.reportComment"""
        return self.post(f'wall.reportComment', params=params)

    def wall_report_post(self, **params):
        """Docs: https://dev.vk.com/method/wall.reportPost"""
        return self.post(f'wall.report_post', params=params)

    def wall_repost(self, **params):
        """Docs: https://dev.vk.com/method/wall.repost"""
        return self.post(f'wall.repost', params=params)

    def wall_restore(self, **params):
        """Docs: https://dev.vk.com/method/wall.restore"""
        return self.post(f'wall.restore', params=params)

    def wall_restore_comment(self, **params):
        """Docs: https://dev.vk.com/method/wall.restoreComment"""
        return self.post(f'wall.restoreComment', params=params)

    def wall_search(self, **params):
        """Docs: https://dev.vk.com/method/wall.search"""
        return self.post(f'wall.search', params=params)
    wall_search.iter_key = 'response.items'
    wall_search.iter_field = 'offset'
    wall_search.iter_mode = 'offset'
    wall_search.iter_next = 'response.items'

    def wall_unpin(self, **params):
        """Docs: https://dev.vk.com/method/wall.unpin"""
        return self.post(f'wall.unpin', params=params)
