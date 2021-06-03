from time import time
from functools import wraps


"""
создать декоратор для замера времени выполнения функции
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
написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел. 
Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа
"""
@count_time
def power_up(*args, level=2):
    return list(map(lambda x: x ** level, args))


"""
написать функцию, которая на вход принимает список из целых чисел, и возвращает только 
чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента)
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
