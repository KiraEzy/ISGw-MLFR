from pyfirmata import Arduino
import time
import tkinter as tk
import numpy
import pynput
import cv2
import math
import mediapipe as mp
import pyscreenshot
import multiprocessing
import time
import os
from datetime import datetime
from pynput.keyboard import Key;
from PIL import Image, ImageTk
from FaceDetectionModule import FaceDetector
from SerialModule import SerialObject
import serial

resized_image = 0;
new_image = 0
resized_image2 = 0;
new_image2 = 0
flip = cv2.flip
detector = FaceDetector()
#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

root = tk.Tk()
panel = tk.Label(root)
panel.pack(padx=10, pady=10)
root.config(cursor="arrow")

def video_loop():
    success, img = cap.read()
    height, width, channels = img.shape
    img = img[int(height/2 - 100):int(height/2 + 100), int(width/2-100): int(width/2+100)]
    img, bbox = detector.findFaces(img)
    # img_flip = cv2.flip(img, 1)
    if detector.results.detections:
        print(detector.results.detections)
        board.digital[10].write(1)
    else:
        print("000");
        board.digital[10].write(0)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("Show", imgRGB)
    cv2.waitKey(2)
if __name__ == '__main__':
    board = Arduino('COM8')
    #board = Arduino('COM4')
    print("Communication Successfully started")
    root.title("MainWindow")
    while True:
        video_loop()
    root.mainloop()
    cap.release()
    cv2.destroyAllWindows()

