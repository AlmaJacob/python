#syntax of lambda method
#------------------------
# lambda(function,iter)

#printing even numbers using lambda function with filter method(here x variable indicates function argument)
# l=[1,3,4,6,7,8,9]
# print(list(filter(lambda x:x%2==0,l)))

#printing odd numbers using lambda function with filter method
# l=[1,3,4,6,7,8,9]
# print(list(filter(lambda x:x%2!=0,l)))

##printing even numbers using normal function with filter method
# l=[1,3,4,6,7,8,9]
# def fun1(x):
#     return x%2==0
# print(list(filter(fun1,l)))

##printing odd numbers using normal function with filter method
# l=[1,3,4,6,7,8,9]
# def fun1(x):
#     return x%2!=0
# print(list(filter(fun1,l)))

#printing perticluar letter in list using lambda function with filter method
# l2=['blue','green','yellow']
# print(list(filter(lambda x:'l' in x,l2)))

#printing perticluar letter in list using normal function with filter method

# l2=['blue','green','yellow']
# def func(x):
#     return 'o' in x
# print(list(filter(func,l2)))

#syntax of map method
#------------------------
# lambda(function,iter)

#finding cube of number using lambda function with map method
# k=[2,4,65,1,4,78,3,4]
# print(list(map(lambda x:x**3,k)))

#finding cube of number using normal function with map method(here a variable indicates function argument)
k=[2,4,65,1,4,78,3,4]
def f(a):
    return a**3
print(list(map(f,k)))