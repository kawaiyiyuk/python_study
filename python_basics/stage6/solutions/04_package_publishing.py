# 包发布练习题参考答案

# 1. setup.py
"""
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.28.0",
        "numpy>=1.21.0",
    ],
    entry_points={
        "console_scripts": [
            "my_package=my_package.cli:main",
        ],
    },
    package_data={
        "my_package": ["data/*.json"],
    },
    include_package_data=True,
)
"""

# 2. MANIFEST.in
"""
include LICENSE
include README.md
include requirements.txt
include requirements-dev.txt
recursive-include tests *
recursive-include docs *
recursive-include my_package/data *
global-exclude *.pyc
global-exclude __pycache__
global-exclude .DS_Store
"""

# 3. pyproject.toml
"""
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "1.0.0"
description = "A sample package"
readme = "README.md"
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
license = {file = "LICENSE"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
requires-python = ">=3.6"
dependencies = [
    "requests>=2.28.0",
    "numpy>=1.21.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "flake8>=4.0.0",
]
docs = [
    "sphinx>=4.4.0",
    "sphinx-rtd-theme>=1.0.0",
]

[project.scripts]
my_package = "my_package.cli:main"

[tool.black]
line-length = 88
target-version = ["py36", "py37", "py38", "py39"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
"""

# 4. 包构建
import subprocess
import os
import shutil

class PackageBuilder:
    """包构建类"""
    def __init__(self):
        self.build_dir = "build"
        self.dist_dir = "dist"
    
    def install_build_tools(self):
        """安装构建工具"""
        subprocess.run([
            "pip", "install", "--upgrade", "build", "wheel"
        ])
    
    def build_package(self):
        """构建包"""
        # 清理旧的构建文件
        if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)
        if os.path.exists(self.dist_dir):
            shutil.rmtree(self.dist_dir)
        
        # 构建包
        subprocess.run([
            "python", "-m", "build"
        ])
    
    def check_build(self):
        """检查构建结果"""
        if not os.path.exists(self.dist_dir):
            print("构建失败：未找到dist目录")
            return False
        
        files = os.listdir(self.dist_dir)
        if not any(f.endswith(".whl") for f in files):
            print("构建失败：未找到wheel文件")
            return False
        
        if not any(f.endswith(".tar.gz") for f in files):
            print("构建失败：未找到源码包")
            return False
        
        print("构建成功！")
        return True
    
    def clean_build(self):
        """清理构建文件"""
        if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)
        if os.path.exists(self.dist_dir):
            shutil.rmtree(self.dist_dir)
        if os.path.exists("*.egg-info"):
            shutil.rmtree("*.egg-info")

# 5. PyPI发布
class PyPIPublisher:
    """PyPI发布类"""
    def __init__(self):
        self.test_pypi = "https://test.pypi.org/legacy/"
        self.pypi = "https://upload.pypi.org/legacy/"
    
    def register_account(self):
        """注册PyPI账号"""
        print("请访问 https://pypi.org/account/register/ 注册账号")
    
    def configure_publishing(self):
        """配置发布工具"""
        subprocess.run([
            "pip", "install", "--upgrade", "twine"
        ])
    
    def upload_to_test_pypi(self):
        """上传到测试PyPI"""
        subprocess.run([
            "twine", "upload", "--repository-url", self.test_pypi,
            "dist/*"
        ])
    
    def upload_to_pypi(self):
        """上传到PyPI"""
        subprocess.run([
            "twine", "upload", "dist/*"
        ])
    
    def verify_upload(self, package_name, version):
        """验证上传"""
        subprocess.run([
            "pip", "install", f"{package_name}=={version}"
        ])

# 6. 版本管理
class VersionManager:
    """版本管理类"""
    def __init__(self):
        self.version_file = "my_package/__init__.py"
        self.current_version = None
    
    def install_bumpversion(self):
        """安装bumpversion"""
        subprocess.run([
            "pip", "install", "bumpversion"
        ])
    
    def configure_version(self):
        """配置版本管理"""
        with open(".bumpversion.cfg", "w") as f:
            f.write("""
[bumpversion]
current_version = 1.0.0
commit = True
tag = True
parse = (?P<major>\\d+)\\.(?P<minor>\\d+)\\.(?P<patch>\\d+)
serialize = 
    {major}.{minor}.{patch}

[bumpversion:file:my_package/__init__.py]
search = __version__ = "{current_version}"
replace = __version__ = "{new_version}"
""")
    
    def bump_version(self, part):
        """更新版本号"""
        subprocess.run([
            "bumpversion", part
        ])
    
    def commit_changes(self):
        """提交更改"""
        subprocess.run([
            "git", "add", "."
        ])
        subprocess.run([
            "git", "commit", "-m", "Bump version"
        ])
    
    def create_tag(self):
        """创建标签"""
        subprocess.run([
            "git", "tag", "-a", f"v{self.current_version}",
            "-m", f"Version {self.current_version}"
        ])

# 7. 包测试
class PackageTester:
    """包测试类"""
    def __init__(self):
        self.test_dir = "tests"
    
    def install_test_dependencies(self):
        """安装测试依赖"""
        subprocess.run([
            "pip", "install", "-r", "requirements-dev.txt"
        ])
    
    def run_unit_tests(self):
        """运行单元测试"""
        subprocess.run([
            "pytest", self.test_dir, "-v"
        ])
    
    def run_integration_tests(self):
        """运行集成测试"""
        subprocess.run([
            "pytest", f"{self.test_dir}/integration", "-v"
        ])
    
    def generate_test_report(self):
        """生成测试报告"""
        subprocess.run([
            "pytest", "--cov=my_package", "--cov-report=html",
            self.test_dir
        ])
    
    def check_test_coverage(self):
        """检查测试覆盖率"""
        subprocess.run([
            "pytest", "--cov=my_package", "--cov-report=term-missing",
            self.test_dir
        ])

# 8. 包文档
class DocumentationManager:
    """文档管理类"""
    def __init__(self):
        self.docs_dir = "docs"
    
    def install_doc_tools(self):
        """安装文档工具"""
        subprocess.run([
            "pip", "install", "sphinx", "sphinx-rtd-theme"
        ])
    
    def create_doc_structure(self):
        """创建文档结构"""
        if not os.path.exists(self.docs_dir):
            os.makedirs(self.docs_dir)
        
        subprocess.run([
            "sphinx-quickstart", self.docs_dir,
            "--project", "My Package",
            "--author", "Your Name",
            "--release", "1.0.0",
            "--language", "en"
        ])
    
    def write_api_docs(self):
        """编写API文档"""
        with open(f"{self.docs_dir}/api.rst", "w") as f:
            f.write("""
API Reference
============

.. automodule:: my_package
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: my_package.core
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: my_package.utils
   :members:
   :undoc-members:
   :show-inheritance:
""")
    
    def write_usage_examples(self):
        """编写使用示例"""
        with open(f"{self.docs_dir}/usage.rst", "w") as f:
            f.write("""
Usage Examples
=============

Basic Usage
----------

.. code-block:: python

    from my_package import main_function
    result = main_function()
    print(result)

Advanced Usage
-------------

.. code-block:: python

    from my_package.core import advanced_function
    result = advanced_function(param1="value1", param2="value2")
    print(result)
""")
    
    def build_docs(self):
        """构建文档"""
        subprocess.run([
            "sphinx-build", "-b", "html",
            self.docs_dir, f"{self.docs_dir}/_build/html"
        ])

# 9. CI/CD配置
class CICDConfigurator:
    """CI/CD配置类"""
    def __init__(self):
        self.github_dir = ".github/workflows"
    
    def configure_github_actions(self):
        """配置GitHub Actions"""
        if not os.path.exists(self.github_dir):
            os.makedirs(self.github_dir)
        
        with open(f"{self.github_dir}/build.yml", "w") as f:
            f.write("""
name: Build and Test

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    - name: Run tests
      run: |
        pytest
    - name: Build package
      run: |
        python -m build
""")
    
    def configure_test_workflow(self):
        """配置测试工作流"""
        with open(f"{self.github_dir}/test.yml", "w") as f:
            f.write("""
name: Test

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    - name: Run tests with coverage
      run: |
        pytest --cov=my_package --cov-report=xml
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v2
      with:
        file: ./coverage.xml
""")
    
    def configure_release_workflow(self):
        """配置发布工作流"""
        with open(f"{self.github_dir}/release.yml", "w") as f:
            f.write("""
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: |
        python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        twine upload dist/*
""")

# 10. 发布清单
class PublishingChecklist:
    """发布清单类"""
    def __init__(self):
        self.package_name = "my_package"
        self.version = "1.0.0"
    
    def update_version(self):
        """更新版本号"""
        version_manager = VersionManager()
        version_manager.bump_version("patch")
    
    def update_changelog(self):
        """更新变更日志"""
        with open("CHANGELOG.md", "a") as f:
            f.write(f"""
## {self.version} ({datetime.now().strftime('%Y-%m-%d')})

### Added
- 新功能1
- 新功能2

### Changed
- 改进1
- 改进2

### Fixed
- 修复1
- 修复2
""")
    
    def run_test_suite(self):
        """运行测试套件"""
        tester = PackageTester()
        tester.run_unit_tests()
        tester.run_integration_tests()
        tester.check_test_coverage()
    
    def check_documentation(self):
        """检查文档"""
        doc_manager = DocumentationManager()
        doc_manager.build_docs()
    
    def validate_publishing(self):
        """验证发布"""
        builder = PackageBuilder()
        builder.build_package()
        if not builder.check_build():
            raise Exception("构建验证失败")
        
        publisher = PyPIPublisher()
        publisher.upload_to_test_pypi()
        publisher.verify_upload(self.package_name, self.version)

# 测试代码
if __name__ == "__main__":
    # 测试包构建
    builder = PackageBuilder()
    builder.install_build_tools()
    builder.build_package()
    
    # 测试版本管理
    version_manager = VersionManager()
    version_manager.install_bumpversion()
    version_manager.configure_version()
    
    # 测试文档管理
    doc_manager = DocumentationManager()
    doc_manager.install_doc_tools()
    doc_manager.create_doc_structure()
    
    # 测试CI/CD配置
    cicd = CICDConfigurator()
    cicd.configure_github_actions()
    
    # 测试发布清单
    checklist = PublishingChecklist()
    checklist.update_version()
    checklist.update_changelog() 