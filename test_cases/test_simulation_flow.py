from events.simulation_flow import Simulation
import pytest

@pytest.fixture     # 没有指定 scope，默认为 "function"
def simulation_workflow(api_client):
    return Simulation(api_client)

class TestSimulation:

    @pytest.mark.parametrize("product_name, product_quantity",[
        ("pen", 1),
        ("phone", 2)])
    def test_simulation_flow(self, simulation_workflow, product_name, product_quantity):
        # 这个测试函数会获得一个独立的 simulation_workflow 实例
        # product_name = "pen"
        # product_quantity = 1
        result = simulation_workflow.perform_complete_flow(product_name, product_quantity)
        # 断言业务层面的结果
        assert result["carts_status"] == 201
        assert "carts_id" in result