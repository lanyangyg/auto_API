import pytest
from base.api_client import ApiClient

@pytest.fixture(scope="session", autouse=True)
def get_auth_token():
    try:
        # 创建API客户端实例用于发送认证请求
        client = ApiClient()
        # 发送用户登录请求获取token
        response = client.post("/user/login", {"username": "emilys", "password": "emilyspass", "expiresInMins": 60})
        # 检查认证响应状态并处理结果
        if response.status_code == 200:
            token = response.json()["accessToken"]
            yield token     # 返回token
        else:
            pytest.fail(f"Authentication failed with status code: {response.status_code}")
    except Exception as e:
        pytest.fail(f"An error occurred during authentication: {e}")

    """
        获取认证令牌的pytest fixture函数

        该fixture具有session级别的作用域，会在整个测试会话开始时自动执行。
        函数通过调用API客户端的登录接口获取访问令牌，并在测试期间提供该令牌。

        参数:
            无参数

        返回值:
            str: 认证成功的访问令牌字符串

        异常:
            pytest.fail: 当认证失败时抛出，包含具体的HTTP状态码信息
    """
