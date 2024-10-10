import mysql.connector
con=mysql.connector.connect(host='localhost',user='work',password='work', database='std1')
con.autocommit=True
cur=con.cursor()

# creating database

# cur.execute("create database std1")
#creating table

try:
    cur.execute("create table std2(roll_no int,name text,age int)")
except:
    print("table exist")
#inserting values into table using user input
# roll_no=int(input("enter roll no of student"))        
# name=input("enter name of student: ")
# age=int(input("enter age of student : "))
# cur.execute("insert into std2(roll_no,name,age) values(%s,%s,%s)",(roll_no,name,age))

#for filteration of valuses from database
# cur.execute("select * from std2 where name='arun' ")
# data=cur.fetchall()
# for i in data:
#     print(i)

# filter the values from database using user input
# name=(input("enter name of the student "))
# cur.execute("select * from std2 where roll_no=%s",(name,))
# data=cur.fetchall()
# for i in data:
#    print(i)

#updating

# data=cur.execute("update std2 set name ='sherly' where  name='lilyy'")

