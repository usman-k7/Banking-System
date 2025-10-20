import time
import random

def display_welcome_screen():
    print("===================================")
    print("      Welcome to INFINIA Bank")
    print("===================================")

def create_account(accounts):
    owner = input("Enter account owner's name: ")
    acc_type = input("Enter account type (Savings/Checking): ").capitalize()
    if acc_type not in ["Savings", "Checking"]:
        print("Invalid account type.")
        return
    acc_no = random.randint(10000, 99999)
    balance = float(input("Enter initial balance: "))
    accounts[acc_no] = {"owner": owner, "type": acc_type, "balance": balance}
    print(f"Account created successfully! Your account number is {acc_no}")

def deposit(accounts):
    acc_no = int(input("Enter account number: "))
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Deposit successful!")
    else:
        print("Account not found.")

def withdraw(accounts):
    acc_no = int(input("Enter account number: "))
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

def check_balance(accounts):
    acc_no = int(input("Enter account number: "))
    if acc_no in accounts:
        print(f"Balance: {accounts[acc_no]['balance']}")
    else:
        print("Account not found.")

def view_all(accounts):
    print("\nAll Accounts:")
    for acc_no, details in accounts.items():
        print(f"{acc_no} | {details['owner']} | {details['type']} | {details['balance']}")

def main():
    accounts = {}
    display_welcome_screen()
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. View All\n6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            view_all(accounts)
        elif choice == "6":
            print("Thank you for banking with INFINIA Bank!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
