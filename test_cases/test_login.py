from apis.auth_api import Auth
import pytest


class TestLogin:
    # def test_login(self):
    #     client = ApiClient()
    #     response = client.post("/user/login", {"username":"emilys", "password":"emilyspass", "expiresInMins":60})
    #     assert response.status_code == 200
    #     token = response.json()["accessToken"]
    #     return token

    @pytest.mark.parametrize("username,password,expected_status_code", [
        ("emilys", "emilyspass", 200),
        ("testuser", "testpass", 400),
        ("anotheruser", "anotherpass", 400)
    ])
    def test_login(self, username, password, expected_status_code):
        # 1. 准备动作，实例化一个Auth对象
        login = Auth()

        # 2. 调用被测方法，获取响应结果（只把 username 和 password 传给了 login 方法）
        response = login.login(username, password)

        # return response       # 注释掉这行，Auth()中已经返回响应结果了

        # 3. 断言（验证结果）
        # 使用第三个参数 expected_status_code, 实际的返回结果进行比较，判断测试是否通过
        assert response.status_code == expected_status_code

