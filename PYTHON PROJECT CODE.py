#An empty transactions to hold all transactions

transactions = []

with open("budget_data.txt", "r") as file:
    file.close()

#Function to load transactons from a file (if it exists)
with open("budget_data.txt", "r") as file:
    for line in file:
        transaction_data = line.strip().split(",")
        transactions.append({
            "date": transaction_data[0],
            "category": transaction_data[1],
            "description": transaction_data[2],
            "amount": float(transaction_data[3])
        })

while True:
    print("\nPersonal Budget Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expense by Category")
    print("4. Save and Exit")

    #Take user input for choosing an option
    choice = input("Please select an option (1-4): ")

    if choice == "1":
        #Add new Expense
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the expense category (e.g., Food, Rent, Utilitites): ")
        description = input("Enter a short description of the expense: ")
        amount = float(input("Enter the amount: "))

        transactions.append({
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        })
        print("\n\nExpense added successfully\n\n")

    elif choice == "2":
        #View all expenses
        if transactions:
            print("\n\nAll expenses:-\n")
            for transaction in transactions:
                print(f"Date: {transaction['date']}, Category: {transaction['category']}, "f"Description: {transaction['description']}, Amount: ₧{transaction['amount']}")
        else:
            print("\n\n\nNo expenses yet...\n")

    elif choice == "3":
        #View expenses by category
        category_to_view = input("Enter the category to view (e.g., Food, Rent, Utilities): ")
        found = False
        total = 0
        print(f"\nExpenses under the '{category_to_view}' category: ")
        for transaction in transactions:
            if transaction["category"].lower() == category_to_view.lower():
                found = True
                total += transaction["amount"]
                print(f"Date: {transaction['date']}, Description: {transaction['description']}, "f"Amount: ₧{transaction['amount']}")
        if not found:
            print(f"No expenses found for the category '{category_to_view}'.")
        else:
            print(f"\nTotal spent in '{category_to_view}': ₧{total}")
            
    elif choice == "4":
        #Save and Exit
        with open("budegt_data.txt", "w") as file:
            for transaction in transactions:
                file.write(f"{transaction['date'], {transaction['category'], transaction['description']}, transaction['amount']}\n")
        print("Data saved. Exiting the program.")
        break
    
    else:
        print("Invalid choice, please select a valid option (1-4).")
