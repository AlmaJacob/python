#product management system using dictionary

prd=[]
while True:
        print(""" 
1.add product
2.view product
3.update product
4.delete product
5.search product
6.break  
             """)
        choice=int(input("enter ur choice"))
        if choice==1:
               product_name=input("enter product name: ")
               price=input("enter product price: ") 
               brand=input("enter product brand: ")
               
               prd.append({'product_name':product_name,"price":price,"brand":brand})
        elif choice==2:
              print('{:<14}{:<8}{:<1}'.format("product_name","price","brand","exp_date",))
              for i in prd:
                      print('{:<14}{:<8}{:<12}'.format(i["product_name"],i["price"],i["brand"]))
        elif choice==3:
               name=(input("enter product name :"))
               f=0
               for i in prd:
                      if i["product_name"]==product_name:
                             price=int(input("enter the price :"))
                             i["price"]=price
                             f=1
               if f==0:
                                    print("product name not in list") 
        elif choice==4:
               name=(input("enter product name"))
               f=0
               for i in prd:
                      if i["product_name"]==product_name:
                           
                             prd.remove(i)
                             f=1
               if f==0:
                                    print("product name not in list")
        elif choice==5:
               name=(input("enter product name"))
               f=0
               for i in prd:
                      if i["product_name"]==product_name:
                             print(i)
                             f=1
               if f==0:
                                    print("prd not in list") 
        elif choice==6:
               break
        else:
          print("invalid choice")                                         
                                

