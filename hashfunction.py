from array import *


def adding_tab(key='', values=type[int], flag=True) -> None:
    '''Функция заполняет словарь'''
    for (key2, i) in key_list:
        if key == key2:
            key_delete = key2
            index_delete = i
            flag = False
            break
    if flag:
        values_array.append(values)
        key_list.append((key, len(values_array) - 1))
    else:
        key_list.remove((key_delete, index_delete))
        values_array.append(values)
        key_list.append((key, len(values_array) - 1))


def clear_tab() -> array and list:
    '''Функция очищает словарь'''
    global values_array, key_list
    values_array = values_array = array('i')
    key_list = []
    return values_array, key_list


def get_values(key='') -> int:
    '''Функции подается ключь, возвращается значение по ключу'''
    for (key2, i) in key_list:
        if key == key2:
            return values_array[i]


def print_glossary() -> None:
    '''Печать словаря'''
    print('{', end='')
    for (key2, i) in key_list:
        print(f'\'{key2}\' : {values_array[i]},', end='')
    print('}')


values_array = array('i')
key_list = []

adding_tab('Sasha', 45)
adding_tab('Mikhail', 27)
adding_tab('John', 52)
print_glossary()
print(get_values('Mikhail'))
clear_tab()
print_glossary()
adding_tab('Ivan', 32)
adding_tab('Oleg', 36)
print_glossary()
