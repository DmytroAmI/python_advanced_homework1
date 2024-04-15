def even_numbers(function):
    """Decorator that returns even numbers"""
    def decorated_func(*args, **kwargs):
        """Modified functions"""
        result = function(*args, **kwargs)
        return [number for number in result if number % 2 == 0]
    return decorated_func


@even_numbers
def fibonacci(n):
    """Return n first fibonacci numbers"""
    num2 = 1
    num_next = num2
    for i in range(1, n+1):
        yield num_next
        num1, num2 = num2, num_next
        num_next = num1 + num2


if __name__ == '__main__':
    print(list(fibonacci(20)))

