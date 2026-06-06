import os

def add_expense():
    date=input("Enter Date (DD/MM/YYYY): ")
    while True: 
        try: 
            amt = float(input("Enter Amount: ")) 
            break 
        except ValueError: 
            print("Invalid amount! Please enter a number.")
    
    category = input("Enter Category (Food/Transport/Entertainment/Other): ") 
    note = input("Enter a note (otherwise press Enter): ")
    if note == "": 
        note = "NA" 
    with open("expense.txt", "a") as file:
        file.write(f"{date},{amt},{category},{note}\n") 

    print("Expense added successfully!")
    
def view_expense():
    if not os.path.exists("expense.txt"): 
        print("No expenses recorded yet.")
        return
    with open("expense.txt", "r") as file:
        total = 0 
        print("\n==============================================================") 
        print(f"{'Date':<15}{'Amount':<12}{'Category':<18}{'Note'}") 
        print("==============================================================")
        for line in file: 
            line = line.strip() 
            if line == "": 
                continue 
            date, amt, category, note = line.split(",") 
            print(f"{date:<15}{float(amt):<12.2f}{category:<18}{note}") 
            total += float(amt) 
        print("==============================================================") 
        print(f"Total Expense: {total:.2f}") 
        print("==============================================================\n") 

def filter_category():
    if not os.path.exists("expense.txt"):  
        print("No expenses recorded yet.")
        return
    with open("expense.txt","r") as file:
        category_i=input("Enter the category to view expenses: ")
        total=0
        print("\n==============================================================") 
        print(f"{'Date':<15}{'Amount':<12}{'Category':<18}{'Note'}") 
        print("==============================================================")
        for line in file:
            line = line.strip() 
            if line == "": 
                continue
            date,amt,category,note=line.split(",")
            if (category.lower()==category_i.lower()):
                print(f"{date:<15}{float(amt):<12.2f}{category:<18}{note}")
                total+=float(amt)
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
