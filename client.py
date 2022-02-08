import socket, threading, sys




server = ('127.0.0.1',9000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(server)


def recv_message():
    while True:
        data = sock.recv(1024)
        print('\b' * 10, end='')
        print(data.decode('utf-8'))
        sys.stdout.flush()


print('Подключитесь к новой комнате или создайте свою: ')
mes = input('"n"-создать свою комнату,или код к комнаты: ')
sock.send(mes.encode('utf-8'))

data = sock.recv(1024) 
print(data)

name = input('your name: ')

recv = threading.Thread(target=recv_message)
recv.start()

while True:

    mes = input() 
    sock.send(f"{name}: {mes}".encode('utf-8'))

    if mes == '_quit':
        recv.join()
        sock.close()
        exit()
        




