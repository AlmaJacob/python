# import sqlite3
# #create a table 

# con=sqlite3.connect("python/sql1.db")
# try:
#     con.execute("create table std (roll_no int,name text,age int, mark real)")
# except:
#     print("table exists")

 #adding values into databse
  # con.execute("insert into std(roll_no,name,age,mark)values(2,ajay,26,46),(7,alen,28,78)")   



#                                                                                                                                                                                                                        
# limit=int(input("enter a limit"))
# for i in range(limit):
#   roll=int(input("enter ur roll_no : "))
#   name=input("enter ur name : ")
#   age=int(input("enter ur age : "))
#   mark=float(input("enter ur mark : "))
# con.execute("insert into students(roll_no,name,age,mark)values(?,?,?,?)",(roll,name,age,mark))
# con.commit()

#for selcect value from database
# data=con.execute("select * from students")

# print("{:<9}{:<8}{:<5}{:<5}".format("roll_no","name","age","mark"))
# print('-'*35)
# for i in data:
#  print("{:<9}{:<8}{:<5}{:<5}".format(i[0],i[1],i[2],i[3]))

  # print(i)

#for filteration of valuses from database
# data=con.execute("select * from students where name='jk' ")
# for i in data:
#     print(i)

#filter the values from database using user input
# roll=int(input("enter roll no  "))
# data=con.execute("select * from students where roll_no=?",(roll,))
# for i in data:
#    print(i)

#updation in database
# data=con.execute("update students set name ='aromal' where  name='jane'")
# con.commit()

#updation in database using user input
# name=(input("enter ur name "))
# new_name=(input("enter ut new name "))
# data=con.execute("update students set name =? where name=?",(new_name,name))
# con.commit()

#deletion in  database
# con.execute("delete from students  where name='aadhi'")
# con.commit()

#deletion using user input
# name=input("enter name to delete ")
# con.execute("delete from students where name=?",(name,))
# con.commit()

#select a value from database
# data=con.execute("select * from students where name like '__e%'")
# for i in data:
#     print(i)


#to make ascending order of  values of database using order by 
# data=con.execute("select * from students order by name ")
# for i in data:
#     print(i) 


#to make descending order of  values of database usin order by
# data=con.execute("select * from students order by name desc")
# for i in data:
#     print(i)     

#to avoid duplicates using group by