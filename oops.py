# class
#--------------

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


# class bank:
#     def __init__(self,min):
#         self.balance=min
#     def deposite(self,amount):
#         self.balance+=amount
#         print("amount added")
#     def withdraw(self,amount):
#         self.balance-=amount
#         print("withdraw")
#     def display(self):
#         print("display",self.balance)
# user1=bank(0)
# user1.deposite(5000)
# user1.withdraw(200)
# user1.display()

# user2=bank(150)
# user2.deposite(1300)
# user2.withdraw(500)
# print(user2.balance)

#inheritance
#------------
# class parent:
#     def property(self):
#         print("proprty of parent")
#     def business(self):
#         print("business of parent")
# class child(parent):
#     def bike(self):
#         print("bike of child")
# aju=child()
# aju.bike()
# aju.business()
# aju.property()
# john=parent()
# john.property()
# john.business()                    

# 1.single inheritance
#-----------------------
# class synnnefo:
#     def python(self):
#         print('python in synnefo')
#     def mernstack(self):
#         print("mernstack in synnefo")
# class novavi(synnnefo):
#     def digital_marketing(self):
#         print("digital marketing in novavi")
#     def web_dev(self):
#         print("web development in novavi")

# jake=novavi()#novavi is a child class so it can acess featurs of both novavi and synnefo
# jake.python()
# jake.digital_marketing()
# jake=synnnefo()#synnefo is parent class it can only acess the featuers of synnefo
# jake.mernstack()

#multiple inheritance
#-----------------------
#eg:1
#------
# class father:#parent class
#     def car(self):
#         print("car of father")
# class mother:#parent class
#     def property(self):
#         print("propert of mother")
# class child(father,mother):#child class
#     def money(self):
#         print("money of child")
# anu=child()
# anu.car()
# anu.property()
# anu.money()

#eg:2
#------
# class school:#parent class
#     def ground(self):
#         print("ground")
#     def libray(self):
#         print("libray")
# class tution:#parent class
#     def wrk_area(self):
#         print("wrk_area")
#     def lectutre(self):
#         print("lecture")
# class student(school,tution):#child class
#     def uniform(self):
#         print("uniform")                        
# ajay=student()
# ajay.ground()
# ajay.wrk_area()
# ajay.uniform()

#multilevel inheritance
#-------------------------
# class grandfather:#parent class
#     def proprty(self):
#         print("property")
# class father(grandfather):#intermediate sub class
#     def house(self):
#         print("house")
# class child(father):#child class
#     def car(self):
#         print("car")
# alen=child()
# alen.car()
# alen.house()
# alen.proprty()

#eg:2
#------

# class university:#parent class
#     def exm_notification(self):
#         print("exam notification")
# class clg(university):#intermediate sub class
#     def notes(self):
#         print("notes")
# class std(clg):#child class
#     def uniform(self):
#         print("uniform")
# alma=std()
# alma.exm_notification()
# alma.notes()
# alma.uniform()


#hirarchial inheritance
#-------------------------
# class grandfather:#parent class
#     def proprty(self):
#         print("property")
# class father(grandfather):#intermediate sub class
#     def house(self):
#         print("house")
# class child(father):#child class
#     def car(self):
#         print("car")
# alen=child()
# alen.car()
# alen.house()
# alen.proprty()

# class father:
#     def proprty(self):
#         print("property")
# class child1(father):
#     def house(self):
#         print("house")
# class child2(father):
#     def car(self)
#         print("car")
# alen=child1()
# alen.house()
# alen.proprty()
# arun=child2()
# arun.car()
# arun.proprty()


#hybrid inheritance
#----------------------



