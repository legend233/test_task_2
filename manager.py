import json
import os
from settings import *


def get_book() -> dict:
    """
    Получает книгу из указанного пути.

    Возвращает:
        Словарь, представляющий данные книги.
    """
    if os.stat(BOOK_PATH).st_size == 0:
        return dict()
    else:
        with open(BOOK_PATH, 'r', encoding='utf-8') as file:
            book = json.load(file)
            return book


def get_page_from_book(page: int, book: dict) -> list:
    """
    Генерирует список данных для определенной страницы из книги.

    Параметры:
        page (int): Номер страницы, для которой нужно получить данные.
        book (dict): Книга, содержащая данные.

    Возвращает:
        list: Список данных для указанной страницы.
    """
    body = []
    for key in list(book.keys())[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]:
        line_data = [key, ] + [value for value in book[key].values()]
        body.append(line_data)
    return body


def update_book(book: dict) -> None:
    """
    Обновляет книгу, записывая ее содержимое в файл JSON.

    Аргументы:
        book (dict): Словарь, представляющий обновляемую книгу.

    Возвращает:
        Ничего
    """
    with open(BOOK_PATH, 'w', encoding='utf-8') as file:
        json.dump(book, file, indent=4, ensure_ascii=False)


def add_person_in_book(
        book: dict,
        surname: str,
        first_name: str,
        last_name: str,
        company: str,
        work_number: str,
        personal_number: str
) -> None:
    """
    Добавляет в книгу запись и обновляет ее содержимое в файле JSON.

    Аргументы:
            book (dict): Телефонная книга.
            surname (str): Фамилия человека.
            first_name (str): Имя человека.
            last_name (str): Отчество человека.
            company (str): Компания человека.
            work_number (str): Рабочий номер человека.
            personal_number (str): Личный номер человека.

    Возвращает:
        Ничего
    """
    if os.stat(BOOK_PATH).st_size == 0:
        new_key = "1"
    else:
        new_key = str(max([int(x) for x in book.keys()]) + 1)
    book[new_key] = {
            'surname': surname,
            'first_name': first_name,
            'last_name': last_name,
            'company': company,
            'work_number': work_number,
            'personal_number': personal_number
        }
    sorted_book = {k: book[k] for k in sorted(book, key=lambda x: int(x))}
    update_book(sorted_book)


def edit_person_in_book(
        book: dict,
        id: str,
        surname: str,
        first_name: str,
        last_name: str,
        company: str,
        work_number: str,
        personal_number: str
) -> None:
    """
        Редактирует информацию о человеке в книге.

        Аргументы:
            book (dict): Книга, содержащая информацию о человеке.
            id (str): Идентификатор человека, которого нужно отредактировать.
            surname (str): Фамилия человека.
            first_name (str): Имя человека.
            last_name (str): Отчество человека.
            company (str): Компания человека.
            work_number (str): Рабочий номер человека.
            personal_number (str): Личный номер человека.

        Возвращает:
            None: Данная функция не возвращает ничего.
        """
    book[id] = {
        'surname': surname,
        'first_name': first_name,
        'last_name': last_name,
        'company': company,
        'work_number': work_number,
        'personal_number': personal_number
    }
    update_book(book)


def find_person_in_book(book: dict, find_request) -> dict:
    """
    Найти человека в книге на основе поискового запроса.

    Параметры:
        book (dict): Книга, в которой будет производиться поиск, представленная в виде словаря.
        find_request: Поисковый запрос.

    Возвращает:
        dict: Словарь, содержащий отфильтрованные записи из книги, соответствующие поисковому запросу.
    """
    
    filtered_book = dict()
    for person_key in book.keys():
        for parameter in book[person_key].keys():
            if find_request.lower() in book[person_key][parameter].lower():
                filtered_book[person_key] = book[person_key]
    return filtered_book
