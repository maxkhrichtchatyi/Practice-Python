#!/bin/python3
# -*- coding: utf-8 -*-

"""
Programming Assignment: Key-value хранилище

На этой неделе мы с вами реализуем собственный key-value storage.
Вашей задачей будет написать скрипт, который принимает в качестве аргументов
ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).

Запись значения по ключу
> storage.py --key key_name --val value

Получение значения по ключу
> storage.py --key key_name

Ответом в данном случае будет вывод с помощью print соответствующего значения
> value
или
> value_1, value_2

если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке
их добавления. Обратите внимание на пробел после запятой.

Если значений по ключу не было найдено, выводите пустую строку или None.

Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей
будет считать аргументы, переданные вашей программе, и записать соответствующую пару
ключ-значение в файл хранилища или вывести значения, если был передан только ключ.
Хранить данные вы можете в формате JSON с помощью стандартного модуля json. Проверьте
добавление нескольких ключей и разных значений.

Файл следует создавать с помощью модуля tempfile.
"""

import os
import json
import tempfile
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def init_data():
    # Create the storage file if it not exist and append empty JSON {}
    if not os.path.isfile(storage_path) == True or os.stat(storage_path).st_size == 0:
        return {}

    with open(storage_path, 'r') as json_file:
        return json.load(json_file)


def put(key, value):
    """Save  value by the """

    data = init_data()

    # Remove comma from list
    args.val = [w.replace(',', '') for w in args.val]

    if args.key in data:
        for new_value in args.val:
            data[args.key].append(new_value)
    else:
        data[args.key] = args.val

    with open(storage_path, 'w') as json_file:
        json_file.write(json.dumps(data))


def get(key):
    data = init_data()
    return ', '.join(data[args.key]) if args.key in data else None


#
# # Create the storage file if it not exist and append empty JSON {}
# if not os.path.isfile(storage_path) == True or os.stat(storage_path).st_size == 0:
#     with open(storage_path, 'w') as json_file:
#         data = {}
#         json_file.write(json.dumps(data))
#
# with open(storage_path, 'r') as json_file:
#     data = json.load(json_file)
#
#     if args.key and not args.val:
#         print(', '.join(data[args.key]) if args.key in data else None)
#     else:
#         # Remove comma from list
#         args.val = [w.replace(',', '') for w in args.val]
#
#         if args.key in data:
#             for new_value in args.val:
#                 data[args.key].append(new_value)
#         else:
#             data[args.key] = args.val
#
#         with open(storage_path, 'w') as json_file:
#             json_file.write(json.dumps(data))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key', required=True)
    parser.add_argument('--val', help='Value', nargs='+', type=str)
    args = parser.parse_args()

    if args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')
