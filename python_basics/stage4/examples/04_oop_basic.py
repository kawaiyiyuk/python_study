# 面向对象编程基础示例

# 基本类定义
class Person:
    """人类"""
    
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """自我介绍"""
        return f"我叫{self.name}，今年{self.age}岁"

# 创建对象
person = Person("张三", 25)
print(person.introduce())

# 继承
class Student(Person):
    """学生类"""
    
    def __init__(self, name, age, student_id):
        """初始化方法"""
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        """学习"""
        return f"{self.name}正在学习"
    
    def introduce(self):
        """重写自我介绍方法"""
        return f"{super().introduce()}，学号是{self.student_id}"

# 创建学生对象
student = Student("李四", 20, "2023001")
print(student.introduce())
print(student.study())

# 多态
class Teacher(Person):
    """教师类"""
    
    def __init__(self, name, age, subject):
        """初始化方法"""
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        """教学"""
        return f"{self.name}正在教授{self.subject}"
    
    def introduce(self):
        """重写自我介绍方法"""
        return f"{super().introduce()}，教授{self.subject}"

# 创建教师对象
teacher = Teacher("王五", 35, "Python")
print(teacher.introduce())
print(teacher.teach())

# 特殊方法
class Vector:
    """向量类"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """向量加法"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """相等比较"""
        return self.x == other.x and self.y == other.y

# 使用向量类
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")
print(f"v1 == v2: {v1 == v2}")

# 属性装饰器
class Circle:
    """圆类"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """半径属性"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value
    
    @property
    def area(self):
        """面积属性"""
        import math
        return math.pi * self._radius ** 2

# 使用圆类
circle = Circle(5)
print(f"圆的半径：{circle.radius}")
print(f"圆的面积：{circle.area:.2f}")
circle.radius = 10
print(f"新的半径：{circle.radius}")
print(f"新的面积：{circle.area:.2f}") 