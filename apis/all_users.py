from base.api_client import ApiClient
import yaml
import os

class AllUsers:
    """
    封装获取所有users的请求
    """
    def get_all_users(self):
        """
        获取所有用户信息
        """
        client = ApiClient()        # 这里创建一个原始的、未认证的客户端
        response = client.get("/users?limit=0")
        return response

    def extract_credentials_to_yaml(self, output_path=None):
        """
        提取用户名和密码并保存到YAML文件
        Args:
        output_path (str): YAML文件输出路径，默认为test_data/user_credentials.yaml
        """
        try:
            if output_path is None:
                # 获取项目根目录
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                output_path = os.path.join(base_dir, "test_data", "user_credentials.yaml")

            # 确保输出目录存在
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # 获取用户数据
            response = self.get_all_users()

            if response.status_code == 200:
                data = response.json()
                users = data.get("users", [])

                # 提取用户名和密码
                credentials = []
                for user in users:
                    # 每个用户应该是一个独立的字典
                    user_cred = {
                        "username": user.get("username"),
                        "password": user.get("password")
                    }
                    credentials.append(user_cred)  # 将字典添加到列表中

                # 保存到YAML文件
                with open(output_path, 'w') as file:
                    yaml.dump(credentials, file, default_flow_style=False, allow_unicode=True, sort_keys=False)     # 按规定顺序写入，不按字母顺序重新排序键

                print(f"successfully extract {len(credentials)} credentials to {output_path}")
                return True
            else:
                print(f"get users_data failed: HTTP {response.status_code}")
                return False


        except Exception as e:
            print(f"extract failed: {str(e)}")
            return False