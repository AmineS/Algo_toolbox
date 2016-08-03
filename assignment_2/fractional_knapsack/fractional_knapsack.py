# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
  value = 0
  vws = list(zip(values, weights))
  vws.sort(key = lambda vw: vw[0] / float(vw[1]), reverse = True)
  for vw in vws:
    if capacity >= vw[1]:
      capacity -= vw[1]
      value += vw[0]
    else:
      value += capacity * vw[0] / float(vw[1])
      break
  return value

if __name__ == "__main__":
  data = list(map(int, sys.stdin.read().split()))
  n, capacity = data[0:2]
  values = data[2:(2 * n + 2):2]
  weights = data[3:(2 * n + 2):2]
  opt_value = get_optimal_value(capacity, weights, values)
  print("{:.10f}".format(opt_value))
