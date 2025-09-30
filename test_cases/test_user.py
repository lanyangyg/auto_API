import pytest
from apis.users_api import User
import allure

# 重构整个TestUser类
@allure.feature("Users Module")
class TestUser:

    @pytest.fixture(scope="class")
    def user_api(self, api_client):
        """
        这个Fixture负责创建并提供一个随时可用的User API工具箱实例。
        """
        # 使用从conftest.py中传来的、已经认证过的api_client方法，实例化User类。
        # 这个实例（user_api）在整个TestUser类的测试过程中是同一个，不会重复创建。
        return User(api_client)


    @pytest.mark.run(order=1)
    @allure.story("Current User")
    def test_get_current_user(self, user_api):
        # 使用user_api实例，调用get_current_user方法
        response = user_api.get_current_user()
        assert response.status_code == 200


    @pytest.mark.run(order=2)
    @allure.story("Add User")
    @pytest.mark.parametrize("firstName, lastName, age", [
        ("test1", "test_1", 10),
        ("test2", "test_2", 20),
        ("test3", "test_3", 30)
    ])
    def test_add_user(self, user_api, firstName, lastName, age):
        response = user_api.add_user(firstName, lastName, age)
        assert response.status_code == 201


    @pytest.mark.run(order=3)
    @allure.story("Search User")
    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_user_by_id(self, user_api, user_id):
        response = user_api.get_user_by_id(user_id)
        assert response.status_code == 200
        assert response.json()["id"] == user_id


    @pytest.mark.run(order=4)
    @allure.story("Update User")
    @pytest.mark.parametrize("test_firstName, test_flastName", [
        ("test1", "test_1"),
        ("test2", "test_2")
    ])
    def test_update_user(self, user_api, test_firstName, test_flastName):
        response = user_api.update_user(test_firstName, test_flastName)
        assert response.status_code == 200
        assert response.json()["firstName"] == test_firstName
        assert response.json()["lastName"] == test_flastName

#
#     def test_get_current_user(self):
#         user_api = User()
#         response = user_api.get_current_user()
#         assert response.status_code == 200
#
#     @pytest.mark.parametrize("firstName, lastName, age", [
#         ("test1", "test_1", 10),
#         ("test2", "test_2", 20),
#         ("test3", "test_3", 30)
#     ])
#     def test_add_user(self, firstName, lastName, age):
#         user_api = User()
#         response = user_api.add_user(firstName, lastName, age)
#         assert response.status_code == 201
#         assert response.json()["lastName"] == lastName
#
#     @pytest.mark.parametrize("firstName, lastName", [
#         ("test1", "test_1"),
#         ("test2", "test_2")
#     ])
#     def test_update_user(self, firstName, lastName):
#         user_api = User()
#         response = user_api.update_user(firstName, lastName)
#         assert response.status_code == 200
#
#     @pytest.mark.parametrize("id", [1, 2, 3])
#     def test_get_user_by_id(self, id):
#         user_api = User()
#         response = user_api.get_user_by_id(id)
#         assert response.status_code == 200
#
# # def test_get_current_user(self, get_auth_token):
#     #     # 获取 fixture 的返回值（已经是 token 字符串）
#     #     token = get_auth_token
#     #     client = ApiClient()
#     #     # 使用set_auth_token方法设置token，而不是作为参数传递
#     #     client.set_auth_token(token)
#     #     response = client.get("/users/me")
#     #     assert response.status_code == 200
#     #     assert response.json()["firstName"] == "Emily"
#     #
#     # def test_add_user(self, get_auth_token):
#     #     token = get_auth_token
#     #     client = ApiClient()
#     #     client.set_auth_token(token)
#     #     response = client.post("/users/add", {"firstName": "mjl123", "lastName": "tiktok12", "age": 30})
#     #     assert response.status_code == 201
#     #     assert response.json()["firstName"] == "mjl123"
#     #
#     # def test_update_user(self, get_auth_token):
#     #     token = get_auth_token
#     #     url = "https://dummyjson.com/users/1"
#     #     data = {
#     #         "firstName": "test111222",
#     #         "lastName": "tiktok12"
#     #     }
#     #     response = requests.put(url=url, json=data, headers={"Authorization": f"Bearer {token}"})
#     #     assert response.status_code == 200
#     #     assert response.json()["firstName"] == "test111222"
#     #
#     # def test_get_user_by_id(self, get_auth_token):
#     #     token = get_auth_token
#     #     response = requests.get(
#     #         url="https://dummyjson.com/users/1",
#     #         headers= {"Authorization": f"Bearer {token}"}
#     #     )
#     #     assert response.status_code == 200
#     #
