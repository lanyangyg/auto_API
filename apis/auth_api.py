from base.api_client import ApiClient

class Auth:
    def login(self, username, password, status_code):
        """
        登录
        :param username: 用户名
        :param password: 密码
        :status_code: 相应状态码
        """
        client = ApiClient()
        response = client.post("/user/login", {"username":username, "password":password})
        assert response.status_code == status_code
        return response.json()