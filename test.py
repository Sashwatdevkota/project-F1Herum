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
        

esewa = EsewaPayment()
khalti = KhaltiPayment()
bank= BankTransferPayment()

esewa.pay(1000)
khalti.pay(2000)
bank.pay(3000)