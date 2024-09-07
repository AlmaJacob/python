import datetime
std=[]
while True:
    print('''
        1.Register
        2.View
        3.Update
        4.Delete
        5.Search
        6.Exit1''')
    choice=int(input('choose an option: '))
    if choice==1:
        id=int(input('Enter the id: '))
        name=input('enter  name: ')
        age=int(input('Enter  age: '))
        phone_no=input('enter  phone_no: ')
        dob=input('Enter  dob: ')
        address=(input('Enter  address: '))
        fees=int(input('Enter  fees: '))
        vechicle_type=(input('Enter  vehicle type: '))
        time=(input('Enter  time: '))

        std.append([id,name,age,phone_no,dob,address,fees,vechicle_type,time])
    elif choice==2:
        print('{:<5}{:<10}{:<5}{:<15}{:<10}{:<30}{:<15}{:<20}{:<8}'.format("id","name","age","phone_no","dob","address","fees","vechicle_type","time"))
        for i in std:
            print('{:<5}{:<10}{:<5}{:<15}{:<10}{:<30}{:<15}{:<20}{:<8}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
    elif choice==3:
        id=int(input('enter the id: '))
        f=0
        for i in std:
            if i[0]==id:
                f=1
                while True:
                    print('''1.age \n 2.fees\n 3.vehicle_type \n 4.time \n 5.exit \n  ''')
                    ch=int(input('choose any option :'))
                    if ch==1:
                        age=int(input("enter updated age: "))
                        i[2]=age
                    elif ch==2:
                        fees=input('enter updated fees: ')
                        i[6]=fees
                    elif ch==3:
                        vechicle_type=input('enter update vechicle type: ')
                        i[7]=vechicle_type
                    elif ch==4:
                        time=int(input('enter updated time: '))
                        i[6]=time
                   
                    elif ch==5:
                        break
                    else:
                        print('please choose an valid option :')
        if f==0:
            print('invali id!!!')
    elif choice==4:
        id=int(input('enter the id to be removed: '))
        f=0
        for i in std:
            if i[0]==id:
                std.remove(i)
                f=1
        if f==0:
            print('invalid id!!!')
    elif choice==5:
        id=int(input('enter id of std: '))
        f=0
        for i in std:
            if i[0]==id:
                print(i)
                f=1
      
    elif choice==6:
        break
    else:
        print('invalid option')