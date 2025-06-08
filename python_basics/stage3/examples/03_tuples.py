# 元组示例

# 元组创建和访问
t = (1, 2, 3, 4, 5)
print(f"原始元组: {t}")
print(f"第一个元素: {t[0]}")
print(f"最后一个元素: {t[-1]}")
print(f"切片: {t[1:4]}")

# 元组特点
# 元组是不可变的
try:
    t[0] = 10
except TypeError as e:
    print(f"错误: {e}")

# 元组解包
x, y, z = (1, 2, 3)
print(f"解包: x={x}, y={y}, z={z}")

# 元组方法
print(f"元组长度: {len(t)}")
print(f"元素2的索引: {t.index(2)}")
print(f"元素2出现的次数: {t.count(2)}")

# 元组嵌套
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(f"嵌套元组: {nested_tuple}")
print(f"访问嵌套元素: {nested_tuple[0][1]}")

# 元组和列表的转换
lst = [1, 2, 3]
t_from_list = tuple(lst)
print(f"列表转元组: {t_from_list}")

t = (1, 2, 3)
lst_from_tuple = list(t)
print(f"元组转列表: {lst_from_tuple}")

# 元组作为字典键
d = {(1, 2): "value"}
print(f"元组作为键: {d}") 