# 字符串示例

# 字符串基本操作
s = "Hello, World!"
print(f"原始字符串: {s}")
print(f"长度: {len(s)}")
print(f"大写: {s.upper()}")
print(f"小写: {s.lower()}")
print(f"首字母大写: {s.capitalize()}")

# 字符串切片
print(f"前5个字符: {s[:5]}")
print(f"后6个字符: {s[-6:]}")
print(f"反转字符串: {s[::-1]}")

# 字符串方法
print(f"查找'World': {s.find('World')}")
print(f"替换'World'为'Python': {s.replace('World', 'Python')}")
print(f"分割字符串: {s.split(',')}")
print(f"去除空格: {'  Hello  '.strip()}")

# 字符串格式化
name = "Alice"
age = 25
print(f"我叫{name}，今年{age}岁")
print("我叫{}，今年{}岁".format(name, age))
print("我叫%s，今年%d岁" % (name, age))

# 字符串连接
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
print(" ".join([s1, s2])) 