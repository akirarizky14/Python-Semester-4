import math
n = int(input())
k = 0
for i in range(1,n+1) :
    k = k + i**-2
print(math.pi**2/k)