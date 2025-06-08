# 字典示例

# 字典创建和访问
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"原始字典: {person}")
print(f"姓名: {person['name']}")
print(f"年龄: {person['age']}")

# 字典操作
# 添加/修改键值对
person["job"] = "Engineer"
print(f"添加工作后: {person}")
person["age"] = 26
print(f"修改年龄后: {person}")

# 删除键值对
del person["city"]
print(f"删除城市后: {person}")
age = person.pop("age")
print(f"弹出年龄: {age}")
print(f"弹出后字典: {person}")

# 字典方法
print(f"所有键: {list(person.keys())}")
print(f"所有值: {list(person.values())}")
print(f"所有键值对: {list(person.items())}")

# 字典推导式
squares = {x: x**2 for x in range(5)}
print(f"平方字典: {squares}")

# 字典嵌套
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(f"嵌套字典: {nested_dict}")
print(f"访问嵌套值: {nested_dict['person1']['name']}")

# 字典合并
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(f"合并后的字典: {merged_dict}")

# 字典的get方法
print(f"获取不存在的键: {person.get('phone', 'Not found')}") 