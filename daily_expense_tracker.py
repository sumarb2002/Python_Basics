expenses = []
print("Welcome to the Daily Expense Tracker!")
while True:
    print("Menu:\n1. Add a new expense\n2. View all expenses\n3. Calculate total and average expense\n4. Clear all expenses\n5. Exit")
    print("Enter your choice ")
    choice = int(input())
    if choice == 1:
        expense = float(input("Enter value "))
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == 2:
                    if len(expenses) == 0:
                        print("No expenses recorded yet.")
                    else:
                        print("Your expenses:")
                        for i in range(len(expenses)):
                            print(f"{i+1}. {expenses[i]}")  
    elif choice == 3:
        total_expense = 0
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            for i in range(len(expenses)):
                total_expense += expenses[i]  
            avg_expense =  total_expense/len(expenses)  
            print(f"Total expense: {total_expense}")     
            print(f"Average expense: {avg_expense}") 
    elif choice == 4:
        expenses.clear()
        print("All expenses cleared.")      

    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")   