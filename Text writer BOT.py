import time

# Приветствие
name = input("What`s your name? ")
if (name == "Dima K") or (name == "Diamond"):
    print("Hi creator!")
else:
    print(f"Hi {name}")

# Начало програмы
user = input("Enter text: ")

alfabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ";", ",", ".", "_", "#", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Проверка на допустимые символы
check = True
for i in user:
    if i.lower() not in alfabet:
        check = False

if check:
    # Сам код
    for i in range(len(user)):
        j = 0
        while alfabet[j] != user[i].lower():
            print(user[:i] + alfabet[j])
            j += 1
        print(user[:i] + alfabet[j])
        time.sleep(0.1)
else:
    print("Unaceptable symbols found!")