#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def checklist(**argument):
    for key, value in argument.items():
        print("{} - {}".format(key, value))


def add(argument):
    message = input('Введите параметр: ')
    argument[message] = input("Введите значение: ")
    return argument


def main():
    argument = {}
    while True:
        mess = input('Введите команду: ').lower()
        if mess == "exit":
            exit()
        elif mess == "add":
            add(argument)
        elif mess == 'list':
            checklist(**argument)
        else:
            print("Неизвестная команда")


if __name__ == '__main__':
    main()
