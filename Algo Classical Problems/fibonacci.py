"""Fibonacci series is a series of numbers following a simple pattern where each number is a sum of
two preceding numbers

0 1 1 2 3 5 8 13 21

The series is a common pattern observed in nature, ex: Arrangement of sunflower seeds in the flower
"""
from typing import Dict, Generator
from functools import lru_cache

# custom exception to not compute fib series for less than 0


class NegativeNumberError(Exception):
    pass


def fib_recursion(n: int) -> int:
    """Calculating fib using plain recursion"""

    # base case
    if n in {0, 1}:
        return n
    elif n < 0:
        raise NegativeNumberError
    else:
        # its the sum of prev two results
        return fib_recursion(n-1) + fib_recursion(n-2)


fib_table: Dict[int, int] = {0: 0, 1: 1}


def fib_from_table(n: int) -> int:
    """Calculating fib series using memoization"""
    if n in fib_table:
        return fib_table[n]
    else:
        fib_table[n] = fib_from_table(n-1) + fib_from_table(n-2)
        return fib_table[n]


@lru_cache(maxsize=None)
def fib_memoization(n: int) -> int:
    """Calculate fib series using builtin python memoization function"""
    if n in {0, 1}:
        return n
    elif n < 0:
        raise NegativeNumberError
    else:
        return fib_memoization(n-1) + fib_memoization(n-2)


def fib_iteration(n: int) -> int:
    """Calculate fib using iterative method
    Any problem that can be solved with recursion can be solved with iterative methods
    """
    if n in {0, 1}:
        return n
    elif n < 0:
        raise NegativeNumberError
    else:
        prev, curr = 0, 1
        for _ in range(1, n):
            prev, curr = curr, curr + prev
        return curr


def fib_generator(n: int) -> Generator(int, None, None):
    """Calculate fib using python generators"""
    if n in {0, 1}:
        yield n
    elif n < 0:
        raise NegativeNumberError
    else:
        prev, curr = 0, 1
        for _ in range(1, n):
            prev, curr = prev, prev + curr
            yield curr
