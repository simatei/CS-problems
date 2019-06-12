# Generates Fibonacci series to a given number of terms

def generate_sequence(terms):
    fib = [0, 1]
    while len(fib)< terms:
        next_no = fib[len(fib)-1] + fib[len(fib)-2]
        fib.append(next_no)
    return fib

