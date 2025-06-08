# 模块基础练习题参考答案

# 1. 数学模块
def gcd(a, b):
    """计算两个数的最大公约数"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """计算两个数的最小公倍数"""
    return a * b // gcd(a, b)

def is_prime(n):
    """判断一个数是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(start, end):
    """生成指定范围内的质数列表"""
    return [n for n in range(start, end + 1) if is_prime(n)]

def factorial(n):
    """计算一个数的阶乘"""
    if n < 0:
        raise ValueError("阶乘不能计算负数")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 2. 配置模块
import os
import json
import yaml

class Config:
    """配置管理类"""
    def __init__(self):
        self.config = {}
    
    def load_from_env(self):
        """从环境变量加载配置"""
        for key, value in os.environ.items():
            if key.startswith("APP_"):
                self.config[key[4:].lower()] = value
    
    def load_from_json(self, filename):
        """从JSON文件加载配置"""
        with open(filename, "r") as f:
            self.config.update(json.load(f))
    
    def load_from_yaml(self, filename):
        """从YAML文件加载配置"""
        with open(filename, "r") as f:
            self.config.update(yaml.safe_load(f))
    
    def merge_configs(self, *configs):
        """合并多个配置源"""
        for config in configs:
            self.config.update(config)
    
    def validate(self):
        """验证配置的有效性"""
        required_keys = ["database", "api_key", "debug"]
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"缺少必需的配置项: {key}")

# 3. 日志模块
import logging
from logging.handlers import RotatingFileHandler

class Logger:
    """日志管理类"""
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
    
    def setup_console_handler(self, format_str=None):
        """配置控制台输出"""
        handler = logging.StreamHandler()
        if format_str:
            handler.setFormatter(logging.Formatter(format_str))
        self.logger.addHandler(handler)
    
    def setup_file_handler(self, filename, max_bytes=1024*1024, backup_count=5):
        """配置文件输出"""
        handler = RotatingFileHandler(
            filename,
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        self.logger.addHandler(handler)
    
    def setup_format(self, format_str):
        """配置日志格式"""
        for handler in self.logger.handlers:
            handler.setFormatter(logging.Formatter(format_str))
    
    def log(self, level, message):
        """记录日志"""
        self.logger.log(level, message)

# 4. 工具模块
import os
import re
from datetime import datetime
import hashlib

def read_file(filename):
    """读取文件内容"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def write_file(filename, content):
    """写入文件内容"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def clean_string(text):
    """清理字符串"""
    return re.sub(r"\s+", " ", text).strip()

def format_date(date_str, input_format="%Y-%m-%d", output_format="%Y年%m月%d日"):
    """格式化日期"""
    date = datetime.strptime(date_str, input_format)
    return date.strftime(output_format)

def validate_email(email):
    """验证邮箱地址"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def encrypt_password(password):
    """加密密码"""
    return hashlib.sha256(password.encode()).hexdigest()

# 5. 测试模块
import unittest
import pytest
from unittest.mock import Mock, patch

class TestMathUtils(unittest.TestCase):
    """数学工具测试类"""
    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(0, 5), 5)
    
    def test_lcm(self):
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(0, 5), 0)
    
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))
    
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

@pytest.fixture
def config():
    """配置测试夹具"""
    return Config()

def test_config_loading(config):
    """测试配置加载"""
    config.load_from_json("test_config.json")
    assert "test_key" in config.config

# 6. 模块导入示例
"""
# main.py
import math_utils
from config import Config
from logger import Logger
from utils import read_file, write_file

# 使用别名导入
import math_utils as mu
from config import Config as Cfg

# 相对导入
from . import math_utils
from .. import config

# 绝对导入
from mypackage.math_utils import gcd
from mypackage.config import Config
"""

# 7. 模块重载示例
"""
# reload_demo.py
import importlib
import time

def print_time():
    print(time.strftime("%H:%M:%S"))

# 第一次导入
print_time()
time.sleep(2)

# 重载模块
importlib.reload(time)
print_time()
"""

# 8. 模块文档示例
"""
\"\"\"
数学工具模块

这个模块提供了一系列数学计算工具函数，包括：
- 最大公约数计算
- 最小公倍数计算
- 质数判断
- 阶乘计算
\"\"\"

def gcd(a, b):
    \"\"\"
    计算两个数的最大公约数
    
    参数:
        a (int): 第一个数
        b (int): 第二个数
    
    返回:
        int: 最大公约数
    \"\"\"
    while b:
        a, b = b, a % b
    return a
"""

# 9. 模块测试示例
"""
# test_main.py
import unittest
import pytest
from unittest.mock import Mock, patch

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
    
    def test_home_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
    
    @patch("mypackage.utils.get_data")
    def test_data_loading(self, mock_get_data):
        mock_get_data.return_value = {"test": "data"}
        result = self.app.get("/api/data")
        self.assertEqual(result.json, {"test": "data"})

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert square(input) == expected
"""

# 10. 模块打包示例
"""
# setup.py
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.28.0",
        "numpy>=1.21.0",
    ],
    entry_points={
        "console_scripts": [
            "mypackage=mypackage.cli:main",
        ],
    },
)
"""

# 测试代码
if __name__ == "__main__":
    # 测试数学模块
    print(f"GCD of 12 and 18: {gcd(12, 18)}")
    print(f"LCM of 12 and 18: {lcm(12, 18)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Factorial of 5: {factorial(5)}")
    
    # 测试配置模块
    config = Config()
    config.load_from_env()
    print(f"Config: {config.config}")
    
    # 测试日志模块
    logger = Logger("test")
    logger.setup_console_handler()
    logger.log(logging.INFO, "Test log message")
    
    # 测试工具模块
    print(f"Clean string: {clean_string('  hello   world  ')}")
    print(f"Formatted date: {format_date('2023-01-01')}")
    print(f"Valid email? {validate_email('test@example.com')}")
    
    # 运行单元测试
    unittest.main() 