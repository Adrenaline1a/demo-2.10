#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_mean_of_numbers(*args):
    summ = 0
    numbers = [float(arg) for arg in args]
    numbers.sort()
    for i in numbers:
        if i == 0:
            return 'Невозможно посчитать, т.к. в списке есть 0'
        else:
            summ += 1/i
    harmonic = 1/(1/len(numbers)*summ)
    return harmonic


def main(arg):
    if arg == '':
        print(None)
    else:
        arg = arg.split(',')
        args = {}
        for i, n in enumerate(arg):
            args[i] = int(n)
        print("Среднее гармоническое элементов: ",
              harmonic_mean_of_numbers(*args.values()))


if __name__ == '__main__':
    arg = input('Введите список аргументов через запятую: ')
    main(arg)
