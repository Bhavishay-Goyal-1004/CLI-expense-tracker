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
