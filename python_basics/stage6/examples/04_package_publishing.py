# 包发布示例

# 1. setup.py文件示例
"""
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
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
            "mypackage=mypackage.cli:main",
        ],
    },
)
"""

# 2. MANIFEST.in文件示例
"""
include LICENSE
include README.md
include requirements.txt
recursive-include mypackage/tests *
recursive-exclude * __pycache__
recursive-exclude * *.py[cod]
"""

# 3. pyproject.toml文件示例
"""
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py36', 'py37', 'py38']
include = '\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3
"""

# 4. 包的构建
"""
# 安装构建工具
pip install build

# 构建包
python -m build

# 这将创建dist目录，包含：
# - mypackage-1.0.0.tar.gz (源码分发包)
# - mypackage-1.0.0-py3-none-any.whl (轮子分发包)
"""

# 5. PyPI发布
"""
# 安装twine
pip install twine

# 上传到PyPI
twine upload dist/*

# 上传到测试PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
"""

# 6. 版本管理
"""
# 使用bumpversion管理版本
pip install bumpversion

# 在setup.cfg中配置
[bumpversion]
current_version = 1.0.0
commit = True
tag = True

[bumpversion:file:setup.py]
search = version="1.0.0"
replace = version="{new_version}"

# 更新版本
bumpversion patch  # 1.0.0 -> 1.0.1
bumpversion minor  # 1.0.1 -> 1.1.0
bumpversion major  # 1.1.0 -> 2.0.0
"""

# 7. 包的测试
"""
# 安装测试依赖
pip install pytest pytest-cov

# 运行测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=mypackage
"""

# 8. 包的文档
"""
# 安装文档工具
pip install sphinx sphinx-rtd-theme

# 初始化文档
sphinx-quickstart

# 构建文档
cd docs
make html
"""

# 9. 包的CI/CD
"""
# .github/workflows/publish.yml
name: Publish Package

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build and publish
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: |
        python -m build
        twine upload dist/*
"""

# 10. 包发布检查清单
"""
1. 更新版本号
2. 更新CHANGELOG.md
3. 运行测试
4. 检查文档
5. 构建包
6. 测试安装
7. 上传到PyPI
8. 创建GitHub发布
9. 更新文档网站
10. 通知用户
"""

# 测试代码
if __name__ == "__main__":
    print("包发布示例")
    print("请参考注释中的示例代码和最佳实践") 