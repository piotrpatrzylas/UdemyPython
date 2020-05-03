# problem 1
def gensquares(number):
    for i in range(number):
        yield i*i

for x in gensquares(10):
    print(x)

#problem 2
from random import randint

def rand_num(low, high, n):
    for i in range(n):
        yield randint(low, high)

for i in rand_num(1, 10, 5):
    print(i)

#problem 3
s = "string"
s_iter = iter(s)
print(next(s_iter))