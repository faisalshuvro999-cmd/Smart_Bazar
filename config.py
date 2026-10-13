import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

APP_NAME = "SmartBazar"
APP_VERSION = "1.0.0"
CURRENCY_SYMBOL = "৳"   # change to "Tk" if your font does not show ৳

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME", "smartbazar"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
}

EXPORT_DIR = os.path.join(BASE_DIR, "exports")
INVOICE_DIR = os.path.join(BASE_DIR, "invoices")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")

for _folder in (EXPORT_DIR, INVOICE_DIR, ASSETS_DIR):
    os.makedirs(_folder, exist_ok=True)