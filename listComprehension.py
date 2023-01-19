import time
# list = [[i for i in range(3)]for j in range(4)]
# print(list)
bc = [[i for i in range(3)] for j in range(5)]
print(bc)
char = [c for c in 'param']
print(char)

a = []
def loop(n):
    for i in range(n):
        a.append(i**2)

def comprehension(n):
    return [j**2 for j in range(n) ]

begin = time.time()
loop(10**6)
end = time.time()
print("time taken for loop",round(end-begin,2))


b = time.time()
comprehension(10**6)
e = time.time()
print("time taken for comprehension",round(e-b,2))
# print("heloo",end=' ')
# print()
# print("world")

# matrix = []
 
# for i in range(3):
 
    # Append an empty sublist inside the list
#     matrix.append([])
 
#     for j in range(5):
#         matrix[i].append(j)
 
# print(matrix)

# numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
numbers = list(map(lambda i: i*10, [1,2,3]))
 
print(numbers)

lis = [("even number: ", i) if i%2==0 else ("odd number: ",i) for i in range(8)]
print(lis)

# List = [string[::-1] for string in ('Geek','for')]
 
# Display list
# print(List)

# s = "param"
# print(s[::-1])

# Initializing string
string = 'Geeks4Geeks'

# Toggle case of each character
List = list(map(lambda i: chr(ord(i) ^ 32), string))

# Display list
print(List)


# numbers = [23,4,57,91,96,55]

# def digitsum(n):
#     dsum=0
#     for i in str(n):
#         dsum+=int(i)
#     return dsum

# sumsu = [digitsum(i) for i in numbers if i & 1]
# print(sumsu)