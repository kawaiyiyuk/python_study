# 文件操作练习题参考答案

import os
import shutil
import time
from datetime import datetime

def file_copier(source_path, target_path):
    """
    文件复制器
    :param source_path: 源文件路径
    :param target_path: 目标文件路径
    """
    # 检查源文件是否存在
    if not os.path.exists(source_path):
        print(f"错误：源文件 {source_path} 不存在")
        return
    
    # 检查目标文件是否已存在
    if os.path.exists(target_path):
        response = input(f"目标文件 {target_path} 已存在，是否覆盖？(y/n): ")
        if response.lower() != 'y':
            print("操作已取消")
            return
    
    # 记录开始时间
    start_time = time.time()
    
    try:
        # 复制文件
        shutil.copy2(source_path, target_path)
        
        # 获取文件大小
        file_size = os.path.getsize(target_path)
        
        # 计算复制时间
        end_time = time.time()
        copy_time = end_time - start_time
        
        print(f"文件复制完成：")
        print(f"源文件：{source_path}")
        print(f"目标文件：{target_path}")
        print(f"文件大小：{file_size} 字节")
        print(f"复制时间：{copy_time:.2f} 秒")
    
    except Exception as e:
        print(f"复制过程中发生错误：{str(e)}")

def file_statistics(file_path):
    """
    文件内容统计器
    :param file_path: 文件路径
    """
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()
        
        # 统计信息
        stats = {
            '字符数': len(content),
            '单词数': len(content.split()),
            '行数': len(lines),
            '空行数': len([line for line in lines if not line.strip()])
        }
        
        # 写入统计结果
        output_file = f"{os.path.splitext(file_path)[0]}_stats.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("文件统计信息：\n")
            f.write(f"文件路径：{file_path}\n")
            f.write(f"统计时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 30 + "\n")
            for key, value in stats.items():
                f.write(f"{key}：{value}\n")
        
        print(f"统计结果已保存到：{output_file}")
        return stats
    
    except Exception as e:
        print(f"统计过程中发生错误：{str(e)}")
        return None

def encoding_converter(source_path, target_path, target_encoding):
    """
    文件编码转换器
    :param source_path: 源文件路径
    :param target_path: 目标文件路径
    :param target_encoding: 目标编码格式
    """
    try:
        # 尝试检测源文件编码
        import chardet
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

def backup_tool(source_path, backup_dir):
    """
    文件备份工具
    :param source_path: 要备份的文件或目录路径
    :param backup_dir: 备份目录
    """
    try:
        # 创建备份目录
        os.makedirs(backup_dir, exist_ok=True)
        
        # 生成备份文件名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        if os.path.isfile(source_path):
            backup_name = f"{os.path.basename(source_path)}_{timestamp}"
            backup_path = os.path.join(backup_dir, backup_name)
            shutil.copy2(source_path, backup_path)
        else:
            backup_name = f"{os.path.basename(source_path)}_{timestamp}"
            backup_path = os.path.join(backup_dir, backup_name)
            shutil.copytree(source_path, backup_path)
        
        # 压缩备份
        shutil.make_archive(backup_path, 'zip', backup_path)
        shutil.rmtree(backup_path)  # 删除未压缩的备份
        
        print(f"备份完成：")
        print(f"源路径：{source_path}")
        print(f"备份文件：{backup_path}.zip")
    
    except Exception as e:
        print(f"备份过程中发生错误：{str(e)}")

def file_monitor(directory, interval=1):
    """
    文件监控器
    :param directory: 要监控的目录
    :param interval: 监控间隔（秒）
    """
    try:
        # 创建日志文件
        log_file = f"file_monitor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        # 获取初始文件状态
        initial_files = set()
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                initial_files.add(file_path)
        
        print(f"开始监控目录：{directory}")
        print(f"日志文件：{log_file}")
        
        while True:
            # 获取当前文件状态
            current_files = set()
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    current_files.add(file_path)
            
            # 检测变化
            created = current_files - initial_files
            deleted = initial_files - current_files
            
            # 记录变化
            if created or deleted:
                with open(log_file, 'a', encoding='utf-8') as f:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    if created:
                        f.write(f"[{timestamp}] 创建文件：\n")
                        for file in created:
                            f.write(f"  - {file}\n")
                    if deleted:
                        f.write(f"[{timestamp}] 删除文件：\n")
                        for file in deleted:
                            f.write(f"  - {file}\n")
            
            # 更新文件状态
            initial_files = current_files
            
            # 等待下一次检查
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("\n监控已停止")
    except Exception as e:
        print(f"监控过程中发生错误：{str(e)}")

# 测试代码
if __name__ == "__main__":
    # 测试文件复制器
    file_copier("test.txt", "test_copy.txt")
    
    # 测试文件统计器
    file_statistics("test.txt")
    
    # 测试编码转换器
    encoding_converter("test.txt", "test_utf8.txt", "utf-8")
    
    # 测试备份工具
    backup_tool("test.txt", "backups")
    
    # 测试文件监控器
    file_monitor(".", interval=1) 