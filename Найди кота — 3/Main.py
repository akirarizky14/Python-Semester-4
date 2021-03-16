word = ''
n = 0
cat = -1
i = 1
while word != 'стоп':
    word = input()
    if 'Кот' in word or 'кот' in word:
        n += 1
    if ('Кот' in word or 'кот' in word) and cat == -1:
        cat = i
    i += 1  
print(n, cat)