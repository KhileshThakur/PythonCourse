#Data Hiding

class BankAcc:
    def __init__(self, balance):
        self.__balance=balance  #private variable
    def balance(self):
        return self.__balance
    def deposite(self, amount):
        self.__balance+=amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance-=amount
        else:
            return "Insufficient Balance"
acc=BankAcc(10000)
print(acc.balance())
acc.deposite(500)
print(acc.balance())
acc.withdraw(200)
print(acc.balance())


