import time
import threading
def square(numbers):
    for i in numbers:
        time.sleep(0.2)
        print("square", i*i)

def cube(numbers):
    for i in numbers:
        time.sleep(0.2)
        print("cube", i*i*i)

arr = [2,3,4,5]
t= time.time()
# square(arr)
# cube(arr)
t1 = threading.Thread(target = square, args = (arr,))
t2 = threading.Thread(target = square, args = (arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("time taken for the process" , time.time()-t)

