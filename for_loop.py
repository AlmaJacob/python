#for loop used in 3 ways
#*************************


#range(limit)
#*************

# for i in range(15):
#    print("suspecious")

   #range(start,end)
#*********************
# for i in range(4,17):
#       print(i)

#range(start,end,updation)
#***************************

# for i in range(2,19,5):
#       print(i)      

#sum of n numbefrs using for loop
#*********************************


# start=int(input("enter first number"))
# end=int(input("enter end value"))
# sum=0
# for i in range(start,end+1):
#     sum+=i
# print("sum",sum)

#print even numbers using for loop
#***********************************


# start=int(input("enter first number"))
# end=int(input("enter end value"))
# for i in range(start,end+1):
#     if i%2==0:
#           print(i)
#     start+=i


    #print odd numbers using for loop
#*********************************************


# start=int(input("enter first number"))
# end=int(input("enter end value"))
# for i in range(start,end+1):
#     if i%2!=0:
#           print(i)
    
# #sum of even numbers
#*********************************************

# a=int(input("enter first no"))
# b=int(input("enter last no"))
# sum=0
# for i in range(a,b+1):
#     sum=sum+a
#     if a%2==0:
#         print(a)
#     a+=1 
# print("sum is : ",sum)   

#sum of odd numbers
#*********************************************

# a=int(input("enter first no"))
# b=int(input("enter last no"))
# sum=0
# for i in range(a,b+1):
#     sum=sum+a
#     if a%2!=0:
#         print(a)
#     a+=1 
# print("sum is : ",sum)   

#multiplication table
#*********************************************

# b=int(input("enter a number"))
# a=1
# for i in range(a,b+1):
#     print(a,'*',b,"=",a*b)
#     a+=1

#displaying sum of both odd and even
#*********************************************

# a=int(input("enter starting number "))
# b=int(input('enter last number'))
# n=0
# even=0
# odd=0
# for i in range(a,b+1):
#     n=n+a
#     if a%2==0:
#         even=even+a
#     else:
#         odd=odd+a
#     a+=1    
# print("sum of n natural numbers :  ",n) 
# print("sum of even  numbers :  ",even)    
# print("sum of odd numbers :  ",odd)    


#factorial of a number
#*********************************************
# b=int(input("enter a limit"))
# fact=1
# a=1

# for i in range(b):
#     fact=fact*a
   
#     a+=1
# print("fact ",fact)


#print string top to bottum using for loop

# j=input("enter a string")


# for i in j:
#     print(i)

#reverse of a string

# j=input("enter a string")
# rev=""
# for i in j:
#     rev=i+rev
# print(rev)


