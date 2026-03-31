📌 Overview

This is a full-stack E-commerce web application built using Django. It allows users to browse products, manage their cart, and securely place orders using Razorpay. Admins can efficiently manage products, inventory, and orders.

🚀 Features

👤 User Features
User registration & authentication
Browse products with details
Add/remove items from cart
Secure checkout with Razorpay
View order history

🛠️ Admin Features
Add, update, delete products
Manage inventory
Track customer orders
Django Admin Dashboard

💳 Payment Integration
Razorpay payment gateway integration
Supports UPI, cards, net banking, wallets
Secure payment verification using API

🧑‍💻 Tech Stack
Layer	Technology
Backend	Python, Django
Frontend	HTML, CSS, JavaScript
Database	SQLite / MySQL
Payment	Razorpay
Others	Django ORM, Bootstrap

📂 Project Structure
ecommerce/
│── manage.py
│── ecommerce/        # Project settings
│── store/            # Products & cart logic
│── users/            # Authentication
│── templates/        # HTML files
│── static/           # CSS, JS, Images
│── db.sqlite3

⚙️ Installation & Setup

1. Clone the repository
git clone https://github.com/your-username/ecommerce-django.git
cd ecommerce-django

2. Create virtual environment
python -m venv env

3. Install dependencies
pip install -r requirements.txt

6. Run migrations
python manage.py migrate

8. Create superuser
python manage.py createsuperuser

10. Start server
python manage.py runserver

🌐 Usage
Home: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

📊 Key Learnings
Payment gateway integration (Razorpay)
Secure transaction handling
Backend & database design
Full-stack development

🔮 Future Improvements
Order tracking system
Email notifications
Product reviews & ratings
REST API (DRF)
