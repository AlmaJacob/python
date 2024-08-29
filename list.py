# l=[12,23.5,8,10,12,'abc']
# for i in l:
#     print(i)
# if 10 in l:
#         print('yes')
# else:
#         print("not found")


 #indexing in list
 #------------------
# l=[10,2,2.3,"raj"]
# print (l[2])       

#updation in list
#------------------
# l=[10,2,2.3,"raj"]
# l[1]="leave"
# print (l)  
# 
#methods in list
# ---------------

#adding methods
#---------------

#append(for a single value adding)
#--------------------------------------
# l=[2,3.4,'jkw']
# l.append(34)
# print(l)

#extend(for addition of multiple values)
#--------------------------------------------
# l=[2,3.4,'jkw']
# l.extend(['a',8,'b'])
# print(l)


#insert(for a value for a perticular position)
#-----------------------------------------------


#deleting methods
#------------------

#clear(to delete all elements in a list)
#-----------------------------------------

# l=[10,2.34,8,'afc']
# l.clear()
# print(l)

#pop(to delete last element in a list)
#-------------------------------------------
#2 types
#------------
#pop()
#------

# l=[10,2.34,8,'afc']
# l.pop()
# print(l)

#pop(index)
#---------------

# l=[10,2.34,8,'afc']
# l.pop(1)
# print(l)

#remove(to remove perticular element)
#---------------------------------------

# l=[10,2.34,8,'afc']
# l.remove(2.34)
# print(l)

#another methods
#------------------

#sort()
#-------

# l=[5,2,8,4,14]
# l.sort()
# print(l)

#reverse()
#-----------

# l=[5,2,8,4,14]
# l.reverse()
# print(l)


#copy()
#-----------

# l=[5,2,8,4,14]
# l2=l.copy()
# print(id(l))
# print(id(l2))
# print("l=",l)
# print("l2=",l2)
# l.pop()
# print("l=",l)
# print("l2=",l2)

#index(to check the index of a element in list)
#------------------------------------------------------

#task
#-------
#sum of even number is sum
#------------------------------

# l=[5,2,8,4,14]
# sum=0
# for i in l:
#     if i%2==0:
#         sum+=i
#         print(i)
# print(sum)        

#print the reverse of string in list of each element
#--------------------------------------------------------

# l=['alma','origin','name']
# for i in l:
#     print(i[::-1])


#if the elements in the list is float or int then print the sum
#------------------------------------------------------------------

# l=[1,2,10.3,5.8,'ajay']
# sum=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         sum+=i
# print(sum)


#if any duplicate element is present in list print non-duplicate elements
#----------------------------------------------------------------------------

# l=[1,34,1,100,4,34]
# l1=[]
# for i in l:
#   if i not in l1:
#     l1.append(i)
# print(l1)

#taking name by inputing and print in list
#-------------------------------------------

# names=[]
# limit=int(input("enter a limit"))
# for i in range(limit):
#     name=input("enter name")
#     names.append(name)
# print(names)

#print the details of a student in list using nested list
#---------------------------------------------------------

# std=[]
# limit=int(input("enter a limit"))
# for i in range(limit):
#     name=input("enter name")
#     age=input("enter age") 
#     mark=input("enter mark")
#     std.append([name,age,mark])
# print(std)


#we want to add,delete,update,view the list
#-------------------------------------------------

# std=[]
# while True:
#         print(""" 
# 1.add std
# 2.view std
# 3.update std
# 4.delete std
#              """)
#         choice=int(input("enter ur choice"))
#         if choice==1:
#                name=input("enter name")
#                age=input("enter age") 
#                mark=input("enter mark")
#                std.append([name,age,mark])
#         elif choice==2:
#               print('{:<10}{:<6}{:<6}'.format("name","age","mark"))
#               for i in std:
#                       print('{:<10}{:<6}{:<6}'.format(i[0],i[1],i[2]))
                    
              
                     
