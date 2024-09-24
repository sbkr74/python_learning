import keyboard

def print_pressed_keys(e):
    print(e.name)

# This will print the name of any key you press
keyboard.on_press(print_pressed_keys)

# Keep the program running to capture the key presses
keyboard.wait('esc')  # Press 'esc' to stop the program
