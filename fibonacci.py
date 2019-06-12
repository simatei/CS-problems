def fib1(n: int) -> int:
    # base case
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

