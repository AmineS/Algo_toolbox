# Uses python3
import sys

def optimal_summands(n):
  summands = []
  current_val = n
  if n == 1:
    summands.append(1)
  for i in range(1, n):
    if 2 * i < current_val:
      current_val -= i
      summands.append(i)
    else:
      summands.append(current_val)
      break
  return summands

if __name__ == '__main__':
  input = sys.stdin.read()
  n = int(input)
  summands = optimal_summands(n)
  print(len(summands))
  for x in summands:
    print(x, end=' ')
