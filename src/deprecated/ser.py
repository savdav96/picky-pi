import serial, time, pickle, os
from threading import Thread

ser = serial.Serial('COM4', 9600)

import io
#import picamera
import logging
import socketserver
from threading import Condition
from http import server
from socket import *

PAGE = """\
<html>
<head>
<title>picamera MJPEG streaming demo</title>
</head>
<body>
<h1>PiCamera MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)


output = StreamingOutput()


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                print(
                    '[STREAMER] Removed streaming client %s: %s' % (self.client_address, str(e)))
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


#camera = picamera.PiCamera(resolution='640x480', framerate=24)


def loop_stream():
    #camera.start_recording(output, format='mjpeg')
    print('Started stream...')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        #camera.stop_recording()
        print('Finished...')


def loop_serial():
    while True:
        print('serial port = ' + ser.name)  # print the port used
        time.sleep(2)
        ser.write(str.encode('R'))
        line = ser.read()
        print(line.decode())
        time.sleep(2)
        ser.write(str.encode('G'))
        line = ser.read()
        print(line.decode())


def loop_dumb():
    while True:
        print('Intanto faccio altro...')
        time.sleep(1)


HOST = '127.0.0.1'
PORT = 8001

ss = socket(AF_INET, SOCK_STREAM)
ss.bind(('', PORT))
ss.listen(1)


def loop_server():
    while True:
        print('Ready')
        connection, address = ss.accept()
        print('Connected with: ', address)

        while True:
            try:
                data = (pickle.loads(connection.recv(1024)))
                print('Received from PC: ', data)
                connection.send('Received correctly!'.encode('utf-8'))
                #if line == 'ciao':
                    #ser.write(str.encode('R'))
            except Exception as e:
                print('Exception occurred.', e)
                time.sleep(2)
        connection.close()


if __name__ == '__main__':

    loop_t = Thread(target=loop_stream)
    loop_t.start()

    loop_s = Thread(target=loop_serial)
    loop_s.start()

    #loop_d = Thread(target=loop_dumb)
    #loop_d.start()

    loop_p = Thread(target=loop_server)
    loop_p.start()

    loop_t.join()
    loop_s.join()
    #loop_d.join()
    loop_p.join()

    print("thread finished...exiting")


