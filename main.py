import os
import time

from manager import *


current_book = get_book()
current_page = 1
max_pages = 1 + len(get_book())//PAGE_SIZE


def print_telephone_book(page, book):
    os.system('clear')
    print(LEFT_SPACE * " " + "ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print(LEFT_SPACE * " " + f"{'':-<105}")
    print(LEFT_SPACE * " " + f"{'№':<10}{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<15}{'Телефон рабочий':<20}{'Телефон личный':<15}")
    print(LEFT_SPACE * " " + f"{'':-<105}")
    for index, line in enumerate(print_book(page, book)):
        print(LEFT_SPACE * " " + f"{(index+1)+(page-1)*PAGE_SIZE:<10}{line}")
    print(LEFT_SPACE * " " + f"{'Страница '+str(page):-^105}")
    print(
          "\n" + LEFT_SPACE * " " + "Выход Q, предыдущая страница 1, следующая страница - 2,",
          "\n" + LEFT_SPACE * " " + "Добавить запись - 3",
          "\n" + LEFT_SPACE * " " + "Поиск по одной или нескольким характеристикам - 4")
    choice = input(LEFT_SPACE * " " + ">>> ")
    return choice



def print_add_person():
    os.system('clear')
    def validate_input(data):
        import re
        regex = r"^[^/]+(/[^/]+){5}$"
        match = re.match(regex, data)
        if match:
            return True
        else:
            return False
    print(LEFT_SPACE * " " + "ДОБАВЛЕНИЕ ЗАПИСИ В ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print(LEFT_SPACE * " " + f"{'':-<95}")
    print(LEFT_SPACE * " " + "Чтобы добавить запись, введите данные в следующем формате:")
    print(LEFT_SPACE * " " + "Фамилия/Имя/Отчество/Организация/Телефон рабочий/Телефон личный")

    while True:
        person = input(LEFT_SPACE * " " + "(выход - Q)>>> ")
        if validate_input(person):
            return person
        elif person == "Q":
            return None
        else:
            print("Не соответсвует формату")





while True:
    choice = print_telephone_book(current_page, current_book)
    if choice == "1":
        if current_page - 1 > 0:
            current_page -= 1
    elif choice == "2":
        if current_page + 1 <= max_pages:
            current_page += 1
    elif choice == "3":
        new_person = print_add_person()
        if new_person:
            add_person_in_book(current_book, *new_person.split('/'))

    elif choice == "4":
        pass
    elif choice == "Q":
        os.system('clear')
        break
    else:
        print("Неверный ввод")

print("Вы вышли из справочника")

