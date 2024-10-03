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
#eg:1
# class synnefo:
#     def python(self):
#         print("python")
#     def php(self):
#         print("php")
#     def networking(self):
#         print("networking")
#     def python(self):
#         print("digital marketing")
#     def registration(self):
#         print("regisration")
# class non_teaching_staff(synnefo):
#     def accounts(self):
#         print("accounts")
#     def front_office(self):
#         print("front_office")
#     def devolpment_team(self):
#         print("development_team")
# class teaching_staff(synnefo):
#     def notes(self):
#         print("notes")
#     def attendance(self):
#         print("attendance")
# class student(teaching_staff):
#     def accesing_notes(self):
#         print("accesing_notes")
#     def accesing_lab(self):
#         print("accesing_lab")            
# ajay=synnefo()
# ajay.networking()
# ajay.php()
# ajay.python()
# ajay.registration()
# arun=non_teaching_staff()
# arun.accounts()
# arun.devolpment_team()
# arun.front_office()
# arun.networking()
# arun.php()
# arun.python()
# arun.registration()
# hema=teaching_staff()
# hema.attendance()
# hema.networking()
# hema.notes()
# hema.php()
# hema.python()
# hema.registration()
# alen=student()
# alen.networking()
# alen.php()
# alen.python()
# alen.registration()
# alen.accesing_lab()
# alen.accesing_notes()
# alen.notes()
# alen.attendance()

# #eg:2
# class restaurnt:
#     def managing_resturant(self):
#         print("managing resurant")
# class food_items(restaurnt):
#     def menu(self):
#         print("menu")           
# class owner(restaurnt):
#     def profit(self):
#         print("profit")
# class manager(owner):
#     def accesing_staff_details(self):
#         print("accesing staff details")  
#     def managing_accounting_section(self):
#         print("managing_accounting_section")
# class staff(manager):
#     def managing_staff_details(self):
#         print("managing staff details")
# class waiter(staff):
#     def serving_food(self):
#         print("serving food")
#     def cleaning_section(self):
#         print("cleaning section")
#     def taking_order(self):
#         print("taking order")    
# class cheif(staff):
#     def making_food(self):
#         print("making food")
# class customer:
#     def giving_order(self):
#         print("giving order")                                                             
    
# hayatil_restaurant=restaurnt()
# hayatil_restaurant.managing_staff()
# hayatil_restaurant.menu()
# meals=food_items()
# meals.managing_resturant()
# meals.menu()
# jeevan=owner()
# jeevan.managing_resturant()
# jeevan.profit()
# karun=staff()
# karun.profit()
# karun.accesing_staff_details()
# karun.managing_accounting_section()
# karun.managing_staff_details()
# karun.managing_resturant()
# athul=cheif
# athul.managing_resturant()
# athul.accesing_staff_details()
# athul.making_food()
# athul.managing_accounting_section()
# athul.managing_staff_details()
# athul.profit()

#polymorphism
#------------------
#method overriding
# class bank:
#     def __init__(self):
#         print("add bank dtls")
# class user(bank):
#     def __init__(self):
#         print("add user dtls")
        
# arun=user()

#2nd type
# class school:
#     def notes(self,sub):
#         print("notes for",sub)
# class std(school):
#     def notes(self,sub):
#         super().notes(sub)  
#         print("notes for std")
       
# ajay=std()
# ajay.notes("python")

# #data abstraction
#-----------------
from abc import ABC,abstractmethod
class syn(ABC):
    @abstractmethod
    def reg(self):
        pass
    def python(self):
        print("pyton topics")
    def php(self):
        print("php topics")
class staff (syn):
    def reg(self):
        print("staff details")
    def notes(self):
        print("notes")
class student(syn):
    def reg(self):
        print("std data")
    def exam(self):
        print("exam")            
staff1=staff()
arun=student()                  
                  
