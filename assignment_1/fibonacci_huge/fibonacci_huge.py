# Uses python3
import sys

def get_fibonaccihuge(n, m):
  if n < 3:
    return 1
  fib_vals = {}
  fib_vals[0] = 0
  fib_vals[1] = 1
  for i in range(2, sys.maxsize):
    fib_vals[i] = (fib_vals[i - 1] + fib_vals[i - 2]) % m
    if fib_vals[i] == fib_vals[0]:
      j = i - 1 # potential end of the period
      distance = i - 1
      while distance > 0:
        i = i + 1
        distance = distance - 1
        fib_vals[i] = (fib_vals[i - 1] + fib_vals[i - 2]) % m
        if fib_vals[i] != fib_vals[j - distance]:
          break
      if distance == 0:
        pisano_period = [v for k,v in fib_vals.items() if k <= j]
        return pisano_period[n % len(pisano_period)]

if __name__ == '__main__':
  input = sys.stdin.read();
  n, m = map(int, input.split())
  print(get_fibonaccihuge(n, m))
