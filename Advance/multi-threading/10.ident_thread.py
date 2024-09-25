import threading

def task():
    print(f"Thread ID: {threading.current_thread().ident}")

# Create and start the thread
thread = threading.Thread(target=task)
thread.start()

# Get the thread's identifier
print(f"\nMain thread ID: {thread.ident}")
