kut = int(input())
take = 1
takb = 0
while kut > 1:
    takb = kut % 4
    if takb == 0:
        takb = 3
    elif takb == 1:
        takb = 1
    else:
        takb -= 1
    print('Забрал', takb)
    kut -= takb
    print('Осталось камней', kut)
    if kut == 1:
        print("ии вин")
    else:
        takb = 0
        take = 0
        while take > 3 or take < 1 or take > kut:
            print("бери")
            take = int(input())
        kut -= take
        print("осталось камней", kut)
        if kut == 1:
            print('ты победил')