import sqlite3
import tkinter


window=tkinter.Tk()
window.maxsize(400,400)
window.minsize(200,200)
window.config(bg="pink")
window.title("tkinter-prgm")
#
def save():
    l2.config(text=e1.get())
# l1=tkinter.Label(window,text="login",bg="white",fg="black")
# l1.pack()
# e1=tkinter.Entry(window)
# e1.pack()
# b1=tkinter.Button(window,text="submitt",bg="yellow",activebackground="orange",fg="black",activeforeground="blue",padx=40,pady=10 ,command=submitt)
# b1.pack()
# l2=tkinter.Label(window)
# l2.pack()
#using place method
def reg_form():
    window1=tkinter.Tk()
    window1.maxsize(400,400)
    window1.minsize(200,200)
    window1.config(bg="pink")
    window1.title("tkinter-prgm")

    def reg():
        # print("username: ",e1.get())
        # l2.config(text=e1.get())
        # print("password: ",e2.get())
        # l3.config(text=e2.get())
        con=sqlite3.connect("sample.db")
        # con.execute("create table user(username text,password text)")
        con.execute("insert into user(username,password)values(?,?)",(e1.get(),e2.get()))
        con.commit()
        window1.destroy()


    l1=tkinter.Label(window1,text="registration page",bg="white",fg="black")
    l1.place(x=150,y=10)
    l2=tkinter.Label(window1,text="user name",bg="white",fg="black")
    l2.place(x=80,y=40)
    e1=tkinter.Entry(window1)
    e1.place(x=200,y=40)
    l3=tkinter.Label(window1,text="password",bg="white",fg="black")
    l3.place(x=80,y=70)
    e2=tkinter.Entry(window1)
    e2.place(x=200,y=70)
    b1=tkinter.Button(window1,text="register",bg="yellow",activebackground="orange",fg="black",activeforeground="blue",padx=40,pady=10,command=reg)
    b1.place(x=150,y=100)
    window1.mainloop()


def home(): 
    window2=tkinter.Tk()
    l1=tkinter.Label(window2,text="home page")
    l1.pack()
    b1=tkinter.Button(window2,text=" logout ",command=window2.quit)
    b1.pack()
    window2.mainloop()


def login():
    con=sqlite3.connect("sample.db")
    data=con.execute("select * from user where username=? and password=?",(e1.get(),e2.get()))
    f=0
    for i in data:
        f=1
        home()
    if f==0:
        l4.config(text=" invalid username or password ")


    

l1=tkinter.Label(window,text="login page",bg="white",fg="black")
l1.place(x=150,y=10)
l2=tkinter.Label(window,text="user name",bg="white",fg="black")
l2.place(x=80,y=40)
l4=tkinter.Label(window)
l4.place(x=130,y=200)
e1=tkinter.Entry(window)
e1.place(x=200,y=40)
l3=tkinter.Label(window,text="password",bg="white",fg="black")
l3.place(x=80,y=70)
e2=tkinter.Entry(window)
e2.place(x=200,y=70)
b1=tkinter.Button(window,text="save",bg="yellow",activebackground="orange",fg="black",activeforeground="blue",padx=40,pady=10,command=login) 
b1.place(x=150,y=100)
b2=tkinter.Button(window,text="Register",bg="yellow",activebackground="orange",fg="black",activeforeground="blue",padx=40,pady=10 ,command=reg_form)
b2.place(x=250,y=150)
l2=tkinter.Label(window)
l2.place(x=160,y=150)
window.mainloop()                                                   