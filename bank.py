#Classes. - Instance/Object?Instantiation
#Methods. - Static/Class?instance?magic

#OOP -

class Customer():
    def __init__(self,name):
        self.name=name
    def set_balance(self,balance):
        self.balance=balance
        return None
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if not amount>self.balance:
            self.balance-=amount
        else:
            raise RuntimeError ("Insufficiet Funds")
        return self.balance
    def get_balance(self):
        return self.balance


    
   
        

