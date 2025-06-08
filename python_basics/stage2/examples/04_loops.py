# 循环语句示例

# for循环
print("for循环示例：")
for i in range(5):
    print(f"当前数字：{i}")

# while循环
print("\nwhile循环示例：")
count = 0
while count < 5:
    print(f"当前计数：{count}")
    count += 1

# break示例
print("\nbreak示例：")
for i in range(10):
    if i == 5:
        break
    print(f"当前数字：{i}")

# continue示例
print("\ncontinue示例：")
for i in range(5):
    if i == 2:
        continue
    print(f"当前数字：{i}")

# 嵌套循环
print("\n嵌套循环示例：")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 带else的循环
print("\n带else的循环示例：")
for i in range(5):
    print(f"当前数字：{i}")
else:
    print("循环正常结束") 