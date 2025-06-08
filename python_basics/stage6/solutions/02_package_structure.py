# 包结构练习题参考答案

# 1. 基本包结构
"""
my_package/
    __init__.py
    core.py
    utils.py
    cli.py
"""

# __init__.py
"""
\"\"\"
my_package - 一个示例包
\"\"\"

__version__ = "1.0.0"
__author__ = "Your Name"

from .core import main_function
from .utils import helper_function

__all__ = ["main_function", "helper_function"]
"""

# core.py
"""
def main_function():
    \"\"\"主要功能函数\"\"\"
    return "Hello from main function"

def _internal_function():
    \"\"\"内部使用的函数\"\"\"
    return "Internal function"
"""

# utils.py
"""
def helper_function():
    \"\"\"辅助功能函数\"\"\"
    return "Helper function"

def _private_function():
    \"\"\"私有函数\"\"\"
    return "Private function"
"""

# cli.py
"""
import argparse
from .core import main_function

def main():
    parser = argparse.ArgumentParser(description="My Package CLI")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    if args.verbose:
        print("Running in verbose mode")
    
    result = main_function()
    print(result)

if __name__ == "__main__":
    main()
"""

# 2. 子包结构
"""
my_package/
    __init__.py
    core.py
    utils.py
    cli.py
    subpackage/
        __init__.py
        module1.py
        module2.py
"""

# subpackage/__init__.py
"""
\"\"\"
my_package.subpackage - 子包示例
\"\"\"

from .module1 import function1
from .module2 import function2

__all__ = ["function1", "function2"]
"""

# subpackage/module1.py
"""
def function1():
    \"\"\"子包模块1的功能\"\"\"
    return "Function 1 from subpackage"

def _internal1():
    \"\"\"内部函数\"\"\"
    return "Internal function 1"
"""

# subpackage/module2.py
"""
def function2():
    \"\"\"子包模块2的功能\"\"\"
    return "Function 2 from subpackage"

def _internal2():
    \"\"\"内部函数\"\"\"
    return "Internal function 2"
"""

# 3. 包初始化
class PackageInitializer:
    """包初始化类"""
    def __init__(self):
        self.version = "1.0.0"
        self.author = "Your Name"
        self.description = "A sample package"
    
    def initialize(self):
        """初始化包"""
        print(f"Initializing package version {self.version}")
        print(f"Author: {self.author}")
        print(f"Description: {self.description}")

# 4. 相对导入
"""
# 在subpackage/module1.py中
from ..core import main_function
from ..utils import helper_function

# 在subpackage/module2.py中
from .module1 import function1
from ..core import main_function
"""

# 5. 包级函数
def package_function():
    """包级函数"""
    return "This is a package-level function"

def _package_private_function():
    """包级私有函数"""
    return "This is a private package-level function"

# 6. 包级变量
PACKAGE_VERSION = "1.0.0"
PACKAGE_AUTHOR = "Your Name"
PACKAGE_DESCRIPTION = "A sample package"

# 7. 包级异常
class PackageError(Exception):
    """包级基础异常"""
    pass

class ConfigurationError(PackageError):
    """配置错误异常"""
    pass

class ValidationError(PackageError):
    """验证错误异常"""
    pass

# 8. 包级接口
class PackageInterface:
    """包级接口类"""
    def __init__(self):
        self._initialized = False
    
    def initialize(self):
        """初始化接口"""
        self._initialized = True
    
    def is_initialized(self):
        """检查是否已初始化"""
        return self._initialized
    
    def cleanup(self):
        """清理资源"""
        self._initialized = False

# 9. 包级测试
import unittest

class TestPackage(unittest.TestCase):
    """包级测试类"""
    def setUp(self):
        self.package = PackageInterface()
    
    def test_initialization(self):
        self.assertFalse(self.package.is_initialized())
        self.package.initialize()
        self.assertTrue(self.package.is_initialized())
    
    def test_cleanup(self):
        self.package.initialize()
        self.package.cleanup()
        self.assertFalse(self.package.is_initialized())

# 10. 包级文档
"""
\"\"\"
my_package
=========

一个示例Python包，展示了包结构的最佳实践。

安装
----

使用pip安装::

    pip install my_package

使用
----

基本用法::

    from my_package import main_function
    result = main_function()
    print(result)

命令行使用::

    $ my_package --verbose

功能
----

- 主要功能
- 辅助功能
- 子包功能

开发
----

1. 克隆仓库
2. 安装依赖
3. 运行测试

许可证
------

MIT License
\"\"\"
"""

# 测试代码
if __name__ == "__main__":
    # 测试包初始化
    initializer = PackageInitializer()
    initializer.initialize()
    
    # 测试包级函数
    print(package_function())
    
    # 测试包级异常
    try:
        raise ConfigurationError("Invalid configuration")
    except PackageError as e:
        print(f"Caught package error: {e}")
    
    # 测试包级接口
    package = PackageInterface()
    package.initialize()
    print(f"Package initialized: {package.is_initialized()}")
    
    # 运行单元测试
    unittest.main() 