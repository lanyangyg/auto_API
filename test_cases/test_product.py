import allure
import pytest
from apis.products_api import Products

# rebuild class TestProduct
@allure.feature("---Products Module---")
class TestProduct:

    @pytest.fixture(scope="class")
    def product_api(self, api_client):
        # 实例化并返回Products类，这里类包含 api_client
        return Products(api_client)

    @pytest.mark.run(order=1)
    @allure.title("products list")
    def test_get_all_products(self, product_api):
        # product_api --> Products(api_client) --> class Products 中的 self.client = api_client --> self.client.get()
        response = product_api.get_all_products()
        assert response.status_code == 200


    @pytest.mark.run(order=2)
    @allure.title("search product")
    @pytest.mark.parametrize("product_name",["phone","test","apple"])
    def test_get_product_by_name(self, product_api, product_name):
        response = product_api.get_product_by_name(product_name)
        assert response.status_code == 200


    @pytest.mark.run(order=3)
    @allure.title("add product")
    @pytest.mark.parametrize("title, description, category, price",
                          [("phone", "phone description", "phone category", 1000),
                           ("test", "test description", "test category", 2000),
                           ("python", "python description", "python category", 3000)])
    def test_add_product(self, product_api, title, description, category, price):
        response = product_api.add_product(title, description, category, price)
        assert response.status_code == 201


    @pytest.mark.run(order=4)
    @allure.title("delete product")
    @pytest.mark.parametrize("product_id",[1,2,3])
    def test_delete_product_by_id(self, product_api, product_id):
        response = product_api.delete_product_by_id(product_id)
        assert response.status_code == 200
        assert response.json()["id"] == product_id


    #
    # def test_get_all_products(self):
    #     products = Products()
    #     response = products.get_all_products()
    #     assert response.status_code == 200
    #
    # @pytest.mark.parametrize("product_name",["phone","test","python"])
    # def test_get_product_by_name(self, product_name):
    #     products = Products()
    #     response = products.get_product_by_name(product_name)
    #     assert response.status_code == 200
    #
    # @pytest.mark.parametrize("title, description, category, price",
    #                          [("phone", "phone description", "phone category", 1000),
    #                           ("test", "test description", "test category", 2000),
    #                           ("python", "python description", "python category", 3000)])
    # def test_add_product(self, title, description, category, price):
    #     products = Products()
    #     response = products.add_product(title=title, description=description, category=category, price=price)
    #     assert response.status_code == 201