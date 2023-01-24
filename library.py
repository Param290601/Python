import os
import sys
import glob
import random
import statistics
import math

# zlib library...
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

# date
from datetime import date
now = date.today()
now
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days

# math
math.cos(math.pi / 4)
math.log(1024, 2)

# statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)

# glob
print(glob.glob('*.py'))
# os
print(os.getcwd())      # Return the current working directory

os.system('mkdir abc')   # Run the command mkdir in the system shell


help(os)