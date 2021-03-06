# Да или Нет

print("Welcome!")
a = input()
b = input()
if a == 'yes' and b == 'yes':
    print("Right")
elif a =='yes' and b == 'no':
    print("Right")
elif a == 'no' and b == 'yes':
    print("Right")
elif a == 'no' and b == 'no':
    print("Right")
else:
    print("Wrong!")