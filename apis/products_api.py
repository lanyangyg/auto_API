from base.api_client import ApiClient

# rebuild class Products
class Products:

    def __init__(self, api_client: ApiClient):
        self.client = api_client

    def get_all_products(self):
        """
        获取所有商品列表。
        :return: 一个包含所有商品信息的列表。
        """
        # 使用self.client属性，调用ApiClient实例的方法，发送HTTP请求。
        response = self.client.get("/products")
        return response

    def get_product_by_name(self, product_name):
        """
        根据商品名称获取商品信息。
        :param product_name: 商品名称。
        :return: 一个包含指定商品名称商品的信息的字典。
        """
        # 使用self.client属性，调用ApiClient实例的方法，发送HTTP请求。
        response = self.client.get(f"/products?q={product_name}")
        return response

    def add_product(self, title, description, category, price):
        """
        添加一个新的商品。
        :param title: 商品标题。
        :param description: 商品描述。
        :param category: 商品类别。
        :param price: 商品价格。
        :return: 一个包含添加商品信息的字典。
        """
        # 使用self.client属性，调用ApiClient实例的方法，发送HTTP请求。
        response = self.client.post("/products/add", {"title": title, "description": description, "category": category, "price": price})
        return response

    def update_product_by_id(self, product_id, title, description, category, price):
        """
        更新一个商品。
        :param product_id: 商品ID。
        :param title: 商品标题。
        :param description: 商品描述。
        :param category: 商品类别。
        :param price: 商品价格。
        :return: 一个包含更新商品信息的字典。
        """
        # 使用self.client属性，调用ApiClient实例的方法，发送HTTP请求。
        response = self.client.put(f"/products/{product_id}", {"title": title, "description": description, "category": category, "price": price})
        return response

    def delete_product_by_id(self, product_id):
        """
        删除一个商品。
        :param product_id: 删除的商品ID。
        :return: 一个包含删除商品信息的字典。
        """
        # 使用self.client属性，调用ApiClient实例的方法，发送HTTP请求。
        response = self.client.delete(f"/products/{product_id}")
        return response



    # def __init__(self):
    #     self.token = self._get_auth_token()
    #     self.client = ApiClient()
    #
    # def _get_auth_token(self):
    #     login_client = ApiClient()
    #     response = login_client.post("/auth/login", {"username": "emilys","password": "emilyspass","expiresInMins": 60})
    #     if response.status_code == 200:
    #         return response.json()["accessToken"]
    #     else:
    #         raise Exception(f"Authentication failed with status code: {response.status_code}")
    #
    #
    # def get_all_products(self):
    #     self.client.set_auth_token(self.token)
    #     response = self.client.get(endpoint="/products")
    #     return response
    #
    # def get_product_by_name(self, product_name):
    #     self.client.set_auth_token(self.token)
    #     response = self.client.get(endpoint=f"/products?q={product_name}")
    #     return response
    #
    # def add_product(self, title, description, category, price):
    #     self.client.set_auth_token(self.token)
    #     response = self.client.post(endpoint="/products/add", data={"title": title, "description": description, "category": category, "price": price})
    #     return response