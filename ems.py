#employeee management system
emp=[]
while True:
        print(""" 
1.registration employee
2.view employee
3.update employee
4.delete employee
5.search employee

             """)
        choice=int(input("enter ur choice"))
        if choice==1:
               id=input("enter id")
               name=input("enter name") 
               age=input("enter age")
               salary=input("enter salary")
               position=input("enter position")
               exp=input("enter age")
               emp.append([id,name,age,salary,position,exp])
        elif choice==2:
              print('{:<6}{:<10}{:<6}{:<6}{:<6}{:<6}'.format("id","name","age","salary","position","age"))
              for i in emp:
                      print('{:<6}{:<10}{:<6}{:<6}{:<6}{:<6}').format(i[0],i[1],i[2],i[3],i[4],i[5])
        elif choice==3:
               name=(input("enter your name"))
               f=0
               for i in std:
                      if i[0]==name:
                             age=int(input("enter the age"))
                             i[1]=age
                             f=1
                             if f==0:
                                    print("name not in list") 
        elif choice==4:
               name=(input("enter your name"))
               f=0
               for i in std:
                      if i[0]==name:
                           
                             std.remove(i)
                             f=1
                             if f==0:
                                    print("name not in list")
        elif choice==5:
               name=(input("enter your name"))
               f=0
               for i in std:
                      if i[0]==name:
                             print(i)
                             f=1
                             if f==0:
                                    print("std not in list") 
        elif choice==6:
               break
        else:
          print("invalid choice")                                         
                                


                    