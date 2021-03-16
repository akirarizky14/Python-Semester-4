password = input()
password2 = input()
while len(password) < 8:
    print("Короткий!")
    password = input()
    password2 = input()
while "123" in password:
    print("Простой!")
    password = input()
    password2 = input()
while password2 != password:
    print("Различаются.")
    password = input()
    password2 = input()
else:
    print("OK")