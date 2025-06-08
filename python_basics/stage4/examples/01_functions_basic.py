# 函数基础示例

# 基本函数定义和调用
def greet(name):
    """
    向指定的人打招呼
    参数:
        name: 要打招呼的人名
    返回:
        打招呼的字符串
    """
    return f"你好，{name}！"

# 调用函数
print(greet("张三"))

# 多参数函数
def add(a, b):
    """计算两个数的和"""
    return a + b

print(f"1 + 2 = {add(1, 2)}")

# 带默认参数的函数
def greet_with_title(name, title="先生"):
    """带称谓的打招呼"""
    return f"你好，{title}{name}！"

print(greet_with_title("李四"))
print(greet_with_title("王五", "女士"))

# 返回多个值
def get_circle_info(radius):
    """计算圆的周长和面积"""
    import math
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

circ, area = get_circle_info(5)
print(f"圆的周长：{circ:.2f}")
print(f"圆的面积：{area:.2f}")

# 作用域示例
x = 10  # 全局变量

def test_scope():
    y = 20  # 局部变量
    print(f"函数内 x = {x}")
    print(f"函数内 y = {y}")

test_scope()
print(f"函数外 x = {x}")
# print(f"函数外 y = {y}")  # 这行会报错，因为y是局部变量 