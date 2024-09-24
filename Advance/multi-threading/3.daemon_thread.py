import sys
from threading import Thread

def printnum():
    for i in range(100):
        print(i, end=" ")

def printalpha():
    for i in range(65, 126):
        print(chr(i), end=" ")

# creating thread
thread1 = Thread(target=printnum)
thread2 = Thread(target=printalpha)

# Set threads as daemon so they terminate with the main program
thread1.daemon = True
thread2.daemon = True

# starting thread
thread1.start()
thread2.start()

# Main program execution
print("\nprogram executed completely")
sys.exit()  # This will exit the program, terminating the daemon threads
