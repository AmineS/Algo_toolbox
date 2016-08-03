# Uses python3
import sys

def get_fibonacci_last_digit(n):
  fib_vals = {}
  fib_vals[0] = 0
  fib_vals[1] = 1
  for i in range(2, n + 1):
    fib_vals[i] = (fib_vals[i - 1] + fib_vals[i - 2]) % 10
  return fib_vals[n]

if __name__ == '__main__':
  input = sys.stdin.read()
  n = int(input)
  print(get_fibonacci_last_digit(n))
