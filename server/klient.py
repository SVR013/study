import socket
from threading import Thread
import threading


SERVER = '127.0.0.1'
PORT = 1790
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def client1(req):
    msg = ''
    def task():
        '''Получение данных с сервера и их декодирование'''
        nonlocal msg
        in_data = client.recv(4096)
        msg = in_data.decode()
        print(msg)

    def task2():
        '''Кодирование данных и отправка на сервер'''
        out_data = req
        client.sendall(bytes(out_data, 'UTF-8'))


    t1 = Thread(target=task2)
    t2 = Thread(target=task)

    t1.start()
    t2.start()

    t2.join()
    t1.join()
    return msg