print("Welcome to Calculator")
print("First Number : " )
a = int(input())
print("Second Number : ")
b = int(input())
print("Choose +,-,x,/")
c = input()

if '+' in c:
    print(a+b) 
elif'-' in c:
    print(a-b)
elif 'x' in c:
    print(a*b)
elif '/' in c:
    if b == 0:
        print("888888")
    else:
        print(a/b)
else:
    print("888888")

