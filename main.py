"""screen"""
from manager import print_book, get_book
import curses
import sys
import os
import time
from settings import *

current_page = 1
max_pages = 1 + len(get_book())//PAGE_SIZE
# Инициализация экрана (модуль curses)
stdscr = curses.initscr()
# Реагировать на нажатие клавиш без подтверждения при помощи ENTER
curses.cbreak()
# Разрешить использование стрелочек на клавиатуре
stdscr.keypad(True)
# Не блокировать программу по времени при опросе событий
stdscr.nodelay(True)

# Отобразим на экране данные по умолчанию


def display(page):
    """Функция отображения информации в терминале"""
    commands = f"Следующая страница: ВПРАВО, Предыдущая страница: ВЛЕВО, Выход: Q"

    stdscr.addstr(0, LEFT_SPACE, f"ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    stdscr.addstr(1, LEFT_SPACE, f"{'':-<95}")
    stdscr.addstr(2, LEFT_SPACE, f"{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<15}{'Телефон рабочий':<20}{'Телефон личный':<15}")
    stdscr.addstr(3, LEFT_SPACE, f"{'':-<95}")
    for number, line in zip(range(4, len(print_book(page))+4), print_book(page)):
        stdscr.addstr(number, LEFT_SPACE, line)
    stdscr.addstr(len(print_book(page)) + 5, LEFT_SPACE, f"{'Страница '+str(page):-^95}")
    stdscr.addstr(len(print_book(page)) + 6, LEFT_SPACE, "")
    stdscr.addstr(len(print_book(page)) + 7, LEFT_SPACE, commands)
    stdscr.refresh()

while True:
    display(current_page)
    # Получаем код нажатия клавиши и проверяем его
    key = stdscr.getch()
    if key != -1:
        if key == NEXT_PAGE:
            if current_page + 1 <= max_pages:
                current_page += 1
                stdscr.clear()
        elif key == PREV_PAGE:
            if current_page - 1 >= 1:
                current_page -= 1
                stdscr.clear()
        elif key == EXIT:
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            # Очистка и выход
            os.system('clear')
            sys.exit()
    # Обновляем текст на экране и делаем небольшую задержку
    stdscr.refresh()
    time.sleep(0.05)
