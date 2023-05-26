def z1():
    print("Ввод слов")
    print(' '.join([input('Введите слово: ') for i in range(int(input('Количество слов: ')))]))
z1()

def z2():
    words = []
    while (newword := str(input())) != "стоп":
        words.append(newword)

    print(" ".join(words))
z2()

def z3():
    words = []
    while (newword := str(input())) != "стоп":
        if "ф" in newword or "Ф" in newword:
            print("редкое слово")
        else:
            print("слово как слово")
z3()

def z4():
    from random import randint

    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        r = input()

        while not r.isdigit() and r != "стоп":
            print("введите правильно!!!: ", end="")
            r = input()
        if r == "стоп":
            break
        r = int(r)
        if a + b == r:
            print("правильно")
        else:
            print("не правильный ответ")
z4()