# Build a simple BankAccount class.

# Requirements:
# 1. Create a class called BankAccount.
# 2. Create a constructor accepting owner and balance.
# 3. Create a deposit() method.
# 4. Create a withdraw() method.
# 5. Create a check_balance() method that returns the balance.
# 6. Add a class attribute called bank_name.
# 7. Create two separate bank account objects.
# 8. Deposit and withdraw different amounts from each account.
# 9. Print both account balances.
# Bonus: Create a static method called is_valid_amount() that checks whether an amount is greater than zero.

class BankAccount:
    
    bank_name = "Test Bank"
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        
    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        
    def withdraw(self,withdraw_amount):
        self.balance-=withdraw_amount
    
    def check_balance(self):
        return self.balance

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
    
    def transfer(self,receipent, amount):
        
        if not self.is_valid_amount(amount):
            print("Invalid Amount")
            return
        
        if self==receipent:
            print("Can not send to same user")
        
        
        self.withdraw(amount)
        receipent.deposit(amount)
        
            
    
bank1 = BankAccount("Alex", 5000)
bank2 = BankAccount("Sarah", 2000)

bank1.transfer(bank2, 1000)

print(bank1.check_balance())  
print(bank2.check_balance())  