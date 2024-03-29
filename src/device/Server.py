from socket import *
import time, pickle
from Driver import ser

TARGET = 'CAN'


def server():
    ss = socket(AF_INET, SOCK_STREAM)
    ss.bind(('', 8001))
    ss.listen(1)

    while True:
        print('[SERVER] Starting.')
        connection, address = ss.accept()
        print('[SERVER] Connected with: ', address)

        while True:
            try:
                data = (pickle.loads(connection.recv(1024)))
                # print('[SERVER] Received from PC: ', data)
                connection.send('Received correctly!'.encode('utf-8'))
                handle(data)
            except Exception as e:
                print('[SERVER] Exception occurred.', e)
                time.sleep(2)
        connection.close()


def handle(data):
    assert type(data) == dict
    if TARGET in data:
        x = data[TARGET][0]
        y = data[TARGET][1]

    else:
        x = -256
        y = -256

    print('[DRIVER] x: %d, y: %d' % (x, y))

    try:
        ser.write(str(x).encode())
        #line = ser.read()
        #print(line.decode())
    except Exception as e:
        print('[DRIVER] Exception occurred. ', e)

