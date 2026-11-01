from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class EsewaPayment(PaymentMethod):
    def pay(self,amount):
        print(f"You just paid {amount} via Esewa")
        
class KhaltiPayment(PaymentMethod):
    def pay(self,amount):
        print(f"You just paid {amount} via Khalti")
        
class BankTransferPayment(PaymentMethod):
    def pay(self,amount):
        print(f"You just paid {amount} via Bank Transfer")
        
class Wallet:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def addmoney(self, deposit):
        if deposit <= 0:
            print("Invalid amount")
            return

        self.__balance += deposit
        print("Money added successfully")
        
    def makepayment(self,account,withdrawl):
        if withdrawl <= 0:
            print("Invalid amount")
            return
        if withdrawl > self.__balance:
            
            print("Less money in your account")
            return
        
        account.pay(withdrawl)
        self.__balance-=withdrawl
        

    def check_balance(self):
        return self.__balance

wallet = Wallet("Alex",5000)

esewa=EsewaPayment()
wallet.makepayment(esewa,1000)