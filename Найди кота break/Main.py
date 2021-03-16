n = int(input())
c = False
for i in range(n):
    a = input()
    if 'кот' in a or 'Кот' in a:
        c = True
    break
if c:
    print('МЯУ')
else:
    print('НЕТ')