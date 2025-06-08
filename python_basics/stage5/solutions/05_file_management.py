# 文件管理练习题参考答案

import os
import shutil
import time
import re
from datetime import datetime
import fnmatch

def file_manager(directory):
    """
    文件管理器
    :param directory: 要管理的目录
    """
    class FileManager:
        def __init__(self, directory):
            self.directory = os.path.abspath(directory)
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        
        def list_files(self, pattern='*'):
            """列出文件"""
            files = []
            for root, _, filenames in os.walk(self.directory):
                for filename in filenames:
                    if fnmatch.fnmatch(filename, pattern):
                        files.append(os.path.join(root, filename))
            return files
        
        def create_file(self, filename, content=''):
            """创建文件"""
            filepath = os.path.join(self.directory, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return filepath
        
        def create_directory(self, dirname):
            """创建目录"""
            dirpath = os.path.join(self.directory, dirname)
            os.makedirs(dirpath, exist_ok=True)
            return dirpath
        
        def delete_file(self, filename):
            """删除文件"""
            filepath = os.path.join(self.directory, filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
            return False
        
        def delete_directory(self, dirname):
            """删除目录"""
            dirpath = os.path.join(self.directory, dirname)
            if os.path.exists(dirpath):
                shutil.rmtree(dirpath)
                return True
            return False
        
        def rename(self, old_name, new_name):
            """重命名文件或目录"""
            old_path = os.path.join(self.directory, old_name)
            new_path = os.path.join(self.directory, new_name)
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                return True
            return False
        
        def copy(self, source, target):
            """复制文件或目录"""
            source_path = os.path.join(self.directory, source)
            target_path = os.path.join(self.directory, target)
            if os.path.exists(source_path):
                if os.path.isfile(source_path):
                    shutil.copy2(source_path, target_path)
                else:
                    shutil.copytree(source_path, target_path)
                return True
            return False
        
        def move(self, source, target):
            """移动文件或目录"""
            source_path = os.path.join(self.directory, source)
            target_path = os.path.join(self.directory, target)
            if os.path.exists(source_path):
                shutil.move(source_path, target_path)
                return True
            return False
        
        def get_info(self, path):
            """获取文件或目录信息"""
            full_path = os.path.join(self.directory, path)
            if not os.path.exists(full_path):
                return None
            
            info = {
                'name': os.path.basename(full_path),
                'path': full_path,
                'type': 'directory' if os.path.isdir(full_path) else 'file',
                'size': os.path.getsize(full_path) if os.path.isfile(full_path) else 0,
                'created': datetime.fromtimestamp(os.path.getctime(full_path)),
                'modified': datetime.fromtimestamp(os.path.getmtime(full_path)),
                'accessed': datetime.fromtimestamp(os.path.getatime(full_path))
            }
            
            if os.path.isdir(full_path):
                info['contents'] = os.listdir(full_path)
            
            return info
    
    return FileManager(directory)

def file_searcher(directory):
    """
    文件搜索器
    :param directory: 要搜索的目录
    """
    class FileSearcher:
        def __init__(self, directory):
            self.directory = os.path.abspath(directory)
        
        def search_by_name(self, pattern, recursive=True):
            """按名称搜索"""
            results = []
            if recursive:
                for root, _, files in os.walk(self.directory):
                    for file in files:
                        if fnmatch.fnmatch(file, pattern):
                            results.append(os.path.join(root, file))
            else:
                for file in os.listdir(self.directory):
                    if fnmatch.fnmatch(file, pattern):
                        results.append(os.path.join(self.directory, file))
            return results
        
        def search_by_size(self, min_size=0, max_size=None):
            """按大小搜索"""
            results = []
            for root, _, files in os.walk(self.directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    size = os.path.getsize(file_path)
                    if min_size <= size and (max_size is None or size <= max_size):
                        results.append(file_path)
            return results
        
        def search_by_date(self, start_date=None, end_date=None):
            """按日期搜索"""
            results = []
            for root, _, files in os.walk(self.directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if (start_date is None or mtime >= start_date) and \
                       (end_date is None or mtime <= end_date):
                        results.append(file_path)
            return results
        
        def search_in_content(self, pattern, file_pattern='*'):
            """在文件内容中搜索"""
            results = []
            for root, _, files in os.walk(self.directory):
                for file in files:
                    if fnmatch.fnmatch(file, file_pattern):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                if re.search(pattern, content):
                                    results.append(file_path)
                        except:
                            continue
            return results
        
        def save_search_conditions(self, filename):
            """保存搜索条件"""
            conditions = {
                'directory': self.directory,
                'timestamp': datetime.now().isoformat()
            }
            with open(filename, 'w') as f:
                json.dump(conditions, f, indent=4)
    
    return FileSearcher(directory)

def file_synchronizer(source_dir, target_dir):
    """
    文件同步器
    :param source_dir: 源目录
    :param target_dir: 目标目录
    """
    class FileSynchronizer:
        def __init__(self, source_dir, target_dir):
            self.source_dir = os.path.abspath(source_dir)
            self.target_dir = os.path.abspath(target_dir)
            self.sync_log = []
        
        def sync(self):
            """同步文件"""
            # 确保目标目录存在
            os.makedirs(self.target_dir, exist_ok=True)
            
            # 获取源目录文件列表
            source_files = set()
            for root, _, files in os.walk(self.source_dir):
                for file in files:
                    source_path = os.path.join(root, file)
                    rel_path = os.path.relpath(source_path, self.source_dir)
                    source_files.add(rel_path)
            
            # 获取目标目录文件列表
            target_files = set()
            for root, _, files in os.walk(self.target_dir):
                for file in files:
                    target_path = os.path.join(root, file)
                    rel_path = os.path.relpath(target_path, self.target_dir)
                    target_files.add(rel_path)
            
            # 同步文件
            for rel_path in source_files:
                source_path = os.path.join(self.source_dir, rel_path)
                target_path = os.path.join(self.target_dir, rel_path)
                
                # 检查文件是否需要更新
                if rel_path not in target_files or \
                   os.path.getmtime(source_path) > os.path.getmtime(target_path):
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    # 复制文件
                    shutil.copy2(source_path, target_path)
                    self.sync_log.append(f"更新文件：{rel_path}")
            
            # 删除多余文件
            for rel_path in target_files - source_files:
                target_path = os.path.join(self.target_dir, rel_path)
                os.remove(target_path)
                self.sync_log.append(f"删除文件：{rel_path}")
            
            return self.sync_log
        
        def handle_conflicts(self, conflict_handler):
            """处理文件冲突"""
            for root, _, files in os.walk(self.source_dir):
                for file in files:
                    source_path = os.path.join(root, file)
                    rel_path = os.path.relpath(source_path, self.source_dir)
                    target_path = os.path.join(self.target_dir, rel_path)
                    
                    if os.path.exists(target_path):
                        # 检查文件是否不同
                        if not self._files_are_identical(source_path, target_path):
                            # 处理冲突
                            conflict_handler(source_path, target_path)
        
        def _files_are_identical(self, file1, file2):
            """检查两个文件是否相同"""
            if os.path.getsize(file1) != os.path.getsize(file2):
                return False
            
            with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
                while True:
                    chunk1 = f1.read(8192)
                    chunk2 = f2.read(8192)
                    if chunk1 != chunk2:
                        return False
                    if not chunk1:
                        break
            
            return True
    
    return FileSynchronizer(source_dir, target_dir)

def permission_manager(directory):
    """
    文件权限管理器
    :param directory: 要管理的目录
    """
    class PermissionManager:
        def __init__(self, directory):
            self.directory = os.path.abspath(directory)
            self.history = []
        
        def get_permissions(self, path):
            """获取文件权限"""
            full_path = os.path.join(self.directory, path)
            if not os.path.exists(full_path):
                return None
            
            return {
                'mode': oct(os.stat(full_path).st_mode)[-3:],
                'uid': os.stat(full_path).st_uid,
                'gid': os.stat(full_path).st_gid
            }
        
        def set_permissions(self, path, mode):
            """设置文件权限"""
            full_path = os.path.join(self.directory, path)
            if not os.path.exists(full_path):
                return False
            
            try:
                os.chmod(full_path, int(mode, 8))
                self.history.append({
                    'path': path,
                    'mode': mode,
                    'timestamp': datetime.now().isoformat()
                })
                return True
            except:
                return False
        
        def set_permissions_recursive(self, path, mode):
            """递归设置权限"""
            full_path = os.path.join(self.directory, path)
            if not os.path.exists(full_path):
                return False
            
            try:
                for root, dirs, files in os.walk(full_path):
                    for item in dirs + files:
                        item_path = os.path.join(root, item)
                        os.chmod(item_path, int(mode, 8))
                        self.history.append({
                            'path': os.path.relpath(item_path, self.directory),
                            'mode': mode,
                            'timestamp': datetime.now().isoformat()
                        })
                return True
            except:
                return False
        
        def inherit_permissions(self, source_path, target_path):
            """继承权限"""
            source_full_path = os.path.join(self.directory, source_path)
            target_full_path = os.path.join(self.directory, target_path)
            
            if not os.path.exists(source_full_path) or not os.path.exists(target_full_path):
                return False
            
            try:
                source_stat = os.stat(source_full_path)
                os.chmod(target_full_path, source_stat.st_mode)
                self.history.append({
                    'path': target_path,
                    'mode': oct(source_stat.st_mode)[-3:],
                    'timestamp': datetime.now().isoformat(),
                    'inherited_from': source_path
                })
                return True
            except:
                return False
        
        def get_history(self):
            """获取权限变更历史"""
            return self.history
    
    return PermissionManager(directory)

def filesystem_monitor(directory):
    """
    文件系统监控器
    :param directory: 要监控的目录
    """
    class FilesystemMonitor:
        def __init__(self, directory):
            self.directory = os.path.abspath(directory)
            self.log_file = f"fs_monitor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
            self.running = False
        
        def start_monitoring(self, interval=1):
            """开始监控"""
            self.running = True
            self._initial_state = self._get_current_state()
            
            while self.running:
                current_state = self._get_current_state()
                self._check_changes(current_state)
                time.sleep(interval)
        
        def stop_monitoring(self):
            """停止监控"""
            self.running = False
        
        def _get_current_state(self):
            """获取当前文件系统状态"""
            state = {}
            for root, dirs, files in os.walk(self.directory):
                for item in dirs + files:
                    path = os.path.join(root, item)
                    state[path] = {
                        'mtime': os.path.getmtime(path),
                        'size': os.path.getsize(path) if os.path.isfile(path) else 0
                    }
            return state
        
        def _check_changes(self, current_state):
            """检查变化"""
            # 检查新文件和修改
            for path, info in current_state.items():
                if path not in self._initial_state:
                    self._log_event('created', path)
                elif info['mtime'] > self._initial_state[path]['mtime']:
                    self._log_event('modified', path)
            
            # 检查删除
            for path in self._initial_state:
                if path not in current_state:
                    self._log_event('deleted', path)
            
            self._initial_state = current_state
        
        def _log_event(self, event_type, path):
            """记录事件"""
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            rel_path = os.path.relpath(path, self.directory)
            log_entry = f"[{timestamp}] {event_type.upper()}: {rel_path}\n"
            
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
        
        def get_log(self):
            """获取日志内容"""
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r') as f:
                    return f.read()
            return ""
    
    return FilesystemMonitor(directory)

# 测试代码
if __name__ == "__main__":
    # 测试文件管理器
    fm = file_manager("test_dir")
    fm.create_file("test.txt", "Hello, World!")
    print(fm.list_files())
    
    # 测试文件搜索器
    fs = file_searcher("test_dir")
    results = fs.search_by_name("*.txt")
    print(results)
    
    # 测试文件同步器
    sync = file_synchronizer("source_dir", "target_dir")
    sync.sync()
    
    # 测试权限管理器
    pm = permission_manager("test_dir")
    pm.set_permissions("test.txt", "644")
    
    # 测试文件系统监控器
    monitor = filesystem_monitor("test_dir")
    monitor.start_monitoring() 