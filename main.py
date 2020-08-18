from pynput import keyboard
from pynput.keyboard import Controller
import time
import random

main = Controller()


def on_press(key):
    if key == keyboard.Key.space:
        main.press('1')
        main.release('1')
        time.sleep(random.uniform(0, 0.4))
        main.press('2')
        main.release('2')
        time.sleep(random.uniform(0, 0.4))
        main.press('3')
        main.release('3')
        time.sleep(random.uniform(0, 0.4))
        main.press('4')
        main.release('4')
        time.sleep(random.uniform(0, 0.4))
        main.press('5')
        main.release('5')
    elif key == keyboard.Key.esc:
        exit()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
