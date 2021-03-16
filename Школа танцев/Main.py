patience = int(input())
indication = 0
 
while patience:
    for counting in ('раз','два','три','четыре'):
        if counting == input():
            indication += 1
        else:
            print(f'Правильных отсчётов было {indication}, но теперь вы ошиблись.')
            indication = 0
            patience  -= 1
            break
    
print('На сегодня хватит')