# 项目结构练习题参考答案

# 1. 标准项目结构
"""
my_project/
    my_package/
        __init__.py
        core.py
        utils.py
        cli.py
    tests/
        __init__.py
        test_core.py
        test_utils.py
    docs/
        conf.py
        index.rst
        api.rst
    examples/
        basic_usage.py
        advanced_usage.py
    README.md
    LICENSE
    setup.py
    requirements.txt
    requirements-dev.txt
"""

# 2. 配置文件管理
"""
my_project/
    my_package/
        config/
            __init__.py
            base.py
            development.py
            testing.py
            production.py
"""

# config/base.py
"""
\"\"\"基础配置\"\"\"

DEBUG = False
TESTING = False
SECRET_KEY = "your-secret-key"
DATABASE_URL = "sqlite:///app.db"
"""

# config/development.py
"""
\"\"\"开发环境配置\"\"\"

from .base import *

DEBUG = True
DATABASE_URL = "sqlite:///dev.db"
"""

# config/testing.py
"""
\"\"\"测试环境配置\"\"\"

from .base import *

TESTING = True
DATABASE_URL = "sqlite:///test.db"
"""

# config/production.py
"""
\"\"\"生产环境配置\"\"\"

from .base import *

DATABASE_URL = "postgresql://user:pass@localhost/dbname"
"""

# 3. 资源文件管理
"""
my_project/
    my_package/
        resources/
            templates/
                base.html
                index.html
            static/
                css/
                    style.css
                js/
                    main.js
                images/
                    logo.png
            data/
                config.json
                sample.csv
            i18n/
                en/
                    messages.po
                zh/
                    messages.po
"""

# 4. 测试组织
"""
my_project/
    tests/
        unit/
            __init__.py
            test_core.py
            test_utils.py
        integration/
            __init__.py
            test_api.py
            test_database.py
        functional/
            __init__.py
            test_workflows.py
        performance/
            __init__.py
            test_load.py
            test_stress.py
        conftest.py
        pytest.ini
"""

# conftest.py
"""
import pytest
from my_package import create_app

@pytest.fixture
def app():
    \"\"\"创建测试应用\"\"\"
    app = create_app("testing")
    return app

@pytest.fixture
def client(app):
    \"\"\"创建测试客户端\"\"\"
    return app.test_client()
"""

# pytest.ini
"""
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --cov=my_package
"""

# 5. 文档管理
"""
my_project/
    docs/
        api/
            core.rst
            utils.rst
        usage/
            getting_started.rst
            advanced.rst
        development/
            setup.rst
            contributing.rst
        deployment/
            installation.rst
            configuration.rst
        conf.py
        index.rst
        Makefile
"""

# conf.py
"""
import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = "My Project"
copyright = "2023, Your Name"
author = "Your Name"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

html_theme = "sphinx_rtd_theme"
"""

# index.rst
"""
Welcome to My Project's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage/getting_started
   usage/advanced
   api/core
   api/utils
   development/setup
   development/contributing
   deployment/installation
   deployment/configuration

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

# 6. 日志管理
"""
my_project/
    my_package/
        logging/
            __init__.py
            config.py
            handlers.py
            formatters.py
        logs/
            app.log
            error.log
            access.log
"""

# logging/config.py
"""
import logging
from .handlers import RotatingFileHandler
from .formatters import CustomFormatter

def setup_logging():
    \"\"\"配置日志系统\"\"\"
    # 创建根日志记录器
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # 添加控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomFormatter())
    root_logger.addHandler(console_handler)
    
    # 添加文件处理器
    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=1024*1024,
        backupCount=5
    )
    file_handler.setFormatter(CustomFormatter())
    root_logger.addHandler(file_handler)
    
    # 添加错误日志处理器
    error_handler = RotatingFileHandler(
        "logs/error.log",
        maxBytes=1024*1024,
        backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(CustomFormatter())
    root_logger.addHandler(error_handler)
"""

# 7. 错误处理
"""
my_project/
    my_package/
        exceptions/
            __init__.py
            base.py
            api.py
            database.py
"""

# exceptions/base.py
"""
class AppError(Exception):
    \"\"\"应用基础异常\"\"\"
    pass

class ValidationError(AppError):
    \"\"\"验证错误\"\"\"
    pass

class ConfigurationError(AppError):
    \"\"\"配置错误\"\"\"
    pass
"""

# exceptions/api.py
"""
from .base import AppError

class APIError(AppError):
    \"\"\"API错误\"\"\"
    pass

class AuthenticationError(APIError):
    \"\"\"认证错误\"\"\"
    pass

class AuthorizationError(APIError):
    \"\"\"授权错误\"\"\"
    pass
"""

# exceptions/database.py
"""
from .base import AppError

class DatabaseError(AppError):
    \"\"\"数据库错误\"\"\"
    pass

class ConnectionError(DatabaseError):
    \"\"\"连接错误\"\"\"
    pass

class QueryError(DatabaseError):
    \"\"\"查询错误\"\"\"
    pass
"""

# 8. 国际化
"""
my_project/
    my_package/
        i18n/
            __init__.py
            translations.py
            locales/
                en/
                    LC_MESSAGES/
                        messages.po
                        messages.mo
                zh/
                    LC_MESSAGES/
                        messages.po
                        messages.mo
"""

# translations.py
"""
import os
import gettext

class Translations:
    \"\"\"国际化翻译类\"\"\"
    def __init__(self):
        self.translations = {}
        self.load_translations()
    
    def load_translations(self):
        \"\"\"加载翻译\"\"\"
        locales_dir = os.path.join(os.path.dirname(__file__), "locales")
        for lang in os.listdir(locales_dir):
            if os.path.isdir(os.path.join(locales_dir, lang)):
                self.translations[lang] = gettext.translation(
                    "messages",
                    os.path.join(locales_dir, lang),
                    ["LC_MESSAGES"]
                )
    
    def gettext(self, message, lang="en"):
        \"\"\"获取翻译\"\"\"
        if lang in self.translations:
            return self.translations[lang].gettext(message)
        return message
"""

# 9. 命令行界面
"""
my_project/
    my_package/
        cli/
            __init__.py
            commands.py
            errors.py
"""

# commands.py
"""
import click
from ..core import process_data
from ..utils import validate_input

@click.group()
def cli():
    \"\"\"命令行工具\"\"\"
    pass

@cli.command()
@click.option("--input", "-i", required=True, help="输入文件")
@click.option("--output", "-o", required=True, help="输出文件")
def process(input, output):
    \"\"\"处理数据\"\"\"
    try:
        validate_input(input)
        process_data(input, output)
        click.echo("处理完成")
    except Exception as e:
        click.echo(f"错误: {str(e)}", err=True)
        raise click.Abort()

@cli.command()
@click.option("--config", "-c", required=True, help="配置文件")
def configure(config):
    \"\"\"配置应用\"\"\"
    try:
        # 配置逻辑
        click.echo("配置完成")
    except Exception as e:
        click.echo(f"错误: {str(e)}", err=True)
        raise click.Abort()
"""

# 10. 最佳实践
class ProjectStructure:
    """项目结构类"""
    def __init__(self):
        self.project_name = "my_project"
        self.package_name = "my_package"
    
    def create_directory_structure(self):
        """创建目录结构"""
        directories = [
            f"{self.project_name}/{self.package_name}",
            f"{self.project_name}/tests",
            f"{self.project_name}/docs",
            f"{self.project_name}/examples",
            f"{self.project_name}/{self.package_name}/config",
            f"{self.project_name}/{self.package_name}/resources",
            f"{self.project_name}/{self.package_name}/logging",
            f"{self.project_name}/{self.package_name}/exceptions",
            f"{self.project_name}/{self.package_name}/i18n",
            f"{self.project_name}/{self.package_name}/cli",
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def create_initial_files(self):
        """创建初始文件"""
        files = [
            f"{self.project_name}/README.md",
            f"{self.project_name}/LICENSE",
            f"{self.project_name}/setup.py",
            f"{self.project_name}/requirements.txt",
            f"{self.project_name}/requirements-dev.txt",
            f"{self.project_name}/{self.package_name}/__init__.py",
            f"{self.project_name}/tests/__init__.py",
            f"{self.project_name}/docs/conf.py",
            f"{self.project_name}/docs/index.rst",
        ]
        
        for file in files:
            with open(file, "w") as f:
                f.write(f"# {os.path.basename(file)}\n")
    
    def setup_git(self):
        """设置Git"""
        gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Logs
logs/
*.log

# Documentation
docs/_build/
"""
        
        with open(f"{self.project_name}/.gitignore", "w") as f:
            f.write(gitignore_content)
    
    def create_project(self):
        """创建项目"""
        self.create_directory_structure()
        self.create_initial_files()
        self.setup_git()
        print(f"项目 {self.project_name} 创建完成！")

# 测试代码
if __name__ == "__main__":
    # 创建项目结构
    project = ProjectStructure()
    project.create_project()
    
    # 测试配置加载
    from my_package.config import development
    print(f"Debug mode: {development.DEBUG}")
    
    # 测试日志配置
    from my_package.logging.config import setup_logging
    setup_logging()
    
    # 测试异常处理
    from my_package.exceptions.api import AuthenticationError
    try:
        raise AuthenticationError("Invalid credentials")
    except AuthenticationError as e:
        print(f"Caught error: {e}")
    
    # 测试国际化
    from my_package.i18n.translations import Translations
    translations = Translations()
    print(translations.gettext("Hello", "zh"))
    
    # 测试命令行
    from my_package.cli.commands import cli
    cli() 