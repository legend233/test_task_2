import os
from manager import *


current_book = get_book()
current_page = 1
max_pages = 1 + len(get_book())//PAGE_SIZE
def print_menu():
    os.system('clear')
    print(LEFT_SPACE * " " + "ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print(LEFT_SPACE*" "+"1. Вывод постранично записей из справочника")
    print(LEFT_SPACE*" "+"2. Добавление новой записи в справочник")
    print(LEFT_SPACE*" "+"3. Поиск записей по одной или нескольким характеристикам")
    print(LEFT_SPACE*" "+"4. Выход")


def print_telephone_book(page, book):
    while True:
        os.system('clear')
        print(LEFT_SPACE * " " + "ТЕЛЕФОННЫЙ СПРАВОЧНИК")
        print(LEFT_SPACE * " " + f"{'':-<105}")
        print(LEFT_SPACE * " " + f"{'№':<10}{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<15}{'Телефон рабочий':<20}{'Телефон личный':<15}")
        print(LEFT_SPACE * " " + f"{'':-<105}")
        for index, line in enumerate(print_book(page, book)):
            print(LEFT_SPACE * " " + f"{index+1:<10}{line}")
        print(LEFT_SPACE * " " + f"{'Страница '+str(page):-^105}")
        choice_page = input("предыдущая страница 1, следующая страница 2, выход Q: ")

        if choice_page == "1":
            if page - 1 > 0:
                page -= 1
        elif choice_page == "2":
            if page + 1 <= max_pages:
                page += 1
        elif choice_page == "Q":
            break
        else:
            print("Неверный ввод")


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

    person = input(LEFT_SPACE * " " + "(выход - Q)>>> ")
    while not validate_input(person) or person == "Q":
        print("Не соответсвует формату")
        person = input(LEFT_SPACE * " " + "(выход - Q)>>> ")
    return person



print_menu()
choice = input("Выберите пункт меню: ")
while True:
    if choice == "1":
        print_telephone_book(current_page, current_book)
        print_menu()
        choice = input("Выберите пункт меню: ")
    elif choice == "2":
        new_person = print_add_person()
        add_person_in_book(current_book, *new_person.split('/'))
        print_menu()
        choice = input("Выберите пункт меню: ")
    elif choice == "3":
        pass
    elif choice == "4":
        os.system('clear')
        break
    else:
        print("Неверный ввод")
        choice = input("Выберите пункт меню: ")
