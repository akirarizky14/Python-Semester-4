c = ''
f = 1
while c != 'x':
    a = int(input())
    c = input()
    if c == 'x':
        print(a)
        break
    else:
        if c == '+':
            b = int(input())
            print(a + b)
        elif c == '!' and a > 0:
            for i in range(1, a + 1):
                f *= i
            print(f)
        elif a == 0 and c == '!':
            print('1')
        elif c == '*':
            b = int(input())
            print(a * b)
        elif c == '-':
            b = int(input())
            print(a - b)
        elif c == '/':
            b = int(input())
            if b == 0:
                continue
            else:
                print(a // b)
        elif c == '%':
            b = int(input())
            if b == 0:
                continue
            else:
                print(a % b)