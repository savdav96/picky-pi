import numpy as np

RASP_IP = '172.20.10.9'
# RASP_IP = '10.149.11.150'
# RASP_IP = 'localhost'
STREAM_PORT = 8000
SERVER_PORT = 8001

#CAN_HSV_LO = np.array([33, 141, 0])
#CAN_HSV_HI = np.array([179, 255, 255])

CAN_HSV_LO = np.array([116, 100, 79])
CAN_HSV_HI = np.array([179, 155, 174])

GLASS_HSV_LO = np.array([50, 35, 0])
GLASS_HSV_HI = np.array([74, 255, 255])

TARGET = 'CAN'
