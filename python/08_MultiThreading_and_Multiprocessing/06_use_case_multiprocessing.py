## For cpu bound tasks

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute the factorials of a given number

def compute_factorial(number):
    print(f"COmputing fatorial of {number}")
    result=math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]

    st_time = time.time()

    ## create a pool of worker processes

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time-st_time} seconds")