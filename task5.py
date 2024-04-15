def squares_of_odd_numbers(numbers):
    """Return squares of odd numbers"""
    return [lambda x=number: x * x for number in numbers if number % 2 != 0]


if __name__ == '__main__':
    nums = [n for n in range(1, 11)]
    print(nums)

    print([f() for f in squares_of_odd_numbers(nums)])
