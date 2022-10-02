#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math
import sys


def cylinder():
    while True:
        vs = int(input("Какую площадь вы хотите вычислит (введите число):\n"
                       "1 -> Боковой поверхности\n"
                       "2 -> Полной поверхности\n"
                       ">>> "))
        if (vs != 1) & (vs != 2):
            print(f"Неизвестная комманда {vs}", file=sys.stderr)
            break

        r = int(input("Введите радиус "))
        h = int(input("Введите высоту цилиндра: "))

        if vs == 1:
            s = 2 * math.pi * r * h
            print("S(бок.) = ", '{:.3f}'.format(s))
            break

        elif vs == 2:
            s = (2 * math.pi * r * h) + (circle(r) * 2)
            print("S(полн.) = ", '{:.3f}'.format(s))
            break


def circle(r):
    s = pow((math.pi * r), 2)
    return s


if __name__ == '__main__':
    cylinder()
