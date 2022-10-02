#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys


def get_input():
    """""
    Заправшивает ввод с клавиатуры и
    возвращает в основную программу полученную строку.
    """""
    get_str = input("Введите число: ")
    return get_str


def test_input(b):
    """""
    Проверяет, можно ли переданное ей значение
    преобразовать к числу. Если да - возвращает True.
    """""
    if type(b) == int or type(b) == float:
        return True
    elif b.isnumeric():
        return True
    else:
        return False


def str_to_int(b):
    """""
    Преобразует переданное значение к
    целочисленному типу.
    """""
    c = int(b)
    return c


def print_int(c):
    """""
    Выводит переданное значение на экран
    """""
    print(c)


if __name__ == '__main__':
    a = get_input()
    # для теста print(type(a))
    bol = test_input(a)
    if bol:
        ch = str_to_int(a)
        # для теста print(type(ch))
        print_int(ch)
    else:
        print(f"Введённое значение не является числом!", file=sys.stderr)
