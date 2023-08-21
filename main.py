import os
import time
from manager import *


current_book = get_book()
current_page = 1
max_pages = 1 + len(get_book())//PAGE_SIZE


def print_telephone_book(page, book):
    os.system('clear')
    print(LEFT_SPACE * " " + "ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print(LEFT_SPACE * " " + f"{'':-<100}")
    print(LEFT_SPACE * " " + f"{'ID':<5}{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<20}{'Телефон рабочий':<20}{'Телефон личный':<15}")
    print(LEFT_SPACE * " " + f"{'':-<100}")
    for index, line in enumerate(print_book(page, book)):
        print(LEFT_SPACE * " " + f"{line}")
    print(LEFT_SPACE * " " + f"{'Страница '+str(page):-^100}")
    print(
          "\n" + LEFT_SPACE * " " + "Выход Q, предыдущая страница 1, следующая страница - 2,",
          "\n" + LEFT_SPACE * " " + "Добавить запись - 3",
          "\n" + LEFT_SPACE * " " + "Редактировать запись - 4",
          "\n" + LEFT_SPACE * " " + "Поиск по одной или нескольким характеристикам - 5")
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
            print("Не соответствует формату")


def print_edit_person():
    id = input(LEFT_SPACE * " " + "(Назад - Q) Чтобы отредактировать запись, введи ID: ")
    if id == 'Q':
        return None
    elif person := current_book.get(id):
        os.system('clear')
        titles = ["Фамилия", "Имя", "Отчество", "Организация", "Телефон рабочий", "Телефон личный"]
        edit_person = dict()
        print(LEFT_SPACE * " " + "Нажми Enter, чтобы не менять")
        for key, title in zip(list(person.keys()), titles):
            new_data = input("\r" + LEFT_SPACE * " " + f"Текущее значение - {title}: {person[key]}: ")
            if new_data:
                edit_person[key] = new_data
            else:
                edit_person[key] = person[key]
        print(LEFT_SPACE * " " + f"{'':-<100}")
        print(LEFT_SPACE * " " + f"{'ID':<5}{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<20}\
{'Телефон рабочий':<20}{'Телефон личный':<15}")
        print(LEFT_SPACE * " " + f"{id:<5}{edit_person['surname']:<15}{edit_person['first_name']:<15}{edit_person['last_name']:<15}\
{edit_person['company']:<20}{edit_person['work_number']:<20}{edit_person['personal_number']:<15}")
        print(LEFT_SPACE * " " + f"{'':-<100}")
        if input(LEFT_SPACE * " " + "Изменить запись? ").lower() in ["yes","да", 'y', "д"]:
            edit_person_in_book(current_book, id, *edit_person.values())
            print(LEFT_SPACE * " " + "Запись изменена")
            time.sleep(2)
            return id, edit_person
    else:
        print("Неверный ИД")


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
        print_edit_person()

    elif choice == "Q":
        os.system('clear')
        break
    else:
        print("Неверный ввод")

print("Вы вышли из справочника")

