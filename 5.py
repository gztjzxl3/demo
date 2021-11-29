import keyboard as kb
import pyperclip
from allslib.get_time import get_now_time
import pyautogui
import time

file_path = input("请输入文件存储路径:\n")
##file_path = r'D:\Py_Files\命令行\test\5'
##file_name = None
file_name = input("输入文件名:  ")

file_name = file_name if file_name else f"{get_now_time()}.txt"
fp = open(f'{file_path}\\{file_name}', 'a', encoding='utf8')


def save_content():
    pyautogui.click(pyautogui.position(), clicks=2)
    pyautogui.hotkey('ctrl', 'c')
    print('copying')
    time.sleep(0.1)
    content = pyperclip.paste()
    fp.write(content + '\n')
    print(content)
    print(f'saved in [{file_path}\{file_name}] at [{get_now_time()}]')

if __name__ == '__main__':
    print('ctrl to copy and save, alt+q to quit.')
##    while True:
    try:
        kb.add_hotkey('ctrl', save_content)
##        break
    except KeyboardInterrupt as e:
        print(e)
    finally:
        kb.wait('alt+q')
        fp.close()
    print('ending...')
