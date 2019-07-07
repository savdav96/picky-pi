import serial, time
from ..common.Constants import *


def drive():
    print('[DRIVER] Starting.')
    try:
        ser = serial.Serial(ARDUINO_SERIAL, 9600)
        print('[DRIVER] Connected with: ' + ser.name + ' at', ser.baudrate)  # print the port used
        while True:
            time.sleep(2)
            ser.write(str.encode('R'))
            line = ser.read()
            print(line.decode())
            time.sleep(2)
            ser.write(str.encode('G'))
            line = ser.read()
            print(line.decode())

    except Exception as e:
        print('[DECODER] Exception occurred.', e)

