import datetime
emp=[]
while True:
    print('''
        1.Register
        2.View
        3.Update
        4.Delete
        5.Search
        6.Add Task
        7.view tasks
        8.Exit1''')
    choice=int(input('choose an option: '))
    if choice==1:
        id=int(input('Enter the id: '))
        name=input('enter your name: ')
        age=int(input('Enter your age: '))
        phone_no=input('enter your phone_no: ')
        Dob=int(input('Enter your dob: '))
        address=int(input('Enter your address: '))
        fees=int(input('Enter your fees: '))
        vechicle_type=int(input('Enter your vehicle type: '))
        time=int(input('Enter your time: '))

        emp.append([id,name,age,phone_no,Dob,address,fees,vechicle_type,time])
    elif choice==2:
        print('{:<5}{:<10}{:<5}{:<10}{:<6}{:<15}{:<5}{:<6}{:<5}'.format("id","name","age","phone_no","Dob","adress","fees","vechicle_type","time"))
        for i in emp:
            print('{:<5}{:<10}{:<5}{:<10}{:<6}{:<15}{:<5}{:<6}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
    elif choice==3:
        id=int(input('enter the id: '))
        f=0
        for i in emp:
            if i[0]==id:
                f=1
                while True:
                    print('''1.age \n 2.phone_no \n 3.dob \n 4.adress \n 5.fees \n 6.vechicle_type \n 7.time \n 8.exit \n ''')
                    ch=int(input('choose any option :'))
                    if ch==1:
                        age=int(input("enter updated age: "))
                        i[2]=age
                    elif ch==2:
                        phone_no=input('enter updated phone_no: ')
                        i[3]=phone_no
                    elif ch==3:
                        dob=input('enter updated salary: ')
                        i[4]=dob
                    elif ch==4:
                        adress=int(input('enter updated experience: '))
                        i[5]=adress
                    elif ch==5:
                        fees=int(input('enter updated experience: '))
                        i[6]=fees
                    elif ch==6:
                        vechicle_type=int(input('enter updated experience: '))
                        i[7]=vechicle_type
                    elif ch==7:
                        adress=int(input('enter updated experience: '))
                        i[5]=adress
                    elif ch==8:
                        break
                    else:
                        print('please choose an valid option :')
        if f==0:
            print('invali id!!!')
    elif choice==4:
        id=int(input('enter the id to be removed: '))
        f=0
        for i in emp:
            if i[0]==id:
                emp.remove(i)
                f=1
        if f==0:
            print('invalid id!!!')
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
        id=int(input('enter id of the employee: '))
        f=0
        for i in emp:
            if i[0]==id:
                f=1
                task=input('enter the task: ')
                date=datetime.datetime.now().strftime("%x")
                i.append([task,date])
        if f==0:
            print('invalid id!!!')
    elif choice==7:
        for i in emp:
            if len(i)>6:
                print('{:<5}{:<10}{:<15}{:<10}'.format('id','name','task','date'))
                print('{:<5}{:<10}{:<15}{:<10}'.format(i[0],i[1],i[6][0],i[6][1]))
    elif choice==8:
        break
    else:
        print('invalid option')