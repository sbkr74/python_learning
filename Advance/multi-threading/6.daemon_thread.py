import threading
import time

def task():
    while True:
        print("Daemon thread running")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=task)
daemon_thread.daemon = True  # Make it a daemon thread

# Start the daemon thread
daemon_thread.start()

time.sleep(3)
print("Main program exits, daemon thread will also stop")
