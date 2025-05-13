
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

## 📁 项目结构
django-project-11AM-main/
├── coursestudent/    # 课程管理模块
├── guestapp/         # 访客功能模块
├── parentsapp/       # 主门户系统
│   ├── static/       # CSS/JS/图片资源
│   └── templates/    # 网页模板
└── manage.py         # 管理脚本
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
（利用ai对内容进行润色，修饰）
```
# 智学智联门户说明书
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


樊宇洋修改：
修改前：
```
## project introduction
- This project is carefully built on the Django framework, integrating three core functional modules, and aims to provide strong support for the development of educational management and service-oriented enterprise portals. Its functional module design is comprehensive and practical. Whether it is the efficient integration of educational resources, the fine management of personnel information, or the online display and interactionof service projects, it can be easily handled, helping enterprises and educational institutionsto stand out in digital operation and realize the efficient and intelligent transformation of business processes.

### 1. Course student management (coursestudent)
- **Informationmanagement background**:Provide a comprehensive management background of curriculum and student information, which is convenient for managers to efficiently enter, query and update relevant information to ensure the accuracy and integrity of data.
- **Course list display**:Through the course list display page(/coursestudent/), the basic information of all courses, including course names,teachers, class times, etc., is intuitively displayed, which is convenient for students and parents to quickly browse the course schedule.
- **Fee and related viewing**:On the student fee and course related viewing page (/coursestudent/stuinfo/), students' payment status and detailed related information of selected courses are clearly displayed, making cost management and course selection more transparent.

### 2. Visitor service (guestapp)
- **Information collection form**:The design of a simple and easy-to-use student information collection form is used to quickly and accurately collect the personal data of visiting students and provide basic data support for subsequent communication and services.
- **Digital calculator function**:built-in practical digital calculator function, which can meet the simple calculation needs of daily teachingand management and improve work efficiency.
- **HTTP response demonstration**: Provide basicHTTP response demonstration to help techniciansand non-technical personnel better understand the data interaction process in Web development, and facilitate system integration and function expansion.

### 3. Parent portal (parentsapp)
- **Responsive enterprise portal**: Build a responsive enterprise portal to ensure that parentscan get a good access experience on various devices (such as mobile phones, tablets, computers) and keep abreast of the latest developments of schools and enterprises anytime and anywhere.
- **User registration/login system**: a perfect user registration/login system ensures the security of parents' accounts,and provides personalized service entrances for parents to facilitate their access to educational information related to their children.
- **Service display and contact form**: Set up aservice display area,introduce the various service contents of educational institutions in detail, and provide contact forms to facilitate parents to consult questions,make suggestions or make appointments and register.
- **Customer dashboard management**: Create an exclusive customer dashboard for parents, integrate students' learning progress, homework, exam results and other keyinformation, so that parents can grasp their children's learning status ata glance. At the same time, they can also set up a reminder function to notify parents of important educational activities and matters in time.

# Usage Tips
- Access the management background, log in with the created administrator account, press Ctrl+C to stop the development server
- It is recommended to use Nginx + Gunicorn deployment in the production environment
```

修改后：
(用AI将一些词组替换成计算机专业名词）
```
## project introduction
- This project is developed using the Django framework, integrating three core functional modulesto facilitate the development of educational management systems and service-oriented enterpriseportals. The system features a well-designed modular architecture, offering both comprehensiveness and practicality in functionality. Whether itinvolves the efficient integration of educational resources, the precise management of personneldata, or the online presentation and interactivedelivery of services, the system effectively supports these key functionalities. It empowers organizations to excel in digital transformation and achieve an efficient and intelligent evolutionof business processes.

### 1. Course student management (coursestudent)
- **Admin Backend for Information Management**:Provides a centralized interface for managing curriculum and student data, allowing administrators to easily input, query, and update information to ensure data accuracy and integrity.
- **Course List Display**: The course list page at `/coursestudent/`presents essential course details-including course name,instructor, and schedule-in an intuitive and user-friendly format,allowing students and parents to easily browse available courses and schedules.
- **student Fee & Enrollment View**: The paymentand course enrollment details page at `/coursestudent/stuinfo/` displays students'payment status and associated course records, enhancing transparency in financial and academic management.

### 2. Visitor service (guestapp)
- **Information Collection Form**:Features a streamlined and user-friendly form for collecting personal data from prospective students, enabling efficient and accurate data gathering to support follow-up communication and service delivery.
- **Integrated Calculator Tool**: Includes a built-in calculator module to address routine computational needs in daily teaching and administrative tasks, thereby enhancing operational efficiency.
- **HTTP Response Demonstration**: Demonstrates fundamental HTTP responses to help both technical and non-technical users understand data exchange mechanisms in web applications, supporting system integration and feature extension.

### 3. Parent portal (parentsapp)
- **Responsive Enterprise Portal**:Features a fully responsive enterprise portal, ensuring seam less access across multiple devices (mobile, tablet, desktop), allowing parents to stay updated with the latest news and announcements from schools and institutions anytime, anywhere.
- **User Authentication System**:Implements a secure user registration and login mechanism to protect parent accounts, offering personalized access points for retrieving child-specific academic data and school-related communications.
- **Service Showcase & Contact Form**:Includes a dedicated section for showcasing institutional services, along with integrated contact forms to streamline parent inquiries, feedback submission s, and appointment bookings.
- **Parent Dashboard Interface**: Provides a customized parent dashboard that aggregates studentperformance data-including academic progress, homework status, and exam scores-for quick visibility into the child's learning journey. An integrated notification system also alerts parents about upcoming events, deadlines, and important updates.

# Usage Tips
- To access the admin backend, log in using theadministrator account you created. During localdevelopment, press 'Ctrl + C' in the terminal to stop the server.
- For production environments, it is recommendedto deploy the application using **Nginx + Gunicorn** for better performance, scalability, and security.
```

李荣湖：
修改
```
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
```
张清璐修改：

修改前：
```
## 📦 Environment requires
- Python 3.8+
- Django 3.2+
- SQLite 3.0+

## 🛠️ Detailed installation steps
### 1. Clone repository
git clone https://github.com/Lcz-lczg/django-project-11AM.git cd django-project-11AM

## Configuration Description
### Create a virtual environment:
Open the project root file
cd django-project-11AM

Open cmd in the project root directory

1. Create Venv file input
- python -m venv venv

2. Enter the Venv virtual environment file
- cd venv

3. Enter Scripts
- cd Scripts（scripts）

4. Start the virtual environment
- Activate

5. Installation dependencies:
- pip install -r requirements.txt

6. Migrate the database:
- python manage.py

7. Create a manager account:
- python manage.py createsuperuser

8. Run the project:
- python manage.py runserver


# 📁 Project Structure
django-project-11AM-main/
├── coursestudent/    # Course management module
├── guestapp/         # Guest function module
├── parentsapp/       # Main portal system
│   ├── static/       # Static assets
│   └── templates/    # Web page template
└── manage.py         # Management script
```

修改后：
```
## 📦 System Requirements
- Python 3.8+
- Django 3.2+
- SQLite 3.0+

## 🛠️ Installation Instructions
### 1. Clone repository
git clone https://github.com/Lcz-lczg/django-project-11AM.git cd django-project-11AM

## Configuration Instructions
### Create a virtual environment:
Navigate to the project root directory
cd django-project-11AM

Open a terminal in the project root directory

1. Set up a venv for the project
- python -m venv venv

2. Activate the virtual environment (venv)
- cd venv

3. Navigate to the Scripts directory in the virtual environment
- cd Scripts（scripts）

4. Activate the virtual environment
- Activate

5. Install dependencies:
- pip install -r requirements.txt

6. Migrate the database:
- python manage.py

7. Create a superuser account:
- python manage.py createsuperuser

8. Launch the project:
- python manage.py runserver


# 📁 Project Structure
django-project-11AM-main/
├── coursestudent/    # Course Management Module
├── guestapp/         # Guest Access Module
├── parentsapp/       # Primary Web Portal
│   ├── static/       # Static assets
│   └── templates/    # Web Template
└── manage.py         # System Management Script
```

黄新浪修改前：
```
📁 项目结构
django-project-11AM-main/
├── coursestudent/    # 课程管理
├── guestapp/         # 访客功能
├── parentsapp/       # 主门户系统
│   ├── static/       # 静态资源
│   └── templates/    # 网页模板
└── manage.py         # 管理脚本
```
修改后：
```
## 📁 项目结构

django-project/

│

├── 📁 coursestudent/        # 课程管理模块

│   ├── models.py

│   └── views.py

│

├── 📁 guestapp/             # 访客功能模块

│   ├── models.py

│   └── views.py

│

├── 📁 parentsapp/            # 主门户系统

│   ├── 📁 static/            # 静态资源

│   │   ├── css/

│   │   ├── js/

│   │   └── images/

│   │

│   └── 📁 templates/         # 网页模板

│       ├── base.html

│       └── index.html

│
└── 📜 manage.py          # Django管理脚本
```



李青桦 修改
```
修改前：
用户认证→User Authentication
Django框架→Django Framework
虚拟环境→VirtualEnvironment
HTTP响应→HTTP Response
迁移数据库→DatabaseMigration


修改后：
| 中文术语         | 英文术语                   |
|------------------|---------------------------|
| 响应式设计       | Responsive Design         |
| 数据迁移         | Data Migration            |
| 用户认证         | User Authentication       |
| 静态资源         | Static Assets             |
| 虚拟环境         | Virtual Environment       |
| REST API         | REST API                  |
| 依赖安装         | Dependency Installation   |
| Django框架     | Django Framework        |
| HTTP响应       | HTTP Response           |
| 迁移数据库     | Database Migration      |
=======
```
