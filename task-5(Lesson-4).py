from functools import reduce

a = range(100, 1001, 2)


def my_func(last, _):
    return last * _


print(reduce(my_func, a))
