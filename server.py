from pydoc import cli
from random import randint
import socket





server = ('127.0.0.1',9000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server)



def new_client_comnat(code ,client):
    global comnats
    if client not in comnats[code]:
        comnats[code].append(client)

    return 'conected'.encode('utf-8')
    



def create_comnat(client):
    global comnats, keys
    code = ''.join([str(randint(0,9)) for i in range(10) ])
    # if client not in comnats[code]:
    comnats[code] = [client]

    keys = list(comnats.keys())

    return f"comnat code: {code}".encode('utf-8')


def SendMessage(ms, client):
    for i in keys:
        if client in comnats[i]:
            for cl in comnats[i]:
                if cl != client:
                    sock.sendto(ms, cl)




comnats = {}
keys = []
otvet = ''

while True:
    data, client = sock.recvfrom(1024)
    if data.decode('utf-8') == 'n':
        otvet = create_comnat(client)
        sock.sendto(otvet, client)
    elif data.decode('utf-8') in keys:
        otvet = new_client_comnat(data.decode('utf-8'), client)
        sock.sendto(otvet, client)
    else:
        SendMessage(data, client)

    print(f'conected client: {client}')
    print(comnats)



