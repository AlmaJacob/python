import sqlite3
con=sqlite3.connect("python/sql1.db")
try:
  con.execute("create table students(roll_no int,name text,age int,mark real)")
except:
  print("table exist")

con.execute("insert into students(roll_no,name,age,mark)values(2,'alma',21,82),(3,'jk',22,78)")
con.commit()


