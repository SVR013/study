import socket, threading, json, copy

LOCALHOST = '127.0.0.1'
PORT = 1790
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print('Сервер запущен!')

slovar = {}

class ClientThread(threading.Thread):
    '''Создаем поток для клиента'''
    def __init__(self, clientaddress, clientsocket, slovar: dict):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientaddress = clientaddress
        self.slovar = copy.deepcopy(slovar)

    def run(self):
        print("Подключение с клиента : ", clinetaddress)
        msg = ''
        login = ''
        value = []
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode('UTF-8')
            print('Команда :', msg)
            self.csocket.send(bytes('1', 'UTF-8'))
            match msg: #Получение команд с клиента
                case 'exit' | '':
                    value2 = slovar[login] #Записываем изменения
                    self.theend(login, value2)
                    break
                case 'SendName': #Здесь происходит авторизация клиента
                    data = self.csocket.recv(4096)
                    msg = data.decode('UTF-8')
                    with open('dela.json', 'r', encoding='UTF-8') as j:
                        self.slovar = json.load(j)
                        self.slovar = dict(self.slovar)
                    print(self.slovar)
                    if msg in self.slovar:
                        login = msg
                        stroka = str(self.slovar[login])
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

    def theend(self, login, value2):
        with open('dela.json', 'r', encoding='UTF-8') as j:
            slovar2 = json.load(j)  # Обновляем данные, чтобы получить изменения других пользователей
            slovar2 = dict(slovar2)
        slovar2[login] = value2  # Записываем в обновленный словарь наши изменения
        with open('dela.json', 'w', encoding='UTF-8') as file:
            json.dump(slovar2, file, indent=4, ensure_ascii=True, sort_keys=True)
        print("Отключение", clinetaddress)

    def addvalue(self, login: str):
        '''Функция добавления дела в список'''
        data = self.csocket.recv(4096)
        values = data.decode('UTF-8')
        print(slovar)
        slovar[login].append(values)


    def getlist(self, login: str):
        '''Функция отправки списка клиенту'''
        output = list(slovar.get(login))
        self.csocket.send(bytes(f'{output}', 'UTF-8'))

if __name__ == "__main__":
    while True:
        server.listen(2)
        clientsock, clinetaddress = server.accept()
        newthread = ClientThread(clinetaddress, clientsock, slovar)
        newthread.start()