productname= input("enter the product you want to search")
number= input("the number of items")
number=int(number)
if (productname=="television"):
    print("price is 1 lakh")
    price=number*100000
    print("price is ",price)
elif (productname=="mobile"):
    print("price is 10000")
    price=number*10000
    print("price is ",price)
elif (productname=="ipad"):
    print("price is 1 crore")
    price=number*10000000
    print("price is ",price)
else:
    print("product not found")
