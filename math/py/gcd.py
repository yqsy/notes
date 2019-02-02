# 欧几里得算法(辗转相除法), 求最大公约数

def gcd(a, b):
     while b != 0:
        t = a % b
        a = b
        b = t
    return a

gcd(8,10)
