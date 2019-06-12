# Calculate fibonacci utilizing memoization.

from typing import Dict

# Base cases
memo: Dict[int, int] = {0:0, 1:1}

def fib2(n: int) -> int:
    if n not in memo:
        # memoization
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]


