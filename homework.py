def Run() -> str:
    # выводит меню пользователю
    commands = ['1', '2', '3', '4', '5', '6']
    print('Что вы хотите сделать? (укажите номер)\n',
          '1. Приветствие\n', '2. Вывести степень числа\n',
          '3. Простой кулькулятор (+,-,*,/)\n',
          '4. Вывести все четные числа от 1 до 100\n',
          '5. Вывести таблицу умножения от 1 до 10\n',
          '6. Выйти')
    command = input()
    while True:
        if command not in commands:
            print('Укажите натуральное число от 1 до 6')
            command = input()
        else:
            break
    return command


def Salutation() -> None:
    # выводит пользователю приветствие
    print('Введите свое имя:')
    name = input()
    print('Введите своей возраст')
    age = input()
    print(f'Привет, {name}. Твой возраст {age}.')


def DegreeOfNumber() -> None:
    # выводит степень числа
    print('Введите число и степень:')
    number, degree = [int(input()) for i in range(2)]
    print(number ** degree)


def Kulkulator() -> None:
    # простой кулькулятор, который работает с операциями (+,-,*,/)
    print('Укажите 2 числа и укажите операцию: +,-,*,/')
    try:
        num1 = int(input())
    except ValueError:
        print('Введите натуральное число')
        num1 = int(input())
    try:
        num2 = int(input())
    except ValueError:
        print('Введите натуральное число')
        num2 = int(input())
    sign = input()
    signs = ['+', '-', '*', '/']
    while True:
        if sign not in signs:
            print('Вы не правильно указали операцию\nУкажите один из символов: +,-,*,/')
            sign = input()
        else:
            break
    if sign == '+':
        print(num1 + num2)
    elif sign == '-':
        print(num1 - num2)
    elif sign == '*':
        print(num1 * num2)
    elif sign == '/':
        print(num1 / num2)


def DefevenNumbers() -> None:
    # выводит все четные числа от 0 до 100
    print(*(defeven := [i for i in range(100) if i % 2 == 0]))


def MultiplicationTable() -> None:
    # выводит таблицу умножения от 1 до 10
    numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    itog = []
    for i in numbers2:
        line_to_print = []
        for j in numbers2:
            line_to_print.append(i * j)
        itog.append(line_to_print)
    for row in itog:
        for x in row:
            print("{:4d}".format(x), end="")
        print()

while True:
    print()
    command = Run()
    if command == '1':
        Salutation()
    elif command == '2':
        DegreeOfNumber()
    elif command == '3':
        Kulkulator()
    elif command == '4':
        DefevenNumbers()
    elif command == '5':
        MultiplicationTable()
    elif command == '6':
        break
