#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(arguments, **argument):
    for k, v in argument.items():
        if k == 'key':
            global a
            a = v
        elif k == 'value':
            global b
            b = v
    listing(arguments)


def listing(argumets):
    arguments[a] = b
    return argumets


if __name__ == '__main__':
    arguments = {}
    while True:
        mess = input('Введите команду: ').lower()
        if mess == "exit":
            exit()
        elif mess == "add":
            add(arguments, key=input("Введите параметр: "), value=input("Введите значение: "))
        elif mess == 'list':
            print(listing(arguments))
        else:
            print("Неизвестная команда")
