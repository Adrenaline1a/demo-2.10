#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def composition(*args):
    a = 1
    numbers = [float(arg) for arg in args]
    numbers.sort()
    for i in numbers:
        a *= i
    a = a ** (1/len(numbers))
    return a


def main(arg):
    if arg == '':
        print(None)
    else:
        arg = arg.split(',')
        args = {}
        for i, n in enumerate(arg):
            args[i] = int(n)
        print("Среднее геометрическое:", composition(*args.values()))


if __name__ == '__main__':
    arg = input('Введите список аргументов через запятую: ')
    main(arg)
