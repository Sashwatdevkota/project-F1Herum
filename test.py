
from abc import ABC, abstractmethod


# Abstraction
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Inheritance + Polymorphism
class EsewaPayment(PaymentMethod):

    def pay(self, amount):
        print(f"You just paid Rs. {amount} via eSewa")


class KhaltiPayment(PaymentMethod):

    def pay(self, amount):
        print(f"You just paid Rs. {amount} via Khalti")


class BankTransferPayment(PaymentMethod):

    def pay(self, amount):
        print(f"You just paid Rs. {amount} via Bank Transfer")


# Encapsulation
class Wallet:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def addmoney(self, deposit):
        if deposit <= 0:
            raise ValueError("Invalid amount")     

        self.__balance += deposit
        print("Money added successfully")

    def makepayment(self, account, withdrawl):

        if withdrawl <= 0:
            raise ValueError("Invalid amount")

        if withdrawl > self.__balance:
            raise ("Insufficient balance")

        account.pay(withdrawl)
        self.__balance -= withdrawl
        print("Payment successful")

    def check_balance(self):
        return self.__balance


# Testing
wallet = Wallet("Alex", 5000)

esewa = EsewaPayment()
khalti = KhaltiPayment()
bank = BankTransferPayment()

wallet.makepayment(esewa, 1000)
wallet.makepayment(khalti, 500)

print("Remaining balance:", wallet.check_balance())
