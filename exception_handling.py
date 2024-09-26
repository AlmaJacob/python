#there are 4 keywords in exception_handling
# print("the way of light")
# a="heaven"
# b="2"
# try:#we write the code inside the try  which is going to be an error
#     print(a+b)
# except:#we write the code inside the except  which is not an error after an incorrect code
#     print("an error occured")
# else:#these code will only work error is not occurd otherwise not work
#     print("else")
# finally:#it will always work even the code correct or not
#     print("these code will run ")        

l=[1,4,4.7,"error"]
sum=0
for i in l:
         if type(i)==int or type(i)==float:
          sum=sum+i
print(sum)
 

