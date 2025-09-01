from apis.auth_api import Auth
import pytest


class TestLogin:
    # def test_login(self):
    #     client = ApiClient()
    #     response = client.post("/user/login", {"username":"emilys", "password":"emilyspass", "expiresInMins":60})
    #     assert response.status_code == 200
    #     token = response.json()["accessToken"]
    #     return token

    @pytest.mark.parametrize("username,password,status_code", [
        ("emilys", "emilyspass", 200),
        ("testuser", "testpass", 400),
        ("anotheruser", "anotherpass", 400)
    ])
    def test_login(self, username, password, status_code):
        login = Auth()
        response = login.login(username, password, status_code)
        return response

