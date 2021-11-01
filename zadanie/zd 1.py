#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def composition(*arg):
    a = 1
    for i in arg:
        a *= i
    a = a ** (1/len(arg))
    return a


if __name__ == '__main__':
    try:
        print('Введите список аргументов через запятую: ')
        arg = list(map(float, input().split(',')))
        print("Среднее геометрическое элементов: ",
              composition(*arg))
    except ValueError:
        print(None)
