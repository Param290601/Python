import time
import multiprocessing
def square(numbers,queue):
    for n in numbers:
        queue.put(n*n)

if __name__ == "__main__":

    arr = [2,3,4,5]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target = square, args = (arr,q))
    p1.start()
    p1.join()
    
    while q.empty() is False:
        print(q.get())
    

