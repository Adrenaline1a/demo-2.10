#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def positive(*arguments):
    summ = 0
    last = 0
    numbers = [int(argument) for argument in arguments]
    for i, n in enumerate(numbers):
        if i >= last and n > 0:
            last = i
    arguments = numbers[:last]
    for i in arguments:
        summ += i
    return summ


def main(argument):
    if argument == '':
        print(None)
    else:
        argument = argument.split(',')
        arguments = {}
        for i, n in enumerate(argument):
            arguments[i] = int(n)
        print("Сумма аргументов, расположенных до последнего"
              " положительного числа:",
              positive(*arguments.values()))


if __name__ == '__main__':
    argument = input('Введите список аргументов через запятую: ')
    main(argument)
