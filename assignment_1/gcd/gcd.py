# Uses python3
import sys

def gcd(a, b):
  while b != 0:
    t = b
    b = a % b
    a = t
  return a

if __name__ == "__main__":
  input = sys.stdin.read()
  a, b = map(int, input.split())
  print(gcd(a, b))
