emp=[]

def login():
    username=input("enter username :")
    password=input("enter password :")
    f=0
    user=''
    if username=="admin" and password=="admin":
        f=1
    for i in emp:
       if i["id"]==username and i["dob"]==password:
            f=2
            user=i
    return f,user
def add_emp():
    id=str(input("enter id :"))
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
    id=str(input("enter id :"))
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
    id=str(input("enter id :"))
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
def view_profile():
   print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','name','age','salary','place','dob'))
   print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(user['id'], user['name'], user['age'],user['salary'],user['place'],user['dob']))
def edit_profile():
   f1=0
   for i in emp:
      if i['id']==user['id']:
         f1=1
         name=input("enter emp name")
         age=int(input("enter emp age"))
         place=input("enter emp place")
         dob=input("date of birth")
         i['name']=name
         i['age']=age
         i['place']=place
         i['dob']=dob
   if f1==0:
      print("invalid id")
while True:
   print("""
1.login
2.exit
          
""")
   ch=int(input("enter ur choice :"))
   if ch==1:
      f,user=login()
      if f==1:
         while True:
            print('''
                1.add
                2.update
                3.delete
                4.display
                5.logout  
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
            elif sub_ch==5:
                break
            elif f==0:
              print("invalid password or username")
            elif f==2:
              while True:
                print("""
                   1.view profile
                   2.edit profile
                   3.logout 
""")

                sub_ch=int(input("enter ur choice :"))
                if sub_ch==1:
                    view_profile(user)
                elif sub_ch==2:
                  edit_profile()
                elif sub_ch==3:
                  break
  
            