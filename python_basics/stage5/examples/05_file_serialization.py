# 文件序列化示例

import pickle
import json
import yaml
import xml.etree.ElementTree as ET

# 测试数据
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Pickle序列化
def pickle_example():
    """Pickle序列化示例"""
    # 序列化对象
    person = Person("张三", 25)
    with open("person.pickle", "wb") as f:
        pickle.dump(person, f)
    
    # 反序列化对象
    with open("person.pickle", "rb") as f:
        loaded_person = pickle.load(f)
        print("Pickle加载的对象：", loaded_person)

# JSON序列化
def json_example():
    """JSON序列化示例"""
    # 序列化字典
    data = {
        "name": "李四",
        "age": 30,
        "scores": [85, 90, 95],
        "info": {
            "city": "北京",
            "job": "工程师"
        }
    }
    
    # 写入JSON文件
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    # 读取JSON文件
    with open("data.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        print("\nJSON加载的数据：")
        print(json.dumps(loaded_data, ensure_ascii=False, indent=2))

# YAML序列化
def yaml_example():
    """YAML序列化示例"""
    # 序列化数据
    data = {
        "name": "王五",
        "age": 35,
        "skills": ["Python", "Java", "C++"],
        "projects": [
            {"name": "项目1", "duration": "6个月"},
            {"name": "项目2", "duration": "3个月"}
        ]
    }
    
    # 写入YAML文件
    with open("data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)
    
    # 读取YAML文件
    with open("data.yaml", "r", encoding="utf-8") as f:
        loaded_data = yaml.safe_load(f)
        print("\nYAML加载的数据：")
        print(yaml.dump(loaded_data, allow_unicode=True))

# XML序列化
def xml_example():
    """XML序列化示例"""
    # 创建XML数据
    root = ET.Element("person")
    name = ET.SubElement(root, "name")
    name.text = "赵六"
    age = ET.SubElement(root, "age")
    age.text = "40"
    skills = ET.SubElement(root, "skills")
    for skill in ["Python", "Java", "C++"]:
        skill_elem = ET.SubElement(skills, "skill")
        skill_elem.text = skill
    
    # 写入XML文件
    tree = ET.ElementTree(root)
    tree.write("person.xml", encoding="utf-8", xml_declaration=True)
    
    # 读取XML文件
    tree = ET.parse("person.xml")
    root = tree.getroot()
    print("\nXML加载的数据：")
    print(f"姓名：{root.find('name').text}")
    print(f"年龄：{root.find('age').text}")
    print("技能：")
    for skill in root.findall("skills/skill"):
        print(f"- {skill.text}")

# 清理测试文件
def cleanup():
    """清理测试文件"""
    import os
    files = ["person.pickle", "data.json", "data.yaml", "person.xml"]
    for file in files:
        if os.path.exists(file):
            os.remove(file)

# 执行示例
if __name__ == "__main__":
    pickle_example()
    json_example()
    yaml_example()
    xml_example()
    cleanup() 