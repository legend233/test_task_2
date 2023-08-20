import json
from settings import *


def get_book() -> list:
    """Функция получения справочника из файла"""
    with open(BOOK_PATH, 'r', encoding='utf-8') as file:
        book = json.load(file)
        return book


def print_book(page: int, book) -> list:
    """Возврат необходимой страницы из справочника"""
    body = []
    for person in book[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]:
        line_data = f"{person['surname']:<15}{person['first_name']:<15}{person['last_name']:<15}{person['company']:<15}{person['work_number']:<20}{person['personal_number']:<15}"
        body.append(line_data)
    return body


def update_book(book: list) -> None:
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


def add_person_in_book(book: list, surname: str, first_name: str, last_name: str, company: str, work_number: str,
                       personal_number: str) -> None:
    """Функция добавления записи в справочник"""
    book.append({
        'surname': surname,
        'first_name': first_name,
        'last_name': last_name,
        'company': company,
        'work_number': work_number,
        'personal_number': personal_number
    })
    book.sort(key=lambda x: x['surname'])
    update_book(book)
