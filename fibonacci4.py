# Generating Fibonacci with a generator

from typing import Generator

def fib4(n: int) -> Generator[int, None, None]:
   # Special cases
    yield 0 
    if n > 0 : yield 1

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last+next
        yield next # main generation step

if __name__ == "__main__":
    seq = []
    for i in fib4(5):
        print(i)
    
