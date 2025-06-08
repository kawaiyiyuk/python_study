# 输入输出示例

# 基本输入
name = input("请输入您的名字：")
age = input("请输入您的年龄：")

# 格式化输出
# 1. f-string（推荐）
print(f"您好，{name}，您今年{age}岁了")

# 2. format方法
print("您好，{}，您今年{}岁了".format(name, age))

# 3. %运算符
print("您好，%s，您今年%s岁了" % (name, age))

# 数字格式化
pi = 3.14159
print(f"π的值是：{pi:.2f}")  # 保留两位小数
print("π的值是：{:.2f}".format(pi))
print("π的值是：%.2f" % pi) 