import os
import os.path

def DrawTree(path, template=''):
    lst = sorted(os.listdir(path))
    for i in lst:
        flag = True if i == lst[-1] else False
        continuation_of_the_line = '└─> ' + i if flag else '├─> ' + i
        print(template + continuation_of_the_line)
        if os.path.isdir(path + '/' + i):
            DrawTree(path + '/' + i, (template + (('    ') if flag else '│   ')))

DrawTree(os.getcwd())

