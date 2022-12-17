#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def sump(*args):
    a1 = 0
    a2 = 0
    s = 0
    print(args)
    if args:
        for i in args:
            if i < 0:
                a1 = args.index(i)
                break

        for i in args[a1+1:]:
            if i < 0:
                a2 = args.index(i)
                break

        for i in args[a1+1:a2:]:
            s += i
        return 'Сумма=', s

    else:
        return None


if __name__ == '__main__':
    print(sump(1, 2, -3, 3, 5, 1, -5, 3, -1))
