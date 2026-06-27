class Account:
    AccountId = 0

    def __init__(self, name, password, balance) -> None:
        Account.AccountId += 1
        self.account_id = Account.AccountId
        self.name = name
        self.password = password
        self.balance = balance

    def deposite(self, password, amount):
        if password == self.password:
            self.balance += amount
        else:
            print("password is wrong")

    def withdraw(self, password, amount):
        if amount > self.balance:
            print(f"Amount is insuffient, your balance is {self.balance}")
            return None
        elif password != self.password:
            print("password is Wrong")
            return None
        self.balance -= amount

    def getBalance(self, password):
        if password == self.password:
            return self.balance
        else:
            print("password is wrong")
            return None

    def show(self):
        print(f"Name    : {self.name}")
        print(f"balance : {self.balance}")


account = Account("devaraj", "hello", 1000)
account.deposite("hello", 100)
account.withdraw("hi", 100)
account.show()
