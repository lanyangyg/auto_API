import yaml
import os


# 这个工具类负责文件读写操作
class DataLoader:
    @staticmethod
    def load_credentials():
        """从YAML文件加载用户凭证"""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        yaml_path = os.path.join(base_dir, "test_data", "user_credentials.yaml")

        with open(yaml_path, 'r') as file:
            return yaml.safe_load(file)

    @staticmethod
    def get_credential_by_username(username):
        """根据用户名获取凭证"""
        credentials = DataLoader.load_credentials()
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