from base.api_client import ApiClient


# 重构整个user类，遵循“依赖注入”原则，它不自己创建工具，而是等待外部给它工具。
class User:
    # 参数 "api_client: ApiClient" 的意思是：
    #   "要创建User这个工具箱，你必须给我一个已经准备好的、能发网络请求的工具（api_client），
    #    而且这个工具必须是ApiClient类型的。"
    # 这种做法叫做“依赖注入”，好处是让User类变得非常灵活和易于测试。
    def __init__(self, api_client: ApiClient):
        """
        初始化用户API的工具箱。
        :param api_client: 一个已经配置好、并且通过了认证的ApiClient实例。
        """
        # 将外部传入的那个api_client工具，保存为自己内部的一个属性 self.client。
        # 这样，这个User工具箱里的其他方法就可以随时使用这个工具了。
        self.client = api_client

    def get_current_user(self):
        """
        获取当前用户信息
        """
        #   不需要再每次都往请求头中加token了，因为实例化的self.client 已经是完成认证的
        response = self.client.get("/users/me")
        return response

    def add_user(self, firstName, lastName, age):
        """
        添加用户
        """
        response = self.client.post("users/add", {"firstName": firstName, "lastName": lastName, "age": age})
        return response

    def update_user(self, firstName, lastName):
        """
        更新用户信息
        """
        response = self.client.put("/users/1", {"firstName": firstName, "lastName": lastName})
        return response

    def get_user_by_id(self, user_id):
        """
        通过ID获取用户信息
        """
        response = self.client.get(f"/users/{user_id}")
        return response




    # def __init__(self):
    #     # User类自己创建了ApiClient实例，和它“绑定”在了一起。每一次实例化都会触发一次登录API的调用（低效和资源浪费）
    #     self.client = ApiClient()   # 紧耦合 (自己创建)
    #     self.token = self._get_auth_token()
    # def _get_auth_token(self):
    #     """
    #     内部方法获取认证token
    #     """
    #     # 直接实现登录逻辑获取token
    #     login_client = ApiClient()
    #     response = login_client.post("/auth/login", {"username": "emilys","password": "emilyspass","expiresInMins": 60})
    #     if response.status_code == 200:
    #         return response.json()["accessToken"]
    #     else:
    #         raise Exception(f"Authentication failed with status code: {response.status_code}")
    #
    # def get_current_user(self):
    #     # 使用set_auth_token方法设置token，而不是作为参数传递
    #     self.client.set_auth_token(self.token) # 请求头中增加token
    #     response = self.client.get("/users/me")
    #     return response
    #
    # def add_user(self, firstName, lastName, age):
    #     self.client.set_auth_token(self.token)
    #     response = self.client.post("/users/add", {"firstName": firstName, "lastName": lastName, "age": age})
    #     return response
    #
    # def update_user(self, firstName, lastName):
    #     self.client.set_auth_token(self.token)
    #     response = self.client.put("/users/1", {"firstName": firstName, "lastName": lastName})
    #     return response
    #
    # def get_user_by_id(self, id):
    #     self.client.set_auth_token(self.token) # 请求头中增加token
    #     response = self.client.get(f"/users/{id}")
    #     return response
    #
    #
    #     # token = get_auth_token
    #     # response = requests.get(
    #     #     url="https://dummyjson.com/users/1",
    #     #     headers= {"Authorization": f"Bearer {token}"}
    #     # )
    #     # assert response.status_code == 200
    #
