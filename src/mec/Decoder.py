import threading
import cv2
from src.mec.Constants import *

url = 'http://' + RASP_IP + ':' + str(STREAM_PORT) + '/stream.mjpg'
# url = 0

font = cv2.FONT_HERSHEY_SIMPLEX
# TOK = "2227LBsNQ4!bNUILok"


class Decoder(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.cap = cv2.VideoCapture(url)
        self.targets = {}

    def draw(self, target, image, contours, color):
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 1000:
                M = cv2.moments(contour)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
                cv2.putText(image, target, (x, y - 10), font, 0.75, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.circle(image, (cx, cy), 5, color, -1)
                cv2.putText(image, 'x: ' + str(cx) + ' y: ' + str(cy), (cx, cy - 10), font, 0.5, (255, 255, 255), 1,
                            cv2.LINE_AA)
                self.targets[target] = (cx, cy)

    def decode(self):
        print('[DECODER] Width: %d px, Height: %d px, FPS: %.2f' % (self.cap.get(3), self.cap.get(4), self.cap.get(5)))
        while True:
            ret, frame = self.cap.read()

            if not ret:
                print('[DECODER] Error reading from source')
                break

            blurred = cv2.GaussianBlur(frame, (5, 5), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            can_mask = cv2.inRange(hsv, CAN_HSV_LO, CAN_HSV_HI)
            glass_mask = cv2.inRange(hsv, GLASS_HSV_LO, GLASS_HSV_HI)

            mask = can_mask + glass_mask
            image = cv2.bitwise_and(frame, frame, mask=mask)

            (_, can_contours, hierarchy) = cv2.findContours(can_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            (_, glass_contours, hierarchy) = cv2.findContours(glass_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            self.draw('CAN', image, can_contours, (0, 0, 255))
            self.draw('GLASS', image, glass_contours, (0, 255, 0))

            cv2.imshow('Result Blurred and Mask', image)
            cv2.imshow('Original frame', frame)
            cv2.imshow('Mask', mask)

            # print('[DECODER] Targets: ', self.targets)

            key = cv2.waitKey(1)
            if key == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()

    def run(self):
        print('[DECODER] Starting.')
        self.decode()
        print('[DECODER] Stopping.')

    def get_targets(self):
        return self.targets


# Testing:
if __name__ == '__main__':
    decoder = Decoder()
    decoder.start()


