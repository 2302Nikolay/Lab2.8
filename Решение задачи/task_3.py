#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def factor():
    """""
    Умножение введённых чисел. пока не будет введён 0
    """""
    print("Вводите числа: ")
    b = 1
    while True:
        a = int(input(">>> "))
        if a == 0:
            break
        else:
            b *= a
    print("Результат: ", b)


if __name__ == '__main__':
    factor()
