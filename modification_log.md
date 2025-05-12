吴和师修改：
```
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
<!-- 李荣湖 -->
## 📁 项目结构
django-project-11AM-main/
├── coursestudent/    # 课程管理模块
├── guestapp/         # 访客功能模块
├── parentsapp/       # 主门户系统
│   ├── static/       # CSS/JS/图片资源
│   └── templates/    # 网页模板
└── manage.py         # 管理脚本
##ai修改后：##
django-project/
│
├── 📁 coursestudent/  # Course Management Module
│   ├── 📄 models.py
│   └── 📄 views.py
│
├── 📁 guestapp/  # Guest Access Module
│   ├── 📄 models.py
│   └── 📄 views.py
│
├── 📁 parentsapp/  # Main Portal System
│   ├── 📁 static/  # Static Resources
│   │   ├── 📁 css/
│   │   ├── 📁 js/
│   │   └── 📁 images/
│   │
│   └── 📁 templates/  # HTML Templates
│       ├── 📄 base.html
│       └── 📄 index.html
│
└── 📄 manage.py  # Django Management Script
<!-- 李荣湖 -->
## ai修改后：##
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
```

梁超哲

修改：

改前：
```
 智学智联门户说明书
---
## 🧾 项目介绍
---
**本项目基于 Django 框架精心打造，集三大核心功能模块于一体，旨在为教育管理及服务型企业门户开发提供强大助力。其功能模块设计全面且实用，无论是教育资源的高效整合、人员信息的精细管理，还是服务项目的在线展示与交互，都能轻松应对，助力企业与教育机构在数字化运营中脱颖而出，实现业务流程的高效化与智能化转型。
**

---
## ✨ 功能模块介绍
---
### 1.课程学生管理 (coursestudent)
- 课程/学生信息管理后台
- 课程列表展示 (`/coursestudent/`)
- 学生费用及课程关联查看 (`/coursestudent/stuinfo/`)
---
### 2. 访客服务 (guestapp)
- 学生信息收集表单
- 数字计算器功能
- 基础HTTP响应演示
---
### 3. 家长门户 (parentsapp)
- 响应式企业门户网站
- 用户注册/登录系统
- 服务展示与联系表单
- 客户仪表盘管理
```
改后：
```
# 智学智联门户说明书
---
## 🧾 项目介绍
---
本项目基于 Django 框架精心打造，集三大核心功能模块于一体，旨在为教育管理及服务型企业门户开发提供强大助力。其功能模块设计全面且实用，无论是教育资源的高效整合、人员信息的精细管理，还是服务项目的在线展示与交互，都能轻松应对，助力企业与教育机构在数字化运营中脱颖而出，实现业务流程的高效化与智能化转型。


---
## ✨ 功能模块介绍
---
### 1.课程学生管理 (coursestudent)
信息管理后台 ：提供课程与学生信息的综合管理后台，方便管理人员高效录入、查询与更新相关信息，确保数据的准确性和完整性。

课程列表展示 ：通过课程列表展示页面（/coursestudent/），直观呈现所有开设课程的基本信息，包括课程名称、授课教师、上课时间等，便于学生和家长快速浏览课程安排。

费用及关联查看 ：在学生费用及课程关联查看页面（/coursestudent/stuinfo/），清晰展示学生的缴费情况以及所选课程的详细关联信息，让费用管理与课程选择更加透明。

---
### 2. 访客服务 (guestapp)

信息收集表单 ：设计简洁易用的学生信息收集表单，用于快速、准确地收集访客学生的个人资料，为后续的沟通和服务提供基础数据支持。

数字计算器功能 ：内置实用的数字计算器功能，满足日常教学、管理中的简单计算需求，提高工作效率。

HTTP 响应演示 ：提供基础 HTTP 响应演示，帮助技术人员和非技术人员更好地理解 Web 开发中的数据交互过程，便于进行系统集成和功能拓展。

---
### 3. 家长门户 (parentsapp)
响应式企业门户网站 ：构建响应式企业门户网站，确保家长在各种设备上（如手机、平板、电脑）都能获得良好的访问体验，随时随地了解学校和企业的最新动态。

用户注册 / 登录系统 ：完善的用户注册 / 登录系统，保障家长账户的安全性，同时为家长提供个性化的服务入口，方便他们访问与自己孩子相关的教育信息。

服务展示与联系表单 ：设置服务展示区域，详细介绍教育机构的各项服务内容，并提供联系表单，方便家长咨询问题、提出建议或进行预约报名等操作。

客户仪表盘管理 ：为家长打造专属的客户仪表盘，整合学生的学习进度、作业情况、考试成绩等关键信息，使家长能够一目了然地掌握孩子的学习状况，同时还可以设置提醒功能，及时通知家长重要的教育活动和事项。
```