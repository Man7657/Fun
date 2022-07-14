import threading
import time


def even():
    for i in range(0,20,2):
        print(i)


def odd():
    for i in range(1,20,2):
        print(i)


thrd1 = threading.Thread(target=odd)
thrd2 = threading.Thread(target=even)

print("Start")

thrd1.start()

thrd2.start()

print("End")