import bot3x
import bot2
import pyautogui as ab
import botx
import time
import importlib
import botx
#import tkpro

#x1,x2,x3,y = ('True','True','True',2)
def main(x1,x2,x3,y):
    for i in range(y):

        if(x1 == 'True'):
            try:
                importlib.reload(bot2)
                bot2.main()
                #x = time.time()
            except:
                importlib.reload(bot2)
                bot2.main()
                #x = time.time()
        if(x2 == 'True'):
            try:
                importlib.reload(bot3x)
                bot3x.main()
                
            except:
                ab.press('esc')
                importlib.reload(bot3x)
                bot3x.main()
        if(x3 == 'True'):
            try:
                importlib.reload(botx)
                botx.main()
                
            except:
                ab.press('esc')
                importlib.reload(botx)
                botx.main() 
        print(i)
            
if __name__ == '__main__':
    main('True','True','True',2)