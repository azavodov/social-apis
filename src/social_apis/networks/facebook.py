from social_apis.networks.network import Network


class Facebook(Network):

    api_url = 'https://graph.facebook.com'
    api_version = 'v13.0'
    url = f"{api_url}/{api_version}"

    quota_headers = ['x-app-usage']

    def __init__(self, **params):
        super(Facebook, self).__init__(self.api_url, self.quota_headers, **params)

    # Albums
    def get_album(self, album_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/album/"""
        return self.get(f"{self.api_url}/{album_id}", params=params)

    # Groups
    def get_group(self, group_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/group"""
        return self.get(f"{self.api_url}/{group_id}", params=params)

    def get_group_albums(self, group_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/group/albums"""
        return self.get(f"{self.api_url}/{group_id}/albums", params=params)
    get_group_albums.iter_key = 'data'
    get_group_albums.iter_field = 'after'
    get_group_albums.iter_next = 'paging.cursors.after'

    def post_group_album(self, group_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/group/albums#publish"""
        return self.post(f"{self.api_url}/{group_id}/albums", params=params)

    def post_group_photo(self, group_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/group/photos"""
        return self.post(f"{self.api_url}/{group_id}/photos", params=params)

    def get_group_videos(self, group_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/group/videos"""
        return self.get(f"{self.api_url}/{group_id}/videos", params=params)
    get_group_videos.iter_key = 'data'
    get_group_videos.iter_field = 'after'
    get_group_videos.iter_next = 'paging.cursors.after'

    # Pages
    def get_page(self, page_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/page/"""
        return self.get(f"{self.api_url}/{page_id}", params=params)

    def update_page(self, page_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/page#Updating"""
        return self.post(f"{self.api_url}/{page_id}", params=params)

    def delete_page(self, page_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/page#Deleting"""
        return self.post(f"{self.api_url}/{page_id}/assigned_users", params=params)

    def get_page_personas(self, page_id, **params):
        """https://developers.facebook.com/docs/graph-api/reference/page/personas/#Reading"""
        return self.get(f"{self.api_url}/{page_id}/personas", params=params)
    get_page_personas.iter_key = 'data'
    get_page_personas.iter_field = 'after'
    get_page_personas.iter_next = 'paging.cursors.after'

    def post_page_personas(self, page_id, **params):
        """https://developers.facebook.com/docs/graph-api/reference/page/personas/#Creating"""
        return self.post(f"{self.api_url}/{page_id}/personas", params=params)

    def get_page_conversations(self, page_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/page/conversations"""
        return self.get(f"{self.api_url}/{page_id}/conversations", params=params)
    get_page_conversations.iter_key = 'data'
    get_page_conversations.iter_field = 'after'
    get_page_conversations.iter_next = 'paging.cursors.after'

    def get_page_groups(self, page_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/page/groups"""
        return self.get(f"{self.api_url}/{page_id}/groups", params=params)
    get_page_groups.iter_key = 'data'
    get_page_groups.iter_field = 'after'
    get_page_groups.iter_next = 'paging.cursors.after'

    def get_page_insights(self, page_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/page/insights"""
        return self.get(f"{self.api_url}/{page_id}/insights", params=params)
    get_page_insights.iter_key = 'data'
    get_page_insights.iter_field = 'after'
    get_page_insights.iter_next = 'paging.cursors.after'

    def get_page_likes(self, page_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/page/likes"""
        return self.get(f"{self.api_url}/{page_id}/likes", params=params)

    # Posts
    def get_post(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/"""
        return self.get(f"{self.url}/{post_id}", params)

    def get_post_attachments(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/attachments/"""
        return self.get(f"{self.url}/{post_id}/attachments", params)

    def get_post_comments(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/object/comments"""
        return self.get(f"{self.url}/{post_id}/comments", params)

    def post_post_comment(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/object/comments#publish"""
        return self.post(f"{self.url}/{post_id}/comments", params)

    def get_post_dynamic_posts(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/dynamic_posts/"""
        return self.get(f"{self.url}/{post_id}/dynamic_posts", params)

    def get_post_insights(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/insights/"""
        return self.get(f"{self.url}/{post_id}/insights", params)

    def get_post_reactions(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/reactions/"""
        return self.get(f"{self.url}/{post_id}/reactions", params)

    def get_post_sharedposts(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/sharedposts/"""
        return self.get(f"{self.url}/{post_id}/sharedposts", params)

    def get_post_sponsor_tags(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/sponsor_tags/"""
        return self.get(f"{self.url}/{post_id}/sponsor_tags", params)

    def get_post_to(self, post_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/post/to/"""
        return self.get(f"{self.url}/{post_id}/to", params)

    # Comments
    def get_comment(self, comment_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/object/comments"""
        return self.get(f"{self.url}/{comment_id}", params)

    def edit_comment(self, comment_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/comment#updating"""
        return self.post(f"{self.url}/{comment_id}", params)

    def delete_comment(self, comment_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/comment#deleting"""
        return self.delete(f"{self.url}/{comment_id}", params)

    def get_comment_replies(self, comment_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/comment#edges"""
        return self.get(f"{self.url}/{comment_id}/comments", params)

    def get_comment_private_replies(self, comment_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/comment#edges"""
        return self.get(f"{self.url}/{comment_id}/private_replies", params)

    def get_comment_likes(self, comment_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/comment#edges"""
        return self.get(f"{self.url}/{comment_id}/likes", params)

    def get_comment_reactions(self, comment_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/comment#edges"""
        return self.get(f"{self.url}/{comment_id}/reactions", params)

    # Messages
    def get_message(self, message_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/message"""
        return self.get(f"{self.url}/{message_id}", params)

    def get_message_attachments(self, message_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/attachments"""
        return self.get(f"{self.url}/{message_id}/attachments", params)

    def get_message_shares(self, message_id, **params):
        """Docs: https://developers.facebook.com/docs/graph-api/reference/v13.0/shares"""
        return self.get(f"{self.url}/{message_id}/shares", params)
