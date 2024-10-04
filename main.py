import json
import datetime

# List to store the expence
expenses = []

def save_expenses(filename = 'expenses.txt'):
    with open(filename,'w') as file:
        json.dump(expenses,file)
    print(f"Expenses saved to {filename}.")
    load_expenses()

def load_expenses(filename = 'expenses.txt'):
    global expenses
    try:
        with open(filename,'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with expty list.")
        expenses = []

def add_expense(date,amount,description):
    global expense_id_counter
    # Capture the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format: YYYY-MM-DD HH:MM:SS
    expense_id_counter +=1
    expense_id = f"EX{expense_id_counter:04d}"
    # one dictionary object will be one expense 
    # {'date':'2024-10-03','description':'Grocery','amount':'15'}
    expense = {
        'id': expense_id,
        'date':date,
        'amount':amount,
        'description':description,
        'timestamp' : timestamp     
    }
    # Adding object in list
    expenses.append(expense)
    expense_id_counter +=1
    print(f"Expense added successfully! Expense ID {expense_id} at {timestamp}")


def view_expense():
    if not expenses:
        print("There are no expenses in Database.")
        return
    
    print("ID\tDate\t\tAmount\t Description\tTimestamp")
    print("--------------------------------------------------------------")
    for ex in expenses:
        print(f"{ex['id']}\t{ex['date']}\t {ex['amount']}\t {ex['description']}\t{ex['timestamp']}")

def total_expenses():
    if not expenses:
        print("No expenses to sum.")
        return
    total = sum(int(ex['amount']) for ex in expenses)
    print(f"Total Expenses : {total}")

def delete_expense(expense_id):
    for id,ex in enumerate(expenses): #enumerate is built-in function which returns both ID and object
        if ex['id'] == expense_id:
            remove = expenses.pop(id) #Pop will remove object at index
            print(f"Removed : {remove['id']} - {remove['description']} - {remove['amount']} on {remove['date']}")
            return remove
    print(f"No records found for {expense_id}")
    return None

def search_expenses(expense_id=None,date=None):
    filtered = []
    for ex in expenses:
        if expense_id is not None and ex['id'] == expense_id:
            filtered.append(ex)
        if date is not None and ex['date'] == date:
            filtered.append(ex)

    if not filtered:
        print(f"No records found on this request!")
    else:
        for ex in filtered:
            print(f"{ex['id']}\t{ex['date']}\t\t{ex['amount']}\t{ex['description']}\t{ex['timestamp']}")

def edit_expense(expense_id,new_date = None, new_amount = None, new_description = None):
    for ex in expenses:
        if ex['id'] == expense_id:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if new_date is not None:
                ex['date'] = new_date
                ex['timestamp'] = timestamp
            if new_amount is not None:
                ex['amount'] = new_amount
                ex['timestamp'] = timestamp
            if new_description is not None:
                ex['description'] = new_description
                ex['timestamp'] = timestamp
            
            print(f"Expense Updated for {expense_id} at {timestamp}!")
    else:
        print("Invalid index.")

def show_menu():
    print("\n1. Add Expenses")
    print("2. Edit Expenses")
    print("3. Delete Expenses")
    print("4. View Expenses")
    print("5. Search Expenses")
    print("6. Total Expenses")
    print("7. Exit")

if __name__ == "__main__":
    load_expenses('expenses.txt')
    latest_record = expenses[-1]
    expense_id_counter = int(latest_record['id'][2:])  # Global counter for ID

    while True:
        show_menu()
        choice = input("Choose an option : ")
        if choice == '1':
            date = input("Enter date(YYYY-MM-DD) : ")
            amount = input("Enter amount : ")
            description = input("Enter description : ")
            add_expense(date,amount,description)
            save_expenses()
        elif choice == '2':
            expense_id = input("Enter id : ")
            new_date = input("Enter new date(YYYY-MM-DD) : ")
            new_amount = input("Enter new  amount : ")
            new_description = input("Enter new description : ")
            edit_expense(expense_id,new_date,new_amount,new_description)
            save_expenses()
        elif choice == '3':
            expense_id = input("Enter id : ")
            delete_expense(expense_id)
            save_expenses()
        elif choice == '4':
            view_expense()
        elif choice == '5':
            expense_id = input("Enter id : ")
            date = input("Enter date(YYYY-MM-DD) : ")
            search_expenses(expense_id=expense_id,date=date)
        elif choice == '6':
            total_expenses()
        elif choice == '7':
            break
        else:
            print("Invalid choice")


# load_expenses()

# # Adding expense
# add_expense('2024-10-02','20','Grocery')
# add_expense('2024-10-02','30','Movie')

# # Call function to show data
# view_expense()

# # Sum of all expenses
# total_expenses()


# # Delete record by Index
# delete_expense(1)

# # Search records by date (YYYY-MM-DD)
# filter_by_date('2024-10-03')

# # Update expenses by index
# edit_expense(2,"2024-10-03","42","Dinner")

# save_expenses()