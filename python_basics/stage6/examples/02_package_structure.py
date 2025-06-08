# 包结构示例

# 1. 创建包的基本结构
"""
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
"""

# 2. 包的初始化
"""
# mypackage/__init__.py
print("Initializing mypackage")

# 定义包级变量
VERSION = "1.0.0"
AUTHOR = "Your Name"

# 导入子模块
from . import module1
from . import module2

# 定义包级函数
def package_function():
    return "This is a package function"
"""

# 3. 相对导入和绝对导入
"""
# mypackage/module1.py
def func1():
    return "This is func1"

# mypackage/module2.py
from .module1 import func1  # 相对导入
from mypackage.module1 import func1  # 绝对导入

def func2():
    return func1() + " and func2"
"""

# 4. 子包的初始化
"""
# mypackage/subpackage/__init__.py
print("Initializing subpackage")

# mypackage/subpackage/module3.py
def func3():
    return "This is func3"
"""

# 5. 包的导入示例
import mypackage
from mypackage import module1, module2
from mypackage.subpackage import module3

# 使用包级变量和函数
print(f"Package version: {mypackage.VERSION}")
print(f"Package author: {mypackage.AUTHOR}")
print(f"Package function: {mypackage.package_function()}")

# 使用模块函数
print(f"Module1 function: {module1.func1()}")
print(f"Module2 function: {module2.func2()}")
print(f"Module3 function: {module3.func3()}")

# 6. 包的命名空间
print("\n包的命名空间：")
print(dir(mypackage))

# 7. 包的文档字符串
print("\n包的文档字符串：")
print(mypackage.__doc__ if hasattr(mypackage, "__doc__") else "No docstring")

# 8. 包的版本信息
print("\n包的版本信息：")
print(mypackage.__version__ if hasattr(mypackage, "__version__") else "No version info")

# 9. 包的路径
print("\n包的路径：")
print(mypackage.__path__ if hasattr(mypackage, "__path__") else "No path info")

# 10. 包的测试
if __name__ == "__main__":
    print("\n运行包测试：")
    # 测试包级函数
    print(f"mypackage.package_function() = {mypackage.package_function()}")
    
    # 测试模块函数
    print(f"module1.func1() = {module1.func1()}")
    print(f"module2.func2() = {module2.func2()}")
    print(f"module3.func3() = {module3.func3()}")
    
    # 测试包级变量
    print(f"mypackage.VERSION = {mypackage.VERSION}")
    print(f"mypackage.AUTHOR = {mypackage.AUTHOR}") 