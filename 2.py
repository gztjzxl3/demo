import keyboard as kb
import datetime as dt
from PIL import ImageGrab
##import subprocess
import pygame
pygame.mixer.init()
pygame.mixer.music.load(r'D:\Py_Files\命令行\stone4.ogg')
pygame.mixer.music.set_volume(50)
##import pygame
##pygame.mixer.init()
##pygame.mixer.music.load(r'D:\Py_Files\命令行\stone4.ogg')


##def ctrl_vol(volume=30):
##    while 1:
##        try:
##            pygame.mixer.music.set_volume(volume)
##            print("now volume=",volume)
####            print("ctrl+up to turn volum up, ctrl+down to lower it.")
##            kb.wait(hotkey="ctrl+up")
##            volume +=5
##            pygame.mixer.music.set_volume(volume)
##            print("now volume=",volume)
##            print('up')
##            pygame.mixer.music.play()
##        except Exception as e:
##            print(e)
    
time = dt.datetime.now().strftime('%Y-%m-%d_%H%M%S')
def f1():
##    ctrl_vol(
    path = input("Enter path to save:\n")
    print("Ctrl+l to start,then ctrl+g to get picture, ctrl+v to save")
    while 1:
        kb.wait(hotkey = 'ctrl+l')
        print('Start')
        start(path)
    
def start(path):
    i=1
    while 1:
        try:
            kb.wait(hotkey = 'ctrl + g')
            time = dt.datetime.now().strftime('%Y-%m-%d_%H%M%S')
            kb.wait(hotkey = 'ctrl+v')
            i+=1
            image = ImageGrab.grabclipboard()
            image.save(path+rf'\{time}.png')
##            print(image)
            print("Img",i)
            
##            subprocess.Popen(['start','stone4.ogg'],shell=True)
            pygame.mixer.music.play()
            


        except OSError as e:
            print(e)
            start(path)

        except AttributeError as e:
            print(e)
            start(path)

        
if __name__ == '__main__':
    f1()
##    ctrl_vol()
