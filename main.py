import pyautogui
import random
import time
import string


def creat_random_str():
    length = random.randint(5, 20)
    sentence = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return sentence


def send_random_str():
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.typewrite(creat_random_str(), 1)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('enter')


def send_haha():
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.typewrite('haha', 1)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('enter')


def delete_last_message():
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')


def spam_message_loop():
    while True:
        wait_time = random.randint(240, 480)
        send_random_str()
        time.sleep(2)
        delete_last_message()
        time.sleep(wait_time)


def spam_haha_loop():
    while True:
        wait_time = random.randint(240, 480)//2
        send_haha()
        time.sleep(wait_time)
        delete_last_message()
        time.sleep(wait_time)


time.sleep(10)
pyautogui.FAILSAFE = False

# spam_message_loop()
spam_haha_loop()
