# Big Oh

# O(x^2)
# O(2^x) + O(1000000)
# O(2^x)


# Time complexity

# [start, end)


def sum_n(n: int) -> int:
    s = 0  # O(1)
    for i in range(1, n + 1):  # O(n)
        s += i  # O(1)

    return s  # O(1)


# O(1) + (O(n) * O(1)) + O(1)
# O(1) + O(n) + O(1)
# O(n)


# (O(n) * (O(n) * O(1)))
# O(n^2)
def nested(n):
    for i in range(n):
        for j in range(n):
            print("hi")


# Multiple variables


def do_something(n: int, m: int):
    for x in range(n):  # O(n)
        pass  # O(1)
    for y in range(m):  # O(m)
        pass  # O(1)


def do_something_2(n: int, m: int):
    for x in range(max(n, m)):
        pass


# O(n + m)


def nested_2(n: int):
    for i in range(n):  # O(n)
        for j in range(i, n):  # O(n)
            print(f"({i=} {j=})", end="")  # O(1)
        print()  # O(1)


#  n + (n-1) + (n-2) + 1 + 0
#  (n * (n+1)) /2
#  n * (n)


def while_loop(n: int):
    while n > 1:
        print(n)  # O(1)
        n = n // 2  # O(1)


# O(log(n))

# O(n^2)
nested_2(5)

from functools import lru_cache
import time


# fib_cache = {}


# @lru_cache(maxsize=4)
def fib(n: int) -> int:
    if n < 1:
        return 1
    # elif n in fib_cache:
    #     return fib_cache[n]
    else:
        res = fib(n - 1) + fib(n - 2)
        # fib_cache[n] = res
        return res


# mathematical recursive runtime

# T(n) = T(n - 1) + T(n -2)
# to be continued...

# for i in range(100):
# t1 = time.time()
# print(fib(100))
# print(time.time() - t1)


# 1, 2, ~4, ~8

# O(2^n)

# print(sum_n(10))


# Space/Memory complexity


x = 5


def foo(n: int):
    l = []
    for i in range(n):
        l.append(i)
    return l
