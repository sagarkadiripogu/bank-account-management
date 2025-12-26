from transaction import Transaction
class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
        self.transactions=[]
    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount must be positive")
        else:
            self.balance+=amount
            transaction=Transaction(amount,"Deposit")
            self.transactions.append(transaction)
            print("Deposit Succesfull")
    def withdrawl(self,amount):
        if amount<=0:
            print("Withdrawl amount must be positive")
        elif amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            transaction=Transaction(amount,"Withdrawl")
            self.transactions.append(transaction)
            print("Withdrawl Succesfull")
    def get_balance(self):
        return f"Balance:{self.balance}/-"
    def show_transactions(self):
        if self.transactions==[]:
            print("No transactions yet")
            return
        for transaction in self.transactions:
            print(transaction)
        
        
