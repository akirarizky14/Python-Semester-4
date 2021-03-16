n = int(input())
iq = int(input('1: '))
print(0)
i = 1
s = iq
while i<n:
    avr = s/i
    iq = int(input(str(i+1)+': '))
    if iq > avr: print('>')
    elif iq < avr: print('<')
    else: print(0)
    i+=1
    s+=iq