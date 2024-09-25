import threading

class MyThread(threading.Thread):
    def run(self):
        print("Custom thread running")

# Create and start the custom thread
thread = MyThread()
thread.start()
