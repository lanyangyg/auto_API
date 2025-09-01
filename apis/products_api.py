from base.api_client import ApiClient

class Products:
    def __init__(self):
        self.token = self._get_auth_token()
        self.client = ApiClient()

    def _get_auth_token(self):
        login_client = ApiClient()
        response = login_client.post("/auth/login", {"username": "emilys","password": "emilyspass","expiresInMins": 60})
        if response.status_code == 200:
            return response.json()["accessToken"]
        else:
            raise Exception(f"Authentication failed with status code: {response.status_code}")


    def get_all_products(self):
        self.client.set_auth_token(self.token)
        response = self.client.get(endpoint="/products")
        return response

    def get_product_by_name(self, product_name):
        self.client.set_auth_token(self.token)
        response = self.client.get(endpoint=f"/products?q={product_name}")
        return response

    def add_product(self, title, description, category, price):
        self.client.set_auth_token(self.token)
        response = self.client.post(endpoint="/products/add", data={"title": title, "description": description, "category": category, "price": price})
        return response