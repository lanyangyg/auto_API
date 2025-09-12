import pytest
from base.api_client import ApiClient

@pytest.fixture(scope="session")
def auth_token():
    """
    Session级别的fixture，负责登录并获取token。
    这个fixture只在整个测试会话开始时执行一次，返回token给下面的 api_client方法使用
    """
    client = ApiClient()  # 使用优化后的ApiClient

    try:
        # 发送登录请求
        response = client.post("/user/login", data={"username": "emilys", "password": "emilyspass"})

        # 确保登录成功
        # 如果登录成功（返回200），代码继续执行，提取并返回token。
        # 如果登录失败（返回400/401/500等），raise_for_status() 会立即抛出 HTTPError 异常。pytest会捕获这个异常，将这个fixture标记为失败，并立即终止整个测试会话，报告一个明确的设置（setup）错误。
        response.raise_for_status()

        # 把响应体中的accessToken提取出来，存到token变量中
        token = response.json()["accessToken"]

        # 返回token，给下面的 api_client方法使用
        return token

    except Exception as e:
        pytest.fail(f"认证失败，无法开始测试: {e}")


@pytest.fixture(scope="session")
def api_client(auth_token):
    """
    Session级别的fixture，提供一个已认证的ApiClient实例。
    后续所有的业务测试都应该使用这个fixture。
    """
    # 1. 创建一个ApiClient实例
    client = ApiClient()

    # 2. 使用上面auth_token fixture返回的token，传给ApiClient实例中的set_auth_token方法，设置请求头
    client.set_auth_token(auth_token)

    # 3. 使用yield将这个配置好的客户端实例提供给测试用例
    yield client

    # 4. (可选) 测试会话结束后，可以执行清理操作
    client.clear_auth_token()
    print("\n测试会话结束，认证Token已清除")


def pytest_collection_modifyitems(config, items):
    """按类名自定义顺序"""
    # 定义测试类的执行顺序
    class_order = {
        "TestLogin": 0,
        "TestUser": 1,
        "TestProduct": 2,
        "TestCarts": 3
    }
    # 按类排序，类内按方法名自然排序
    items.sort(key=lambda item: (
        class_order.get(item.cls.__name__, 999) if item.cls else 999,
        item.name  # 类内按测试方法名排序
    ))

#
# @pytest.fixture(scope="session", autouse=True)
# def get_auth_token():
#     try:
#         # 创建API客户端实例用于发送认证请求
#         client = ApiClient()
#         # 发送用户登录请求获取token
#         response = client.post("/user/login", {"username": "emilys", "password": "emilyspass", "expiresInMins": 60})
#         # 检查认证响应状态并处理结果
#         if response.status_code == 200:
#             token = response.json()["accessToken"]
#             yield token     # 返回token
#         else:
#             pytest.fail(f"Authentication failed with status code: {response.status_code}")
#     except Exception as e:
#         pytest.fail(f"An error occurred during authentication: {e}")
