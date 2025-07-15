'''
Write a decorator that calculates the execution time of a function and displays it after the function is executed. Then, use this decorator for a function that creates a list from 1 to n.

Input:
The number n that specifies the size of the list.

Output:
The function's return value (list 1 to n)
The execution time of the function in seconds
'''

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def create_list(n):
    return list(range(1, n + 1))

# Example usage:
n = int(input("Enter the size of the list: "))
result = create_list(n)
print(result)
