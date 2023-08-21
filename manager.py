import json
from settings import *


def get_book() -> dict:
    """Функция получения справочника из файла"""
    with open(BOOK_PATH, 'r', encoding='utf-8') as file:
        book = json.load(file)
        return book


def print_book(page: int, book) -> list:
    """Возврат необходимой страницы из справочника"""
    body = []
    for key in list(book.keys())[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]:
        line_data = f"{key:<5}{book[key]['surname']:<15}{book[key]['first_name']:<15}{book[key]['last_name']:<15}{book[key]['company']:<20}{book[key]['work_number']:<20}{book[key]['personal_number']:<15}"
        body.append(line_data)
    return body


def update_book(book: dict) -> None:
    """Функция обновления справочника"""
    with open(BOOK_PATH, 'w', encoding='utf-8') as file:
        json.dump(book, file)


def filter_book(book: list, *args) -> list:  # ToDo функция фильтрации справочника закончить
    """Функция фильтрации справочника"""
    filtered_book = []
    for person in book:
        for arg in args:
            if arg in person.values():
                filtered_book.append(person)
    return filtered_book


def add_person_in_book(book: dict, surname: str, first_name: str, last_name: str, company: str, work_number: str,
                       personal_number: str) -> None:
    """Функция добавления записи в справочник"""
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


def edit_person_in_book(book: dict, id: str, surname: str, first_name: str, last_name: str, company: str, work_number: str,
                       personal_number: str) -> None:
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
