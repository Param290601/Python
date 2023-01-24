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
t2 = threading.Thread(target = cube, args = (arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("time taken for the process" , time.time()-t)

# Python program to illustrate the concept
# of threading
# import threading
# import os

# def task1():
# 	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
# 	print("ID of process running task 1: {}".format(os.getpid()))

# def task2():
# 	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
# 	print("ID of process running task 2: {}".format(os.getpid()))

# if __name__ == "__main__":

# 	# print ID of current process
# 	print("ID of process running main program: {}".format(os.getpid()))

# 	# print name of main thread
# 	print("Main thread name: {}".format(threading.current_thread().name))

# 	# creating threads
# 	t1 = threading.Thread(target=task1, name='t1')
# 	t2 = threading.Thread(target=task2, name='t2')

# 	# starting threads
# 	t1.start()
# 	t2.start()

# 	# wait until all threads finish
# 	t1.join()
# 	t2.join()


