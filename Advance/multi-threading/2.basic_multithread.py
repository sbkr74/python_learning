from threading import Thread

def printnum():
    for i in range(100):
        print(i,end=" ")

def printalpha():
    for i in range(65,126):
        print(chr(i),end=" ")

# creating thread
thread1 = Thread(target=printnum)
thread2 = Thread(target=printalpha)

# starting thread
thread1.start()
thread2.start()

# waiting to finish threads
thread1.join()
thread2.join()

print("\nBoth threads are finished")
