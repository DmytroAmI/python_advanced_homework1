import time


def timing(func):
    """Decorator who measures the time of the function"""
    def decorated_func(*args, **kwargs):
        """Modified functions"""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('func:%r args:[%r, %r], execution time: %2.4f sec' %
              (func.__name__, args, kwargs, end_time - start_time))
        return result
    return decorated_func


@timing
def even_nums(n):
    """Return even numbers from sequence"""
    return [even for even in range(1, n + 1) if even % 2 == 0]


if __name__ == '__main__':
    even_nums(1000)
    even_nums(10000)
    even_nums(100000)
    even_nums(10000000)
