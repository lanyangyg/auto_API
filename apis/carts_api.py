from base.api_client import ApiClient

class Carts:
    def __init__(self, api_client: ApiClient):
        self.client = api_client

    def get_carts_by_user_id(self, user_id):
        response = self.client.get(f"/carts/user/{user_id}")
        return response

    def get_all_carts(self):
        response = self.client.get("/carts")
        return response

    def add_cart(self, user_id, products):
        data = {
            "userId": user_id,
            "products": products
        }
        response = self.client.post("/carts/add", data)
        return response

    def update_cart_by_carts_id(self, carts_id, product_id, quantity):
        response = self.client.put(f"/carts/{carts_id}", {"productId": product_id, "quantity": quantity})
        return response

    def delete_cart_by_carts_id(self, carts_id):
        response = self.client.delete(f"/carts/{carts_id}")
        return response
