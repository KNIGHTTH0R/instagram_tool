from requests import get


class Instagram(object):
    class Constants(object):
        BASE_URL = 'https://api.instagram.com/v1/'

    def __init__(self, access_token):
        self._access_token = access_token

    @property
    def access_token(self):
        return self._access_token

    def users_self(self):
        url = "%susers/self/?access_token=%s" % (self.Constants.BASE_URL, self.access_token)
        return get(url=url).json()

    def users_user_id(self, user_id):
        url = "%susers/%s/?access_token=%s" % (self.Constants.BASE_URL ,user_id, self.access_token)
        return get(url=url).json()

    def users_self_media_recent(self):
        url = "%susers/self/media/recent/?access_token=%s" % (self.Constants.BASE_URL, self.access_token)
        return get(url=url).json()

    def users_user_id_media_recent(self, user_id):
        url = "%susers/%s/media/recent/?access_token=%s" % (self.Constants.BASE_URL ,user_id, self.access_token)
        return get(url=url).json()

    def users_search(self, q):
        url = "%susers/search?q=%s&access_token=%s" % (self.Constants.BASE_URL, q, self.access_token)
        return get(url=url).json()