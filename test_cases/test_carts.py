import pytest
from apis.carts_api import Carts


class TestCarts:
    @pytest.fixture(scope="class")
    def carts_api(self, api_client):
        return Carts(api_client)


    def test_get_all_carts(self, carts_api):
        response = carts_api.get_all_carts()
        assert response.status_code == 200


    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_carts_by_user_id(self, carts_api, user_id):
        response = carts_api.get_carts_by_user_id(user_id)
        assert response.status_code == 200


    @pytest.mark.parametrize("user_id, products", [
        (2, [{"id": 2, "quantity": 3}]),
        (3, [{"id": 3, "quantity": 1}]),
        (4, [{"id": 4, "quantity": 2}]),
    ])
    def test_add_cart(self, carts_api, user_id, products):
        """
        添加购物车
        :param user_id: 用户ID
        :param products: 产品列表，格式为 [{"id": 1, "quantity": 1}, ...]
        :return: API响应
        """
        response = carts_api.add_cart(user_id, products)
        assert response.status_code == 201

    @pytest.mark.parametrize("carts_id, product_id, quantity", [
        (1, 1, 3),
        (2, 2, 3),
        (3, 3, 1)
    ])
    def test_update_cart_by_carts_id(self, carts_api, carts_id, product_id, quantity):
        response = carts_api.update_cart_by_carts_id(carts_id, product_id, quantity)
        assert response.status_code == 200


    @pytest.mark.parametrize("carts_id", [1, 2, 3])
    def test_delete_cart_by_carts_id(self, carts_api, carts_id):
        response = carts_api.delete_cart_by_carts_id(carts_id)
        assert response.status_code == 200





    # @pytest.mark.parametrize("user_id, product_id, quantity", [
    #     (1, 1, 1),
    #     (2, 2, 2),
    #     (3, 3, 3)
    # ])
    # def test_add_cart(self, carts_api, user_id, product_id, quantity):
    #     response = carts_api.add_cart(user_id, product_id, quantity)
    #     assert response.status_code == 200
    #     assert response.json()["id"] > 0
    #
    # @pytest.mark.parametrize()