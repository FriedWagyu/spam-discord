import pyautogui, time, random

time.sleep(10)
pyautogui.FAILSAFE = False

text = open("spam.txt", encoding = "utf-8")
msg = [x.strip('\n') for x in text]

while True:

    ran = random.randint(0, len(msg) - 1)
    randInt = random.randint(120, 180)
    randSec = randInt / 1000
    pyautogui.typewrite(msg[ran], randSec)
    time.sleep(randSec)
    pyautogui.press('enter')
    time.sleep(randInt)
