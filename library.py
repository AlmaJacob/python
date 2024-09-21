lb=[{'id':101,'name':'alma','place':'ksrgd','address':'abcd','mob':3419573124,'email_id':'amg','password':"123",'books':[]}]
book=[{'b_id':2,'book_name':"blossom",'stock':4,'price':350}]
def register():
    if len(lb)==0:
        id=101
    else:
        id=lb[-1]['id']+1
        email=input("enter your email: ")
        f=0
        for i in lb:
             if i['email_id']==email:
                f=1
                print("already existing!!!")
                register()
        if f==0:
            name=input("enter your name: ")
            place=input("enter your place: ")
            address=input("enter your address: ")
            mob=int(input("enter your mobile number: "))
            passw=input("set password: ")
            lb.append({'id':id,'name':name,'place':place,'address':address,'mob':mob,'email_id':email,'password':passw,'books':[]})
            print("registration successful!")
def login():
     uname=input("enter your username(email): ")
     passwrd=input("enter your password: ")
     f=0
     if uname=='admin' and passwrd=='admin':
          f=1
     user=''
     for i in lb:
         if uname==i['email_id'] and passwrd==i['password']:
              f=2
              user=i
     return f,user
def add():
    if len(book)==0:
          id=10
    else:
        id=book[-1]['b_id']+1
    bname=input("enter name of the book: ")
    stock=int(input("enter the book stock: "))
    price=int(input("enter the book price: "))
    book.append({'b_id':id,'book_name':bname,'stock':stock,'price':price})
def view_book():
     print('_'*40)
     print("{:<10}{:<15}{:<10}{:<10}".format('book_id','book_name','stock','price'))
     print('_'*40)
     for i in book:
          print("{:<10}{:<15}{:<10}{:<10}".format(i['b_id'],i['book_name'],i['stock'],i['price']))
def update():
     id=int(input("enter the update book id: "))
     f=0
     for i in book:
          if i['b_id']==id:
               f=1
               stock=int(input("enter the updated stock: "))
               price=int(input("enter updated price: "))
               i['stock']=stock
               i['price']=price
               print("updated successfully")
     if f==0:
          print("invalid id!!!")
def delete_book():
     id=int(input("enter the book id to be removed: "))
     f=0
     for i in book:
          if i['b_id']==id:
               f=1
               book.remove(i)
               print("DELETED!!")
     if f==0:
          print("invalid id!!!")
def view_users():
    print('_'*70)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format('id','name','place','address','mob','email'))
    print('_'*70)
    for i in lb:
         print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['place'],i['address'],i['mob'],i['email']))
          
def view_profile(user):
     print('_'*70)
     print("{:1<0}{:<15}{:<15}{:<15}{:<15}{:<15}".format('id','name','place','address','mob','email')) 
     print('_'*70)
     for i in lb:
         print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['place'],i['address'],i['mob'],i['email_id']))    
def take_book(user):
     id=int(input("enter ur id"))
     f=0
     for i in book:
          if i['b_id']==id:
               f=1
               if i['stock']>0:
                    user['book'.append(i['b_ id'])]
                    i['stock']-=1
               else:
                    print("out of stock")
def return_books(user):
     id=int(input("enter ur id"))
     f=0
     for i in book:
          if i['b_id']==id and id in user["books"]:
               f=1
               i['stock']+=1
               user["books"].remove(id)
               print("book returned")
               if f==0:
                    print("book not found")
def books_in_hand(user):
     print(user['books'])                                        
while True:
    print('''
        1.register
        2.login
        3.exit
''')
    choice=int(input("enter your choice: "))
    if choice==1:
        register()
    elif choice==2:
         f,user=login()
         if f==1:
              while True:
                   print('''
                    1.add book
                    2.view book
                    3.update book
                    4.delete book
                    5.view users
                    ''')
                   sub_ch=int(input("enter your choice: "))
                   if sub_ch==1:
                        add()
                   elif sub_ch==2:
                        view_book()
                   elif sub_ch==3:
                        update()
                   elif sub_ch==4:
                        delete_book()
                   elif sub_ch==5:
                        view_users()
         elif f==2:
                 while True:
                      print("""
                          1.view profile
                          2.view book
                          3.take a book
                          4.return book
                          5.books in hand
                          6.exit
                        """)
                      user_choice=int(input("enter ur choice: "))
                      if user_choice==1:
                           view_profile(user)
                      elif user_choice==2:
                           view_book()
                      elif user_choice==3:
                           take_book(user)
                      elif user_choice==4:
                           return_books(user)
                      elif user_choice==5:
                           books_in_hand(user)     

                   
                           
    else:
            print("invalid uname or password: ")