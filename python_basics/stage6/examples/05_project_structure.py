# 项目结构示例

# 1. 标准项目结构
"""
myproject/
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── MANIFEST.in
├── myproject/
│   ├── __init__.py
│   ├── core.py
│   ├── utils.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── api.rst
└── examples/
    └── example.py
"""

# 2. 配置文件管理
"""
# config.py
import os
from pathlib import Path

class Config:
    # 基础配置
    BASE_DIR = Path(__file__).parent.parent
    DEBUG = False
    TESTING = False
    
    # 数据库配置
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
    
    # 日志配置
    LOG_LEVEL = "INFO"
    LOG_FILE = BASE_DIR / "logs" / "app.log"
    
    @classmethod
    def init_app(cls, app):
        # 初始化应用配置
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = "DEBUG"

class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = "sqlite:///:memory:"

class ProductionConfig(Config):
    LOG_LEVEL = "WARNING"

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
"""

# 3. 资源文件管理
"""
# 资源文件结构
myproject/
├── myproject/
│   ├── resources/
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   └── index.html
│   │   ├── static/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   └── images/
│   │   └── data/
│   │       ├── config.json
│   │       └── i18n/
│   │           ├── en.json
│   │           └── zh.json
"""

# 4. 测试组织
"""
# tests/conftest.py
import pytest
from myproject import create_app

@pytest.fixture
def app():
    app = create_app("testing")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# tests/test_core.py
def test_core_functionality(client):
    response = client.get("/")
    assert response.status_code == 200

# tests/test_utils.py
def test_utility_function():
    from myproject.utils import some_function
    assert some_function() == expected_result
"""

# 5. 文档管理
"""
# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = "MyProject"
copyright = "2023, Your Name"
author = "Your Name"
version = "1.0.0"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# docs/index.rst
Welcome to MyProject's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   usage
   contributing
"""

# 6. 日志管理
"""
# myproject/utils/logging.py
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    
    handler = RotatingFileHandler(
        log_file,
        maxBytes=10000000,
        backupCount=5
    )
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger
"""

# 7. 错误处理
"""
# myproject/utils/errors.py
class MyProjectError(Exception):
    """基础异常类"""
    pass

class ValidationError(MyProjectError):
    """验证错误"""
    pass

class DatabaseError(MyProjectError):
    """数据库错误"""
    pass

def handle_error(error):
    """错误处理函数"""
    if isinstance(error, ValidationError):
        return {"error": "validation_error", "message": str(error)}
    elif isinstance(error, DatabaseError):
        return {"error": "database_error", "message": str(error)}
    else:
        return {"error": "internal_error", "message": str(error)}
"""

# 8. 国际化
"""
# myproject/utils/i18n.py
import json
from pathlib import Path

class I18n:
    def __init__(self, locale="en"):
        self.locale = locale
        self.translations = {}
        self.load_translations()
    
    def load_translations(self):
        i18n_dir = Path(__file__).parent.parent / "resources" / "data" / "i18n"
        for file in i18n_dir.glob("*.json"):
            locale = file.stem
            with open(file, "r", encoding="utf-8") as f:
                self.translations[locale] = json.load(f)
    
    def translate(self, key, **kwargs):
        if self.locale in self.translations:
            text = self.translations[self.locale].get(key, key)
            return text.format(**kwargs)
        return key
"""

# 9. 命令行接口
"""
# myproject/cli.py
import click

@click.group()
def cli():
    """MyProject命令行工具"""
    pass

@cli.command()
@click.option("--config", default="config.json", help="配置文件路径")
def run(config):
    """运行应用"""
    click.echo(f"使用配置文件: {config}")
    # 运行应用逻辑

@cli.command()
@click.option("--port", default=5000, help="服务器端口")
def serve(port):
    """启动开发服务器"""
    click.echo(f"启动服务器在端口: {port}")
    # 启动服务器逻辑
"""

# 10. 项目结构最佳实践
"""
1. 使用清晰的目录结构
2. 分离配置和代码
3. 使用相对导入
4. 保持模块独立性
5. 使用适当的命名约定
6. 组织测试结构
7. 管理资源文件
8. 提供完整的文档
9. 实现错误处理
10. 支持国际化
"""

# 测试代码
if __name__ == "__main__":
    print("项目结构示例")
    print("请参考注释中的示例代码和最佳实践") 