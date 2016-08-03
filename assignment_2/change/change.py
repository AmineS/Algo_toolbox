# Uses python3
import sys

def get_change(n):
  tens = int(n / 10)
  fives = int((n % 10) / 5)
  return tens + fives + n - (tens * 10 + fives * 5)

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(int(get_change(n)))
