import sqlite3
con=sqlite3.connect("python/sql1.db")
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
name=input("enter name to delete ")
con.execute("delete from students where name=?",(name,))
con.commit()