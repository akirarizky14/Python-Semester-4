print('Введите количество камней в куче:')
a = int(input())
while a > 0:
    b = a % 4
    if b == 0:
        b = 2
    print('Забираю камни в количестве', b)
    a -= b
    print('Осталось камней:', a)
    if a == 0:
        print('ИИ выиграл!')
    else:
        print('Сколько камней вы хотите взять?')
        b = 0
        while not (1 <= b <= 3 and b <= a):
            b = int(input())
        a -= b
        print('Осталось камней:', a)
        if a == 0:
            print('Вы проиграли!')