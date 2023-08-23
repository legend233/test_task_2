import time
from manager import *
from rich.table import Table
from rich.console import Console


current_book = get_book()
current_page = 1
max_pages = 1 + len(get_book())//PAGE_SIZE
console = Console()
titles = ["ID", "Фамилия", "Имя", "Отчество", "Организация", "Телефон рабочий", "Телефон личный"]


def utf_valid(data: str):
    """Проверка на соответствие строки UTF-8"""
    try:
        data.encode('utf-8')
        return True
    except UnicodeEncodeError:
        print("Не соответствует UTF-8")
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
    console.print("ТЕЛЕФОННЫЙ СПРАВОЧНИК", justify='center', style="Red")
    # тело
    print_telephone_book_page(page, book)
    # подвал
    console.print(
          "\nВыход Q, предыдущая страница 1, следующая страница - 2,",
          "\nДобавить запись - 3",
          "\nРедактировать запись - 4",
          "\nПоиск по запросу - 5",
          justify="left"
    )


def print_telephone_book_page(page: int, book: dict) -> None:
    """
    Выводит страницу из телефонной книги.

    Аргументы:
        page (int): Номер страницы для вывода.
        book (dict): Название телефонной книги.

    Возвращает:
        None
    """
    table = Table(title=f"--Страница {page}--")
    for title in titles:
        table.add_column(title, no_wrap=True, header_style="red")
    for row in get_page_from_book(page, book):
        table.add_row(*row)

    console.print(table, justify="center")


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
    console.print("ДОБАВЛЕНИЕ ЗАПИСИ В ТЕЛЕФОННЫЙ СПРАВОЧНИК", style="red")
    console.print("Нажми Enter, чтобы пропустить")
    person = []
    for title in titles[1:]:
        new_data = input(f"\rВведите - {title}: ")
        if new_data and utf_valid(new_data):
            person.append(new_data)
        else:
            person.append("None")
    # рисуем табличку
    table = Table()
    for title in titles[1:]:
        table.add_column(title, header_style="red")
    table.add_row(*person)
    console.print(table, justify="center")

    if input("Добавить запись? да/нет: ").lower() in ["yes", "да", 'y', "д"]:
        return person
    else:
        return None


def print_edit_person():
    """
    Запрашивает у пользователя ввод ID и затем позволяет внести изменения в данные соответствующего человека.

    Возвращает:
        - Если пользователь вводит 'Q', возвращает None.
        - Если человек с указанным ID существует, позволяет пользователю внести изменения в его данные
          и возвращает обновленный ID и отредактированные данные человека.
        - Если человек с указанным ID не существует, выводит "Неверный ИД" и ничего не возвращает.
    """

    id = input("(Назад - Q) Чтобы отредактировать запись, введи ID: ")
    if id == 'Q':
        return None
    elif person := current_book.get(id):
        os.system('clear')
        edit_person = dict()
        console.print("ИЗМЕНЕНИЕ ЗАПИСИ", style="red")
        console.print("Нажми Enter, чтобы не менять")
        for key, title in zip(list(person.keys()), titles[1:]):
            new_data = input(f"\rТекущее значение - {title}: {person[key]}: ")
            if new_data and utf_valid(new_data):
                edit_person[key] = new_data
            else:
                edit_person[key] = person[key]
        # рисуем табличку
        table = Table()
        for title in titles:
            table.add_column(title, header_style="red")
        table.add_row(id, *edit_person.values())
        console.print(table, justify="center")

        if input("Изменить запись? да/нет: ").lower() in ["yes", "да", 'y', "д"]:
            return [id, ] + list(edit_person.values())
        else:
            return None

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
    console.print(f"ПОИСК ПО ЗАПРОСУ: ", end="", style="red")
    console.print(find_request, style="cyan")
    console.print("Продолжите, чтобы фильтровать результат")
    print_telephone_book_page(first_page_of_request, book)


while True:
    print_telephone_book(current_page, current_book)
    choice = input(">>> ")
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
            console.print("Запись добавлена", style="red")
        else:
            console.print("Добавление отменено", style="red")
        time.sleep(2)

    elif choice == "4":
        edit_person = print_edit_person()
        if edit_person:
            edit_person_in_book(current_book, *edit_person)
            console.print("Запись изменена", style="red")
        else:
            console.print("Изменения отменены", style="red")
        time.sleep(2)

    elif choice == "5":
        while s := input("Введите запрос для поиска (Enter - выход): "):
            find_persons = find_person_in_book(current_book, s)
            print_find_person_book(find_persons, s)

    elif choice == "Q":
        os.system('clear')
        break


console.print("Вы вышли из справочника", style="red", justify="center")
 