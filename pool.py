from multiprocessing import Pool
import time

def addition(x):
    sum =0
    for i in range(1000):
        sum += i*i
    return sum

if __name__ == "__main__":

    t1 = time.time()
    p  = Pool()
    result = p.map(addition,range(100000))
    p.close()
    p.join()

    print("pool time",time.time() - t1)
    
    t2=time.time()
    result = []
    for i in range(100000):
        result.append(addition(i))

    print("noraml time", time.time()- t2)
