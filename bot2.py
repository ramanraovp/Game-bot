import pyautogui
import time
import pyscreeze
import sys
from tkinter import messagebox
#import bot3

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

#Box(left=385, top=429, width=1114, height=225
def open_chrome():
    pyautogui.mouseDown(1287,1155)
    time.sleep(2)
    x,y = pyautogui.locateCenterOnScreen(r"g1\chrome.png",confidence=0.8)
    pyautogui.click(x,y)
    pyautogui.click(x,y)

def select() :
    try:
        x,y = pyautogui.locateCenterOnScreen(r"g2\select.png",confidence=0.8)
        pyautogui.click(x,y+400)
    except :
        pyautogui.press("pageup")
        pyautogui.click(371,95)
        time.sleep(2)
        select()

def start():
    x,y = pyautogui.locateCenterOnScreen(r"g2\start.png", confidence=0.6) 
    pyautogui.click(x,y)
    

def locate(rv,gv,bv):
    coords = (385,429,1114,425)
    im = pyautogui.screenshot(region = coords)
    #im = bot3.screenshot_region_pillow(385,429,1114,425)
    for x in range (0,1114,25):
        for y in range (0,425,25):
            r,g,b = im.getpixel((x,y))
            if (r == rv and g == gv and b == bv):
                pyautogui.click(x+387,y+431)
                #pyautogui.click(x+385,y+429)

def play():
    pixel = pyautogui.pixel(1417,263)
    val = [(242,138,0),(85,90,190),(255,244,202),(190,190,190)]
    while 1:
        if (pyautogui.pixel(1417,263) != pixel) :
                break
        for i in val :
            locate(i[0],i[1],i[2])

def gain():
    try:
        x,y = pyautogui.locateCenterOnScreen(r"g1\get.png",confidence=0.8)
        pyautogui.click(x,y)
    except:
        #sys.exit()
        print("lost")
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
    x,y = pyautogui.locateCenterOnScreen(r"g2\tryagain.png",confidence=0.8)
    pyautogui.click(x,y)
    time.sleep(3.1)
    play()
    time.sleep(1)
    gain()
    

def main():
    open_chrome()
    time.sleep(2)
    for i in range (1): 
        select()
        time.sleep(3)
        start()
        time.sleep(3.5)
        play()
        time.sleep(2)
        gain()
        time.sleep(8)
        goto()
        time.sleep(3)
        pyautogui.click(113,20)
        #time.sleep(32)

if __name__ =='__main__' :
    main()