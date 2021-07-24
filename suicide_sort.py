#Suicide Sort Algorithm
#https://github.com/pel-ex

import random
import time
import sys
import string

list = [4, 5, 3, 1, 2]
letters = string.ascii_lowercase
n=10

print("Your list:", list)

time.sleep(3)

print("Ok, I will now sort the array")
for i in range(n):
    print ( ''.join(random.choice(letters) for i in range(10)) )
    time.sleep(0.5)
    i=i+1


random.shuffle(list)
print("My result is:", list)
time.sleep(1.5)


if list == [1, 2, 3, 4, 5]:
    print("Nice, all sorted!")
else:
    print("oh... ok, i guess")
    time.sleep(3)
    sys.exit('Let me die in peace')
