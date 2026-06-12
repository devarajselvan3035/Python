from enum import Enum

class AccountType(Enum):
    SAVING="Saving"
    CURRENT="Current"
    NONE="None"
    
class Customer:
    customerId = 0
    
    def __init__(self, customer_name):
        Customer.customerId += 1
        self.customer_id = Customer.customerId
        self.customer_name = customer_name
        

class Account:
    accountId = 10000
    
    def __init__(self, secret_pin, customer):
        Account.accountId += 1
        self.account_id = Account.accountId
        self.account_type: AccountType = AccountType.NONE
        self.account_pin: int = secret_pin
        self.total_amount: int = 0
        self._customer: Customer = customer
        
class Inventory:
    
    def __init__(self):
        self.account_dict: dict[int, Account] = {}
    
        
class BankManagement:
    
    def __init__(self):
        self.inventory = Inventory().account_dict
    
    def createAccount(self, customer_name: str,
                      account_type: AccountType,
                      secret_pin: int,
                      deposite_amount: int
                      ):
        
        type_dict = {'1': AccountType.SAVING, '2':AccountType.CURRENT}
    
        customer = Customer(customer_name)
        account = Account(secret_pin, customer)

        if deposite_amount >= 1000:
            account.account_type = type_dict[account_type]
            account.total_amount += deposite_amount
            self.inventory[account.account_id] = account
            print(f"""
              [SUCCESS]: Account created successfully
              Account No: {account.account_id}
              """)
        else:
            print(f"[ERROR] Minimum balance required above Rs.1000, but given amount is {deposite_amount}")
            
            
    def depositMoney(self, account_no, deposite, pin):
        account:Account = self.inventory[account_no]
        if pin == account.account_pin:
            account.total_amount += deposite
            print(f"{account.accountId=}, {account.account_type=}, {account.total_amount=}")
            return True

        else:
            print("Invalid PIN")
            return False
            
            
    def withdrawMoney(self, account_no, deposite, pin):
        account = self.inventory[account_no]
        if pin == account.account_pin:
            difference = account.total_amount - deposite
            if difference >= 1000:
                account.total_amount = difference
            else:
                print("After withdraw total account going to below minimum")
                
    # def transferWithAccounts(self, from_acc_no, to_acc_no, from_pin, amount):
    #     from_acc = self.inventory[from_acc_no]
    #     to_acc = self.inventory[to_acc_no]
        
    #     if from_acc.account_pin == from_pin:
            
                
                
if __name__ == "__main__":
    bm = BankManagement()
    while True:
        option = int(input(("""
              1. Create Bank Account
              2. Deposite Money
              3. Withdraw Money
              4. Transfer Funds to Another Account
              5. View Account Statement
              6. Exit
              Enter your choice (1-6) : 
              """)))

        if option == 1:
            name = input("Enter the customer Name : ")
            account_type = input("Select Account Type (Saving(1) or Current(2)) : ")
            pin = int(input("Enter 4 digits pin : "))
            deposite = int(input("Enter Initial Deposit Amount : "))
            bm.createAccount(name, account_type, pin, deposite)

        elif option == 2:
            act_no = int(input("Enter account no : "))
            deposite = int(input("Enter the deposite amount : "))
            count = 0
            while count < 3:
                pin = int(input("Enter the 4 digit pin : "))
                if bm.depositMoney(act_no, deposite, pin):
                    break
                count += 1
            if count == 3:
                print("3 attempts are finished")
        else:
            break
