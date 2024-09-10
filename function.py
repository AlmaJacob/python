# def fun1():
#     print("addition")
   
# def fun2():
#     print("substraction")
# def fun3():
#       print("multiplication")
# def fun4():
#      print("divsion")
           

# print(10+5)
# fun1()
# print(10-5)
# fun2()
# print(10*5)
# fun3()
# print(10/5)
# fun4()
    
# def fun1():#function creation
#   print("addition")
#   print("substraction")
#   print("multiplication")
#   print("divsion")

# print(10+5)
# fun1()#function calling
# print(10-5)
# fun1()
# print(10*5)
# fun1()
# print(10/5)
# fun1()

#scope of function
#-----------------------
# def func1():
#     a=21     #local variable
#     print("a inside ",a)
#     print("b insdide ",b)

# b=37   #global variable
# func1()
# print('b outside ',b) 
 #it did not work because it is a local variable
# print("a outside ",a)


#we can change local variable into global variable using global keyword

# def func2():
#     global a
#     a=32
#     print("a is",a)
#     print("c is",c)
# c=21
# func2()
# print("a is",a)
# print("c is ",c)  


#prgm
# def func1():
#     return "hello guyzz",11,48

# a,b,c=func1()
# print(a)
# print(b)
# print(c)

#prgrm
# def func1():
#     a="heyy"
#     b=1 
#     c=2
#     return a,b,c

# a1,b1,c1=func1()
# print(a1)
# print(b1)
# print(c1)


# functional arguments
#---------------------------
#types of functional arguments
#-------------------------------
#positional arguments
#---------------------
# def dtls(age,name):
#     print("age =",age)
#     print('name =',name)

# dtls(21,'anu')
# dtls(31,"jake")


#keyword argument
#-------------------
# def dtls(age,name):
#     print("age =",age)
#     print('name =',name)

# dtls(name="hari",age="23") 