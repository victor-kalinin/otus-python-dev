from time import time
from functools import wraps


"""
Create a decorator to measure the time of the function
"""
def count_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_before_start = time()
        result = func(*args, **kwargs)
        print(f'Func {func} working time is:', time() - time_before_start)
        return result
    return wrapper


"""
Write a function that takes N integers and returns a list of squares of those integers. 
A bonus would be to make a keyword argument to select the degree to which the numbers will be raised
"""
@count_time
def power_up(*args, level=2):
    return list(map(lambda x: x ** level, args))


"""
Write a function that takes a list of integers as input, and returns only 
even/odd/prime numbers (the choice is made by passing an additional argument)
"""
def is_prime_number(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


@count_time
def filter_num(nums=None, t=None):
    if any([nums is None, not nums, t is None, t not in (0, 1, 2)]):
        return 'Wrong args'
    if t == 2:
        return list(filter(is_prime_number, nums))
    else:
        return list(filter(lambda x: x % 2 == t, nums))

    
if __name__ == '__main__':
    print(power_up(*range(10)), end='\n\n')
    print(filter_num(range(500), t=2))
