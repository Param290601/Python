import time
import multiprocessing
def square(numbers):
    for i in numbers:
        time.sleep(5)
        print("square", i*i)

def cube(numbers):
    for i in numbers:
        time.sleep(5)
        print("cube", i*i*i)

if __name__ == "__main__":        

    arr = [2,3,4,5]
    # t= time.time()
    # square(arr)
    # cube(arr)
    p1 = multiprocessing.Process(target = square, args = (arr,))
    p2 = multiprocessing.Process(target = cube, args = (arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    

