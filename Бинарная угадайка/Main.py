y = 1
y1 = 1000
print('500')
b = input()
while b != '=':
    if b == '>':
        y1 = y1 - (y1 - y) // 2
        x = y1 - (y1 - y) // 2
    if b == '<':
        y = y + (y1 - y) // 2
        x = y + (y1 - y) // 2
    print(x)
    b = input()