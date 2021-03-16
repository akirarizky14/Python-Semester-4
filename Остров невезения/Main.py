d = int(input())
m = int(input())
y = int(input())
if m == 1 or m == 2:
    y -= 1
m = m - 2
if m <= 0:
    m += 12
c = y // 100
y = y - c * 100
d = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
print(d)