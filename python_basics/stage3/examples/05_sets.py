# 集合示例

# 集合创建和基本操作
s = {1, 2, 3, 4, 5}
print(f"原始集合: {s}")

# 添加元素
s.add(6)
print(f"添加元素后: {s}")
s.update([7, 8, 9])
print(f"更新多个元素后: {s}")

# 删除元素
s.remove(1)
print(f"删除元素后: {s}")
s.discard(10)  # 安全删除，不存在的元素不会报错
print(f"安全删除后: {s}")
popped = s.pop()
print(f"弹出元素: {popped}")
print(f"弹出后集合: {s}")

# 集合运算
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"并集: {a | b}")
print(f"交集: {a & b}")
print(f"差集: {a - b}")
print(f"对称差集: {a ^ b}")

# 集合方法
print(f"集合长度: {len(a)}")
print(f"是否包含元素: {2 in a}")
print(f"是否为子集: {a.issubset(b)}")
print(f"是否为超集: {a.issuperset(b)}")

# 集合推导式
squares = {x**2 for x in range(5)}
print(f"平方集合: {squares}")

# 集合去重
lst = [1, 2, 2, 3, 3, 3]
unique = set(lst)
print(f"去重后的列表: {list(unique)}")

# 不可变集合
fs = frozenset([1, 2, 3, 4, 5])
print(f"不可变集合: {fs}") 