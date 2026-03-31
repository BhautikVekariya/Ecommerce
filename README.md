📌 Overview

This is a full-stack E-commerce web application built using Django. It allows users to browse products, manage a cart, and securely place orders using online payments via Razorpay. Admins can manage products, inventory, and orders efficiently.

🚀 Features
👤 User Features
User registration & login authentication
Browse products with details
Add/remove items from cart
Secure checkout with Razorpay payment gateway
Place orders & view order history

🛠️ Admin Features
Add, update, delete products
Manage inventory
Track customer orders
Django Admin Dashboard

💳 Payment Integration
Integrated Razorpay Payment Gateway for secure transactions
Supports online payments (UPI, cards, net banking, wallets)
Order verification using Razorpay API

🧑‍💻 Tech Stack
Backend: Python, Django
Frontend: HTML, CSS, JavaScript
Database: SQLite / MySQL
Payment Gateway: Razorpay
Others: Django ORM, Bootstrap

📂 Project Structure
ecommerce/
│── manage.py
│── ecommerce/
│── store/
│── users/
│── templates/
│── static/
│── db.sqlite3

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/ecommerce-django.git
cd ecommerce-django
2️⃣ Create virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add Razorpay Keys

Create a .env file or update settings:

RAZORPAY_KEY_ID = 'your_key_id'
RAZORPAY_KEY_SECRET = 'your_key_secret'
5️⃣ Apply migrations
python manage.py migrate
6️⃣ Create superuser
python manage.py createsuperuser
7️⃣ Run the server
python manage.py runserver

🌐 Usage
Home: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

📊 Key Learnings
Payment gateway integration (Razorpay)
Secure transaction handling
Django backend & database design
Full-stack application development

🔮 Future Improvements
Order tracking system
Email notifications
Product reviews & ratings
REST API (Django REST Framework)
