import os
from urllib.parse import urljoin
import requests
from utils.logger import log

class ApiClient:
    # 优化ApiClient的健壮性、使其更高效、更通用
    def __init__(self):
        # 从环境变量获取base_url，如果未设置，则使用默认值
        self.base_url = os.environ.get("API_BASE_URL", "https://dummyjson.com")
        # 引入requests.Session: Session对象可以在多个请求之间保持某些参数（如headers），并且会自动处理cookies。
        self.session = requests.Session()   # 实例化requests.Session类
        self.session.headers.update({"Content-Type": "application/json"})   #.headers: 是 Session对象的一个属性（用于读取、添加、修改或删除其中的键值对）

    def set_auth_token(self, token):
        """设置认证token到session的headers中，一次设置，后续请求都有效"""
        # 1.验证 token 是否存在且有效
        # 2.如果有效，就按照 Bearer 认证方案格式化认证信息。
        # 3.将其添加到 session 的全局请求头中，使得后续所有通过此 session 发出的API请求都能自动携带此身份凭证，无需重复设置。
        if token:   # 当token不为空时，设置HTTP请求头
            self.session.headers["Authorization"] = f"Bearer {token}"   # Python的f-string（格式化字符串字面值），可以将变量的值直接嵌入到字符串中。
            log.info("认证Token已设置")
        else:
            log.warning("尝试设置一个空的Token")

    def clear_auth_token(self):
        """清除认证token"""
        # 当请求头有token，则调用del方法删除
        if "Authorization" in self.session.headers:
            del self.session.headers["Authorization"]
            log.info("认证Token已清除")

    # 定义一个_request内部方法，封装requests库的请求方法
    def _request(self, method, endpoint, **kwargs):
        """统一的请求处理方法"""
        # 构建完整的URL, urljoin保证URL拼接的正确性和鲁棒性，避免各种因为斜杠 (/) 带来的潜在问题
        url = urljoin(self.base_url, endpoint)
        log.info(f"请求: {method.upper()} {url}")     # method.upper()在日志中将HTTP方法转换为大写
        if 'json' in kwargs:
            log.info(f"请求体: {kwargs['json']}")      # 日志打印请求体 keys:values

        try:
            # 使用session对象发送请求，传参格式：请求方法，URL，参数kwargs
            response = self.session.request(method, url, **kwargs)
            # 日志只打印部分响应体，避免打印过长的响应体
            log.info(f"响应: {response.status_code} {response.text[:300]}")   # [:300]字符串切片，截取响应体的前300个字符
            # 如果是4xx或5xx状态码，则抛出HTTPError
            response.raise_for_status()
            # 返回响应对象
            return response

        except requests.exceptions.RequestException as e:
            log.error(f"请求发生异常: {e}")
            raise  # 重新抛出异常，让测试框架捕获


    def get(self, endpoint, **kwargs):
        """发送GET请求"""
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, **kwargs):      # data默认值None，等到要使用时传data给到请求体json
        """发送POST请求"""
        return self._request("POST", endpoint, json=data, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        """发送PUT请求"""
        return self._request("PUT", endpoint, json=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        """发送DELETE请求"""
        return self._request("DELETE", endpoint, **kwargs)

    def patch(self, endpoint, data=None, **kwargs):
        """发送PATCH请求"""
        return self._request("PATCH", endpoint, json=data, **kwargs)


    # base_url = "https://dummyjson.com"
    # def __init__(self):
    #     self.headers = {"Content-Type": "application/json"}
    #
    # def get(self, endpoint):
    #     url = self.base_url + endpoint
    #     response = requests.get(url, headers=self.headers)
    #     return response
    #
    #
    # def post(self, endpoint, data):
    #     url = self.base_url + endpoint
    #     response = requests.post(url, headers=self.headers, json=data)
    #     return response
    #
    # def put(self, endpoint, data):
    #     url = self.base_url + endpoint
    #     response = requests.put(url, headers=self.headers, json=data)
    #     return response
    #
    # def delete(self, endpoint):
    #     url = self.base_url + endpoint
    #     response = requests.delete(url, headers=self.headers)
    #     return response
    #
    # def patch(self, endpoint, data):
    #     url = self.base_url + endpoint
    #     response = requests.patch(url, headers=self.headers, json=data)
    #     return response
    #
    # def options(self, endpoint):
    #     url = self.base_url + endpoint
    #     response = requests.options(url, headers=self.headers)
    #     return response
    #
    # # 添加 set_auth_token 和 clear_auth_token 方法来管理认证头
    # def set_auth_token(self, token):
    #     """
    #     设置认证token到headers中
    #     """
    #     self.headers["Authorization"] = f"Bearer {token}"
    #
    # def clear_auth_token(self):
    #     """
    #     清除认证token
    #     """
    #     if "Authorization" in self.headers:
    #         del self.headers["Authorization"]
