import requests

class ApiClient:
    base_url = "https://dummyjson.com"

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url, headers=self.headers)
        return response


    def post(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url, headers=self.headers)
        return response

    def patch(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.patch(url, headers=self.headers, json=data)
        return response

    def options(self, endpoint):
        url = self.base_url + endpoint
        response = requests.options(url, headers=self.headers)
        return response

    # 添加 set_auth_token 和 clear_auth_token 方法来管理认证头
    def set_auth_token(self, token):
        """
        设置认证token到headers中
        """
        self.headers["Authorization"] = f"Bearer {token}"

    def clear_auth_token(self):
        """
        清除认证token
        """
        if "Authorization" in self.headers:
            del self.headers["Authorization"]
