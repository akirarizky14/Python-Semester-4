price = int(input())
a = list()
in_stock = False
workflag = False 
while price != 0:
    a.append(price)
    if (len(a) >= 3) & (workflag == False):
        if (in_stock == False):
            if a[len(a)-3] > a[len(a)-2] < a[len(a)-1]:
                inprice = a[len(a)-1]
                in_stock = True
             
        if (in_stock == True):
            if a[len(a)-3] < a[len(a)-2] > a[len(a)-1]:
                outprice = a[len(a)-1]
                #break
                workflag == True
    price = int(input())
print(inprice, outprice, outprice - inprice)