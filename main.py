import time
from manager import *


current_book = get_book()
current_page = 1
max_pages = 1 + len(get_book())//PAGE_SIZE


def utf_valid(data: str):
    """Проверка на соответствие строки UTF-8"""
    try:
        data.encode('utf-8')
        return True
    except UnicodeEncodeError:
        print(LEFT_SPACE * " " + "Не соответствует UTF-8")
        return False


def print_telephone_book(page: int, book: dict) -> None:
    """
    Выводит телефонную книгу с заданным номером страницы и данными книги.

    Аргументы:
        page (int): Номер страницы для вывода.
        book (dict): словарь, представляющий строки телефонной книги.

    Возвращает:
        None
    """
    # шапка
    os.system('clear')
    print(LEFT_SPACE * " " + "ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    # тело
    print_telephone_book_page(page, book)
    # подвал
    print(LEFT_SPACE * " " + f"{'Страница '+str(page):-^105}")
    print(
          "\n" + LEFT_SPACE * " " + "Выход Q, предыдущая страница 1, следующая страница - 2,",
          "\n" + LEFT_SPACE * " " + "Добавить запись - 3",
          "\n" + LEFT_SPACE * " " + "Редактировать запись - 4",
          "\n" + LEFT_SPACE * " " + "Поиск по запросу - 5")


def print_telephone_book_page(page: int, book: dict) -> None:
    """
    Выводит страницу из телефонной книги.

    Аргументы:
        page (int): Номер страницы для вывода.
        book (dict): Название телефонной книги.

    Возвращает:
        None
    """
    print(LEFT_SPACE * " " + f"{'':-<105}")
    print(LEFT_SPACE * " " + f"{'ID':<5}{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<20}\
{'Телефон рабочий':<20}{'Телефон личный':<15}")
    print(LEFT_SPACE * " " + f"{'':-<105}")
    for index, line in enumerate(get_page_from_book(page, book)):
        print(LEFT_SPACE * " " + f"{line}")
    

def print_add_person() -> list or None:
    """
    Выводит информацию о человеке и добавляет ее в телефонный справочник.

    Очищает экран и запрашивает у пользователя ввод информации о новом человеке в телефонный справочник.
    Функция не принимает параметров.

    Возвращает:
        - Если пользователь решает добавить человека, возвращает список с информацией о человеке.
        - Если пользователь решает не добавлять человека, возвращает None.
    """
    os.system('clear')
    print(LEFT_SPACE * " " + "ДОБАВЛЕНИЕ ЗАПИСИ В ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print(LEFT_SPACE * " " + "Нажми Enter, чтобы пропустить")
    titles = ["Фамилия", "Имя", "Отчество", "Организация", "Телефон рабочий", "Телефон личный"]
    person = []
    for title in titles:
        new_data = input("\r" + LEFT_SPACE * " " + f"Введите - {title}: ")
        if new_data and utf_valid(new_data):
            person.append(new_data)
        else:
            person.append("None")

    print(LEFT_SPACE * " " + f"{'':-<100}")
    print(LEFT_SPACE * " " + f"{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<20}\
{'Телефон рабочий':<20}{'Телефон личный':<15}")
    print(LEFT_SPACE * " " + f"{person[0]:<15}{person[1]:<15}{person[2]:<15}\
{person[3]:<20}{person[4]:<20}{person[5]:<15}")
    print(LEFT_SPACE * " " + f"{'':-<100}")
    if input(LEFT_SPACE * " " + "Добавить запись? да/нет: ").lower() in ["yes", "да", 'y', "д"]:
        return person
    else:
        return None


def print_edit_person() -> None:
    """
    Запрашивает у пользователя ввод ID и затем позволяет внести изменения в данные соответствующего человека.

    Возвращает:
        - Если пользователь вводит 'Q', возвращает None.
        - Если человек с указанным ID существует, позволяет пользователю внести изменения в его данные
          и возвращает обновленный ID и отредактированные данные человека.
        - Если человек с указанным ID не существует, выводит "Неверный ИД" и ничего не возвращает.
    """

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
            if new_data and utf_valid(new_data):
                edit_person[key] = new_data
            else:
                edit_person[key] = person[key]
        print(LEFT_SPACE * " " + f"{'':-<100}")
        print(LEFT_SPACE * " " + f"{'ID':<5}{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<20}\
{'Телефон рабочий':<20}{'Телефон личный':<15}")
        print(LEFT_SPACE * " " + f"{id:<5}{edit_person['surname']:<15}{edit_person['first_name']:<15}\
{edit_person['last_name']:<15}{edit_person['company']:<20}{edit_person['work_number']:<20}\
{edit_person['personal_number']:<15}")
        print(LEFT_SPACE * " " + f"{'':-<100}")
        if input(LEFT_SPACE * " " + "Изменить запись? да/нет: ").lower() in ["yes", "да", 'y', "д"]:
            edit_person_in_book(current_book, id, *edit_person.values())
            print(LEFT_SPACE * " " + "Запись изменена")
            time.sleep(2)
            
    else:
        print("Неверный ИД")


def print_find_person_book(book: dict, find_request) -> None:
    """
    Выводит результаты поиска для указанного запроса в телефонной книге.

    Параметры:
    - book (dict): Словарь, содержащий записи телефонной книги.
    - find_request (str): Запрос для поиска в телефонной книге.

    Возвращает:
    None
    """
    first_page_of_request = 1  # Первая страница результатов
    os.system('clear')
    print(LEFT_SPACE * " " + f"ПОИСК ПО ЗАПРОСУ: {find_request}")
    print(LEFT_SPACE * " " + "Продолжите, чтобы фильтровать результат")
    print_telephone_book_page(first_page_of_request, book)
    print(LEFT_SPACE * " " + f"{'':-<105}\n")


while True:
    print_telephone_book(current_page, current_book)
    choice = input(LEFT_SPACE * " " + ">>> ")
    if choice == "1":
        if current_page - 1 > 0:
            current_page -= 1
    elif choice == "2":
        if current_page + 1 <= max_pages:
            current_page += 1
    elif choice == "3":
        new_person = print_add_person()
        if new_person:
            add_person_in_book(current_book, *new_person)
            print(LEFT_SPACE * " " + "Запись добавлена")
        else:
            print(LEFT_SPACE * " " + "Добавление отменено")
        time.sleep(2)

    elif choice == "4":
        print_edit_person()

    elif choice == "5":
        while s := input(LEFT_SPACE * " " + "Введите запрос для поиска (Enter - выход): "):
            find_persons = find_person_in_book(current_book, s)
            print_find_person_book(find_persons, s)

    elif choice == "Q":
        os.system('clear')
        break


print("Вы вышли из справочника")
 