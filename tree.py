import os
import os.path

def DrawTreeLinux(path, template=''):
    lst = sorted(os.listdir(path))
    for i in lst:
        flag = True if i == lst[-1] else False
        continuation_of_the_line = '└─> ' + i if flag else '├─> ' + i
        print(template + continuation_of_the_line)
        if os.path.isdir(path + '/' + i):
            DrawTreeLinux(path + '/' + i, (template + (('    ') if flag else '│   ')))

def DrawTreeWindows(path, template=''):
    lst = sorted(os.listdir(path))
    for i in lst:
        flag = True if i == lst[-1] else False
        continuation_of_the_line = '└─> ' + i if flag else '├─> ' + i
        print(template + continuation_of_the_line)
        if os.path.isdir(path + '\\' + i):
            DrawTreeWindows(path + '\\' + i, (template + (('    ') if flag else '│   ')))

def Run() -> str:
    # выводит меню пользователю
    commands = ['1', '2', '0']
    print('Какая у вас операционная система? (укажите номер)\n',
          '1. Linux\n', '2.Windows\n',
          '0. Выход из программы')
    command = input()
    while True:
        if command not in commands:
            print('Укажите натуральное число от 0 до 2')
            command = input()
        else:
            break
    return command

while True:
    print()
    command = Run()
    if command == '1':
        DrawTreeLinux(os.getcwd())
    elif command == '2':
        DrawTreeWindows(os.getcwd())
    elif command == '0':
        break

