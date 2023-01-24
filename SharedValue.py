import time
import multiprocessing
def square(numbers,result,v):
    v.value = 5
    for idx, n in enumerate(numbers):
        result[idx] = n*n

# def cube(numbers):
#     for i in numbers:
#         time.sleep(5)
#         print("cube", i*i*i)

if __name__ == "__main__":

    arr = [2,3,4,5]
    r = multiprocessing.Array('i',4)
    v = multiprocessing.Value('i',0)
    # t= time.time()
    # square(arr)
    # cube(arr)
    p1 = multiprocessing.Process(target = square, args = (arr,r,v))
    # p2 = multiprocessing.Process(target = cube, args = (arr,))

    p1.start()

    p1.join()
    print(v.value)
    print(r[:])
    

