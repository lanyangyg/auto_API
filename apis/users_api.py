from base.api_client import ApiClient

class User:
    def __init__(self):
        self.client = ApiClient()
        self.token = self._get_auth_token()
    def _get_auth_token(self):
        """
        内部方法获取认证token
        """
        # 直接实现登录逻辑获取token
        login_client = ApiClient()
        response = login_client.post("/auth/login", {"username": "emilys","password": "emilyspass","expiresInMins": 60})
        if response.status_code == 200:
            return response.json()["accessToken"]
        else:
            raise Exception(f"Authentication failed with status code: {response.status_code}")

    def get_current_user(self):
        # 使用set_auth_token方法设置token，而不是作为参数传递
        self.client.set_auth_token(self.token) # 请求头中增加token
        response = self.client.get("/users/me")
        return response

    def add_user(self, firstName, lastName, age):
        self.client.set_auth_token(self.token)
        response = self.client.post("/users/add", {"firstName": firstName, "lastName": lastName, "age": age})
        return response

    def update_user(self, firstName, lastName):
        self.client.set_auth_token(self.token)
        response = self.client.put("/users/1", {"firstName": firstName, "lastName": lastName})
        return response

    def get_user_by_id(self, id):
        self.client.set_auth_token(self.token) # 请求头中增加token
        response = self.client.get(f"/users/{id}")
        return response


        # token = get_auth_token
        # response = requests.get(
        #     url="https://dummyjson.com/users/1",
        #     headers= {"Authorization": f"Bearer {token}"}
        # )
        # assert response.status_code == 200

