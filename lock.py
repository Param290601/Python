import multiprocessing
import time

def deposit(balance,lock):
    for i in range(100):

        time.sleep(0.02)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.02)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":

    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    t1 = multiprocessing.Process(target = deposit,args=(balance,lock))
    t2 = multiprocessing.Process(target = withdraw,args=(balance,lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(balance.value)