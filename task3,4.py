from functools import lru_cache
from task2 import timing


def fibonacci_by_inx1(index):
    """Return fibonacci number by index"""
    if index < 0:
        return 1
    else:
        return fibonacci_by_inx1(index - 1) + fibonacci_by_inx1(index - 2)


@timing
def fibonacci1(n=25):
    """Return first n fibonacci numbers"""
    for i in range(1, n + 1):
        print(fibonacci_by_inx1(i))


@lru_cache(maxsize=None)
def fibonacci_by_inx2(index):
    """Return fibonacci number by index, with lru_cache maxsize=None"""
    if index < 0:
        return 1
    else:
        return fibonacci_by_inx2(index - 1) + fibonacci_by_inx2(index - 2)


@timing
def fibonacci2(n=25):
    """Return first n fibonacci numbers"""
    for i in range(1, n + 1):
        print(fibonacci_by_inx2(i))


@lru_cache(maxsize=10)
def fibonacci_by_inx3(index):
    """Return fibonacci number by index, with lru_cache maxsize=10"""
    if index < 0:
        return 1
    else:
        return fibonacci_by_inx3(index - 1) + fibonacci_by_inx3(index - 2)


@timing
def fibonacci3(n=25):
    """Return first n fibonacci numbers"""
    for i in range(1, n + 1):
        print(fibonacci_by_inx2(i))


@lru_cache(maxsize=16)
def fibonacci_by_inx4(index):
    """Return fibonacci number by index, with lru_cache maxsize=16"""
    if index < 0:
        return 1
    else:
        return fibonacci_by_inx4(index - 1) + fibonacci_by_inx4(index - 2)


@timing
def fibonacci4(n=25):
    """Return first n fibonacci numbers"""
    for i in range(1, n + 1):
        print(fibonacci_by_inx3(i))


if __name__ == '__main__':
    fibonacci1()
    fibonacci2()
    fibonacci3()
    fibonacci4()
