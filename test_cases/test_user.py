import pytest
from apis.users_api import User

class TestUser:

    def test_get_current_user(self):
        user_api = User()
        response = user_api.get_current_user()
        assert response.status_code == 200

    @pytest.mark.parametrize("firstName, lastName, age", [
        ("test1", "test_1", 10),
        ("test2", "test_2", 20),
        ("test3", "test_3", 30)
    ])
    def test_add_user(self, firstName, lastName, age):
        user_api = User()
        response = user_api.add_user(firstName, lastName, age)
        assert response.status_code == 201
        assert response.json()["lastName"] == lastName

    @pytest.mark.parametrize("firstName, lastName", [
        ("test1", "test_1"),
        ("test2", "test_2")
    ])
    def test_update_user(self, firstName, lastName):
        user_api = User()
        response = user_api.update_user(firstName, lastName)
        assert response.status_code == 200

    @pytest.mark.parametrize("id", [1, 2, 3])
    def test_get_user_by_id(self, id):
        user_api = User()
        response = user_api.get_user_by_id(id)
        assert response.status_code == 200

# def test_get_current_user(self, get_auth_token):
    #     # 获取 fixture 的返回值（已经是 token 字符串）
    #     token = get_auth_token
    #     client = ApiClient()
    #     # 使用set_auth_token方法设置token，而不是作为参数传递
    #     client.set_auth_token(token)
    #     response = client.get("/users/me")
    #     assert response.status_code == 200
    #     assert response.json()["firstName"] == "Emily"
    #
    # def test_add_user(self, get_auth_token):
    #     token = get_auth_token
    #     client = ApiClient()
    #     client.set_auth_token(token)
    #     response = client.post("/users/add", {"firstName": "mjl123", "lastName": "tiktok12", "age": 30})
    #     assert response.status_code == 201
    #     assert response.json()["firstName"] == "mjl123"
    #
    # def test_update_user(self, get_auth_token):
    #     token = get_auth_token
    #     url = "https://dummyjson.com/users/1"
    #     data = {
    #         "firstName": "test111222",
    #         "lastName": "tiktok12"
    #     }
    #     response = requests.put(url=url, json=data, headers={"Authorization": f"Bearer {token}"})
    #     assert response.status_code == 200
    #     assert response.json()["firstName"] == "test111222"
    #
    # def test_get_user_by_id(self, get_auth_token):
    #     token = get_auth_token
    #     response = requests.get(
    #         url="https://dummyjson.com/users/1",
    #         headers= {"Authorization": f"Bearer {token}"}
    #     )
    #     assert response.status_code == 200
    #
