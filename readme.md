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


# 🚀 Usage Tips
- **Stop the Development Server**: Press `Ctrl + C` in the terminal.
- **Production Deployment**: Use **Nginx + Gunicorn** for scalable and secure deployment in production environments.
- **Admin Access**: Log in using the administrator account created via the `createsuperuser` command.
=======
This project is developed using the Django framework, integrating three core functional modules, and aims to facilitate the development of educational management systems and service-oriented enterprise portals. Its modular architecture design is comprehensive and practical. Whether it is the efficient integration of educational resources, the precise management of personnel information, or the online display and interaction of service projects, it can be easily handled, helping enterprises and educational institutions to excel in digital transformation and realize the efficient and intelligent transformation of business processes.

## ✨ Core Modules

### 1. Course student management (coursestudent)
- **Admin Backend for Information Management**: Provide a comprehensive management background of curriculum and student information, which is convenient for managers to efficiently enter, query and update relevant information to ensure the accuracy and integrity of data.
- **Course list display**: Through the course list display page (/coursestudent/), the basic information of all courses, including course names, teachers, class times, etc., is intuitively displayed, which is convenient for students and parents to quickly browse the course schedule.
- **Student Fee & Enrollment View**: On the student fee and payment and enrollment details page (/coursestudent/stuinfo/), students' payment status and detailed related information of selected courses are clearly displayed, making cost management and course selection more transparent.
### 2. Visitor service (guestapp)
- **Information collection form**: The design of a streamlined and user-friendly student information collection form is used to quickly and accurately collect the personal data of prospective students and provide basic data support for subsequent communication and services.
- **Digital calculator function**: built-in practical digital calculator function, which can meet the routine computational requirements of daily teaching and management and improve work efficiency.
- **HTTP response demonstration**: Provide basic HTTP response demonstration to help technicians and non-technical personnel better understand the data interaction process in Web development, and facilitate system integration and function expansion.

### 3. Parent portal (parentsapp)
- **Responsive enterprise portal**: Build a responsive enterprise portal to ensure that parents can ensures seamless access across multiple devices on various devices (such as mobile phones, tablets, computers) and keep abreast of the latest developments of schools and enterprises anytime and anywhere.
- **User registration/login system**: Secure user authentication system ensures the security of parents' accounts, and provides personalized service entrances for parents to facilitate their access to educational information related to their children.
- **Service display and contact form**: Includes a dedicated section for service presentation, introduce the various institutional services of educational institutions in detail, and provide contact forms to facilitate parents to consult questions, make suggestions or make appointments and register.
- **Customer dashboard management**: Create an exclusive Parent Dashboard Interface for parents, integrate students' learning progress, homework, exam results and other key information, so that parents can grasp their children's learning status at a glance. At the same time, they can also set up a notification system to notify parents of important educational activities and matters in time.

## 📦 Requirements


## 🛠️ Installation steps

# 📁 Project Structure

# 🚀 Usage Tips
- Access the admin backend, log in with the created administrator account, press Ctrl+C to stop the development server

- It is recommended to deploy using Nginx and Gunicorn deployment in the production environment
