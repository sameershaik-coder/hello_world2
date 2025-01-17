import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    print("am in thread 1")
    lock1.acquire()
    print("lock 1 acquried by thread 1")
    time.sleep(5)
    lock2.acquire()
    print("lock 2 acquried by thread 1")
    lock2.release()
    lock1.release()
    print("lock 1 released by thread 1")

def thread2():
    print("am in thread 2")
    lock1.acquire()
    print("lock 1 acquried by thread 2")
    time.sleep(5)
    lock1.release()
    print("lock 1 released by thread 2 ")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()