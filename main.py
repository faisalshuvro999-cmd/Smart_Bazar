import sys
import tkinter as tk
from tkinter import messagebox

from database.seed import setup_database
from utils.theme import init_theme


def fatal(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("SmartBazar - Database error", message)
    root.destroy()
    sys.exit(1)


def main():
    # Creates the database, tables and sample data if they do not exist yet.
    try:
        setup_database()
    except Exception as exc:
        fatal(
            "Cannot connect to PostgreSQL.\n\n"
            "1. Make sure PostgreSQL is running.\n"
            "2. Check DB_HOST, DB_PORT, DB_USER and DB_PASSWORD in your .env file.\n\n"
            f"Details: {str(exc).strip()[:400]}"
        )

    init_theme()
    from ui.app import App  # imported after the theme is initialised

    App().mainloop()


if __name__ == "__main__":
    main()