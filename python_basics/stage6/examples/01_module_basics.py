# 模块基础示例

# 1. 模块的导入方式
import math  # 导入整个模块
from math import sqrt  # 导入特定函数
from math import *  # 导入所有内容（不推荐）
import math as m  # 使用别名

# 2. 模块的搜索路径
import sys
print("Python搜索模块的路径：")
for path in sys.path:
    print(path)

# 3. 模块的命名空间
print("\nmath模块的命名空间：")
print(dir(math))

# 4. 模块的重载
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

# 5. 创建自定义模块
"""
# 在mymodule.py中：
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("This is a module")
"""

# 导入自定义模块
import mymodule
print(mymodule.greet("World"))
print(mymodule.add(1, 2))

# 6. 包内模块的导入
"""
# 在mypackage/__init__.py中：
print("Initializing mypackage")

# 在mypackage/module1.py中：
def func1():
    return "This is func1"

# 在mypackage/module2.py中：
def func2():
    return "This is func2"
"""

# 导入包内模块
from mypackage import module1, module2
print(module1.func1())
print(module2.func2())

# 7. 模块的文档字符串
print("\n模块的文档字符串：")
print(math.__doc__)

# 8. 模块的版本信息
print("\n模块的版本信息：")
print(math.__version__ if hasattr(math, "__version__") else "No version info")

# 9. 模块的缓存
print("\n模块的缓存文件：")
print(math.__cached__ if hasattr(math, "__cached__") else "No cache file")

# 10. 模块的测试
if __name__ == "__main__":
    print("\n运行模块测试：")
    # 测试math模块
    print(f"sqrt(16) = {sqrt(16)}")
    print(f"pi = {math.pi}")
    
    # 测试自定义模块
    print(f"mymodule.greet('Python') = {mymodule.greet('Python')}")
    print(f"mymodule.add(3, 4) = {mymodule.add(3, 4)}") 