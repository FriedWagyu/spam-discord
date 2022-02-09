import pyautogui
import random
import time
import string


def creat_random_str():
    length = random.randint(1, 4)
    sentence = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return sentence


def send_str(str_to_send):
    pyautogui.press('space')
    time.sleep(0.1)
    pyautogui.typewrite(str_to_send, 0.1)
    time.sleep(0.1)
    pyautogui.press('space')
    time.sleep(0.1)
    pyautogui.press('space')
    time.sleep(0.1)
    pyautogui.press('enter')


def delete_last_message():
    pyautogui.press('up')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.press('backspace')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('enter')


def spam_message_loop():
    while True:
        wait_time = random.randint(60, 120)//2
        send_str(creat_random_str())
        time.sleep(wait_time)
        delete_last_message()
        time.sleep(wait_time)


def spam_message_loop_no_delete():
    while True:
        wait_time = random.randint(300, 600)
        send_str(creat_random_str())
        time.sleep(wait_time)


def spam_haha_loop():
    while True:
        wait_time = random.randint(60, 120)//2
        send_str('haha')
        time.sleep(wait_time)
        delete_last_message()
        time.sleep(wait_time)


def delete_all():
    while True:
        delete_last_message()


time.sleep(10)
pyautogui.FAILSAFE = True

spam_message_loop_no_delete()
#spam_message_loop()
# spam_haha_loop()
# delete_all()
