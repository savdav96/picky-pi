from socket import *
# from src.deprecated.decoder import Decoder
from src.mec.Decoder import Decoder
import pickle, time


HOST = '172.20.10.9'  # The server's hostname or IP address
PORT = 8001        # The port used by the server

HOST = 'localhost'

cs = socket(AF_INET, SOCK_STREAM)

cs.connect((HOST, PORT))

decoder = Decoder()
decoder.start()

while True:
    data = decoder.get_targets()
    print('Sending: ', data)
    cs.send(pickle.dumps(data))
    response = (cs.recv(1024)).decode('utf-8')
    print('Response from Picky: ' + response)
    time.sleep(0.5)

cs.close()

