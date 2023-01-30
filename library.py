# import os
# import sys
# import glob
# import random
# import statistics
# import math

# # zlib library...
# import zlib
# s = b'witch which has which witches wrist watch'
# len(s)

# t = zlib.compress(s)
# len(t)
# zlib.decompress(t)

# # date
# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# # dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age)
# age.days

# # math
# print(math.cos(math.pi / 4))
# print(math.log(1024, 2))

# # statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# # random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.sample(range(100), 10))   # sampling without replacement
# print(random.random())    # random float
# print(random.randrange(6))    # random integer chosen from range(6)

# # glob
# print(glob.glob('*.py'))
# # os
# print(os.getcwd())      # Return the current working directory

# os.system('mkdir abc')   # Run the command mkdir in the system shell
from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b = b,a', 'a=1; b=2').timeit())
# help(os)