import time
import random

def display_welcome_screen():
    print("===============================================")
    print("             WELCOME TO INFINIA BANK           ")
    print("===============================================")
    print("     Empowering Your Digital Banking Journey   ")
    print("===============================================")
    print("Loading system", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\nSystem ready.\n")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            print("\nAll Bank Accounts:")
            for acc in self.accounts:
                print(f"Account: {acc.account_number} | Owner: {acc.owner} | Balance: {acc.balance}")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return "AC" + str(random.randint(10000, 99999))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid or insufficient funds.")


display_welcome_screen()
bank = Bank()

while True:
    print("\nMenu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        name = input("Enter account holder name: ").strip()
        initial_balance = float(input("Enter initial deposit: "))
        account = BankAccount(name, initial_balance)
        bank.add_account(account)
        print(f"Account created successfully for {name}. Account No: {account.account_number}")

    elif choice == '2':
        acc_no = input("Enter account number: ").strip()
        acc = bank.find_account(acc_no)
        if acc:
            amount = float(input("Enter deposit amount: "))
            acc.deposit(amount)
        else:
            print("Account not found.")

    elif choice == '3':
        acc_no = input("Enter account number: ").strip()
        acc = bank.find_account(acc_no)
        if acc:
            amount = float(input("Enter withdrawal amount: "))
            acc.withdraw(amount)
        else:
            print("Account not found.")

    elif choice == '4':
        acc_no = input("Enter account number: ").strip()
        acc = bank.find_account(acc_no)
        if acc:
            print(f"Owner: {acc.owner} | Account: {acc.account_number} | Balance: {acc.balance}")
        else:
            print("Account not found.")

    elif choice == '5':
        bank.display_all_accounts()

    elif choice == '6':
        print("\nThank you for choosing INFINIA BANK. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")