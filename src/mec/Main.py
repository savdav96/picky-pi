import src.mec.Client as Client
# from threading import Thread

if __name__ == '__main__':

    print('[MAIN] Starting.')
    Client.client()

    # client = Thread(target=Client.client())
    # client.start()
    # client.join()
    print("[MAIN] All threads finished. Stopping")

