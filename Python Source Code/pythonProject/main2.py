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
from pyfirmata import Arduino
import time
from FaceDetectionModule import FaceDetector
from SerialModule import SerialObject
import serial

resized_image = 0;
new_image = 0
resized_image2 = 0;
new_image2 = 0
flip = cv2.flip
detector = FaceDetector()
cap = cv2.VideoCapture(0)
arduino = SerialObject()
c = serial.Serial('COM7')


root = tk.Tk()
panel = tk.Label(root)
panel.pack(padx=10, pady=10)
root.config(cursor="arrow")
board = Arduino("COM7")

board.exit()
def video_loop():
    global isStart, isCap,isTrig,isPaged,isSet,isEnabled,isSpace,isVolume,isSetHand,handPos,indexPos, lastMilliTime,startPopTime
    global isPop, startPopTime, isPopStart,imgSide, isSpeed,imgPop,volume

    success,img = cap.read()

    img, bbox = detector.findFaces(img)
    img_flip = cv2.flip(img, 1)

    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)

    imgRGB = cv2.cvtColor(img_flip, cv2.COLOR_BGR2RGB)
    current_image = Image.fromarray(imgRGB)
    imgtk = ImageTk.PhotoImage(image=current_image)
    panel.imgtk = imgtk
    panel.config(image = imgtk)
    root.after(1,video_loop)


if __name__ == '__main__':
    board = Arduino('YOUR_PORT_HERE')
    print("Communication Successfully started")
    video_loop()
    root.title("MainWindow")
    root.mainloop()
    cap.release()
    cv2.destroyAllWindows()
