class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")


account_number = input("Enter your account number: ")
account_holder_name = input("Enter your name: ")
initial_balance = float(input("Enter initial balance: "))

account1 = BankAccount(account_number, account_holder_name, initial_balance)

account1.display_balance()

deposit_amount = float(input("Enter the deposit amount: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))

account1.deposit(deposit_amount)
account1.withdraw(withdrawal_amount)

account1.display_balance()
