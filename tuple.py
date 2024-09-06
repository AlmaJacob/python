# t=(1,3,4.8,"acg")
# print(t)

#itration of tuple
# t=(1,3,4.8,"acg")
# for i in t:
#     print(i)

#checking whether value is present in list or not using membership operator
# t=(1,3,4.8,"acg")
# for i in t:
#     if 2 in t:
#         print("True")
#     else:
#         print("false")  

#accesing a value from tuple
# t=(1,3,4.8,"acg")
# print(t[0])

#tuple basics
#1
# t=1,2,3.8,"sd"
# print(type(t))
#tuple

#2
# t2=(10,)
# print(type(t2))
#tuple

# t4=(23)
# print(type(t4))
#int

#3(we can add values into tuple inside list because list is mutable)
# k=(1,2,['abc',3])
# print(k[2])
# k[2].append("jake")
# print(k)


#3(we can't add values into list inside tuple because tuple is  emutable)
# j=["a",4,5(32,"arun")]
# print(j[3])
# j[2].append(3)
# print(j)

#methods in tuple
#1.index(to find the index position of a value in tuple)
# t=(2,5,6)
# print(t.index(2))

#2.count(to find how many times a value is repeated in a tuple)
# t=(2,5,7,2)
# print(t.count(2)) 

#we can make deletion or updation in tuple by coverting tuple into list using type casting
# t=(3,6,46)
# t=list(t)
# t.append(678)
# t=tuple(t)
# print(t)
# print(type(t))


