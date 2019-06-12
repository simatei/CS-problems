# Fibonacci with automatic memoization

from functools import lru_cache

@lru_cache(maxsize = None)
def fib3(n: int) -> int:
    # base case
    if n < 2:
        return n
    return fib3(n-1) + fib3(n-2)

