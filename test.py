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

    def check_balance(self):
        return self.__balance

