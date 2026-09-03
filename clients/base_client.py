


class BaseApiClient:
    def __init__(self, request_context, base_url):
        self.request = request_context
        self.base_url = base_url

    def get(self, endpoint, **kwargs):
        response = self.request.get(f"{self.base_url}{endpoint}", **kwargs)
        return response
        
    