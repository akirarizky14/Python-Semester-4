i = 0
s = 0
while True:
    a = int(input('Температура: '))
    if a > 0:
        s = s + 1
        i = i + a
        i = i/s
    elif a <= -300:
        print(i)
        break