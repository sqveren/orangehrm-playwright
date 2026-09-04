


class BaseApiClient:
    def __init__(self, request_context, base_url):
        self.request = request_context
        self.base_url = base_url

    def get(self, endpoint, **kwargs):
        response = self.request.get(f"{self.base_url}{endpoint}", **kwargs)
        return response
    
    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        print(f"POSTING TO: {url}") 
        response = self.request.post(url, data=data)
        return response
        
    def put(self, endpoint,data=None):
        url = f"{self.base_url}{endpoint}"
        print(f"PUTTING TO: {url}") 
        response = self.request.put(url, data=data)
        return response
    
    def delete(self, endpoint, data=None):
        response = self.request.delete(f"{self.base_url}{endpoint}", data=data)
        return response
    
    