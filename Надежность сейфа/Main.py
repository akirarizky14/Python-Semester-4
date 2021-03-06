print("Check yout digits!")
a = input()
b = len(set(a))

if b == 2:
    print("you have 2 same digits")
elif b == 3:
    print("OK")
else:
    print("you have 3 same digits")
