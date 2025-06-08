# 函数进阶示例

# 可变参数 *args
def sum_all(*args):
    """计算所有参数的和"""
    return sum(args)

print(f"1 + 2 + 3 = {sum_all(1, 2, 3)}")
print(f"1 + 2 + 3 + 4 + 5 = {sum_all(1, 2, 3, 4, 5)}")

# 关键字参数 **kwargs
def print_info(**kwargs):
    """打印所有关键字参数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=25, city="北京")

# lambda表达式
square = lambda x: x ** 2
print(f"5的平方：{square(5)}")

# 在排序中使用lambda
students = [
    {"name": "张三", "age": 20},
    {"name": "李四", "age": 18},
    {"name": "王五", "age": 22}
]
sorted_students = sorted(students, key=lambda x: x["age"])
print("按年龄排序：", sorted_students)

# 装饰器
def timer(func):
    """计算函数执行时间的装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间：{end_time - start_time:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    """一个耗时的函数"""
    import time
    time.sleep(1)
    return "完成"

print(slow_function())

# 带参数的装饰器
def repeat(times):
    """重复执行指定次数的装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"你好，{name}！")

greet("张三") 