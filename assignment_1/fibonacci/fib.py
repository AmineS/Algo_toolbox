# Uses python3

fib_vals = {}
def calc_fib(n):
    fib_vals[0] = 0
    fib_vals[1] = 1
    for i in range(2, n + 1):
        fib_vals[i] = fib_vals[i - 1] + fib_vals[i - 2]
    return fib_vals[n]

n = int(input())
print(calc_fib(n))
