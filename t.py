#get now-time
##import time 
import datetime as dt
import pyperclip as  p
import keyboard as kb
def start():
    try:
        kb.wait('ctrl+v')
        t = dt.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        res1 =p.copy(t)
        p.paste()
    except Exception as e :
        print(e)

while True:
        start()        

        
