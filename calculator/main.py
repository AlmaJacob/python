#whenever we using from to import a modlue we can directly call the function
import number
import add as c
from sub import sub
from mul import*
import div as d
from mod import mod
while True:
    print("""
1.add
2.sub
3.mul
4.div
5.mod
6.exit
    """)
    
    ch=int(input("enter ur choice : "))
    if ch==1:
        a,b=number.number()
        c.add(a,b)
    elif ch==2:
        a,b=number.number()
        sub(a,b)
    elif ch==3:
         a,b=number.number()
         mul(a,b)
    elif ch==4:
        a,b=number.number()
        d.div(a,b)
    elif ch==5:
         a,b=number.number()
         mod(a,b)
    elif ch==6:
        break
    else:
        print('invalid option')




