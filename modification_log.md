### 🛠️ 详细安装步骤
克隆仓库：
```bash
git clone https://github.com/Lcz-lczg/django-project-11AM.git

## 配置说明
创建虚拟环境：
在项目根目录打开cmd，输入python -m venv venv
然后进入venv\Scripts\activate
-安装依赖：
```bash
- pip install -r requirements.txt
- 
迁移数据库：
```bash
python manage.py migrate
创建管理者账号
```bash
python manage.py createsuperuser
运行项目
```bash
python manage.py runserver
 ---
------

## 📁 项目结构
django-project-11AM-main/
├── coursestudent/    # 课程管理模块
├── guestapp/         # 访客功能模块
├── parentsapp/       # 主门户系统
│   ├── static/       # CSS/JS/图片资源
│   └── templates/    # 网页模板
└── manage.py         # 管理脚本

ai修改后：
🛠️ 安装步骤
1. 克隆仓库
git clone https://github.com/Lcz-lczg/django-project-11AM.git
cd django-project-11AM
2. 配置虚拟环境
# 创建虚拟环境
python -m venv venv

# 激活环境

.\venv\Scripts\activate


source venv/bin/activate
3. 安装依赖
pip install -r requirements.txt
注意：若路径不同请指定完整路径

4. 数据库迁移
python manage.py makemigrations
python manage.py migrate
5. 创建管理员
python manage.py createsuperuser
6. 运行项目
python manage.py runserver
📁 项目结构
django-project-11AM-main/
├── coursestudent/    # 课程管理
├── guestapp/         # 访客功能
├── parentsapp/       # 主门户系统
│   ├── static/       # 静态资源
│   └── templates/    # 网页模板
└── manage.py         # 管理脚本
    
🚀 使用提示
访问 管理后台 使用创建的管理员账号登录
按 Ctrl+C 停止开发服务器
生产环境建议使用 Nginx + Gunicorn 部署