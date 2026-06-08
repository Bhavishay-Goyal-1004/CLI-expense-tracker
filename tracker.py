import os

def add_expense():
    """Prompts user for expense details and saves to expense.txt."""
    date=input("Enter Date (DD/MM/YYYY): ")
    while True: 
        try: 
            amt = float(input("Enter Amount: "))
            if amt <= 0:
                print("Amount must be greater than 0.")
                continue
            break 
        except ValueError: 
            print("Invalid amount! Please enter a number.")
    
    valid = ["food", "transport", "entertainment", "other"]
    while True:
        category = input("Enter Category (Food/Transport/Entertainment/Other): ")
        if category.lower() in valid:
            category = category.capitalize()  
            break
        print("Invalid category! Choose from Food/Transport/Entertainment/Other.") 
    note = input("Enter a note (otherwise press Enter): ")
    if note == "": 
        note = "NA" 
    with open("expense.txt", "a") as file:
        file.write(f"{date},{amt},{category},{note}\n") 

    print("Expense added successfully!")
    
def view_expense():
    """Reads expenses from expense.txt and displays them in a formatted table."""
    if not os.path.exists("expense.txt"): 
        print("No expenses recorded yet.")
        return
    with open("expense.txt", "r") as file:
        total = 0 
        print("\n==============================================================") 
        print(f"{'Date':<15}{'Amount':<12}{'Category':<18}{'Note'}") 
        print("==============================================================")
        found = False
        for line in file: 
            line = line.strip() 
            if line == "": 
                continue 
            found = True
            date, amt, category, note = line.split(",", 3) 
            print(f"{date:<15}{float(amt):<12.2f}{category:<18}{note}") 
            total += float(amt)
        if not found:
            print("No expenses recorded yet.")
        else:
            print("==============================================================") 
            print(f"Total Expense: {total:.2f}") 
            print("==============================================================\n") 

def filter_category():
    """Prompts user for a category and displays expenses that match the category."""
    if not os.path.exists("expense.txt"):  
        print("No expenses recorded yet.")
        return
    with open("expense.txt","r") as file:
        category_i=input("Enter the category to view expenses: ")
        total=0
        print("\n==============================================================") 
        print(f"{'Date':<15}{'Amount':<12}{'Category':<18}{'Note'}") 
        print("==============================================================")
        found = False
        for line in file:
            line = line.strip() 
            if line == "": 
                continue
            date,amt,category,note=line.split(",",3)
            if (category.lower()==category_i.lower()):
                found = True
                print(f"{date:<15}{float(amt):<12.2f}{category:<18}{note}")
                total+=float(amt)
        if not found:
            print(f"No expenses found for category '{category_i}'.")
        else:
            print("==============================================================") 
            print(f"Subtotal Expense: {total:.2f}") 
            print("==============================================================\n") 

def main():
    while True:
        print("======== Welcome to Expense Tracker! ========")
        print("1. Add an expense.")
        print("2. View all expenses.")
        print("3. Filter by category.")
        print("4. Exit")

        try: 
            ch = int(input("Enter Choice: ")) 
        except ValueError: 
            print("Invalid input! Please enter a number.\n") 
            continue

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

if __name__=="__main__":
    main()
