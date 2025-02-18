# 定义一个函数，计算斐波那契数列的第n项
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(40))

from functools import lru_cache


@lru_cache()
def fib2(n):
    if n < 2:
        return n
    else:
        return fib2(n - 1) + fib2(n - 2)


print(fib2(40))
# functools.cache()
