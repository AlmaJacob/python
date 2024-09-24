f=open("python/mul_table1.txt",'w')
b=int(input("enter a number"))
a=1
while a<=10:
    print(a,'*',b,"=",a*b)
    f.write(str(a)+'*'+str(b)+'='+str(a*b)+"\n")   
    a+=1
