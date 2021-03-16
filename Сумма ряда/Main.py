n = int(input())
b = 0
for i in range(n):
    a = int(input())
    if i % 2 == 0:
        b += a
    else:
        b -= a
print(b)