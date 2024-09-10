def numbers():
    a=int(input("enter a first number :"))
    b=int(input("enter a first number :"))
    return(a,b)
def add():
    a,b=numbers()
    print(a+b)
def sub():
    a,b=numbers()
    print(a-b)
def mul():
    a,b=numbers()
    print(a*b)
def div():
    a,b=numbers()
    print(a/b)
def mod_div():
    a,b=numbers()
    print(a%b)


while True:
    print("""
          1.additon
          2.subsrtaction
          3.multiplication
          4.division
          5.modulas division
          6.exit""")
    choice=(input("enter the choice :"))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        mod_div()
    elif choice==6:
        break
    else:
        print('invalid option')          