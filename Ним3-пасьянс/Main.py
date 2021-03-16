a = int(input())
b = int(input())
y = int(input())
 
while a != 0 or b != 0 or y != 0:
    n = int(input())
    c = int(input())
 
    if n == 1:
        a -= c
        print(a, b, y)
    elif n == 2:
        b -= c
        print(a, b, y)
    elif n == 3:
        y -= c
        print(a, b, y)