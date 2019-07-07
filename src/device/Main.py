import os
from threading import Thread

if os.name == 'posix':
    from Streamer import *
    from Driver import *
    from Server import *

elif os.name == 'nt':
    from src.device.Streamer import *
    from src.device.Driver import *
    from src.device.Server import *


if __name__ == '__main__':

    print('[MAIN] Starting.')

    streamer = Thread(target=stream)
    streamer.start()

    driver = Thread(target=drive)
    driver.start()

    server = Thread(target=server)
    server.start()

    streamer.join()
    driver.join()
    server.join()

    print("[MAIN] All threads finished. Stopping")
