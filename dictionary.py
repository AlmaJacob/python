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
d={'name':"anu","age":20}
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
d={}
d.setdefault('password')
print(d)