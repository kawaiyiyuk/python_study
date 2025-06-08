# 文件序列化练习题参考答案

import pickle
import json
import yaml
import xml.etree.ElementTree as ET
from datetime import datetime
import csv
import os

def object_serializer(obj, format_type='pickle'):
    """
    对象序列化器
    :param obj: 要序列化的对象
    :param format_type: 序列化格式（pickle/json/yaml/xml）
    """
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return obj.__dict__
    
    try:
        if format_type == 'pickle':
            # Pickle序列化
            with open('object.pickle', 'wb') as f:
                pickle.dump(obj, f)
            return 'object.pickle'
        
        elif format_type == 'json':
            # JSON序列化
            with open('object.json', 'w', encoding='utf-8') as f:
                json.dump(obj, f, cls=CustomEncoder, ensure_ascii=False, indent=4)
            return 'object.json'
        
        elif format_type == 'yaml':
            # YAML序列化
            with open('object.yaml', 'w', encoding='utf-8') as f:
                yaml.dump(obj, f, allow_unicode=True)
            return 'object.yaml'
        
        elif format_type == 'xml':
            # XML序列化
            root = ET.Element('object')
            for key, value in obj.__dict__.items():
                child = ET.SubElement(root, key)
                child.text = str(value)
            
            tree = ET.ElementTree(root)
            tree.write('object.xml', encoding='utf-8', xml_declaration=True)
            return 'object.xml'
        
        else:
            raise ValueError(f"不支持的序列化格式：{format_type}")
    
    except Exception as e:
        print(f"序列化过程中发生错误：{str(e)}")
        return None

def config_manager(config_file):
    """
    配置文件管理器
    :param config_file: 配置文件路径
    """
    class ConfigManager:
        def __init__(self, config_file):
            self.config_file = config_file
            self.config = self._load_config()
        
        def _load_config(self):
            """加载配置文件"""
            if not os.path.exists(self.config_file):
                return {}
            
            ext = os.path.splitext(self.config_file)[1].lower()
            try:
                if ext == '.json':
                    with open(self.config_file, 'r', encoding='utf-8') as f:
                        return json.load(f)
                elif ext == '.yaml':
                    with open(self.config_file, 'r', encoding='utf-8') as f:
                        return yaml.safe_load(f)
                elif ext == '.xml':
                    tree = ET.parse(self.config_file)
                    root = tree.getroot()
                    return self._xml_to_dict(root)
                else:
                    raise ValueError(f"不支持的配置文件格式：{ext}")
            except Exception as e:
                print(f"加载配置文件时发生错误：{str(e)}")
                return {}
        
        def _xml_to_dict(self, element):
            """将XML元素转换为字典"""
            result = {}
            for child in element:
                if len(child) > 0:
                    result[child.tag] = self._xml_to_dict(child)
                else:
                    result[child.tag] = child.text
            return result
        
        def _save_config(self):
            """保存配置文件"""
            ext = os.path.splitext(self.config_file)[1].lower()
            try:
                if ext == '.json':
                    with open(self.config_file, 'w', encoding='utf-8') as f:
                        json.dump(self.config, f, ensure_ascii=False, indent=4)
                elif ext == '.yaml':
                    with open(self.config_file, 'w', encoding='utf-8') as f:
                        yaml.dump(self.config, f, allow_unicode=True)
                elif ext == '.xml':
                    root = ET.Element('config')
                    self._dict_to_xml(self.config, root)
                    tree = ET.ElementTree(root)
                    tree.write(self.config_file, encoding='utf-8', xml_declaration=True)
            except Exception as e:
                print(f"保存配置文件时发生错误：{str(e)}")
        
        def _dict_to_xml(self, data, parent):
            """将字典转换为XML元素"""
            for key, value in data.items():
                child = ET.SubElement(parent, key)
                if isinstance(value, dict):
                    self._dict_to_xml(value, child)
                else:
                    child.text = str(value)
        
        def get(self, key, default=None):
            """获取配置项"""
            return self.config.get(key, default)
        
        def set(self, key, value):
            """设置配置项"""
            self.config[key] = value
            self._save_config()
        
        def delete(self, key):
            """删除配置项"""
            if key in self.config:
                del self.config[key]
                self._save_config()
        
        def merge(self, other_config):
            """合并配置"""
            self.config.update(other_config)
            self._save_config()
    
    return ConfigManager(config_file)

def data_converter(source_file, target_file):
    """
    数据转换器
    :param source_file: 源文件路径
    :param target_file: 目标文件路径
    """
    def detect_format(file_path):
        """检测文件格式"""
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.json':
            return 'json'
        elif ext == '.yaml':
            return 'yaml'
        elif ext == '.xml':
            return 'xml'
        elif ext == '.csv':
            return 'csv'
        else:
            raise ValueError(f"不支持的文件格式：{ext}")
    
    def read_data(file_path):
        """读取数据"""
        format_type = detect_format(file_path)
        try:
            if format_type == 'json':
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            elif format_type == 'yaml':
                with open(file_path, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f)
            elif format_type == 'xml':
                tree = ET.parse(file_path)
                root = tree.getroot()
                return xml_to_dict(root)
            elif format_type == 'csv':
                data = []
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        data.append(dict(row))
                return data
        except Exception as e:
            print(f"读取文件时发生错误：{str(e)}")
            return None
    
    def write_data(data, file_path):
        """写入数据"""
        format_type = detect_format(file_path)
        try:
            if format_type == 'json':
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            elif format_type == 'yaml':
                with open(file_path, 'w', encoding='utf-8') as f:
                    yaml.dump(data, f, allow_unicode=True)
            elif format_type == 'xml':
                root = ET.Element('data')
                dict_to_xml(data, root)
                tree = ET.ElementTree(root)
                tree.write(file_path, encoding='utf-8', xml_declaration=True)
            elif format_type == 'csv':
                with open(file_path, 'w', encoding='utf-8', newline='') as f:
                    if data and isinstance(data, list):
                        writer = csv.DictWriter(f, fieldnames=data[0].keys())
                        writer.writeheader()
                        writer.writerows(data)
        except Exception as e:
            print(f"写入文件时发生错误：{str(e)}")
    
    def xml_to_dict(element):
        """XML转字典"""
        result = {}
        for child in element:
            if len(child) > 0:
                result[child.tag] = xml_to_dict(child)
            else:
                result[child.tag] = child.text
        return result
    
    def dict_to_xml(data, parent):
        """字典转XML"""
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, key)
                dict_to_xml(value, child)
        elif isinstance(data, list):
            for item in data:
                child = ET.SubElement(parent, 'item')
                dict_to_xml(item, child)
        else:
            parent.text = str(data)
    
    # 执行转换
    data = read_data(source_file)
    if data is not None:
        write_data(data, target_file)
        print(f"数据转换完成：")
        print(f"源文件：{source_file}")
        print(f"目标文件：{target_file}")

def object_persistence(obj, storage_dir):
    """
    对象持久化
    :param obj: 要持久化的对象
    :param storage_dir: 存储目录
    """
    class PersistentObject:
        def __init__(self, obj, storage_dir):
            self.obj = obj
            self.storage_dir = storage_dir
            self.version = 1
            self._ensure_storage_dir()
        
        def _ensure_storage_dir(self):
            """确保存储目录存在"""
            os.makedirs(self.storage_dir, exist_ok=True)
        
        def save(self):
            """保存对象"""
            try:
                # 创建版本目录
                version_dir = os.path.join(self.storage_dir, f"v{self.version}")
                os.makedirs(version_dir, exist_ok=True)
                
                # 保存对象数据
                with open(os.path.join(version_dir, 'object.pickle'), 'wb') as f:
                    pickle.dump(self.obj, f)
                
                # 保存元数据
                metadata = {
                    'version': self.version,
                    'timestamp': datetime.now().isoformat(),
                    'class': self.obj.__class__.__name__
                }
                with open(os.path.join(version_dir, 'metadata.json'), 'w') as f:
                    json.dump(metadata, f, indent=4)
                
                self.version += 1
                print(f"对象已保存，版本：{self.version-1}")
            
            except Exception as e:
                print(f"保存对象时发生错误：{str(e)}")
        
        def load(self, version=None):
            """加载对象"""
            try:
                if version is None:
                    # 加载最新版本
                    versions = [int(d[1:]) for d in os.listdir(self.storage_dir) if d.startswith('v')]
                    if not versions:
                        raise ValueError("没有找到已保存的版本")
                    version = max(versions)
                
                version_dir = os.path.join(self.storage_dir, f"v{version}")
                if not os.path.exists(version_dir):
                    raise ValueError(f"版本 {version} 不存在")
                
                # 加载对象数据
                with open(os.path.join(version_dir, 'object.pickle'), 'rb') as f:
                    self.obj = pickle.load(f)
                
                print(f"已加载版本 {version} 的对象")
                return self.obj
            
            except Exception as e:
                print(f"加载对象时发生错误：{str(e)}")
                return None
        
        def list_versions(self):
            """列出所有版本"""
            try:
                versions = []
                for d in os.listdir(self.storage_dir):
                    if d.startswith('v'):
                        version_dir = os.path.join(self.storage_dir, d)
                        metadata_file = os.path.join(version_dir, 'metadata.json')
                        if os.path.exists(metadata_file):
                            with open(metadata_file, 'r') as f:
                                metadata = json.load(f)
                                versions.append(metadata)
                return sorted(versions, key=lambda x: x['version'])
            
            except Exception as e:
                print(f"列出版本时发生错误：{str(e)}")
                return []
    
    return PersistentObject(obj, storage_dir)

def data_validator(data, schema):
    """
    数据验证器
    :param data: 要验证的数据
    :param schema: 验证模式
    """
    class DataValidator:
        def __init__(self, data, schema):
            self.data = data
            self.schema = schema
            self.errors = []
        
        def validate(self):
            """验证数据"""
            self.errors = []
            self._validate_data(self.data, self.schema)
            return len(self.errors) == 0
        
        def _validate_data(self, data, schema, path=''):
            """递归验证数据"""
            if isinstance(schema, dict):
                if not isinstance(data, dict):
                    self.errors.append(f"{path}: 期望字典类型，实际为 {type(data).__name__}")
                    return
                
                # 验证必需字段
                for key, value in schema.items():
                    if key.startswith('required_'):
                        field = key[9:]
                        if field not in data:
                            self.errors.append(f"{path}: 缺少必需字段 '{field}'")
                
                # 验证字段类型和值
                for key, value in data.items():
                    if key in schema:
                        self._validate_data(value, schema[key], f"{path}.{key}")
            
            elif isinstance(schema, list):
                if not isinstance(data, list):
                    self.errors.append(f"{path}: 期望列表类型，实际为 {type(data).__name__}")
                    return
                
                # 验证列表元素
                for i, item in enumerate(data):
                    self._validate_data(item, schema[0], f"{path}[{i}]")
            
            elif isinstance(schema, type):
                if not isinstance(data, schema):
                    self.errors.append(f"{path}: 期望 {schema.__name__} 类型，实际为 {type(data).__name__}")
        
        def get_errors(self):
            """获取验证错误"""
            return self.errors
        
        def fix_errors(self):
            """修复常见错误"""
            fixed_data = self.data.copy()
            
            for error in self.errors:
                if "期望字典类型" in error:
                    # 将非字典类型转换为字典
                    path = error.split(':')[0]
                    self._set_value(fixed_data, path, {})
                
                elif "期望列表类型" in error:
                    # 将非列表类型转换为列表
                    path = error.split(':')[0]
                    self._set_value(fixed_data, path, [])
                
                elif "缺少必需字段" in error:
                    # 添加缺失的必需字段
                    field = error.split("'")[1]
                    path = error.split(':')[0]
                    parent = self._get_parent(fixed_data, path)
                    if parent is not None:
                        parent[field] = None
            
            return fixed_data
        
        def _set_value(self, data, path, value):
            """设置嵌套字典的值"""
            parts = path.split('.')
            current = data
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]
            current[parts[-1]] = value
        
        def _get_parent(self, data, path):
            """获取嵌套字典的父对象"""
            parts = path.split('.')
            current = data
            for part in parts[:-1]:
                if part not in current:
                    return None
                current = current[part]
            return current
    
    return DataValidator(data, schema)

# 测试代码
if __name__ == "__main__":
    # 测试对象序列化器
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    person = Person("张三", 25)
    object_serializer(person, 'json')
    
    # 测试配置文件管理器
    config_mgr = config_manager("config.json")
    config_mgr.set("name", "测试配置")
    config_mgr.set("version", "1.0")
    
    # 测试数据转换器
    data_converter("data.json", "data.yaml")
    
    # 测试对象持久化
    persistent_obj = object_persistence(person, "storage")
    persistent_obj.save()
    persistent_obj.load()
    
    # 测试数据验证器
    schema = {
        'required_name': str,
        'required_age': int,
        'optional_email': str
    }
    data = {'name': '李四', 'age': '30'}
    validator = data_validator(data, schema)
    if not validator.validate():
        print("验证错误：")
        for error in validator.get_errors():
            print(error)
        fixed_data = validator.fix_errors()
        print("修复后的数据：", fixed_data) 