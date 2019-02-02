# 指在大于1的自然数中,除了1和该数自身外,无法被其他自然数整处的数.大于1的自然数若不是质数,即称之为合数.
# 编程思路:对正整数N,如果用2到根号n的所有整数去除,均无法整除,则n为质数

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for i in range(2, 1000):
    if is_prime(i):
        print(i)
