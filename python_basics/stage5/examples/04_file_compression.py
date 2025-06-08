# 文件压缩示例

import os
import zipfile
import gzip
import shutil

# ZIP文件操作
def zip_operations():
    """ZIP文件操作示例"""
    # 创建ZIP文件
    with zipfile.ZipFile("example.zip", "w") as zipf:
        # 添加文件
        zipf.write("test.txt", "test.txt")
        # 添加目录
        for root, dirs, files in os.walk("test_dir"):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, "test_dir")
                zipf.write(file_path, arcname)
    
    # 读取ZIP文件
    with zipfile.ZipFile("example.zip", "r") as zipf:
        # 列出文件
        print("ZIP文件内容：")
        for file in zipf.namelist():
            print(file)
        
        # 读取特定文件
        with zipf.open("test.txt") as f:
            print("\n文件内容：")
            print(f.read().decode())

# GZIP压缩
def gzip_operations():
    """GZIP压缩示例"""
    # 压缩文件
    with open("test.txt", "rb") as f_in:
        with gzip.open("test.txt.gz", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    # 解压文件
    with gzip.open("test.txt.gz", "rb") as f_in:
        with open("test_decompressed.txt", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

# 创建测试文件
def create_test_files():
    """创建测试文件"""
    # 创建测试文件
    with open("test.txt", "w") as f:
        f.write("This is a test file.")
    
    # 创建测试目录
    os.makedirs("test_dir/subdir", exist_ok=True)
    with open("test_dir/file1.txt", "w") as f:
        f.write("File 1 content")
    with open("test_dir/subdir/file2.txt", "w") as f:
        f.write("File 2 content")

# 清理测试文件
def cleanup():
    """清理测试文件"""
    # 删除测试文件
    if os.path.exists("test.txt"):
        os.remove("test.txt")
    if os.path.exists("test.txt.gz"):
        os.remove("test.txt.gz")
    if os.path.exists("test_decompressed.txt"):
        os.remove("test_decompressed.txt")
    if os.path.exists("example.zip"):
        os.remove("example.zip")
    
    # 删除测试目录
    if os.path.exists("test_dir"):
        shutil.rmtree("test_dir")

# 执行示例
if __name__ == "__main__":
    create_test_files()
    zip_operations()
    gzip_operations()
    cleanup() 