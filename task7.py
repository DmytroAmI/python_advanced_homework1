def multiple(x, y):
    """Ordinary multiplication"""
    return x * y


def curried_multiple(x):
    """Curried multiplication"""
    def second_value(y):
        """Multiplication with second value"""
        return x * y
    return second_value


if __name__ == '__main__':
    print(multiple(3, 4))
    print(curried_multiple(3)(4))

    multi_by_two = curried_multiple(2)
    print(multi_by_two(2))
    print(multi_by_two(3))
    print(multi_by_two(4))
