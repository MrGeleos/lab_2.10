#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Найти среднеквадратическое отклонение 4 чисел,
используя в решении переменное число именованных аргументов.
"""


def plot(**long):
    n = len(long.values())
    s = sum(long.values())/n
    v = 0
    for i in long.values():
        v += (i-s)**2
    return (v/(n-1))**0.5


if __name__ == '__main__':
    print(plot(a=1, b=2, c=3, d=1, e=4, f=2))
