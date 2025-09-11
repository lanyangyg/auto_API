import yaml
import os


# 这个工具类负责文件读写操作
class DataLoader:
    """
    数据加载器类

    用于从YAML配置文件中加载测试数据，特别是用户凭证信息。
    支持加载所有凭证或根据用户名获取特定用户的凭证。
    """
    @staticmethod
    def load_credentials():
        """
        从YAML文件加载用户凭证

        该方法会定位到项目根目录下的 test_data/user_credentials.yaml 文件，
        并将其内容解析为Python对象返回。

        Returns:
            list: 包含多个用户凭证字典的列表，每个字典包含用户名和密码键值对
                  例如: [{"username": "user1", "password": "pass1"}, ...]

        Example:
            credentials = DataLoader.load_credentials()
            # 返回 [{"username": "noahh", "password": "secret123"}, ...]
        """
        # 获取项目根目录路径
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 构建YAML文件的完整路径
        yaml_path = os.path.join(base_dir, "test_data", "user_credentials.yaml")
        # 以只读模式打开YAML文件并安全加载内容
        with open(yaml_path, 'r') as file:
            return yaml.safe_load(file)

    @staticmethod
    def get_credential_by_username(username):
        """
        根据用户名获取凭证

        在所有加载的用户凭证中查找指定用户名的凭证信息。

        Args:
            username (str): 要查找的用户名

        Returns:
            dict or None: 如果找到匹配的用户名，返回包含该用户凭证的字典；
                         如果未找到，返回None

        Example:
            credential = DataLoader.get_credential_by_username("noahh")
            # 返回 {"username": "noahh", "password": "secret123"}
        """
        # 加载所有用户凭证
        credentials = DataLoader.load_credentials()
        # 遍历凭证列表查找匹配的用户名
        for cred in credentials:
            if cred["username"] == username:
                return cred
        return None


# 使用示例
if __name__ == "__main__":
    # 获取所有凭证
    all_creds = DataLoader.load_credentials()
    print(f"加载了 {len(all_creds)} 组凭证")

    # 获取特定用户的凭证
    emily_cred = DataLoader.get_credential_by_username("noahh")
    if emily_cred:
        print(f"Emily的密码: {emily_cred['password']}")