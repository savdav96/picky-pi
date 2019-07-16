from socket import *
from src.mec.Decoder import Decoder
import time, pickle
from src.mec.Constants import *


def client():

    decoder = Decoder()
    decoder.start()

    print('[CLIENT] Starting.')
    cs = socket(AF_INET, SOCK_STREAM)
    cs.connect((RASP_IP, SERVER_PORT))
    print('[CLIENT] Connected to: ', cs.getsockname())

    while True:
        try:
            data = decoder.get_targets()
            print('[CLIENT] Sending: ', data)
            cs.send(pickle.dumps(data))
            response = (cs.recv(1024)).decode('utf-8')
            print('[CLIENT] Response from Picky: ' + response)
            #time.sleep(0.5)

        except Exception as e:
            print('[CLIENT] Exception occurred.', e)
            break
    cs.close()
