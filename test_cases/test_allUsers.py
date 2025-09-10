from apis.all_users import AllUsers
import pytest
import os
import yaml

class TestAllUsers:
    def test_get_all_users(self):
        """
        测试获取所有用户信息
        """
        all_users = AllUsers()
        response = all_users.get_all_users()
        assert response.status_code == 200


    def test_extract_credentials_to_yaml(self):
        """
        测试提取用户凭证并保存到YAML文件
        """
        all_users = AllUsers()
        # 定义输出路径
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_path = os.path.join(base_dir, "test_data", "user_credentials.yaml")
        # 执行提取操作
        extract_users = all_users.extract_credentials_to_yaml(output_path)

        # 验证操作是否成功
        assert extract_users == True
        # 验证文件是否创建
        assert os.path.exists(output_path)

        # 验证文件内容（使用读取模式）
        with open(output_path, 'r') as file:
            data = yaml.safe_load(file)
            assert len(data) > 0
            assert "username" in data[0]
            assert "password" in data[0]