#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def positive(*arguments):
        summ = 0
        last = 0
        for i, n in enumerate(arguments):
            if i >= last and n > 0:
                last = i
        arguments = arguments[:last]
        for i in arguments:
            summ += i
        return summ


if __name__ == '__main__':
    try:
        print('Введите список аргументов через запятую: ')
        argument = list(map(float, input().split(',')))
        print("Сумма аргументов, расположенных до последнего"
              " положительного числа:",
              positive(*argument))
    except ValueError:
        print(None)
