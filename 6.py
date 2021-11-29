import pyautogui
import keyboard as kb

def quick_scroll():
    while 1:
        kb.wait('ctrl+u')
        
        while 1:
            pyautogui.scroll(500)
            if kb.is_pressed('space'):
                break
            if kb.is_pressed('q') and kb.is_pressed('alt'):
                break    
        if kb.is_pressed('q') and kb.is_pressed('ctrl'):
            break
##        if kb.is_pressed('ctrl') and kb.is_pressed('down'):
##                        while 1:
##                                pyautogui.scroll(-500)
##                                if kb.is_pressed('up'):
##                                        break
if __name__=='__main__':
    print("Ctrl+u快速上滑，空格停止，alt+q退出程序")
    quick_scroll()
    
