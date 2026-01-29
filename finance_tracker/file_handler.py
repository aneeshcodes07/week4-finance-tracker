import json
import os
from finance_tracker.expense import Expense

DATA_FILE = "data/expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Expense(**item) for item in data]
    except Exception:
        return []

def save_expenses(expenses):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)
