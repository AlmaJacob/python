#employeee management system
import datetime
emp=[]
while True:
        print(""" 
    1.registration employee
    2.view employee
    3.update employee
    4.delete employee
    5.search employee
    6.add task employee
    7.view task employee
    8.exit 
    """)
        choice=int(input("enter ur choice"))
        if choice==1:
               id=input("enter id")
               name=input("enter name") 
               age=input("enter age")
               salary=input("enter salary")
               position=input("enter position")
               exp=input("enter exp")
               emp.append([id,name,age,salary,position,exp])
        elif choice==2:
              print('{:<6}{:<10}{:<6}{:<8}{:<8}{:<8}'.format("id","name","age","salary","position","age"))
              for i in emp:
                      print('{:<6}{:<10}{:<6}{:<8}{:<8}{:<8}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
        elif choice==3:
            id=int(input('enter the id: '))
            f=0
            for i in emp:
                if i[0]==id:
                    print('''1.age \n 2.position \n 3.salary \n 4.experience''')
                    ch=int(input('enter the choice'))
                    if ch==1:
                        age=int(input(" updated age "))
                        i[2]=age
                    elif ch==2:
                        position=input(' updated position ')
                        i[3]=position
                    elif ch==3:
                        salary=input(' updated salary ')
                        i[4]=salary
                    elif ch==4:
                        exp=int(input(' updated experience '))
                        i[5]=exp
                    else:
                        print('please choose an valid option')
                    f=1
            if f==0:
                print('invali id')
        elif choice==4:
            id=int(input('enter the id to be removed '))
            f=0
            for i in emp:
                if i[0]==id:
                    emp.remove(i)
                    f=1
            if f==0:
                print('invalid id')
        elif choice==5:
            id=int(input('enter id of employee: '))
            f=0
            for i in emp:
                if i[0]==id:
                    print(i)
                    f=1
            if f==0:
                print('employee not found')
        elif choice==6:
              id=int(input('enter the id '))
              f=0
              for i in emp:
                   if i[0]==id:
                       f=1
                       task=input("enter task")
                       date=datetime.datetime.now().strftime("%x")
                       i.append([task,date])
              if f==0:
                       print("invalid id")
                  
                  
        elif choice==7:
             id=int(input('enter the choice '))
             if choice==7:
                  for i in emp:
                       if len(i)>6:
                             print('{:<6}{:<10}{:<8}{:<6}'.format("empid","name","task","date"))
                             print('{:<6}{:<10}{:<8}{:<6}'.format(i[0],i[1],i[6][0],i[6][1]))
        elif choice==8:
             break
        else:
             print("invalid option")
                                    