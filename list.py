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

l=[5,2,8,4,14]
print(l.index(4
              ))

