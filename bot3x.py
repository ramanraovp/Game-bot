import pyautogui as ab
import time
import pyscreeze
import sys
from tkinter import messagebox
from PIL import ImageChops,ImageGrab
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
#(591,112)(194,119,90)
#ab.alert(button = 'ok')
btc =(242,138,0)
Btc=[]
bnb =(255,244,202)
Bnb=[]
eth =(85,90,190)
Eth=[]
lrt =(19,23,28)#(185, 247, 0)
Lrt=[]
sol =(208, 43, 250)#,(255,255,255)#][(22, 232, 173)
Sol=[]
xrp =(190,190,190)
Xrp=[]
ltc =(38, 105, 184)
Ltc =[]
dog = (241, 242, 242)#(221, 205, 0)
Dog =[]
pol = (122, 50, 170)
Pol = []
pin = (230, 0, 122)
Pin = []


def check_h(regio,s):
    btc =(242,138,0)
    bnb =(255,244,202)
    eth =(85,90,190)
    lrt =(19,23,28)
    sol =(208, 43, 250)
    xrp =(190,190,190)
    ltc =(38, 105, 184)
    dog = (241, 242, 242)#(221, 205, 0)
    pol = (122, 50, 170)
    pin = (230, 0, 122)
    x = [1,1,1,1,1,1,1,1,1,1]
    y = [1,1,1,1,1,1,1,1,1,1]
    im = ab.screenshot(region=regio)
    for k in range(0,regio[2],s):
                
                for l in range(0,regio[3],s):
                    
                    pix = im.getpixel((k,l))
                    [i,j] = [k+regio[0],l+regio[1]]
                    if((pix == btc and x[0] == 1 and len(Btc)<2)):
                        if(x[0] == 1):
                            x[0] += 1
                            Btc.append([i,j])
                        elif(y[0] == 1):
                            y[0] += 1
                            Btc.append([i,j])
                        
                    elif((pix == eth and x[1] == 1 and len(Eth)<2)):
                            if(x[1] == 1):
                                x[1] += 1
                                Eth.append([i,j])
                            elif(y[1] == 1):
                                y[1] += 1
                                Eth.append([i,j])
                    elif((pix == bnb and x[2] == 1 and len(Bnb)<2)):
                        if(x[2] == 1):
                            x[2] += 1
                            Bnb.append([i,j])
                        elif(y[2] == 1):
                            y[2] += 1
                            Bnb.append([i,j])
                    elif((pix == sol and x[3] == 1 and len(Sol)<2)):
                        if(x[3] == 1):
                            x[3] += 1
                            Sol.append([i,j])
                        elif(y[3] == 1):
                            y[3] += 1
                            Sol.append([i,j])
                    elif((pix == lrt and x[4] == 1 and len(Lrt)<2 )):
                        if(x[4] == 1):
                            x[4] += 1
                            Lrt.append([i,j])
                        elif(y[4] == 1):
                            y[4] += 1
                            Lrt.append([i,j])
                    elif((pix == xrp and x[5] == 1 and len(Xrp)<2)):
                        if(x[5] == 1):
                            x[5] += 1
                            Xrp.append([i,j])
                        elif(y[5] == 1):
                            y[5] += 1
                            Xrp.append([i,j])
                    elif((pix == ltc and x[6] == 1 and s == 7 and len(Ltc)<2)):
                            if(x[6] == 1):
                                x[6] += 1
                                Ltc.append([i,j])
                            elif(y[6] == 1):
                                y[6] += 1
                                Ltc.append([i,j])
                    elif((pix == dog and x[7] == 1 and s ==7 and len(Dog)<2)):
                            if(x[7] == 1):
                                x[7] += 1
                                Dog.append([i,j])
                            elif(y[7] == 1):
                                y[7] += 1
                                Dog.append([i,j])
                    elif((pix == pol and x[8] == 1 and s ==7 and len(Pol)<2)):
                            if(x[8] == 1):
                                x[8] += 1
                                Pol.append([i,j])
                            elif(y[8] == 1):
                                y[8] += 1
                                Pol.append([i,j])
                    elif((pix == pin and x[9] == 1 and s ==7 and len(Pin)<2)):
                            if(x[9] == 1):
                                x[9] += 1
                                Pin.append([i,j])
                            elif(y[9] == 1):
                                y[9] += 1
                                Pin.append([i,j])


def open_chrome():
    ab.mouseDown(1287,1155)
    time.sleep(2)
    x,y = ab.locateCenterOnScreen(r"g1\chrome.png",confidence=0.8)
    ab.click(x,y)
    ab.click(x,y)

def select() :
    try:
        x,y = ab.locateCenterOnScreen(r"g3\select.png",confidence=0.6)
        ab.click(x,y+400)
    except :
        #sys.exit()
        ab.press("pageup")
        time.sleep(0.5)
        ab.click(371,95)
        time.sleep(2)
        ab.press("pagedown")
        time.sleep(0.5)
        select()

def start():
    x,y = ab.locateCenterOnScreen(r"g3\Start.png", confidence=0.6) 
    ab.click(x,y)
#(600,115,700,935)


def check(regio,s):
       btc =(242,138,0)
       bnb =(255,244,202)
       eth =(85,90,190)
       lrt =(19,23,28)
       sol =(208, 43, 250)
       xrp =(190,190,190)
       ltc =(38, 105, 184)
       dog = (241, 242, 242)#(221, 205, 0)
       pol = (122, 50, 170)
       pin = (230, 0, 122)
       x = [1,1,1,1,1,1,1,1,1,1]
       y = [1,1,1,1,1,1,1,1,1,1]
       im = ab.screenshot(region=regio)
       for k in range(0,regio[2],s):
                
                for l in range(0,regio[3],s):
                    
                    pix = im.getpixel((k,l))
                    [i,j] = [k+regio[0],l+regio[1]]
                    if((pix == btc and x[0] == 1 and len(Btc)<2)):
                        if len(Btc) == 1 :
                             ab.click(Btc[0][0],Btc[0][1])
                             time.sleep(1)
                             Btc.clear()
                             return(1)
                        return(2)
                    elif((pix == eth and x[1] == 1 and len(Eth)<2)):
                            if len(Eth) == 1 :
                             ab.click(Eth[0][0],Eth[0][1])
                             time.sleep(1)
                             Eth.clear()
                             return(1)
                            return(2)
                    elif((pix == bnb and x[2] == 1 and len(Bnb)<2)):
                        if len(Bnb) == 1 :
                             ab.click(Bnb[0][0],Bnb[0][1])
                             time.sleep(1)
                             Bnb.clear()
                             return(1)
                        return(2)
                    elif((pix == sol and x[3] == 1 and len(Sol)<2)):
                        if len(Sol) == 1 :
                             ab.click(Sol[0][0],Sol[0][1])
                             time.sleep(1)
                             Sol.clear()
                             return(1)
                        return(2)
                    elif((pix == lrt and x[4] == 1 and len(Lrt)<2 )):
                        if len(Lrt) == 1 :
                             ab.click(Lrt[0][0],Lrt[0][1])
                             time.sleep(1)
                             Lrt.clear()
                             return(1)
                        return(2)
                    elif((pix == xrp and x[5] == 1 and len(Xrp)<2)):
                        if len(Xrp) == 1 :
                             ab.click(Xrp[0][0],Xrp[0][1])
                             time.sleep(1)
                             Xrp.clear()
                             return(1)
                        return(2)
                    elif((pix == ltc and x[6] == 1 and s == 7 and len(Ltc)<2)):
                            if len(Ltc) == 1 :
                             ab.click(Ltc[0][0],Ltc[0][1])
                             time.sleep(1)
                             Ltc.clear()
                             return(1)
                            return(2)
                    elif((pix == dog and x[7] == 1 and s ==7 and len(Dog)<2)):
                            if len(Dog) == 1 :
                             ab.click(Dog[0][0],Dog[0][1])
                             time.sleep(1)
                             Dog.clear()
                             return(1)
                            return(2)
                    elif((pix == pol and x[8] == 1 and s ==7 and len(Pol)<2)):
                            if len(Pol) == 1 :
                             ab.click(Pol[0][0],Pol[0][1])
                             time.sleep(1)
                             Pol.clear()
                             return(1)
                            return(2)
                    elif((pix == pin and x[9] == 1 and s ==7 and len(Pin)<2)):
                            if len(Pin) == 1 :
                             ab.click(Pin[0][0],Pin[0][1])
                             time.sleep(1)
                             Pin.clear()
                             return(1)
                            return(2)


                    
                    

#(600,115,700,935)


def play(x,regio,s,p,q):
    pi = ab.pixel(p,q)
    k=1  
    for i in x:
            if(ab.pixel(p,q) == pi):
                        #time.sleep(0.5)
                        ab.click(i[0],i[1])
                        time.sleep(0.5)
                        
                        if(k == 1):  
                            #k = 2     
                            k = check(regio,s) 
                            
                          
                            
                        else:
                            k = 1
                            check_h(regio,s)
                            time.sleep(0.4)
                            '''for i in [Btc,Eth,Bnb,Sol,Xrp,Lrt,Ltc,Dog,Pol,Pin]:
                                res(i,p,q)
                            time.sleep(1)'''

                            
def res(x,p,q):

    pi = ab.pixel(p,q)
    if(len(x) > 1):
        k=1  
        for i in x:
                if(ab.pixel(p,q) == pi):
                            #time.sleep(0.5)
                            ab.click(i[0],i[1])
                            #print(ab.pixel(i[0],i[1]))
                            time.sleep(0.5)
                            #im = ab.screenshot(region=(i[0]-85//2,i[1]-46//2,85,46))
                            if(k == 1):                        
                                k = k+1
                            else:
                                k = 1
                                x.clear()
                                #check()
                                #time.sleep(1)   
def res_h(x,p,q):
    pi = ab.pixel(p,q)
    if(len(x) == 2): 
        if(ab.pixel(p,q) == pi):
                            time.sleep(0.5)
                            ab.click(x[0][0],x[0][1])
                            time.sleep(1)
                            x.clear()
                            return(1)
    else:
             return(2)
    
        
     



def gain():
    try:
        x,y = ab.locateCenterOnScreen(r"g3\get.png",confidence=0.8)
        ab.click(x,y)
    except:
        #sys.exit()
        print("lost")
        exept()

def goto():
    try:
        x,y = ab.locateCenterOnScreen(r"g1\goto.png",confidence=0.8)
        ab.click(x,y)
    except:
        messagebox.showwarning("showwarning","Captcha Ahead !!!!")
        res = ab.confirm(text = 'Did you clear the captcha ?',title = 'Error',buttons = ['YES','NO'])
        if (res=='YES'):
            time.sleep(1)
            goto()
        else:
            ab.alert(text = "Program closed !",button = 'OK')
            sys.exit()

def exept():
    a = [[730, 236], [958, 236], [1118, 236], [730, 468], [958, 468], [1118, 468], [730, 695], [958, 695], [1118, 695], [730, 930], [958, 930], [1118, 930]]
    b = a
    c = [[617, 230], [844, 230], [1072, 230], [1298, 230], [[617, 460], [844, 460]],[[1072, 460], [1298, 460]], [[617, 690], [844, 690]], [[1072, 690], [1298, 690]], [[617, 920], [844, 920]], [[1072, 920], [1298, 920]]]

    e = [[504, 235], [730, 235], [960, 235], [1190, 235], [1408, 235],[504,465],[730, 465], [960, 465], [1190, 465], [1408, 465], [504, 695], [730, 695], [960, 695], [1190, 695], [1408, 695], [504, 925], [730, 925], [960, 925], [1190, 925], [1408, 925]]

    x,y = ab.locateCenterOnScreen(r"g3\tryagain.png",confidence=0.8)
    ab.click(x,y)
    time.sleep(3.1)
    n = ab.pixel(591,112)
    if(n == (194,119,90)):
        play(b,(600,115,700,935))
    else:
        play(c,(491,118,924,932))
    time.sleep(1)
    gain()
#(491,118,924,932)
def main():
    a = [[730, 236], [958, 236], [1118, 236], [730, 468], [958, 468], [1118, 468], [730, 695], [958, 695], [1118, 695], [730, 930], [958, 930], [1118, 930]]
    b = a
    c = [[617, 230], [844, 230],[1072, 230], [1298, 230],[617, 460], [844, 460],[1072, 460], [1298, 460],[617, 690], [844, 690],[1072, 690], [1298, 690],[617, 920], [844, 920],[1072, 920], [1298, 920]]

    e = [[504, 235], [730, 235], [960, 235], [1190, 235], [1408, 235],[504,465],[730, 465], [960, 465], [1190, 465], [1408, 465],[504, 695], [730, 695],[960, 695], [1190, 695],[1408, 695], [504, 925],[730, 925], [960, 925],[1190, 925], [1408, 925]]

    open_chrome()
    time.sleep(2)
     
    select()
    time.sleep(3)
    start()
    time.sleep(5)
    n = ab.pixel(591,115)
    if(n == (194,119,90)):
        play(b,(600,115,700,935),2,1403,269)
        for i in [Btc,Eth,Bnb,Sol,Xrp,Lrt,Ltc,Dog,Pol,Pin]:
                                if(len(i) == 2):
                                    res(i,1404,269)
                                    time.sleep(1)
    elif(ab.pixel(430,179) != (40, 39, 47)):
            
                play(c,(491,118,924,932),7,1403,269)
                for i in [Btc,Eth,Bnb,Sol,Xrp,Lrt,Ltc,Dog,Pol,Pin]:
                                if(len(i) == 2):
                                    res(i,1404,269)
                                    time.sleep(1)

    else:
        
            play(e,(377,118,1154,915),7,1404,56)
            #time.sleep(1)
            for i in [Btc,Eth,Bnb,Sol,Xrp,Lrt,Ltc,Dog,Pol,Pin]:
                                if(len(i) == 2):
                                    res(i,1404,56)
                                    time.sleep(1)

    time.sleep(2)
    gain()
    time.sleep(8)
    goto()
    time.sleep(3)
    ab.click(113,20)
                    
if __name__ == "__main__" :
    main()
    
    
     
    
