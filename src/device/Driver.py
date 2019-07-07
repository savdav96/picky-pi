import serial, time, os

if os.name == 'posix':
    ARDUINO_SERIAL = '/dev/ttyACM0'
elif os.name == 'nt':
    ARDUINO_SERIAL = 'COM4'

try:
    ser = serial.Serial(ARDUINO_SERIAL, 9600)
    print('[DRIVER] Connected with: ' + ser.name + ' at', ser.baudrate)  # print the port used
except Exception as e:
    print('[DECODER] Exception occurred.', e)


def drive():
    print('[DRIVER] Starting.')
    while True:
        time.sleep(2)
        ser.write(str.encode('R'))
        line = ser.read()
        print(line.decode())
        time.sleep(2)
        ser.write(str.encode('G'))
        line = ser.read()
        print(line.decode())

