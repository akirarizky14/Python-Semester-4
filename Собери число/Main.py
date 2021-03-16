input('Welcome!')
a = int(input('Исходный пароль: '))
b = a // 100 + (a % 100) // 10
c = (a % 100) // 10 + a % 10
d = str(c) + str(b) if c > b else str(b) + str(c)
print('Зашифрованный пароль: ', d)