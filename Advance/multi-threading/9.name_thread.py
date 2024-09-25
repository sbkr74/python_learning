import threading

def task():
    print(f"Thread name: {threading.current_thread().name}")

# Create a thread
thread = threading.Thread(target=task)

# Start the thread
thread.start()

# Set a custom name for the thread
thread.name= "MyCustomThread"

# Get the name of the thread
print(f"\nMain Thread name: {thread.name}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import threading

def task():
    print(f"Thread name: {threading.current_thread().name}")

# Create a thread with a custom name
thread = threading.Thread(target=task, name="CustomThread")

# Start the thread
thread.start()

thread.name = "myCustomThread"
# Get the name of the thread
print(f"Thread name: {thread.name}")

