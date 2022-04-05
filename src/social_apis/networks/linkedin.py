from social_apis.networks.network import Network


class Linkedin(Network):

    api_url = 'https://api.linkedin.com'
    api_version = 'v2'
    url = f"{api_url}/{api_version}"

    def __init__(self, **params):
        super(Linkedin, self).__init__(self.api_url, **params)

    # Profile
    def me(self, **params):
        """Docs: https://docs.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api"""
        return self.get(f'{self.url}/me', params=params)

    def get_people(self, **params):
        """Docs: https://docs.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api#retrieve-other-members-profile"""
        return self.get(f'{self.url}/people', params=params)

    def get_people_by_id(self, id, **params):
        """Docs: https://docs.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api#retrieve-other-members-profile"""
        return self.get(f'{self.url}/people/{id}', params=params)

    # Organizations
    def get_organizations(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/organizations/organization-lookup-api"""
        return self.get(f'{self.url}/organizations', params=params)

    def get_organizations_by_id(self, id, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/organizations/organization-lookup-api#sample-request-1"""
        return self.get(f'{self.url}/organizations/{id}', params=params)

    def get_organization_access_control(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/compliance/integrations/organizations/organization-access-control"""
        return self.get(f'{self.url}/organizationAcls', params=params)

    def search_company(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/organizations/company-search"""
        return self.get(f'{self.url}/companySearch', params=params)

    # Posts
    def create_post(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/ugc-post-api"""
        return self.get(f'{self.url}/ugcPosts', params=params)

    # Social Actions
    def get_summary_of_social_actions(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.get(f'{self.url}/socialActions', params=params)

    def get_social_action(self, action, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.get(f'{self.url}/socialActions/{action}', params=params)

    def get_social_action_likes(self, action, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.get(f'{self.url}/socialActions/{action}/likes', params=params)

    def post_social_action_likes(self, action, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.post(f'{self.url}/socialActions/{action}/likes', params=params)

    def delete_social_action_likes(self, action, actor_urn, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.delete(f'{self.url}/socialActions/{action}/likes/{actor_urn}', params=params)

    def get_social_action_comments(self, action, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.get(f'{self.url}/socialActions/{action}/comments', params=params)

    def post_social_action_comment(self, action, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.post(f'{self.url}/socialActions/{action}/comments', params=params)

    def delete_social_action_comment(self, action, comment_id, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/network-update-social-actions"""
        return self.delete(f'{self.url}/socialActions/{action}/comments/{comment_id}', params=params)

    # Messages
    def post_message(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/shared/integrations/communications/messages"""
        return self.post(f'{self.url}/messages', params=params)

    # Assets
    def post_asset(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/vector-asset-api"""
        return self.post(f'{self.url}/assets', params=params)

    # Articles
    def search_articles(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/articles-api#sample-request"""
        return self.get(f'{self.url}/originalArticles', params=params)

    def get_article(self, original_articles_id, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/articles-api#sample-request-1"""
        return self.get(f'{self.url}/originalArticles/{original_articles_id}', params=params)

    def delete_article(self, original_articles_id, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/marketing/integrations/community-management/shares/articles-api"""
        return self.delete(f'{self.url}/originalArticles/{original_articles_id}', params=params)

    # Groups
    def search_groups(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/compliance/integrations/groups/group-definitions"""
        return self.get(f'{self.url}/groupDefinitions', params=params)

    def get_group(self, group_id, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/compliance/integrations/groups/group-definitions"""
        return self.get(f'{self.url}/groupDefinitions/{group_id}', params=params)

    def edit_group_definition(self, group_id, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/compliance/integrations/groups/group-definitions"""
        return self.post(f'{self.url}/groupDefinitions/{group_id}', params=params)

    def delete_group(self, group_id, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/compliance/integrations/groups/group-definitions"""
        return self.delete(f'{self.url}/groupDefinitions/{group_id}', params=params)

    # Database
    def places(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/compliance/"""
        return self.get(f'{self.url}/places', params=params)

    def regions(self, **params):
        """Docs: https://docs.microsoft.com/ru-ru/linkedin/compliance/"""
        return self.get(f'{self.url}/regions', params=params)
