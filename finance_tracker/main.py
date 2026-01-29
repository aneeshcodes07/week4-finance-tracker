from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import load_expenses, save_expenses
from finance_tracker.reports import category_summary

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.manager.expenses = load_expenses()

    def add_expense(self):
        print("\n--- ADD EXPENSE ---")
        date = input("Date (YYYY-MM-DD): ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        description = input("Description: ")

        expense = Expense(date, amount, category, description)
        self.manager.add_expense(expense)
        save_expenses(self.manager.expenses)

        print("✅ Expense added successfully!")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        if not self.manager.get_all_expenses():
            print("No expenses found.")
            return

        for e in self.manager.get_all_expenses():
            print(f"{e.date} | {e.category} | ₹{e.amount} | {e.description}")

    def view_category_report(self):
        print("\n--- CATEGORY REPORT ---")
        report = category_summary(self.manager.get_all_expenses())
        for cat, total in report.items():
            print(f"{cat}: ₹{total}")

    def run(self):
        while True:
            print("\n1. Add Expense")
            print("2. View Expenses")
            print("3. Category Report")
            print("0. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.view_category_report()
            elif choice == '0':
                print("Goodbye 👋")
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    FinanceTracker().run()
