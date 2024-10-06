import functions as fn

def main():
    expenses = fn.load_expenses('expenses.txt')
    latest_record = expenses[-1]
    expense_id_counter = int(latest_record['id'][2:])  # Global counter for ID

    while True:
        fn.show_menu()
        choice = input("Choose an option : ")
        if choice == '1':
            date = input("Enter date(YYYY-MM-DD) : ")
            amount = input("Enter amount : ")
            description = input("Enter description : ")
            fn.add_expense(expense_id_counter,date,amount,description)
            
        elif choice == '2':
            expense_id = input("Enter id : ")
            new_date = input("Enter new date(YYYY-MM-DD) : ")
            new_amount = input("Enter new  amount : ")
            new_description = input("Enter new description : ")
            result = fn.edit_expense(expense_id,new_date,new_amount,new_description)
            if result == 0:
                print(f"No records Found in {expense_id}")

        elif choice == '3':
            expense_id = input("Enter id : ")
            fn.delete_expense(expense_id)
            fn.save_expenses()
        elif choice == '4':
            fn.view_expense()
        elif choice == '5':
            expense_id = input("Enter id : ")
            date = input("Enter date(YYYY-MM-DD) : ")
            fn.search_expenses(expense_id=expense_id,date=date)
        elif choice == '6':
            fn.total_expenses()
        elif choice == '7':
            fn.summery_menu()
        elif choice == '8':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()    

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