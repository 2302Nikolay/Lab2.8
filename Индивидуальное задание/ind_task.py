#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import datetime


def add(list_man):
    # Запросить данные .
    name = input("Имя:  ")
    number = input("Номер телефона ")
    date = input("Дата рождения: ")
    date = datetime.datetime.strptime(date, '%d.%m.%Y').date()

    # Создать словарь.
    man = {
        'name': name,
        'number': number,
        'date': date,
    }

    # Добавить словарь в список.
    list_man.append(man)
    # Отсортировать список.
    if len(list_man) > 1:
        list_man.sort(key=lambda item: item.get('date', ''))
    return list_man


def list_d(list_man):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Имя",
            "Номер телефона",
            "Дата рождения"
        )
    )
    print(line)

    # Вывести данные о человеке.
    for idx, man in enumerate(list_man, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:<20}  |'.format(
                idx,
                man.get('name', ''),
                man.get('number', ''),
                man.get('date', '')
            )
        )

    print(line)


def select(mans_list, sel_d):
    count = 0
    for man in mans_list:
        if man.get('number') == sel_d:
            count += 1
            print(
                '{:>4}: {}'.format(count, man.get('name', ''))
            )
            print('Номер телефона:', man.get('number', ''))
            print('Дата рождения:', man.get('date', ''))

    # Если счетчик равен 0, то человек не найден.
    if count == 0:
        print("Человек не найден.")


def help_d():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <товар> - информация о человеке;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    manlist = []
    while True:
        # Запросить команду
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            manlist = add(manlist)
        elif command == 'list':
            list_d(manlist)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            sel = parts[1]
            select(manlist, sel)
        elif command == 'help':
            help_d()
        else:
            print("неизвестная команда {command}", file=sys.stderr)
