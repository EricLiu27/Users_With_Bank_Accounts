class BankAccount_Checking:
    all_account = []
    def __init__(self, int_rate, balance, account_type): 
        self.int_rate = int_rate
        self.balance = balance
        self.account_type = account_type
        BankAccount_Checking.all_account.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print(f"Your bank account balance is {self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_account:
            account.display_account_info()


class BankAccount_Saving:
    all_account = []
    def __init__(self, int_rate, balance, account_type): 
        self.int_rate = int_rate
        self.balance = balance
        self.account_type = account_type
        BankAccount_Saving.all_account.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print(f"Your bank account balance is {self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_account:
            account.display_account_info()




class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking_account = BankAccount_Checking(int_rate=0.02, balance=0, account_type = "checking")
        self.saving_account = BankAccount_Saving(int_rate = 0.02, balance = 0, account_type = "saving")
    
    # other methods
    
    def make_deposit(self, amount, account):
        if account == self.checking_account.account_type:
            self.checking_account.deposit(amount)
            print(f"Your total balance in your checking account is {self.checking_account.balance}")	
        elif account == self.saving_account.account_type:
            self.saving_account.deposit(amount)
            print(f"Your total balance in your saving account is {self.saving_account.balance}")	

    def make_withdrawal(self, amount, account):
        if account == self.checking_account.account_type:
            self.checking_account.withdraw(amount)
            print(f"Your total balance in your checking account is {self.checking_account.balance}")	
        elif account == self.saving_account.account_type:
            self.saving_account.withdraw(amount)
            print(f"Your total balance in your saving account is {self.saving_account.balance}")	
    
    def display_user_balance (self, account):
        if account == self.checking_account.account_type:
            self.checking_account.display_account_info()
            print(f"Your total balance in your checking account is {self.checking_account.balance}")	
        elif account == self.saving_account.account_type:
            self.saving_account.display_account_info()
            print(f"Your total balance in your saving account is {self.saving_account.balance}")	

user_eric = User("Eric Liu","eric.liu82794@gmail.com")

user_eric.make_deposit(400, "saving")
user_eric.make_deposit(400,"checking")
user_eric.make_withdrawal(40, "checking")
