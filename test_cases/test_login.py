from apis.auth_api import Auth
import pytest
import allure

@allure.feature("Login Module")
class TestLogin:

    @allure.story("Login Success")
    @pytest.mark.parametrize("username,password,expected_status_code", [
        ("emilys", "emilyspass", 200)
        # ("testuser", "testpass", 400),
        # ("anotheruser", "anotherpass", 400)
    ])
    def test_login(self, username, password, expected_status_code):
        # 1. 准备动作，实例化一个Auth对象
        login = Auth()
        # 2. 调用被测方法，获取响应结果（只把 username 和 password 传给了 login 方法）
        response = login.login(username, password)
        # 3. 断言（验证结果）
        # 使用第三个参数 expected_status_code, 实际的返回结果进行比较，判断测试是否通过
        assert response.status_code == expected_status_code

    # # 运行时跳过这条测试用例
    # @pytest.mark.skip
    @allure.story("Get All Tokens")
    def test_get_all_tokens(self):
        auth = Auth()
        tokens = auth.get_all_users_token(max_workers=20)

        # 验证结果
        assert len(tokens) > 0
        assert "username" in tokens[0]
        assert "accessToken" in tokens[0]
        print(f"成功获取 {len(tokens)} 个token")



