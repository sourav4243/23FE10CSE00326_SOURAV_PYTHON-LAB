class ATM:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.previous_balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: Rs{amount}")
            print(f"Deposited: Rs{amount}")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: Rs{amount}")
            print(f"Withdrew: Rs{amount}")
        else:
            print("Insufficient ammount.")

    def check_balance(self):
        print(f"Current Balance: Rs{self.balance}")

    def home(self):
        print(f"Welcome to the ATM, {self.account_holder}!")

    def go_back(self):
        self.balance = self.previous_balance
        print("Went back to the previous state.")

    def view_transaction_history(self):
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)

atm = ATM("Sourav", balance=1000)

atm.home()
atm.deposit(500)
atm.withdraw(200)
atm.check_balance()
atm.view_transaction_history()
atm.go_back()
atm.check_balance()
