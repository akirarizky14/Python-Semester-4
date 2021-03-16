a = int(input("Первая кучка: "))
b = int(input("Вторая кучка: "))
 
while a !=0 or b !=0:    
    n = int(input("Кучка: "))-1
    c = int(input("Сколько: "))
  
    if n:
        b -= c
        print(a,b)
    else:
        a -= c