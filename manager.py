import json
from settings import *

def get_book() -> list:
    with open('book.json', 'r', encoding='utf-8') as file:
        book = json.load(file)
        return book


def print_book(page: int) -> list:
    page_size = 3
    body = []
    for person in get_book()[(page-1)*page_size:page*page_size]:
        line_data = f"{person['surname']:<15}{person['first_name']:<15}{person['last_name']:<15}{person['company']:<15}{person['work_number']:<20}{person['personal_number']:<15}"
        body.append(line_data)
    return body
