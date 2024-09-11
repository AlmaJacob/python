emp=[]

def login():
    username=input("enter username :")
    password=input("enter password :")
    f=0
    if username=="admin" and password=="admin":
     f=1
    return f
def add_emp():
    id=int(input("enter id :"))
    f1=0
    for i in emp:
        if i["id"]==id:
            f1=1
            print("id exits")
            add_emp()
    if f1==0:        
      name=(input("enter name :"))
      age=int(input("enter age :"))
      salary=int(input("enter salary :"))
      place=(input("enter place :"))
      dob=(input("enter dob :"))
      emp.append({"id":id,"name":name,"age":age,"salary":salary,"place":place,"dob":dob})

def update():
    id=int(input("enter id :"))
    f1=0
    for i in emp:
        if i["id"]==id:
            f1=1
            name=(input("enter name :"))
            age=int(input("enter age :"))
            salary=int(input("enter salary :"))
            place=(input("enter place :"))
            dob=(input("enter dob :"))
            emp.append({"id":id,"name":name,"age":age,"salary":salary,"place":place,"dob":dob})
            i["name"]=name
            i["age"]=age
            i["salary"]=salary
            i["place"]=place
            i["dob"]=dob
            break
    if f1==0:
            print("invalid id") 
def delete():
    id=int(input("enter id :"))
    f1=0
    for i in emp:
        if i["id"]==id:
            f1=1
            emp.remove(i)
    if f1==1:
        print("invalid id") 
def display():
    print('{:<5}{:<10}{:<5}{:<15}{:<10}{:<18}'.format("id","name","age","salary","place","dob"))
    for i in emp:
            print('{:<5}{:<10}{:<5}{:<15}{:<10}{:<18}'.format(i["id"],i["name"],i["age"],i["salary"],i["place"],i["dob"]))

while True:
   print("""
1.login
2.exit
3.logout         
""")
   ch=int(input("enter ur choice :"))
   if ch==1:
      f=login()
      if f==1:
         while True:
            print('''
                1.add
                2.update
                3.delete
                4.display
            ''')
            sub_ch=int(input("enter ur sub choice :"))
            if sub_ch==1:
               add_emp()
            elif sub_ch==2:
                update()
            elif sub_ch==3:
                delete()
            elif sub_ch==4:
                display()
elif ch==3:
break
    else:
        print("invalid choice") 

            