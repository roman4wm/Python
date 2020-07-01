# def greet_user():
#     """Выводит простое приветствие."""
#     print("Hello!")
#
#
# greet_user()


# def greet_user(username):
#     """Выводит простое приветствие."""
#     print(f"Hello, {username.title()}!")
#
#
# greet_user('jesse')

# Переменная username в определении greet_user() — параметр, то есть условные
# данные, необходимые функции для выполнения ее работы. Значение 'jesse'
# в greet_user('jesse') — аргумент, то есть конкретная информация, переданная
# при вызове функции.

# Передача аргументов
# Позиционные аргументы

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('hamster', 'harry')

# О важности порядка позиционных аргументов

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('harry', 'hamster')

# Именованные аргументы

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')
#
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# Значения по умолчанию

#
#
# describe_pet(pet_name='willie')
#
# # describe_pet('willie')
#
# describe_pet(pet_name='harry', animal_type='hamster')

# ПРИМЕЧАНИЕ Если вы используете значения по умолчанию, все параметры со значением по умолчанию должны следовать после параметров, у которых значений по
# умолчанию нет. Это необходимо для того, чтобы Python правильно интерпретировал
# позиционные аргументы.

# Эквивалентные вызовы функций

# def describe_pet(pet_name, animal_type='dog')

# def describe_pet(animal_type='dog', pet_name):
#     """Выводит информацию о животном."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('willie')

# # Пес по имени Вилли.
# describe_pet('willie')
# describe_pet(pet_name='willie')
# # Хомяк по имени Гарри.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# Предотвращение ошибок в аргументах

# Возвращаемое значение

# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def q(a, b):
#     return a**b
#
# print(q(5, 2))

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# Необязательные аргументы

# def get_formatted_name(first_name, middle_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Возвращает аккуратно отформатированное полное имя."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# Возвращение словаря

# def build_person(first_name, last_name):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     return person
#
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=None):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#

# musician = build_person('jimi', 'hendrix')
# print(musician)
#
# musician1 = build_person(1, 2)
# print(musician1)

# Использование функции в цикле while

# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# # Бесконечный цикл!
#
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# Передача списка

# def greet_users(names):
#     """Вывод простого приветствия для каждого пользователя в списке."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# Изменение списка в функции
#
# Список моделей, которые необходимо напечатать.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed_models.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)


# # Вывод всех готовых моделей.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
#
# #
# def print_models(unprinted_designs, completed_models):
#     """
#     Имитирует печать моделей, пока список не станет пустым.
#     Каждая модель после печати перемещается в completed_models.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """Выводит информацию обо всех напечатанных моделях."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# Запрет изменения списка в функции

# имя_функции(имя_списка[:])

# print_models(unprinted_designs[:], completed_models)

# Передача произвольного набора аргументов

# def make_pizza(*toppings):
#     """Вывод списка заказанных топпингов."""
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(*toppings):
#     """Выводит описание пиццы."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Позиционные аргументы с произвольными наборами аргументов

# def make_pizza(size, name="Margarita", *toppings):
#     """Выводит описание пиццы."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# ПРИМЕЧАНИЕ В программах часто используется имя обобщенного параметра *args
# для хранения произвольного набора позиционных аргументов.

# Использование произвольного набора именованных аргументов

# def build_profile(first, last, **user_info):
#     """Строит словарь с информацией о пользователе."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

# ПРИМЕЧАНИЕ В программах часто используется имя обобщенного параметра
# **kwargs для хранения произвольного набора ключевых аргументов.

# Хранение функций в модулях
# Импортирование всего модуля

# pizza.py
# def make_pizza(size, *toppings):
#     """Выводит описание пиццы."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# # making_pizzas.py
# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# имя_модуля.имя_функции()

# Импортирование конкретных функций

# from имя_модуля import имя_функции

# from имя_модуля import функция_0, функция_1, функция_2

# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Назначение псевдонима для функции

# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# from имя_модуля import имя_функции as псевдоним

# Назначение псевдонима для модуля

# Вызов p.make_pizza() получается более компактным, чем pizza.
# make_pizza():
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Общий синтаксис выглядит так:
# import имя_модуля as псевдоним

# Импортирование всех функций модуля

# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from имя_модуля import *

# Стилевое оформление функций

# def имя_функции(параметр_0, параметр_1='значение_по_умолчанию')

# PEP 8 (https://www.python.org/dev/peps/pep-0008/)

# def имя_функции(параметр_0, параметр_1, параметр_2,
#                 параметр_3, параметр_4, параметр_5):
#     тело     функции...

# print(a)
#
# a = 10
