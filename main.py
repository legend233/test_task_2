
from manager import print_book, get_book, add_person_in_book
import sys
import os
import time
from settings import *

def main(stdscr):
    """Основная функция"""
    current_page = 1
    max_pages = 1 + len(get_book())//PAGE_SIZE


    stdscr = curses.initscr() # Инициализация экрана (модуль curses)
    curses.noecho() # Не выводить символы ввода
    curses.cbreak() # Реагировать на нажатие клавиш без подтверждения при помощи ENTER
    stdscr.keypad(True) # Разрешить использование стрелочек на клавиатуре
    stdscr.nodelay(True)# Не блокировать программу по времени при опросе событий

    current_book = get_book()
    current_menu = "Справочник"

    def display_book(page):
        """Функция отображения информации в терминале"""
        commands = "Следующая страница: ВПРАВО, Предыдущая страница: ВЛЕВО, Выход: F12, Добавить запись: F10"

        stdscr.addstr(0, LEFT_SPACE, f"ТЕЛЕФОННЫЙ СПРАВОЧНИК", curses.A_BOLD)
        stdscr.addstr(1, LEFT_SPACE, f"{'':-<95}", curses.A_BOLD)
        stdscr.addstr(2, LEFT_SPACE, f"{'Фамилия':<15}{'Имя':<15}{'Отчество':<15}{'Организация':<15}{'Телефон рабочий':<20}{'Телефон личный':<15}", curses.A_BOLD)
        stdscr.addstr(3, LEFT_SPACE, f"{'':-<95}", curses.A_BOLD)
        for number, line in zip(range(4, len(print_book(page, current_book))+4), print_book(page, current_book)):
            stdscr.addstr(number, LEFT_SPACE, line)
        stdscr.addstr(len(print_book(page, current_book)) + 5, LEFT_SPACE, f"{'Страница '+str(page):-^95}", curses.A_BOLD)

        stdscr.addstr(len(print_book(page, current_book)) + 6, LEFT_SPACE, " ")
        stdscr.addstr(len(print_book(page, current_book)) + 7, LEFT_SPACE, commands)
        stdscr.refresh()


    def display_add_person():
        stdscr.addstr(0, LEFT_SPACE, "ДОБАВЛЕНИЕ ЗАПИСИ В ТЕЛЕФОННЫЙ СПРАВОЧНИК")
        stdscr.addstr(1, LEFT_SPACE,  f"{'':-<95}")
        stdscr.addstr(2, LEFT_SPACE,  "Чтобы добавить запись, введите данные в следующем формате:")
        stdscr.addstr(3, LEFT_SPACE, "Фамилия/Имя/Отчество/Организация/Телефон рабочий/Телефон личный")
        stdscr.addstr(4, LEFT_SPACE, ">>> ")
        writed_data = stdscr.getstr(4+4, LEFT_SPACE, 100)
        stdscr.getch()
        return writed_data

    def display_add_person_ask(data):
        stdscr.addstr(0, LEFT_SPACE, f"ДОБАВЛЕНИЕ ЗАПИСИ В ТЕЛЕФОННЫЙ СПРАВОЧНИК", curses.A_BOLD)
        stdscr.addstr(1, LEFT_SPACE, f"{'':-<95}")
        stdscr.addstr(2, LEFT_SPACE, "Добавить контакт в книгу?", curses.A_BOLD)
        stdscr.addstr(3, LEFT_SPACE, f"{str(data.decode('utf-8').split('/')):-^95}")
        stdscr.addstr(4, LEFT_SPACE, "Отменить добавление: F-12, Добавить запись: F10")
        stdscr.refresh()

    while True: # главный цикл
        key = stdscr.getch()  # Получаем код нажатия клавиши
        # Выводим необходимую страницу экрана
        if current_menu == "Справочник":
            display_book(current_page)
            if key != -1:
                if key == NEXT_PAGE:
                    if current_page + 1 <= max_pages:
                        current_page += 1
                        stdscr.clear()
                elif key == PREV_PAGE:
                    if current_page - 1 >= 1:
                        current_page -= 1
                        stdscr.clear()
                elif key == ADD_PERSON:
                    stdscr.clear()
                    current_menu = "Добавить запись"
                    curses.echo()
                    new_person = display_add_person()

                elif key == EXIT:
                    stdscr.keypad(False)
                    curses.echo()
                    curses.endwin()
                    # Очистка и выход
                    os.system('clear')
                    sys.exit()

        elif current_menu == "Добавить запись":
            display_add_person_ask(new_person)
            if key != -1:
                if key == ADD_PERSON:
                    add_person_in_book(current_book, *new_person.split('/'))
                    current_book = get_book()
                stdscr.clear()
                current_menu = "Справочник"



        # Обновляем текст на экране и делаем небольшую задержку
        stdscr.refresh()
        time.sleep(0.05)

if __name__ == '__main__':
    curses.wrapper(main)
