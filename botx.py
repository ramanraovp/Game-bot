import pyautogui
import pyscreeze
import time
import random
import sys
from tkinter import messagebox
from PIL import ImageGrab,ImageChops

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
#(x=1287, y=1055)"C:\Users\raman\Desktop\phython\g1\chrome.png"
def open_chrome():
    pyautogui.mouseDown(1287,1155)
    time.sleep(2)
    x,y = pyautogui.locateCenterOnScreen(r"C:\Users\raman\Desktop\phython\g1\chrome.png",confidence=0.8)
    pyautogui.click(x,y)
    pyautogui.click(x,y)
#(x=1163, y=546)  game icon location = (x=371, y=95) 
def select_2048() :
    try:
        x,y = pyautogui.locateCenterOnScreen(r"C:\Users\raman\Desktop\phython\g1\2048.png",confidence=0.8)
        pyautogui.click(x,y+400)
    except :
        pyautogui.press("pageup")
        pyautogui.click(371,95)
        time.sleep(2)
        select_2048()

def start():
    x,y = pyautogui.locateCenterOnScreen(r"C:\Users\raman\Desktop\phython\g3\start.png",confidence=0.8)
    pyautogui.click(x,y)
#(79, 83, 100) at 1343 266
def play():
    region = (416,119,1327,1031)
    #pixel = pyautogui.pixel(1000,266)
    pixel = pyautogui.pixel(1477,67)
    while 1:
        #if (pyautogui.pixel(1000,266) != pixel) :
        if(pixel != pyautogui.pixel(1477,67)):
            break
        #arrow = random.choice(['up','down','left','right','left','left','left','left','up','up','up','up'])
        im1 = ImageGrab.grab(bbox=region)
        pyautogui.press('left')
        im2 = ImageGrab.grab(bbox=region)
        diff = ImageChops.difference(im1, im2)
        bbox = diff.getbbox()
        if bbox is None:
            im1 = ImageGrab.grab(bbox=region)
            pyautogui.press('up')
            im2 = ImageGrab.grab(bbox=region)
            bbox = diff.getbbox()
            if bbox is None:
                if (pyautogui.pixel(525,914) != (34,36,40)):#525,914
                    im1 = ImageGrab.grab(bbox=region)
                    pyautogui.press('down')
                    im2 = ImageGrab.grab(bbox=region)
                    bbox = diff.getbbox()
                    if bbox is None:
                        pyautogui.press('right')
                elif (pyautogui.pixel(1206,232) != (34,36,40)):
                    im1 = ImageGrab.grab(bbox=region)
                    pyautogui.press('right')
                    im2 = ImageGrab.grab(bbox=region)
                    bbox = diff.getbbox()
                    if bbox is None:
                        pyautogui.press('down')
                else:
                    im1 = ImageGrab.grab(bbox=region)
                    pyautogui.press('down')
                    im2 = ImageGrab.grab(bbox=region)
                    bbox = diff.getbbox()
                    if bbox is None:
                        pyautogui.press('right')

                
def gain():
    try:
        x,y = pyautogui.locateCenterOnScreen(r"g3\get.png",confidence=0.8)
        pyautogui.click(x,y)
    except:
        exept()

def goto():
    try:
        x,y = pyautogui.locateCenterOnScreen(r"g1\goto.png",confidence=0.8)
        pyautogui.click(x,y)
    except:
        messagebox.showwarning("showwarning","Captcha Ahead !!!!")
        res = pyautogui.confirm(text = 'Did you clear the captcha ?',title = 'Error',buttons = ['YES','NO'])
        if (res=='YES'):
            time.sleep(1)
            goto()
        else:
            pyautogui.alert(text = "Program closed !",button = 'OK')
            sys.exit()


def exept():
    x,y = pyautogui.locateCenterOnScreen(r"g1\tryagain.png",confidence=0.8)
    pyautogui.click(x,y)
    time.sleep(5)
    play()
    time.sleep(1)
    gain()

#refresh 89 22
def main():
    open_chrome()
    time.sleep(2)
    for i in range (1): 
        select_2048()
        time.sleep(3)
        start()
        time.sleep(5)
        play()
        time.sleep(1)
        gain()
        time.sleep(8)
        goto()
        time.sleep(3)
        pyautogui.click(113,20)
        time.sleep(32)
        
if __name__ == '__main__' :
    main()
