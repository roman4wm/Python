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