import threading
import time

def task():
    time.sleep(2)
    print("Thread finished")

# Create and start the thread
thread = threading.Thread(target=task)
thread.start()

# Check if the thread is still alive
print(f"Is thread alive? {thread.is_alive()}")

# Wait for thread to finish
thread.join()

# Check again
print(f"Is thread alive? {thread.is_alive()}")
