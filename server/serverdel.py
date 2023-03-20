import socket, threading, json

LOCALHOST = '127.0.0.1'
PORT = 1488
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print('Сервер запущен!')

slovar = {}

class ClientThread(threading.Thread):
    '''Создаем поток для клиента'''
    def __init__(self, clientaddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientaddress = clientaddress

    def run(self):
        print("Подключение с клиента : ", clinetaddress)
        msg = ''
        login = ''
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode('UTF-8')
            print('Команда :', msg)
            self.csocket.send(bytes('1', 'UTF-8'))
            global slovar
            match msg: #Получение команд с клиента
                case 'exit' | '':
                    print(type(slovar), slovar)
                    with open('dela.json', 'w', encoding='UTF-8') as file:
                        json.dump(slovar, file, indent=4, ensure_ascii=True, sort_keys=True)
                    print("Отключение", clinetaddress)
                    slovar.clear()
                    break
                case 'SendName': #Здесь происходит авторизация клиента
                    data = self.csocket.recv(4096)
                    msg = data.decode('UTF-8')
                    with open('dela.json', 'r', encoding='UTF-8') as j:
                        slovar = json.load(j)
                        slovar = dict(slovar)
                    print(slovar)
                    if msg in slovar:
                        login = msg
                        stroka = str(slovar[login])
                        self.csocket.send(bytes(stroka, 'UTF-8'))
                    else:
                        login = msg
                        slovar[login] = []
                        self.csocket.send(bytes('registration', 'UTF-8'))
                case 'GetList':
                    self.getlist(login)
                case 'AddValue':
                    self.addvalue(login)
                    self.getlist(login)
                case 'ClearList':
                    slovar[login] = []
                case _: #wildcard
                    continue


    def addvalue(self, login: str):
        '''Функция добавления дела в список'''
        global slovar
        data = self.csocket.recv(4096)
        values = data.decode('UTF-8')
        print(slovar)
        slovar[login].append(values)


    def getlist(self, login: str):
        '''Функция отправки списка клиенту'''
        global slovar
        output = list(slovar.get(login))
        self.csocket.send(bytes(f'{output}', 'UTF-8'))

if __name__ == "__main__":
    while True:
        server.listen(1)
        clientsock, clinetaddress = server.accept()
        newthread = ClientThread(clinetaddress, clientsock)
        newthread.start()