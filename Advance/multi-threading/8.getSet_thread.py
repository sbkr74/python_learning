'''
getName() was used to fetch name of thread i.e Thread-1 and so on in default case.
setName() was used to set name of thread from default to any custom name.

Now these are deprecated and only name is used for getting name of thread as well set name of thread
example:
thread.name : To fetch name 
thread.name = "custom naming" : To set name

See 9.name_thread.py for better understanding.
'''
import threading

def task():
    print(f"Thread name: {threading.current_thread().getName()}")

# Create a thread
thread = threading.Thread(target=task)

# Set a custom name for the thread
thread.setName("MyCustomThread")

# Start the thread
thread.start()

# Get the name of the thread
print(f"Main Thread name: {thread.getName()}")


