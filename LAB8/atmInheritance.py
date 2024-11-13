# basic bank function using inheritance
# create a base class account with attributes like accountnum, account holder name, balance
# define methods such as check balance, deposit, withdraw
# extent account into specialized classes like saving account, current account and checking account.
# How would you modify the withdraw method in these subclasses to handle withdrawl limits for each account type.
# add a transaction history class that maintains a record of all deposit and withdrawls for an account.account
# In this class implement a show_history method to display the transactions.
 
class Account:
    def __init__(self, account_num, account_holder_name, balance=0):
        self.account_num = account_num
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transaction_history = []
 
    def check_balance(self):
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")
        return self.balance
 
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount}")
            return self.balance
        else:
            return "Insufficient balance"
 
    def show_history(self):
        return "\n".join(self.transaction_history)
 
 
class SavingsAccount(Account):
    def __init__(self, account_num, account_holder_name, balance=0, withdraw_limit=1000):
        super().__init__(account_num, account_holder_name, balance)
        self.withdraw_limit = withdraw_limit
 
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            return f"Withdrawal exceeds the limit of {self.withdraw_limit}"
        else:
            return super().withdraw(amount)
 
 
class CurrentAccount(Account):
    def __init__(self, account_num, account_holder_name, balance=0, overdraft_limit=500):
        super().__init__(account_num, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit
 
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return f"Withdrawal exceeds overdraft limit of {self.overdraft_limit}"
        else:
            return super().withdraw(amount)
 
 
class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount > 5000: 
            return "Withdrawal exceeds the limit of 5000"
        else:
            return super().withdraw(amount)
 
 
# Create accounts
savings = SavingsAccount("1234567890", "Alice", 1500, 1000)
current = CurrentAccount("0987654321", "Bob", 2000, 500)
checking = CheckingAccount("1122334455", "Charlie", 3000)
 
# Perform transactions
savings.deposit(200)
savings.withdraw(800)
savings.withdraw(1200)  # Exceeds withdrawal limit
current.deposit(500)
current.withdraw(2500)
current.withdraw(1000)  # Within overdraft limit
checking.deposit(1000)
checking.withdraw(6000)  # Exceeds checking withdrawal limit
checking.withdraw(4000)  # Valid withdrawal
 
# Display transaction history
print("Savings Account Transaction History:")
print(savings.show_history())
 
print("\nCurrent Account Transaction History:")
print(current.show_history())
 
print("\nChecking Account Transaction History:")
print(checking.show_history())