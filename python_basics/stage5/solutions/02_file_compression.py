# 文件压缩练习题参考答案

import os
import zipfile
import gzip
import bz2
import shutil
from datetime import datetime

def zip_manager(zip_path, password=None):
    """
    ZIP文件管理器
    :param zip_path: ZIP文件路径
    :param password: 密码（可选）
    """
    class ZipManager:
        def __init__(self, zip_path, password=None):
            self.zip_path = zip_path
            self.password = password
        
        def create_zip(self, files_to_add):
            """创建ZIP文件"""
            with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in files_to_add:
                    if os.path.isfile(file):
                        zipf.write(file, os.path.basename(file))
                    elif os.path.isdir(file):
                        for root, _, files in os.walk(file):
                            for f in files:
                                file_path = os.path.join(root, f)
                                arcname = os.path.relpath(file_path, os.path.dirname(file))
                                zipf.write(file_path, arcname)
        
        def extract_zip(self, extract_path):
            """提取ZIP文件"""
            with zipfile.ZipFile(self.zip_path, 'r') as zipf:
                if self.password:
                    zipf.setpassword(self.password.encode())
                zipf.extractall(extract_path)
        
        def list_contents(self):
            """列出ZIP文件内容"""
            with zipfile.ZipFile(self.zip_path, 'r') as zipf:
                if self.password:
                    zipf.setpassword(self.password.encode())
                return zipf.namelist()
    
    return ZipManager(zip_path, password)

def compression_tool(file_path, compression_type='zip', level=6):
    """
    文件压缩工具
    :param file_path: 要压缩的文件或目录路径
    :param compression_type: 压缩类型（zip/gzip/bzip2）
    :param level: 压缩级别（1-9）
    """
    def get_original_size(path):
        """获取原始大小"""
        if os.path.isfile(path):
            return os.path.getsize(path)
        total_size = 0
        for root, _, files in os.walk(path):
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))
        return total_size
    
    try:
        # 获取原始大小
        original_size = get_original_size(file_path)
        
        # 根据压缩类型选择压缩方法
        if compression_type == 'zip':
            output_path = f"{file_path}.zip"
            if os.path.isfile(file_path):
                with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=level) as zipf:
                    zipf.write(file_path, os.path.basename(file_path))
            else:
                shutil.make_archive(file_path, 'zip', file_path)
        
        elif compression_type == 'gzip':
            output_path = f"{file_path}.gz"
            with open(file_path, 'rb') as f_in:
                with gzip.open(output_path, 'wb', compresslevel=level) as f_out:
                    shutil.copyfileobj(f_in, f_out)
        
        elif compression_type == 'bzip2':
            output_path = f"{file_path}.bz2"
            with open(file_path, 'rb') as f_in:
                with bz2.open(output_path, 'wb', compresslevel=level) as f_out:
                    shutil.copyfileobj(f_in, f_out)
        
        # 获取压缩后大小
        compressed_size = os.path.getsize(output_path)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f"压缩完成：")
        print(f"原始大小：{original_size} 字节")
        print(f"压缩后大小：{compressed_size} 字节")
        print(f"压缩比：{compression_ratio:.2f}%")
        print(f"输出文件：{output_path}")
    
    except Exception as e:
        print(f"压缩过程中发生错误：{str(e)}")

def incremental_backup(source_path, backup_dir):
    """
    增量备份工具
    :param source_path: 要备份的文件或目录路径
    :param backup_dir: 备份目录
    """
    class BackupManager:
        def __init__(self, source_path, backup_dir):
            self.source_path = source_path
            self.backup_dir = backup_dir
            self.history_file = os.path.join(backup_dir, "backup_history.json")
            self.history = self._load_history()
        
        def _load_history(self):
            """加载备份历史"""
            if os.path.exists(self.history_file):
                import json
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            return {}
        
        def _save_history(self):
            """保存备份历史"""
            import json
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f, indent=4)
        
        def create_full_backup(self):
            """创建完整备份"""
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"full_backup_{timestamp}"
            backup_path = os.path.join(self.backup_dir, backup_name)
            
            if os.path.isfile(self.source_path):
                shutil.copy2(self.source_path, backup_path)
            else:
                shutil.copytree(self.source_path, backup_path)
            
            # 记录备份信息
            self.history[backup_name] = {
                'type': 'full',
                'timestamp': timestamp,
                'path': backup_path
            }
            self._save_history()
            
            return backup_path
        
        def create_incremental_backup(self):
            """创建增量备份"""
            if not self.history:
                return self.create_full_backup()
            
            # 获取上次备份时间
            last_backup = max(self.history.items(), key=lambda x: x[1]['timestamp'])
            last_backup_time = datetime.strptime(last_backup[1]['timestamp'], '%Y%m%d_%H%M%S')
            
            # 查找修改过的文件
            modified_files = []
            for root, _, files in os.walk(self.source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.getmtime(file_path) > last_backup_time.timestamp():
                        modified_files.append(file_path)
            
            if not modified_files:
                print("没有文件被修改，跳过增量备份")
                return None
            
            # 创建增量备份
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"incremental_backup_{timestamp}"
            backup_path = os.path.join(self.backup_dir, backup_name)
            
            with zipfile.ZipFile(f"{backup_path}.zip", 'w') as zipf:
                for file in modified_files:
                    zipf.write(file, os.path.relpath(file, self.source_path))
            
            # 记录备份信息
            self.history[backup_name] = {
                'type': 'incremental',
                'timestamp': timestamp,
                'path': f"{backup_path}.zip",
                'based_on': last_backup[0]
            }
            self._save_history()
            
            return f"{backup_path}.zip"
    
    return BackupManager(source_path, backup_dir)

def file_splitter(file_path, chunk_size=1024*1024):
    """
    文件分割器
    :param file_path: 要分割的文件路径
    :param chunk_size: 每个分块的大小（字节）
    """
    try:
        # 获取文件大小
        file_size = os.path.getsize(file_path)
        
        # 计算分块数量
        num_chunks = (file_size + chunk_size - 1) // chunk_size
        
        # 创建分割信息文件
        info_file = f"{file_path}.split_info"
        with open(info_file, 'w') as f:
            f.write(f"原始文件：{file_path}\n")
            f.write(f"文件大小：{file_size} 字节\n")
            f.write(f"分块大小：{chunk_size} 字节\n")
            f.write(f"分块数量：{num_chunks}\n")
        
        # 分割文件
        with open(file_path, 'rb') as f:
            for i in range(num_chunks):
                chunk_file = f"{file_path}.part{i+1}"
                with open(chunk_file, 'wb') as chunk:
                    chunk.write(f.read(chunk_size))
        
        print(f"文件分割完成：")
        print(f"原始文件：{file_path}")
        print(f"分块数量：{num_chunks}")
        print(f"分块大小：{chunk_size} 字节")
        print(f"信息文件：{info_file}")
    
    except Exception as e:
        print(f"分割过程中发生错误：{str(e)}")

def compression_browser(archive_path):
    """
    压缩文件浏览器
    :param archive_path: 压缩文件路径
    """
    class ArchiveBrowser:
        def __init__(self, archive_path):
            self.archive_path = archive_path
            self.archive = None
            self._open_archive()
        
        def _open_archive(self):
            """打开压缩文件"""
            if self.archive_path.endswith('.zip'):
                self.archive = zipfile.ZipFile(self.archive_path, 'r')
            elif self.archive_path.endswith('.gz'):
                self.archive = gzip.open(self.archive_path, 'rb')
            elif self.archive_path.endswith('.bz2'):
                self.archive = bz2.open(self.archive_path, 'rb')
            else:
                raise ValueError("不支持的压缩格式")
        
        def list_contents(self):
            """列出压缩文件内容"""
            if isinstance(self.archive, zipfile.ZipFile):
                return self.archive.namelist()
            return [os.path.basename(self.archive_path)]
        
        def preview_text(self, file_name):
            """预览文本文件内容"""
            if isinstance(self.archive, zipfile.ZipFile):
                with self.archive.open(file_name) as f:
                    content = f.read()
                    try:
                        return content.decode('utf-8')
                    except UnicodeDecodeError:
                        return "无法解码文件内容"
            else:
                content = self.archive.read()
                try:
                    return content.decode('utf-8')
                except UnicodeDecodeError:
                    return "无法解码文件内容"
        
        def search_content(self, keyword):
            """搜索文件内容"""
            results = []
            if isinstance(self.archive, zipfile.ZipFile):
                for file_name in self.archive.namelist():
                    if file_name.endswith(('.txt', '.py', '.md')):
                        with self.archive.open(file_name) as f:
                            content = f.read().decode('utf-8', errors='ignore')
                            if keyword in content:
                                results.append(file_name)
            return results
        
        def close(self):
            """关闭压缩文件"""
            if self.archive:
                self.archive.close()
    
    return ArchiveBrowser(archive_path)

# 测试代码
if __name__ == "__main__":
    # 测试ZIP文件管理器
    zip_mgr = zip_manager("test.zip", password="123456")
    zip_mgr.create_zip(["test.txt"])
    print(zip_mgr.list_contents())
    
    # 测试压缩工具
    compression_tool("test.txt", compression_type="zip", level=9)
    
    # 测试增量备份
    backup_mgr = incremental_backup("test.txt", "backups")
    backup_mgr.create_full_backup()
    backup_mgr.create_incremental_backup()
    
    # 测试文件分割器
    file_splitter("test.txt", chunk_size=1024)
    
    # 测试压缩文件浏览器
    browser = compression_browser("test.zip")
    print(browser.list_contents())
    browser.close() 