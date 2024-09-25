import threading

def task():
    print("Daemon thread running")

# Create a thread and set it as a daemon
thread = threading.Thread(target=task)
thread.setDaemon(True)

# Start the thread
thread.start()

print("\nMain program finished")
