# 条件语句示例

# 基本if语句
age = 18
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# if-elif-else结构
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 嵌套if语句
age = 20
if age >= 18:
    if age >= 60:
        print("老年人")
    else:
        print("青年人")
else:
    print("未成年人")

# 条件表达式（三元运算符）
age = 20
status = "成年人" if age >= 18 else "未成年人"
print(status) 