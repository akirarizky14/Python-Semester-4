d = int(input())
for i in range(0, 17):
    if i % d == 0:
        print('ДА')
    else:
        print('НЕТ')
    d = int(input())