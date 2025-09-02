from base.api_client import ApiClient

class Auth:
    def login(self, username, password):        # 去掉status_code参数
        """
        封装登录请求。
        它不关心请求是否成功，只负责发送请求并返回原始的response对象。
        """
        client = ApiClient()        # 这里创建一个原始的、未认证的客户端
        response = client.post("/user/login", {"username":username, "password":password})
        # assert response.status_code == status_code
        return response

    # 优化后具有高复用性：这个 login 方法现在可以在任何地方被调用，无论是为了在 conftest.py 中获取一个有效token，还是为了在 test_login.py 中测试一个失败场景。