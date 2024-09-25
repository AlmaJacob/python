
# b=int(input("enter a number"))
# a=1
# while a<=10:
#     print(a,'*',b,"=",a*b)
#     f.write(str(a)+'*'+str(b)+'='+str(a*b)+"\n")   
#     a+=1
f=open("mul_table1.txt",'w')
a=int(input("enter a number"))
for i in range(1,11):
    for j in range(1,a+1):
         f.write(str(i)+'*'+str(j)+'='+str(j*i)+"\t")
    f.write("\n")        

