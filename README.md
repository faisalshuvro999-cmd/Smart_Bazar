# SmartBazar

Multi-vendor e-commerce management desktop app for Bangladesh.
Built with Python, CustomTkinter and PostgreSQL.

## Features
- Login with Admin / Staff roles (bcrypt password hashing)
- Dashboard: sales, orders, vendors, low-stock alerts, 7-day chart
- Vendors with commission %, approve / suspend
- Categories, Products with SKU and stock tracking
- Customers with Bangladesh divisions and districts, +880 phone validation
- Orders: cart, stock check, auto delivery charge (60 inside Dhaka, 120 outside)
- Payments: Cash on Delivery, bKash, Nagad, Rocket, Card
- Order status flow: Pending, Processing, Shipped, Delivered, Cancelled
- PDF invoices, CSV export, vendor commission and payout report
- Dark and light theme (remembered)

## Requirements
- Python 3.10 or newer
- PostgreSQL 13 or newer

## Setup
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. copy .env.example .env  (then edit your PostgreSQL password)
5. python main.py

The database, tables and sample data are created on first run.

## Default logins
- admin / admin123
- staff / staff123
Change these after the first login.

## Security
Never upload your .env file to GitHub or share it.