import random

print('Вы играете в Bashe game')
rule = "\n\tВ игре участвуют два человека, ходят поочередно.\nЗа каждый ход любой из играющих может брать из общей группы,\nкоторая к началу игры содержит N предметов, от 1 до Р предметов включительно."
rule += "\n\nПеред началом каждой партии числа N и Р задаются."
rule += "\n\nПобедителем считается тот, кто сумеет вести игру так,\nчто его соперник вынужден будет взять последний предмет."
print(rule)
style_game = input(
    "\n\n\t\tПротив кого вы хотите играть?\nЕсли против игрока, введите 1\nЕсли против компьютера, введите 2:\n\t")
style_game = style_game.lower()
while style_game != "1" and style_game != "2":
    style_game = input("Вы неправильно ввели режим! Повторите попытку:\n\t")
#   Против игрока
if style_game == "1":
    first_player = input("Введите ник первого игрока:\n\t")
    second_player = input("Введите ник второго игрока:\n\t")
    status = "2"
    while status == "2":
        number_items = input("Введите кол-во преметов:\n\t")
        number_items = int(number_items)
        # T - число предметов которое можно брать за ход
        T = input("Введите максимальное кол-во предметов, которое можно брать за ход:\n\t")
        T = int(T)
        if T >= number_items:
            print("Эээ так низя!")
        else:
            while number_items > 1:
                print(f"Ходит {first_player}\nВыберите от 1 до {T} предметов:\t")
                items = input()
                items = int(items)
                while items > T:
                    print("Вы ввели число превышабщее допустимое значение.\nВведите заново\n")
                    items = input()
                    items = int(items)
                number_items = number_items - items
                print(f"Осталось {number_items} предмет(ов)")
                if number_items == 1:
                    print(f"Выигрывает {first_player}! Поздравляем!")
                    status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                    break
                elif number_items < 1:
                    print(f"Выигрывает {second_player}! Поздравляем!")
                    status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                    break
                else:
                    print(f"Ходит {second_player}\n Выберите от 1 до {T} предметов:\t")
                    items = input()
                    items = int(items)
                    while items > T:
                        print("Вы ввели число превышабщее допустимое значение.\nВведите заново\n")
                        items = input()
                        items = int(items)
                    number_items = number_items - items
                    print(f"Осталось {number_items} предмет(ов)")
                    if number_items == 1:
                        print(f"Выигрывает {second_player}! Поздравляем!")
                        status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                    elif number_items < 1:
                        print(f"Выигрывает {first_player}! Поздравляем!")
                        status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                        break
        while status != "1" and status != "2":
            print("Неправильно введены данные! Повторите попытку\n")
            status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
        if status == "1":
            print("Спасибо что играли в мою игру")
            break

# Против компьютера

elif style_game == "2":
    difficult = input('Выберите сложность:\n\teasy - "1"\n\thard - "2"\n:')
    while difficult != "1" and difficult != "2":
        print("Вы неправильно ввели сложность! Повторите попытку:\n\t")
        difficult = input('Выберите сложность:\n\teasy - "1"\n\thard - "2"\n:')
    # Сложная игра

    if difficult == "2":
        status = "2"
        while status == "2":
            first_player = input("Введите свой ник:\n\t")
            number_items = input("Введите кол-во преметов:\n\t")
            number_items = int(number_items)
            T = input("Введите максимальное кол-во предметов, которое можно брать за ход:\n\t")
            T = int(T)
            if T >= number_items:
                print("Эээ так низя!")
            else:
                R = number_items % (T + 1)
                if R == 1:
                    while number_items > 1:
                        print(f"Ходит {first_player}\nВыберите от 1 до {T} предметов:\t")
                        items = input()
                        items = int(items)
                        while items > T:
                            print("Вы ввели число превышабщее допустимое значение.\nВведите заново\n")
                            items = input()
                            items = int(items)
                        number_items = number_items - items
                        print(f"Осталось {number_items} предмет(ов)")
                        if number_items < 1:
                            print(f"Выигрывает компьютер! Слава ИИ!")
                            status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                            break
                        elif number_items == 1:
                            print(f"Выигрывает {first_player}! Поздравляем!")
                            status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                        else:
                            print("Ходит компьютер")
                            # P - переменная, означающая сколько будет брать компьютер
                            P = T + 1 - items
                            number_items = number_items - P
                            print(f"Осталось {number_items} предмет(ов)")
                            if number_items < 1:
                                print(f"Выигрывает {first_player}! Поздравляем!")
                                status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                            elif number_items == 1:
                                print(f"Выигрывает компьютер! Слава ИИ!")
                                status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                elif R == 0:
                    print("Ходит компьютер")
                    number_items = number_items - 1
                    print(f"Осталось {number_items} предмет(ов)")
                    while number_items > 0:
                        print(f"Ходит {first_player}\nВыберите от 1 до {T} предметов:\t")
                        items = input()
                        items = int(items)
                        while items > T:
                            print("Вы ввели число превышабщее допустимое значение.\nВведите заново\n")
                            items = input()
                            items = int(items)
                        number_items = number_items - items
                        print(f"Осталось {number_items} предмет(ов)")
                        if number_items < 1:
                            print(f"Выигрывает компьютер! Слава ИИ!")
                            status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                        elif number_items == 1:
                            print(f"Выигрывает {first_player}! Поздравляем!")
                            status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                        else:
                            print("Ходит компьютер")
                            P = T + 1 - items
                            number_items = number_items - P
                            print(f"Осталось {number_items} предмет(ов)")
                            if number_items < 1:
                                print(f"Выигрывает {first_player}! Поздравляем!")
                                status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                            elif number_items == 1:
                                print(f"Выигрывает компьютер! Слава ИИ!")
                                status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
            while status != "1" and status != "2":
                print("Неправильно введены данные! Повторите попытку\n")
                status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
            if status == "1":
                print("Спасибо что играли в мою игру!")
                break
    # Простая игра

    elif difficult == "1":
        status = "2"
        while status == "2":
            first_player = input("Введите свой ник:\n\t")
            print('Если вы играете в "easy" режим то будет выбрано:\n\t21 предмет\n\t4 предмета за ход')
            number_items = 21
            T = 4
            while number_items > 0:
                print(f"Ходит {first_player}\nВыберите от 1 до {T} предметов:\t")
                items = input()
                items = int(items)
                while items > T:
                    print("Вы ввели число превышабщее допустимое значение.\nВведите заново\n")
                    items = input()
                    items = int(items)
                number_items = number_items - items
                print(f"Осталось {number_items} предмет(ов)")
                if number_items < 1:
                    print(f"Выигрывает компьютер! Слава ИИ!")
                    status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                elif number_items == 1:
                    print(f"Выигрывает {first_player}! Поздравляем!")
                    status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                else:
                    print("Ходит компьютер")
                    number_items = number_items - random.randint(1, 4)
                    print(f"Осталось {number_items} предмет(ов)")
                    if number_items == 1:
                        print(f"Выигрывает компьютер! Слава ИИ!")
                        status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
                    elif number_items < 1:
                        print(f"Выигрывает {first_player}! Поздравляем!")
                        status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
            while status != "1" and status != "2":
                print("Неправильно введены данные! Повторите попытку\n")
                status = input('Для выхода из игры напишите "1"\nДля рестарта игры напишите "2":\n\t')
            if status == "1":
                print("Спасибо что играли в мою игру!")
                break
