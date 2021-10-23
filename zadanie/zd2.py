#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_mean_of_numbers(*arg):
    summ = 0
    for i in arg:
        if i == 0:
            return 'Невозможно посчитать, т.к. в списке есть 0'
        else:
            summ += 1/float(i)
    harmonic = 1/(1/len(arg)*summ)
    return harmonic


if __name__ == '__main__':
    try:
        print('Введите список аргументов через запятую: ')
        arg = list(map(float, input().split(',')))
        print("Среднее гармоническое элементов: ",
              harmonic_mean_of_numbers(*arg))
    except ValueError:
        print(None)
