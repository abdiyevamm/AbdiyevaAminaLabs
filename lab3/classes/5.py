"""Create a bank account class that has attributes owner, balance
and two methods deposit and withdraw.
Withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals,
and test to make sure the account can't be overdrawn."""

class Account:
    pass

class Dep(Account):

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self):
        print(f'{self.owner}, u vas na schetu : {self.balance}')

    def withdraw(self):
        while(True):
            a=int(input())
            if(a>self.balance):
                print("Insufficient funds,try again")
            else:
                print(f'You withdrew {a} dollars')
                self.balance = self.balance - a
                break

    def replesh(self):
        a=int(input())
        self.balance+=a
        print(f'vash balance : {self.balance}')

