import cv2
import pyautogui



def getMouseCoordinate():
    x, y = pyautogui.position()
    print(x, y)


getMouseCoordinate()