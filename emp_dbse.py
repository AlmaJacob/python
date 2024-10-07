import sqlite3
con=sqlite3.connect("python/emp_dbse.db")
try:
    con.execute("create table employee(id int,name text,age int,position text,exp text,salary int)")
except:
    print("table exist")    
emp=[]
while True:
    print("""
1.add
2.view
3.delete
4.update
5.search""")
    choice=int(input("enter ur choice : "))
    if choice==1
