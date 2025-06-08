# 依赖管理示例

# 1. requirements.txt文件示例
"""
# requirements.txt
requests==2.28.1
numpy>=1.21.0
pandas~=1.4.0
matplotlib>=3.5.0,<3.6.0
scikit-learn==1.0.2
"""

# 2. 虚拟环境管理
"""
# 创建虚拟环境
python -m venv myenv

# 激活虚拟环境
# Windows:
myenv\Scripts\activate
# Unix/MacOS:
source myenv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 导出依赖
pip freeze > requirements.txt
"""

# 3. pip命令示例
"""
# 安装包
pip install package_name

# 安装特定版本
pip install package_name==1.0.0

# 升级包
pip install --upgrade package_name

# 卸载包
pip uninstall package_name

# 查看已安装的包
pip list

# 查看包信息
pip show package_name
"""

# 4. 依赖版本控制
"""
# 版本说明符
package_name==1.0.0  # 精确版本
package_name>=1.0.0  # 最低版本
package_name~=1.0.0  # 兼容版本
package_name!=1.0.0  # 排除版本
"""

# 5. 依赖冲突解决
"""
# 1. 使用虚拟环境隔离项目
# 2. 明确指定依赖版本
# 3. 使用pip-tools管理依赖
# 4. 定期更新依赖
# 5. 使用依赖分析工具
"""

# 6. 使用pip-tools
"""
# 安装pip-tools
pip install pip-tools

# 创建requirements.in
echo "requests>=2.28.0" > requirements.in
echo "numpy>=1.21.0" >> requirements.in

# 生成requirements.txt
pip-compile requirements.in

# 同步依赖
pip-sync requirements.txt
"""

# 7. 使用conda管理依赖
"""
# 创建环境
conda create -n myenv python=3.9

# 激活环境
conda activate myenv

# 安装包
conda install package_name

# 导出环境
conda env export > environment.yml

# 从文件创建环境
conda env create -f environment.yml
"""

# 8. 使用poetry管理依赖
"""
# 安装poetry
curl -sSL https://install.python-poetry.org | python3 -

# 初始化项目
poetry init

# 添加依赖
poetry add package_name

# 安装依赖
poetry install

# 更新依赖
poetry update
"""

# 9. 使用pipenv管理依赖
"""
# 安装pipenv
pip install pipenv

# 安装依赖
pipenv install package_name

# 激活环境
pipenv shell

# 安装开发依赖
pipenv install --dev package_name

# 生成Pipfile.lock
pipenv lock
"""

# 10. 依赖管理最佳实践
"""
1. 使用虚拟环境
2. 明确指定依赖版本
3. 定期更新依赖
4. 使用依赖管理工具
5. 保持requirements.txt的更新
6. 使用依赖分析工具
7. 记录依赖变更
8. 测试依赖更新
9. 使用CI/CD自动化依赖管理
10. 文档化依赖管理流程
"""

# 测试代码
if __name__ == "__main__":
    print("依赖管理示例")
    print("请参考注释中的示例代码和最佳实践") 