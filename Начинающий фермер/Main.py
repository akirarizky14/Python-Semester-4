credit = int(input())
livestock = int(input())
for b in range(1, min(livestock, credit // 20) + 1):
    for k in range(0, min(livestock, credit // 10) + 1):
        for t in range(0, min(livestock, credit // 5) + 1):
            if b * 20 + k * 10 + t * 5 == credit:
                if b + k + t == livestock:
                    print(b, k, t)