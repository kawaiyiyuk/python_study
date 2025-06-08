# 列表示例

# 列表创建和访问
numbers = [1, 2, 3, 4, 5]
print(f"原始列表: {numbers}")
print(f"第一个元素: {numbers[0]}")
print(f"最后一个元素: {numbers[-1]}")
print(f"切片: {numbers[1:4]}")

# 列表操作
# 添加元素
numbers.append(6)
print(f"添加元素后: {numbers}")
numbers.insert(0, 0)
print(f"插入元素后: {numbers}")

# 删除元素
numbers.pop()
print(f"删除最后一个元素后: {numbers}")
numbers.remove(3)
print(f"删除元素3后: {numbers}")

# 列表方法
print(f"列表长度: {len(numbers)}")
print(f"元素2的索引: {numbers.index(2)}")
print(f"元素2出现的次数: {numbers.count(2)}")

# 列表排序
numbers.sort()
print(f"排序后: {numbers}")
numbers.reverse()
print(f"反转后: {numbers}")

# 列表推导式
squares = [x**2 for x in range(5)]
print(f"平方数列表: {squares}")

# 列表嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"矩阵: {matrix}")
print(f"矩阵[1][1]: {matrix[1][1]}")

# 列表解包
a, b, c = [1, 2, 3]
print(f"解包: a={a}, b={b}, c={c}") 