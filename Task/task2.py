#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fio(*args):

    if args:
        values = [float(arg) for arg in args]
        l = len(values)
        b = 0
        for i in values:
            b = b + (1 / i)
        return l / b

    else:
        return None


if __name__ == "__main__":
    print(fio(1, 6, 2, 2, 21))
