#library management system using dictionary inside list
book=[{'b_id': 11, 'book_name': 'aa', 'stock': '22', 'book_price': '33'},{'b_id': 12, 'book_name': 'bbb', 'stock': '55', 'book_price': '666'}]

while True:
    print("""
welcome to the library management system!!!
          
1.add book
2.update book
3.remove book
4.view all book
5.search book
6.exit
          """)
    choice=int(input("enter ur choice : "))
    if choice==1:
        b_id=int(input('enter the book id: '))
        book_name=(input('enter the name: '))
        stock=input("enter the book stock : ")
        book_price=input("enter the price of the book : ")
        book.append({'b_id':b_id,"book_name":book_name,"stock":stock,"book_price":book_price})
        print(book)
    elif choice==2:
        book_name=input("enter the name of the book : ")
        f=0
        for i in book:
            if i["book_name"]==book_name:
                    stock=input("enter the book_stock : ")
                    book_price=input('enter the price: ')
                    i['stock']=stock
                    i['book_price']=book_price
                    f=1
        if f==0:
             print(" name not avialable ")            
    elif choice==3:
        b_id=input("enter id of the book : ")
        f=0
        for j in book:
            print(j)
            if j['b_id']==b_id:
                book.remove(j)
            f=1
        # for i in book:
        #     print(i)
        #     if i['b_id']==b_id:
        #          book.remove(i)
        #          f=1
        #     if i["book_name"]==book_name:
        #         book.remove(i)
        #         f=1
        if f==0:
            print("name not available")

    # elif choice==4:
    #         print('_'*40)
    #         print('{:<6}{:<4}{:<8}'.format('book_name','stock','book_price'))
    #         print('_'*40)
    #         print('{:<6}{:<4}{:<8}'.format(i[0],i[1],i[2]))

    # elif choice==5:
    #         book_name=("enter name of the book")
    #         f=0
    #         for i in book:
    #                   if i["book_name"]==book_name:
    #                          print(i)
    #                          f=1
    #         if f==0:
    #                             print(" book not available ")

    # elif choice==5:
    #         break
    # else:
    #         print(" invalid choice ")                                                                 