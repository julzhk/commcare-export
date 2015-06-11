from requests.auth import AuthBase

class ApiAuth(AuthBase):
    """
    Auth with an API header for tastypie
    """
    def __init__(self, username, key):
        self.username = username
        self.key = key

    def __call__(self, req):
        req.headers['Authorization'] = 'ApiKey %s:%s' % (self.username, self.key)
        return req
