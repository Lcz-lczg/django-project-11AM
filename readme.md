<!-- by 樊宇洋 -->
# Smart Learning & Connectivity Portal

## 🧾 project introduction  
This project is developed using the Django framework, integrating three core functional modules to support educational administration and service-oriented enterprise portal development. The system features a well-designed modular architecture, offering comprehensive and practical functionality. It facilitates the efficient integration of educational resources, precise management of personnel data, and the online presentation and interactive delivery of services, enabling enterprises and educational institutions to excel in digital transformation and realize an efficient and intelligent evolution of business processes.

## ✨ Core Modules

### 1. Course & Student Management (coursestudent)
- **Admin Backend for Information Management**: Provides a centralized backend system for managing course and student data, supporting efficient CRUD operations (create, read, update, delete) by administrative staff, ensuring data accuracy and integrity.
- **Course List Display**: The course list page at `/coursestudent/` presents essential course details—such as course name, instructor, and schedule—in a clear and user-friendly format, enabling students and parents to easily browse available classes.
- **Fee & Enrollment Information View**: The student fee and course enrollment page at `/coursestudent/stuinfo/` displays payment status and detailed course enrollment records, enhancing transparency in financial and academic management.

### 2. Visitor Services (guestapp)
- **Information Collection Form**: Features a streamlined and user-friendly form for collecting personal data from prospective students, enabling efficient and accurate data gathering to support follow-up communication and service delivery.
- **Integrated Calculator Tool**: Incorporates a built-in calculator module to address common computational requirements in daily teaching and administrative tasks, thereby enhancing operational efficiency.
- **HTTP Response Demonstration**: Demonstrates fundamental HTTP responses to help both technical and non-technical users understand data exchange mechanisms in web applications, supporting system integration and feature extension.

### 3. Parent Portal (parentsapp)
- **Responsive Institutional Portal**: Features a fully responsive web design, ensuring seamless access across various devices (mobile, tablet, desktop), allowing parents to stay updated with the latest news and announcements from schools or institutions anytime, anywhere.
- **Authentication & Authorization System**: Implements a secure user registration and login mechanism to protect parent accounts, offering personalized access points for retrieving child-specific academic data and school-related communications.
- **Service Showcase & Contact Form**: Includes a dedicated section for showcasing institutional services, along with an integrated contact form to streamline parent inquiries, feedback submissions, and appointment bookings.
- **Parent Dashboard Interface**: Provides a customized parent dashboard that consolidates key student data—such as academic progress, homework status, and exam performance—for quick and clear visibility into the child’s learning journey. An integrated notification system also alerts parents about upcoming events, deadlines, and important updates.
<!-- by 樊宇洋 -->
<!-- by 张清璐 -->
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

<!-- 李荣湖 -->
# 📁 Project Structure
django-project-11AM-main/
├── coursestudent/    # Course Management Module
├── guestapp/         # Guest Access Module
├── parentsapp/       # Primary Web Portal
│   ├── static/       # Static assets
│   └── templates/    # Web Template
└── manage.py         # System Management Script
<!-- 李荣湖 -->
<!-- by 张清璐 -->
<!-- by 樊宇洋 -->
# 🚀 Usage Tips
- **Stop the Development Server**: Press `Ctrl + C` in the terminal.
- **Production Deployment**: Use **Nginx + Gunicorn** for scalable and secure deployment in production environments.
- **Admin Access**: Log in using the administrator account created via the `createsuperuser` command.
<!-- by 樊宇洋 -->