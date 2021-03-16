words = input()
i = 1
row = None
while words.lower() != "стоп":
    for j in words.lower().split(" "):
        if j == "кот":
            row = i
    i += 1
    words = input()
if row:
    print(row)
else:
    print(-1)