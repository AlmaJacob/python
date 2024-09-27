# class synnefo:
#     def python():
#         print("python in synnefo")
#     def mernstack():
#         print('mernstack in synnefo')
#     def flutter():
#         print("flutter in synnefo")
# std=synnefo
# synnefo.python()
# synnefo.flutter()
# std2=synnefo
# synnefo.mernstack()


class bank:
    def __init__(self,min):
        self.balance=min
    def deposite(self,amount):
        self.balance+=amount
        print("amount added")
    def withdraw(self,amount):
        self.balance-=amount
        print("withdraw")
    def display(self):
        print("display",self.balance)
user1=bank(0)
user1.deposite(5000)
user1.withdraw(200)
user1.display()

user2=bank(150)
user2.deposite(1300)
user2.withdraw(500)
print(user2.balance)



                       