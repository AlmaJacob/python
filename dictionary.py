# d={'name':"anu","age":20}

#acess
#-------

# print(d['name'])

#updation
#-----------
# d['name']='arjoy'
# print(d)

#insertion
#-----------
# d['country']='europe'
# print(d)

#itrating dictonary
#-------------------
# d={'name':"anu","age":20}
# for i in d:
    # print(i) # to get the key
    # print(d[i]) # to get the value
    # print(i,d[i]) # to get both key and value
 
 #to check a key is present in dictionary
# d={'name':"anu","age":20}
# if 'place' in d:
#     print('true')
# else:
#     print('false')

#to check a value is present in dictionary 
# d={'name':"anu","age":20}
# if d['name']=='alen':
#    print("true")
# else:
#    print('false')

#methods in dictionary
#---------------------------
# d={'name':"anu","age":20}
#get
#----
# print(d.get('name'))
# print(d.get('lang'))

#values
#---------
# print(d.values())

#keys
#-----
# print(d.keys())

#items
#-------
# print(d.items())

#pop
#----
#2 types
#(a).pop()
#--------
# print(d.pop())
#print(d)

#(b).pop(key)
#-------------
# print(d.pop('age'))
# print(d)

#update
#-------
#to update
# print(d.update({"age":23}))

#from keys(to print the  multiple values in alist into keys in a dictionary)
# ------------------------------------------------------------------
# d={}
# a={'age',"name",'colour'}
# d=d.fromkeys(a)
# print(d)
 
#setdefault(to print a single value as a key in dictionary)
# d={}
# d.setdefault('password')
# print(d)


#student management system using dictionary

# std=[]
# while True:
#         print(""" 
# 1.add std
# 2.view std
# 3.update std
# 4.delete std
# 5.search std
# 6.break  std
#              """)
#         choice=int(input("enter ur choice"))
#         if choice==1:
#                name=input("enter name")
#                age=input("enter age") 
#                mark=input("enter mark")
#                std.append({'name':name,"age":age,"mark":mark})
#         elif choice==2:
#               print('{:<10}{:<6}{:<6}'.format("name","age","mark"))
#               for i in std:
#                       print('{:<10}{:<6}{:<6}'.format(i["name"],i["age"],i["mark"]))
#         elif choice==3:
#                name=(input("enter your name"))
#                f=0
#                for i in std:
#                       if i["name"]==name:
#                              age=int(input("enter the age"))
#                              i["age"]=age
#                              f=1
#                if f==0:
#                                     print("name not in list") 
#         elif choice==4:
#                name=(input("enter your name"))
#                f=0
#                for i in std:
#                       if i["name"]==name:
                           
#                              std.remove(i)
#                              f=1
#                if f==0:
#                                     print("name not in list")
#         elif choice==5:
#                name=(input("enter your name"))
#                f=0
#                for i in std:
#                       if i["name"]==name:
#                              print(i)
#                              f=1
#                if f==0:
#                                     print("std not in list") 
#         elif choice==6:
#                break
#         else:
#           print("invalid choice")                                         
                                


#prgrm
#------
# a=[]
# b=[]
# std=[{"name":"anu","age":21},{"name":"jeeva","age":11},{"name":"hage","age":67},{"name":"jane","age":89}]
# for i in std:
#     if i["age"]>=30:
#         a.append(i)
#     else:
#         b.append(i)
# print("age >=30")
# print("*"*10)
# print("{:10}{:5}".format("name","age"))
# print("_"*14)
# for i in a:
#     print("{:10}{:5}".format(i["name"],i["age"]))

# print("age <=30")
# print("*"*10)
# print("{:10}{:5}".format("name","age"))
# print("_"*14)
# for i in b:
#     print("{:10}{:5}".format(i["name"],i["age"]))

#task2
#--------
# a={}
# num=int(input("enter a number :"))
# for i in range(num+1):
#     # print(i)
#     a[i]=i*i
# print(a)    

#task3
#-------
# a={}
# num=int(input("enter a number :"))
# for i in range(num+1):
#     if i%2==0:
#         a[i]=i*i
          
#     else:
#         a[i]=i*i*i 
# print(a)

#task4(print 123 and get input as 123 in letters)
#----------
# num=int(input("enter a number"))
# numbers={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
# s=""
# while num>0:
#    a=num%10
#    s=numbers[a]+" "+s
#    num//=10
# print(s)
    
l=[{'name':"anu","age":21,"lang":['mal',"eng"]}]
lg=input("enter the language")
l[0]["lang"].append()
print(l)