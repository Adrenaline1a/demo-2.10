#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    argument = {}
    while True:
        mess = input('Введите команду: ').lower()
        if mess == "exit":
            exit()
        elif mess == "add":
            message = input('Введите параметр: ')
            argument[message] = input("Введите значение: ")
        elif mess == 'list':
            for key, value in argument.items():
                print("{} - {}".format(key, value))
        else:
            print("Неизвестная команда")


if __name__ == '__main__':
    main()

