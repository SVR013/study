def find_small(list) -> int:
    '''Поиск самого наименьшего элемента списка'''
    elem = list[0]
    index = 0
    for i in range(1, len(list)):
        if list[i] < elem:
            elem = list[i]
            index = i
    return index

def sorting_by_choice(list) -> list:
    '''Сортировка выбором'''
    new_list = []
    while len(list) != 0:
        elem = list.pop(find_small(list))
        new_list.append(elem)
    return new_list

def quick_sorting(list) -> list:
    '''БЫстрая сортировка списка'''
    if len(list) < 2:
        return list
    else:
        mid = list[0]
        start = [i for i in list[1:] if i <= mid]
        end = [i for i in list[1:] if i >= mid]
        return quick_sorting(start) + [mid] + quick_sorting(end)

def bynary_searh(list, item) -> int:
    '''Функция бинарного поиска'''
    start, end = 0, len(list) - 1
    print('Выберите сортировку:\n1. Cортировка выбором\n2. Быстрая сортировка')
    choice = int(input())
    if choice == 1:
        list = sorting_by_choice(list)
    if choice == 2:
        list = quick_sorting(list)
    print('Отсортированный список =', list)
    while start <= end:
        center = (start + end) // 2
        elem = list[center]
        if item == elem:
            return center
        if elem > item:
            end = center - 1
        else:
            start = center + 1
    return None


print('Функция бинарного поиска работает с любым списком.\nМожете вводить числа в любом порядке, через \'Enter\':')
print('    Введите 5 целых чисел:')
lst = [int(input()) for i in range(5)]
print('Введите число, индекс которого хотите узнать')
itm = int(input())
print('Искомый индекс :', bynary_searh(lst, itm))

