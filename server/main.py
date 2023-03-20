from tkinter import *
from tkinter import ttk
from klient import client1

lst = []

root = Tk()
root.title("Ваш список дел")
root.geometry("400x690")

def dismiss(window, req):
    '''Функция закрытия окна с авторизацией'''
    global lst
    lst = client1(req)
    if lst == 'registration' or lst == '[]':
        window.grab_release()
        window.destroy()
        languages_listbox['text'] = 'Добавьте свое\nпервое дело!'
    else:
        window.grab_release()
        window.destroy()
        lst = formatlst(lst, flag=True)
        languages_listbox['text'] = lst

def click():
    '''Это функция открытия всплывающего окна с авторизацией пользователя'''
    client1('SendName')
    window = Toplevel()
    window.title("Авторизация")
    window.geometry("300x80")
    window['background'] = '#797979'
    window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window)) # перехватываем нажатие на крестик
    entry2 = Entry(window)
    entry2.pack(anchor="s", fill=X, padx=10, pady=10)
    close_button = ttk.Button(window, text="Авторизоваться", command=lambda: dismiss(window, entry2.get()))
    close_button.pack(anchor="s", expand=True, fill=X, padx=10, pady=5)
    window.grab_set()

def add_value():
    '''Функция добавление нового дела в список и отправка его на сервер'''
    global lst
    client1('AddValue')
    req = entry.get()
    lst = client1(req)
    lst = formatlst(lst, flag=True)
    print(req)
    languages_listbox['text'] = lst

def formatlst(lst, flag:bool):
    '''Функция, которая форматирует получаемую строку к списку'''
    lst = lst[2:-2] if flag else lst[3:-2]
    lst = lst.split('\', \'')
    lst = '\n\n'.join(lst)
    return lst

def update_list():
    '''Функция получения актуального списка с сервера'''
    global lst
    lst = client1('GetList')
    lst = formatlst(lst, flag=False)
    languages_listbox['text'] = lst

def delete_list():
    '''Функция очистки списка дел'''
    global lst
    lst = client1('ClearList')
    languages_listbox['text'] = 'Добавьте свое\nпервое дело!'

click()

root['background']='#797979'
languages = lst
# Код графического интерфейса
languages_var = Variable(value=languages)
languages_listbox = Label(text=languages_var, height=23, font=('Arial', 15))
languages_listbox.pack(anchor=NW, expand=True, fill=X, padx=5, pady=5)
#Формируем поле вывода списка дел
entry = Entry()
entry.pack(anchor="s", fill=X, padx=10, pady=10)
entry.insert(0, "Введите ваше дело")
#Формируем кнопки
btn = ttk.Button(text="Добавить дело", command=add_value, padding=5)
btn1 = ttk.Button(text="Обновить", command=update_list, padding=5)
btn2 = ttk.Button(text="Очистить список дел", command=delete_list, padding=5)

btn.pack(anchor="s", fill=X, padx=10)
btn1.pack(anchor="s", fill=X, padx=10)
btn2.pack(anchor="s", fill=X, padx=10)

root.mainloop()