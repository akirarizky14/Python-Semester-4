nstr = int(input())
for _ in range(nstr):
    txt = input()
    if txt.lower().find('кот') >= 0:
        print('МЯУ')
        break