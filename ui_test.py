import customtkinter as ctk

from ui.components.data_table import DataTable
from ui.components.form_dialog import FormDialog
from ui.components.message_box import ask_confirm, show_info
from ui.components.stat_card import StatCard
from utils.bd_data import get_districts, get_divisions
from utils.helpers import format_bdt
from utils.theme import COLORS, init_theme, toggle_theme

init_theme()
root = ctk.CTk()
root.title("SmartBazar UI test")
root.geometry("980x620")
root.configure(fg_color=COLORS["bg"])

ALL_ROWS = [
    {"id": i, "name": f"Product {i}", "price": 450 * i, "stock": (i * 3) % 12}
    for i in range(1, 21)
]

FIELDS = [
    {"key": "name", "label": "Name", "required": True, "placeholder": "Product name"},
    {"key": "division", "label": "Division", "type": "combo",
     "options": get_divisions(), "required": True},
    {"key": "district", "label": "District", "type": "combo",
     "depends_on": "division", "options_func": get_districts, "required": True},
    {"key": "note", "label": "Note", "type": "textarea"},
    {"key": "active", "label": "Active", "type": "switch"},
]

cards = ctk.CTkFrame(root, fg_color="transparent")
cards.pack(fill="x", padx=20, pady=(20, 10))
for col in range(3):
    cards.grid_columnconfigure(col, weight=1)
StatCard(cards, "Total Sales", format_bdt(1250000), icon="৳", accent="success").grid(
    row=0, column=0, sticky="ew", padx=(0, 8))
StatCard(cards, "Orders", "128", icon="#", accent="primary").grid(
    row=0, column=1, sticky="ew", padx=8)
StatCard(cards, "Low Stock", "5", icon="!", accent="warning").grid(
    row=0, column=2, sticky="ew", padx=(8, 0))


def search(text):
    text = text.lower()
    table.set_data([r for r in ALL_ROWS if text in r["name"].lower()])


def add_item():
    FormDialog(root, "Add Item", FIELDS, lambda values: print("Saved:", values))


def edit_item():
    row = table.get_selected()
    if not row:
        show_info(root, "Select a row", "Please click a row first.")
        return
    FormDialog(root, "Edit Item", FIELDS, lambda values: print("Updated:", values),
               initial={"name": row["name"], "division": "Dhaka", "district": "Gazipur"})


def delete_item():
    if ask_confirm(root, "Delete", "Delete the selected row?", danger=True):
        print("Delete confirmed")


table = DataTable(
    root,
    columns=[
        {"key": "id", "title": "ID", "width": 60},
        {"key": "name", "title": "Name", "width": 220},
        {"key": "price", "title": "Price", "width": 140, "anchor": "e", "fmt": format_bdt},
        {"key": "stock", "title": "Stock", "width": 90, "anchor": "center"},
    ],
    on_search=search,
    on_double_click=lambda row: print("Double-clicked:", row["name"]),
    tag_func=lambda row: "danger" if row["stock"] <= 3 else None,
)
table.pack(fill="both", expand=True, padx=20, pady=(0, 20))
table.add_button("+ Add", add_item)
table.add_button("Edit", edit_item, color="warning", width=80)
table.add_button("Delete", delete_item, color="danger", width=90)
table.add_button("Theme", toggle_theme, color="success", width=80)
table.set_data(ALL_ROWS)

root.mainloop()