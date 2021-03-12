"""
simple example of Python decorator usage.
1. how the decorator implemented
2. how to measure the execution speed of two different functions.
"""

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    # call a function within a function

    def wrapper_function():
        # calculate the starting time before call the function
        start_time = time.time()

        function()

        # calculate the end time after the function completed
        end_time = time.time()

        # get the function name from the function that uses this decorator
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    # return this inner function and let the function uses this decorator to run it
    return wrapper_function


@speed_calc_decorator
def ten_million_loop_function():
    for i in range(10_000_000):
        i *= i


@speed_calc_decorator
def hundred_million_loop_function():
    for i in range(100_000_000):
        i *= i


ten_million_loop_function()
hundred_million_loop_function()
