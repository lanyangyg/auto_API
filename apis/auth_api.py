from base.api_client import ApiClient
# from utils.data_loader import DataLoader
from typing import List, Dict       # 写类型注解，不影响运行结果
import yaml
import os
from concurrent.futures import ThreadPoolExecutor


class Auth:
    def login(self, username: str, password: str) -> Dict:      # 代表接收字符串返回字典
        """
        封装处理单个用户的登录请求
        这个方法接收明确的用户名和密码参数，不读取yaml文件
        """
        # 优化后具有高复用性：
        # 这个 login 方法现在可以在任何地方被调用，无论是为了在 conftest.py 中获取一个有效token，还是为了在 test_login.py 中测试一个失败场景。
        client = ApiClient()        # 这里创建一个原始的、未认证的客户端
        response = client.post("/auth/login", {"username":username, "password":password})
        return response     # 返回原始响应对象


    def get_all_users_token(self, output_path: str = None, max_workers: int = 10) -> List[Dict]:
        """多线程获取所有用户token"""
        # 设置输出路径
        if output_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            output_path = os.path.join(base_dir, "test_data", "users_token.yaml")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 加载用户凭证
        from utils.data_loader import DataLoader
        credentials = DataLoader.load_credentials()
        total_users = len(credentials)
        print(f"开始获取 {total_users} 个用户的token（并发数：{max_workers}）")

        # 准备结果存储
        tokens = []
        failed = []

        # 单线程处理函数
        def process_user(cred):
            # 登录并返回结果
            try:
                response = self.login(cred["username"], cred["password"])
                if response.status_code == 200:
                    token = response.json().get("accessToken")
                    if token:
                        return {"username": cred["username"], "accessToken": token}
                    else:
                        return {"username": cred["username"], "error": "缺少accessToken字段"}
                else:
                    return {"username": cred["username"], "error": f"HTTP {response.status_code}"}
            except Exception as e:
                return {"username": cred["username"], "error": str(e)}

        # 并发执行
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(process_user, credentials))

        # 处理结果
        for result in results:
            if "accessToken" in result:
                tokens.append(result)   # 成功结果
            else:
                failed.append(result)   # 失败结果

        # 保存结果
        with open(output_path, 'w') as file:
            yaml.dump(tokens, file, default_flow_style=False, allow_unicode=True, sort_keys=False)   # 保存成功token

        # 打印统计信息
        success = len(tokens)
        print(f"完成! 成功: {success}, 失败: {len(failed)}")

        # 可选：保存错误信息
        if failed:
            error_path = output_path.replace(".yaml", "_errors.yaml")
            with open(error_path, 'w') as file:
                yaml.dump(failed, file, default_flow_style=False, allow_unicode=True, sort_keys=False)
            print(f"失败详情已保存到 {error_path}")

        print(f"结果已保存到 {output_path}")
        return tokens

    #
    # def get_all_users_token(self, output_path: str = None, delay: float = 0.1, max_workers: int = 10) -> List[Dict]:
    #     """
    #     批量获取所有用户的token - 修改字段映射逻辑
    #     从user_credentials.yaml读取数据，调用login方法，处理accessToken字段
    #     Args:
    #         output_path (str): token输出文件路径，默认为test_data/user_tokens.yaml
    #         delay (float): 请求之间的延迟时间（秒），避免服务器压力过大
    #     Returns:    成功时返回包含accessToken的字典，失败时返回None
    #     """
    #     if output_path is None:
    #         # 获取项目根目录
    #         base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #         output_path = os.path.join(base_dir, "test_data", "users_token.yaml")
    #
    #     # 确保输出目录存在
    #     os.makedirs(os.path.dirname(output_path), exist_ok=True)
    #
    #     # 加载用户凭证
    #     credentials = DataLoader.load_credentials()
    #     print(f"调试: 加载的凭证数量 = {len(credentials)}")  # 添加调试信息
    #
    #     # 存储token结果
    #     tokens = []
    #     failed_attempts = []
    #
    #     print(f"开始获取 {len(credentials)} 个用户的token...")
    #     for i, cred in enumerate(credentials, 1):
    #         username = cred["username"]
    #         password = cred["password"]
    #
    #         if delay > 0 and i > 1:
    #             time.sleep(delay)
    #
    #         try:
    #             response = self.login(username, password)
    #
    #             if response.status_code == 200:
    #                 access_token = response.json().get("accessToken")
    #                 if access_token:
    #                     tokens.append({"username": username, "accessToken": access_token})
    #                     print(f"({i}/{len(credentials)}) {username} token获取成功")
    #                 else:
    #                     failed_attempts.append({
    #                         "username": username,
    #                         "error": "响应中缺少accessToken字段",
    #                         "response": response.text
    #                     })
    #             else:
    #                 failed_attempts.append({
    #                     "username": username,
    #                     "error": f"HTTP {response.status_code}",
    #                     "response": response.text
    #                 })
    #         except Exception as e:
    #             failed_attempts.append({
    #                 "username": username,
    #                 "error": str(e),
    #                 "response": None
    #             })
    #
    #     # 循环结束后统一保存
    #     with open(output_path, 'w') as file:
    #         yaml.dump(tokens, file, default_flow_style=False, allow_unicode=True, sort_keys=False)
    #
    #     if failed_attempts:
    #         error_path = output_path.replace(".yaml", "_errors.yaml")
    #         with open(error_path, 'w') as file:
    #             yaml.dump(failed_attempts, file, default_flow_style=False, allow_unicode=True, sort_keys=False)
    #         print(f"失败: {len(failed_attempts)} 个用户")
    #
    #     print(f"成功: {len(tokens)} 个用户token已保存到 {output_path}")
    #     return tokens