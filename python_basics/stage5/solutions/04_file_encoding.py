# 文件编码练习题参考答案

import os
import chardet
import codecs
from datetime import datetime

def encoding_detector(file_path):
    """
    编码检测器
    :param file_path: 文件路径
    """
    try:
        # 读取文件内容
        with open(file_path, 'rb') as f:
            raw_data = f.read()
        
        # 检测编码
        result = chardet.detect(raw_data)
        
        print(f"文件编码检测结果：")
        print(f"文件：{file_path}")
        print(f"编码：{result['encoding']}")
        print(f"置信度：{result['confidence']:.2%}")
        
        return result
    
    except Exception as e:
        print(f"检测编码时发生错误：{str(e)}")
        return None

def encoding_converter(source_path, target_path, target_encoding):
    """
    编码转换器
    :param source_path: 源文件路径
    :param target_path: 目标文件路径
    :param target_encoding: 目标编码格式
    """
    try:
        # 检测源文件编码
        with open(source_path, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            source_encoding = result['encoding']
        
        # 读取源文件
        with open(source_path, 'r', encoding=source_encoding) as f:
            content = f.read()
        
        # 写入目标文件
        with open(target_path, 'w', encoding=target_encoding) as f:
            f.write(content)
        
        print(f"编码转换完成：")
        print(f"源文件：{source_path} ({source_encoding})")
        print(f"目标文件：{target_path} ({target_encoding})")
    
    except UnicodeDecodeError:
        print(f"错误：无法使用检测到的编码 {source_encoding} 读取文件")
    except UnicodeEncodeError:
        print(f"错误：无法使用目标编码 {target_encoding} 写入文件")
    except Exception as e:
        print(f"转换过程中发生错误：{str(e)}")

def text_cleaner(file_path):
    """
    文本清理器
    :param file_path: 文件路径
    """
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 清理文本
        cleaned_content = content
        
        # 统一换行符
        cleaned_content = cleaned_content.replace('\r\n', '\n').replace('\r', '\n')
        
        # 处理特殊字符
        cleaned_content = cleaned_content.replace('\t', '    ')  # 制表符转换为空格
        
        # 删除不可见字符
        cleaned_content = ''.join(char for char in cleaned_content if char.isprintable() or char == '\n')
        
        # 修复常见的编码问题
        cleaned_content = cleaned_content.replace('？', '?').replace('！', '!')
        
        # 保存清理后的文件
        output_path = f"{os.path.splitext(file_path)[0]}_cleaned.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"文本清理完成：")
        print(f"原始文件：{file_path}")
        print(f"清理后文件：{output_path}")
    
    except Exception as e:
        print(f"清理过程中发生错误：{str(e)}")

def encoding_validator(file_path, expected_encoding='utf-8'):
    """
    编码验证器
    :param file_path: 文件路径
    :param expected_encoding: 期望的编码格式
    """
    try:
        # 读取文件内容
        with open(file_path, 'rb') as f:
            raw_data = f.read()
        
        # 检测实际编码
        result = chardet.detect(raw_data)
        actual_encoding = result['encoding']
        
        # 验证编码
        is_valid = actual_encoding.lower() == expected_encoding.lower()
        
        # 检查非法字符
        illegal_chars = []
        try:
            with open(file_path, 'r', encoding=expected_encoding) as f:
                content = f.read()
        except UnicodeDecodeError as e:
            illegal_chars.append(str(e))
        
        # 生成报告
        report = {
            'file': file_path,
            'expected_encoding': expected_encoding,
            'actual_encoding': actual_encoding,
            'is_valid': is_valid,
            'confidence': result['confidence'],
            'illegal_chars': illegal_chars
        }
        
        print(f"编码验证报告：")
        print(f"文件：{file_path}")
        print(f"期望编码：{expected_encoding}")
        print(f"实际编码：{actual_encoding}")
        print(f"是否有效：{'是' if is_valid else '否'}")
        print(f"置信度：{result['confidence']:.2%}")
        if illegal_chars:
            print(f"非法字符：{illegal_chars}")
        
        return report
    
    except Exception as e:
        print(f"验证过程中发生错误：{str(e)}")
        return None

def encoding_analyzer(file_path):
    """
    编码分析器
    :param file_path: 文件路径
    """
    try:
        # 读取文件内容
        with open(file_path, 'rb') as f:
            raw_data = f.read()
        
        # 检测编码
        result = chardet.detect(raw_data)
        
        # 分析字符分布
        char_distribution = {}
        try:
            content = raw_data.decode(result['encoding'])
            for char in content:
                if char in char_distribution:
                    char_distribution[char] += 1
                else:
                    char_distribution[char] = 1
        except UnicodeDecodeError:
            pass
        
        # 检测潜在的编码问题
        potential_issues = []
        if result['confidence'] < 0.8:
            potential_issues.append("编码检测置信度较低")
        if len(char_distribution) == 0:
            potential_issues.append("无法解码文件内容")
        
        # 生成报告
        report = {
            'file': file_path,
            'encoding': result['encoding'],
            'confidence': result['confidence'],
            'char_distribution': char_distribution,
            'potential_issues': potential_issues
        }
        
        print(f"编码分析报告：")
        print(f"文件：{file_path}")
        print(f"编码：{result['encoding']}")
        print(f"置信度：{result['confidence']:.2%}")
        print(f"字符分布：")
        for char, count in sorted(char_distribution.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  '{char}': {count}")
        if potential_issues:
            print(f"潜在问题：")
            for issue in potential_issues:
                print(f"  - {issue}")
        
        return report
    
    except Exception as e:
        print(f"分析过程中发生错误：{str(e)}")
        return None

# 测试代码
if __name__ == "__main__":
    # 测试编码检测器
    encoding_detector("test.txt")
    
    # 测试编码转换器
    encoding_converter("test.txt", "test_utf8.txt", "utf-8")
    
    # 测试文本清理器
    text_cleaner("test.txt")
    
    # 测试编码验证器
    encoding_validator("test.txt", "utf-8")
    
    # 测试编码分析器
    encoding_analyzer("test.txt") 