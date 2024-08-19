#while loop

# a=int(input("enter first no"))
# b=int(input("enter ending no"))
# while a<=b:
#     print(a)
#     a += 7

#while loop in the case of string

# i=1
# a=int(input("enter a limit"))
# while i<=a:
#     print("delema")
#     i+=1

#sum of n numbers

# a=int(input("enter first no"))
# b=int(input("enter last no"))
# sum=0
# while a<=b:
#     sum=sum+a
#     a+=3
# print("sum is : ",sum)

#print even numbers using loop

# a=int(input("enter first no"))
# b=int(input("enter last no"))
# while a<=b:
#     if a%2==0:
#         print(a)
#     a+=1  


#print odd numbers using loop

# a=int(input("enter first no"))
# b=int(input("enter last no"))
# while a<=b:
#     if a%2!=0:
#         print(a)
#     a+=1 
   




# sum of even numbers
# a=int(input("enter first no"))
# b=int(input("enter last no"))
# sum=0
# while a<=b:
#     sum=sum+a
#     if a%2==0:
#         print(a)
#     a+=1 
# print("sum is : ",sum)   

#sum of odd numbers


# a=int(input("enter first no"))
# b=int(input("enter last no"))
# sum=0
# while a<=b:
#     sum=sum+a
#     if a%2!=0:
#         print(a)
#     a+=1 
# print("sum is : ",sum)  
#  

#multiplication table

# b=int(input("enter a number"))
# a=1
# while a<=25:
#     print(a,'*',b,"=",a*b)
#     a+=1

a=int(input("enter starting number "))
b=int(input('enter last number'))
n=0
even=0
odd=0
while a<=b:
    n=n+a
    if a%2==0:
        even=even+a
    else:
        odd=odd+a
    a+=1    
print("sum of n natural numbers :  ",n) 
print("sum of even  numbers :  ",even)    
print("sum of odd numbers :  ",odd)    
       
    