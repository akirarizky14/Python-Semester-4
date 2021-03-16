cat = False
for _ in range(int(input())):
    fraza = input().lower()
    if "кот" in fraza:
        cat = True
    if  "пёс" in fraza:
        cat = False
        
print("МЯУ" if cat else "НЕТ")
