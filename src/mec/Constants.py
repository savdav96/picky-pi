import numpy as np

RASP_IP = '172.20.10.9'
# RASP_IP = '192.168.43.96'
# RASP_IP = 'localhost'
RASP_NAME = 'raspberry.local'
STREAM_PORT = 8000
SERVER_PORT = 8001

CAN_HSV_LO = np.array([37, 75, 91])
CAN_HSV_HI = np.array([179, 255, 247])

GLASS_HSV_LO = np.array([50, 35, 0])
GLASS_HSV_HI = np.array([74, 255, 255])

TARGET = 'CAN'
