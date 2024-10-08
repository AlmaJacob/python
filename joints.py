import sqlite3
con=sqlite3.connect("python/joints.db")
try:
 con.execute("create table std(roll_no int,name text,age int)")
except:
 print("Table Exists....")
try:
 con.execute("create table mark(roll_no int,sub text,mark real)")
except:
 print("Table Exists...")
con.execute("insert into mark(roll_no,sub,mark)values(1,'py',65),(2,'php',75),(4,'java',80),(1,'php',72)")
con.commit()
con.execute("insert into std(roll_no,name,age)values(1,'a',21),(2,'b',24),(3,'c',23)")
con.commit()
#inner join

# data=con.execute("select std.roll_no,std.name,std.age,mark.sub,mark.mark from std inner join mark on std.roll_no=mark.roll_no")
# for i in  data:
#  print(i)

#left join

# data=con.execute("select std.roll_no,std.name,std.age,mark.sub,mark.mark from std left join mark on std.roll_no=mark.roll_no")
# for i in  data:
#  print(i)

#cross join

# data=con.execute("select std.roll_no,std.name,std.age,mark.sub,mark.mark from std cross join mark on std.roll_no=mark.roll_no")
# for i in  data:
#  print(i)