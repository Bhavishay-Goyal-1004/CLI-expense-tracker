# CLI-expense-tracker
A simple Command Line Interface (CLI) based Personal Expense Tracker built using Python.

This project allows users to:

» Add expenses

» View all expenses

» Filter expenses by category

All expense data is stored in a text file so the data persists between program runs.

## Features
### 1. Add Expense

Users can add:

» Date

» Amount

» Category

» Note

Categories supported:

» Food

» Transport

» Entertainment

» Other

### 2. View All Expenses

Displays all saved expenses in a formatted table along with the total expense amount.

### 3. Filter by Category

Users can filter expenses by category and view subtotal expenses for that category.


## Project Structure
expense-tracker/

│

├── main.py

├── expense.txt

├── README.md

└── .gitignore


## How to Run the Program
### Step 1: Clone the Repository
git clone https://github.com/Bhavishay-Goyal-1004/CLI-expense-tracker.git

### Step 2: Open Project Folder
cd expense-tracker

### Step 3: Run the Program
tracker.py

## Sample Menu
======== Welcome to Expense Tracker! ========
1. Add an expense
2. View all expenses
3. Filter by category
4. Exit

## Sample Expense File Format
01/06/2026,250,Food,Burger

02/06/2026,120,Transport,Metro Ticket

03/06/2026,500,Entertainment,Movie

Format:

Date,Amount,Category,Note

## Error Handling Implemented
» Invalid amount input handling

» Invalid menu choice handling

» Empty note handling

» Case-insensitive category filtering

## Learning Outcomes

Through this project, I learned:

» Python basics

» Functions

» Loops and conditionals

» File handling

» Exception handling

» Git and GitHub workflow

» Building CLI applications

## Screenshot
<img width="1294" height="727" alt="image" src="https://github.com/user-attachments/assets/6db9ffc7-594b-4e59-ba84-134921ba13d1" />

### GitHub Requirements Completed
Meaningful commits
README.md
.gitignore
File persistence using text file

### Author

Bhavishay Goyal
