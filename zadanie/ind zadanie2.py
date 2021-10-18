#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def the_amount(*arguments):
    summ = 0
    numbers = [float(arg) for arg in arguments]
    numbers.sort()
    for i in numbers:
        summ += i
    summ = summ/len(numbers)
    return summ


def main(argument):
    if argument == '':
        print(None)
    else:
        argument = argument.split(',')
        arguments = {}
        for i, n in enumerate(argument):
            arguments[i] = int(n)
        print("Среднее арифметическое:", the_amount(*arguments.values()))


if __name__ == '__main__':
    argument = input('Введите список аргументов через запятую: ')
    main(argument)
