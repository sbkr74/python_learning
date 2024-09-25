import threading

def task():
    print("Task is running in thread...")

thread = threading.Thread(target=task)
thread.start()

print("Program execution complete.")
