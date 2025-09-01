import pytest
from apis.products_api import Products

class TestProduct:

    def test_get_all_products(self):
        products = Products()
        response = products.get_all_products()
        assert response.status_code == 200

    @pytest.mark.parametrize("product_name",["phone","test","python"])
    def test_get_product_by_name(self, product_name):
        products = Products()
        response = products.get_product_by_name(product_name)
        assert response.status_code == 200

    @pytest.mark.parametrize("title, description, category, price",
                             [("phone", "phone description", "phone category", 1000),
                              ("test", "test description", "test category", 2000),
                              ("python", "python description", "python category", 3000)])
    def test_add_product(self, title, description, category, price):
        products = Products()
        response = products.add_product(title=title, description=description, category=category, price=price)
        assert response.status_code == 201