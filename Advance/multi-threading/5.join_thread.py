import threading
import time

def task():
    print("Task started in Thread")
    time.sleep(2)
    print("Thread finished")

# Create and start the thread
thread = threading.Thread(target=task)
thread.start()

# Wait for the thread to complete
thread.join()

print("Main thread finished waiting for the other thread")
