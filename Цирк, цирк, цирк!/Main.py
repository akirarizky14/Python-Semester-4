a = int(input())
count = 0
 
while a > 1:
    count += 1 + a % 2
    a //= 2
print(count)