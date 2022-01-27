import pyperclip
import time

list = [] # clipboard content
while True:
    if pyperclip.paste() != "None":
        value = pyperclip.paste()

        if value not in list:
            list.append(value)

        print(list)

        time.sleep(3)