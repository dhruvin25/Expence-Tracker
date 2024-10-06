import json
import datetime

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
    return expenses

def add_expense(expense_id_counter,date,amount,description):
    # Capture the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format: YYYY-MM-DD HH:MM:SS
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
    save_expenses()

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
    return total

def delete_expense(expense_id):
    for id,ex in enumerate(expenses): #enumerate is built-in function which returns both ID and object
        if ex['id'] == expense_id:
            remove = expenses.pop(id) #Pop will remove object at index
            print(f"Removed : {remove['id']} - {remove['description']} - {remove['amount']} on {remove['date']}")
            return remove
    print(f"No records found for {expense_id}")
    save_expenses()
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
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
            save_expenses()
            return 1
    return 0
        
    

def show_menu():
    print("\n1. Add Expenses")
    print("2. Edit Expenses")
    print("3. Delete Expenses")
    print("4. View Expenses")
    print("5. Search Expenses")
    print("6. Total Expenses")
    print("7. Summery Report")
    print("8. Exit")


def spending_by_date(date):
    total = sum(int(ex['amount']) for ex in expenses if ex['date'] == date)
    print(f"Total spending on {date} is ${total:.2f}")
    return total


def spending_by_category():
    category_total= {}
    # This code calculates the total amount spent in each category by treating the description field of each expense as the category and adding up the amounts spent in each one. It handles the case where a new category is encountered by initializing it with 0.
    for ex in expenses:
        category = ex['description']
        category_total[category] = int(category_total.get(category,0)) + int(ex['amount'])

    print("Spending by Category : ")
    for category,total in category_total.items():
        print(f"{category} : ${total:.2f}")
    return category_total

def avg_daily_spending():
    if not expenses:
        print("No expenses to calculate")
        return 0
    # Extract unique dates
    unique_dates = set(ex['date']for ex in expenses)
    total_spent = sum(int(ex['amount']) for ex in expenses)
    avg_spending = total_spent/len(unique_dates)

    print(f"Average daily spending is : ${avg_spending:.2f}")
    return avg_spending
    
def highest_expense():
    if not expenses:
        print("No expenses to calculate")
        return 0
    highest = max(expenses, key=lambda x :int(x ['amount']))
    print(f"Highest Expense : {highest['description']} on {highest['date']} for {highest['amount']}")
    return highest

def lowest_expense():
    if not expenses:
        print("No expenses to calculate")
        return 0
    lowest = min(expenses, key=lambda x :int(x ['amount']))
    print(f"Lowest Expense : {lowest['description']} on {lowest['date']} for {lowest['amount']}")
    return lowest

def summery_menu():
    while True:
        print("\n---------Summery Report---------")
        print("1. Total Spending")
        print("2. Spending by date")
        print("3. Spending by category")
        print("4. Average Daily spending")
        print("5. Highest Expense")
        print("6. Lowest Expense")
        print("7. Back to main menu")

        choise = input("Enter your choice : ")
        if choise =='1':
            total_expenses()
        elif choise =='2':
            date = input("Enter date (YYYY-MM-DD) : ")
            spending_by_date(date)
        elif choise == '3':
            spending_by_category()
        elif choise == '4':
            avg_daily_spending()
        elif choise =='5':
            highest_expense()
        elif choise == '6':
            lowest_expense()
        elif choise == '7':
            break
        else:
            print("Invalid choice. Please try again.")
    