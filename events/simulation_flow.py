from apis.users_api import User
from apis.products_api import Products
from apis.carts_api import Carts


class Simulation:
    """
    模拟流程
    """
    # 实例化底层的API封装类
    def __init__(self, api_client):
        self.user_api = User(api_client)
        self.product_api = Products(api_client)
        self.carts_api = Carts(api_client)

    def perform_complete_flow(self, product_name, product_quantity):
        """
        执行一个完整的模拟流程 (这就是一个'event'或'workflow')。
        这个方法封装了所有必要的底层API调用和逻辑。
        """
        current_user = self.user_api.get_current_user()
        user_id = current_user.json()["id"]

        target_product = self.product_api.get_product_by_name(product_name)

        # 检查是否找到了产品
        products = target_product.json()["products"]    #提取产品products对象的数组
        if not products:
            raise ValueError(f"未找到名为 '{product_name}' 的产品")

        # 获取数组中第一个匹配产品的ID
        target_product_id = products[0]["id"]

        # 创建产品列表
        products_list = [
            {
                "id": target_product_id,
                "quantity": product_quantity
            }
        ]

        carts_response = self.carts_api.add_cart(user_id, products_list)
        carts_id = carts_response.json()["id"]

        # 返回一个包含关键信息的字典，方便测试用例断言
        return {
            "carts_status": carts_response.status_code,
            "carts_id": carts_id
        }