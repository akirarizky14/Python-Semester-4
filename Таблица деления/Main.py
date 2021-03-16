i = int(input())
j = int(input())
for x in range(1, j+1):
    print(*(y/x for y in range(1, i+1)), sep=' ')
