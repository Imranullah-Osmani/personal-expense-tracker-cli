from datetime import datetime
import pandas as pd

def main():
    transaction_empty_list = []
    budget_empty_list = []
    next_id = 1

    while True:
        try:
            print(menu)
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                t = add_transaction(next_id)
                transaction_empty_list.append(t)
                next_id += 1
            elif choice == 2:
                view_transactions(transaction_empty_list)
            elif choice == 3:
                delete_transaction(transaction_empty_list)
            elif choice == 4:
                b = set_budget(budget_empty_list)
                if b:
                    budget_empty_list.append(b)
            elif choice == 5:
                view_budget(budget_empty_list)
            elif choice == 6:
                if not transaction_empty_list:
                    print("No Transaction To Export")
                else:
                    report = ([{
            "ID": t.id,
            "Type": t.typee,
            "Amount": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date
        } for t in transaction_empty_list])

                    df = pd.DataFrame(report, )
                    df.to_csv("transaction.csv")
                    print("""Transaction Exported to "transaction.csv" """)
            elif choice == 7:
                print("good Bye")
                break
            else:
                print("Please Choose Number From The List")
        except ValueError:
            print("Invalid Key, Please Enter Digit From List")


def add_transaction(next_id):
    while True:
        try:
            t_type = (
                input("\nEnter Transaction Type (Expense/Income): ").title().strip()
            )
            if not t_type in (["Expense", "Income"]):
                print("Transaction Type Should Be in (Expense/Income)")
                continue

            elif t_type == "Income":
                while True:
                    try:
                        t_amount = float(input("Enter Amount: $"))
                        break
                    except ValueError:
                        print("Invalid Amount\n")

                while True:
                    t_category = (
                        input("Enter Category (e.g. Salary, Freelance, Other): ")
                        .title()
                        .strip()
                    )
                    if not t_category in (["Salary", "Freelance", "Other"]):
                        print("Category Should Be In (Salary, Freelance, Other)\n")
                        continue
                    break

            elif t_type == "Expense":
                while True:
                    try:
                        t_amount = float(input("Enter Amount: $"))
                        break
                    except ValueError:
                        print("invalid amount\n")

                while True:
                    t_category = (
                        input("Enter Category (e.g. Food, Rent, Entertainment): ")
                        .title()
                        .strip()
                    )
                    if not t_category in (["Food", "Rent", "Entertainment"]):
                        print("Category Should Be In (Food, Rent, Entertainment)\n")
                        continue
                    break

            t_description = input("Enter Description (Optional): ").title().strip()
            transaction = Transaction(
                next_id, t_type, t_amount, t_category, t_description
            )
            print("\nTransaction Added Successfuly!")
            return transaction
        except ValueError:
            print("invalid")




def view_transactions(transaction):
    if not transaction:
        print("\nNo Transaction Yet!")
        return
    print("\nTransactions:")
    print(
        """\nID  | Type      | Amount     | Category     | Description                   | Date"
______________________________________________________________________________________________________"""
    )
    for _ in transaction:
        print(_.display())
    print()



def delete_transaction(transaction_d):
    if not transaction_d:
        print("\nNo Transaction Yet!")
        return
    while True:
        try:
            delete = int(input("""\n0: Menu\nEnter Transaction ID To Delete: """))
            if delete == 0:
                break
            for d in transaction_d:
                if d.id == delete:
                    transaction_d.remove(d)
                    print(f"Transaction ID {delete} Delete Successfuly!")
                    return
            print(f"No Transaction Found With ID {delete}. Try again.")
        except ValueError:
            print("ID Should Be Digit")


class Transaction:
    def __init__(self, id, typee, amount, category, description):
        self.id = id
        self.typee = typee
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def display(self):
        return f"{self.id: <3} | {self.typee: <9} | ${self.amount: <9} | {self.category:<12} | {self.description:<29} | {self.date}"





class Budget:
    def __init__(self, b_category, b_amount, b_spend, b_remaining):
        self.b_category = b_category
        self.b_amount = b_amount
        self.b_spend = b_spend
        self.b_remaining = b_remaining

    def new_spend(self, new):
        self.b_spend+= new
        self.b_remaining = self.b_amount - self.b_spend



    def __str__(self):
        return f"{self.b_category: <13} | ${self.b_amount: <11} | ${self.b_spend: <11} | ${self.b_remaining}"




def set_budget(already_budget):

    while True:
        category_for_budget = input(
        "Enter Category To Set Budget For (e.g. Food, Rent, Entertainment, Other): "
    ).strip().title()
        if not category_for_budget in (["Food", "Rent", "Entertainment", "Other"]):
            print("Category Should Be In (Food, Rent, Entertainment, Other)\n")
            continue


        for all in already_budget:
            if all.b_category == category_for_budget:
                while True:
                    try:
                        new_b_t = float(input("\n0: Skip Budget Transaction\nEnter Budget Transaction: $"))
                        if new_b_t == 0:
                            break
                        elif new_b_t + all.b_spend > all.b_amount:
                            print("Budget Transaction Is More Than Your Budget!")
                            continue
                        print("Budget Transaction Done")
                        all.new_spend(new_b_t)
                        return
                    except ValueError:
                        print("Invalid Amount")
        break


    while True:
        try:
            amount_for_budget = float(input("Enter Monthly Budget Amount: $"))
            while True:
                try:
                    budget_t = float(input("\n0: Skip Budget Transaction\nEnter Budget Transaction: $"))
                    if budget_t > amount_for_budget:
                        print("Budget Transaction Is More Than Your Budget!")
                        continue
                    else :

                        remain = amount_for_budget - budget_t
                    break
                except ValueError:
                    print("Invalid Amount")
            budget = Budget(category_for_budget, amount_for_budget, budget_t, remain)
            print(
            f"Budget Set For Category {category_for_budget} At {amount_for_budget}$ Amount"
    )
            return budget
        except ValueError:
            print("Invalid Amount\n")


def calculate_remaining_budget(total, spend):
    return total - spend


def view_budget(view_all_budget):

    if not view_all_budget:
        print("\nNo Budget Yet!")
        return
    print("\nBudget Summury:")
    print(
        """\nCategory      | Budget       | Spend        | Remaining
___________________________________________________________________"""
    )
    for _ in view_all_budget:
        print(_.__str__())
    print()




title = print("""\nWelcome To Personal Expense Tracker!""")
menu = """____________________________________________

1. Add Transaction
2. View Transaction
3. Delete Transaction
4. set Budget
5. View Budget Summary
6. Export Report
7. Quit
"""



if __name__ == "__main__":
    main()
