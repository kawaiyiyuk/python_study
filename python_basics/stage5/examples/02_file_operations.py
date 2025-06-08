# 文件操作进阶示例

import os
import shutil
import tempfile
from pathlib import Path

# 文件路径操作
def path_operations():
    """文件路径操作示例"""
    # 创建Path对象
    path = Path("example.txt")
    
    # 获取文件信息
    print(f"文件名：{path.name}")
    print(f"文件后缀：{path.suffix}")
    print(f"父目录：{path.parent}")
    print(f"绝对路径：{path.absolute()}")
    
    # 路径拼接
    new_path = path.parent / "subdir" / "new_file.txt"
    print(f"新路径：{new_path}")

# 文件系统操作
def filesystem_operations():
    """文件系统操作示例"""
    # 创建目录
    os.makedirs("test_dir/subdir", exist_ok=True)
    
    # 创建文件
    with open("test_dir/test.txt", "w") as f:
        f.write("测试文件")
    
    # 列出目录内容
    print("\n目录内容：")
    for item in os.listdir("test_dir"):
        print(item)
    
    # 获取文件信息
    file_stat = os.stat("test_dir/test.txt")
    print(f"\n文件大小：{file_stat.st_size} 字节")
    print(f"最后修改时间：{file_stat.st_mtime}")

# 文件复制和移动
def file_copy_move():
    """文件复制和移动示例"""
    # 复制文件
    shutil.copy2("test_dir/test.txt", "test_dir/test_copy.txt")
    
    # 复制目录
    shutil.copytree("test_dir", "test_dir_backup")
    
    # 移动文件
    shutil.move("test_dir/test_copy.txt", "test_dir/subdir/test_moved.txt")

# 临时文件操作
def temp_file_operations():
    """临时文件操作示例"""
    # 创建临时文件
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"临时文件内容")
        temp_path = temp_file.name
    
    # 读取临时文件
    with open(temp_path, "r") as f:
        print(f"临时文件内容：{f.read()}")
    
    # 删除临时文件
    os.unlink(temp_path)

# 文件遍历
def file_walk():
    """文件遍历示例"""
    print("\n目录结构：")
    for root, dirs, files in os.walk("test_dir"):
        level = root.replace("test_dir", "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

# 文件权限操作
def file_permissions():
    """文件权限操作示例"""
    # 设置文件权限
    os.chmod("test_dir/test.txt", 0o644)
    
    # 获取文件权限
    mode = os.stat("test_dir/test.txt").st_mode
    print(f"\n文件权限：{oct(mode & 0o777)}")

# 清理测试文件
def cleanup():
    """清理测试文件"""
    shutil.rmtree("test_dir")
    shutil.rmtree("test_dir_backup")

# 执行示例
if __name__ == "__main__":
    path_operations()
    filesystem_operations()
    file_copy_move()
    temp_file_operations()
    file_walk()
    file_permissions()
    cleanup() 