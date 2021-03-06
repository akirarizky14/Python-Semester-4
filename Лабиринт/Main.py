# Лабиринт
print("Welcome to Labirin!")
print("Choose Number 1 For Left, 2 For Right, 3 For Straight")
number = int(input())
if number == 1:
    print("you're turn to the left")
    print("Choose Number 1 For Left, 2 For Right, 3 For Straight")
    number1 = int(input())
    if number1 == 1:
        print("you're turn to the left, Game Over")
    elif number1 == 2:
        print("you're turn to the right")
        print("Congrats! The Giant Frog eat your body")
    else:
        print("you're lose, Game Over")
elif number == 2:
    print("you're turn to the right, Game Over")
elif number == 3:
    print("you're straight, Game Over ")   
else:
    print("you're lose, Game Over")
