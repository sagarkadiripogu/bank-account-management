import time
class Transaction:
    def __init__(self,amount,transaction_type):
        self.amount=amount
        self.transaction_type=transaction_type
        self.timestamp=time.time()
    def __str__(self):
        redabletime=time.ctime(self.timestamp)
        return f"{self.transaction_type} of {self.amount}/- at {redabletime}"
