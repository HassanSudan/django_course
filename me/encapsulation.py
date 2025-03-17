

class BankAccount:

    def __init__(self, owner,balance=0):
        self.owner = owner
        self._balance = balance
    def deposit(self, amount):
        if(amount >0):
         self._balance += amount
         return f"Deposited ${amount}. New Balance: ${self._balance}"
        return "Deposit amount must be Positive"
        
    
    def withdraw(self, amount):
        if(amount > self._balance):
         return "Insificent balance"
        self._balance -= amount
        return f"Withdraw ${amount}. New Balance ${self._balance}"
    
if __name__ == "__main__":
   account = BankAccount("Sudan",1000)
   print(account.deposit(-1))
   print(account.withdraw(100))
            
         
