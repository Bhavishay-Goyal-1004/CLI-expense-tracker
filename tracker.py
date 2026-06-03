def add_expense():
    date=input("Enter Date (DD/MM/YYYY): ")
    amt=float(input("Enter Amount: "))
    category=input("Enter Category (Food/Transport/Entertainment/Other): ")
    note=input("Enter a note (otherwise NA):")
    file = open("expense.txt","a")
    file.write(f"{date},{amt},{category},{note}")
    file.close()
    
    
while True:
    print("========Welcome to Expense Tracker!========")
    print("1. Add an expense.")
    print("2. View all expenses.")
    print("3. Filter by category.")
    print("4. Exit")

    ch=int(input("Enter Choice: "))

    if (ch==1):
        add_expense()
    elif (ch==2):
        view_expense()
    elif (ch==3):
        filter_category()
    elif (ch==4):
        break
    else:
        print("Invalid Choice!")
