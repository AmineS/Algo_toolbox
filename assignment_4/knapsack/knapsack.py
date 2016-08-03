# Uses python3
import sys

def optimal_weight(W, w):
  # write your code here
  result = 0
  for x in w:
      if result + x <= W:
        result = result + x
  return result

def print_matrix(m):
  for row_id in range(len(m)):
    print(' '.join(map(str, m[row_id])))

def optimal_weight_dp(W, w):
  item_count = len(w) + 1
  weight_count = W + 1
  value = [[None] * item_count for i in range(weight_count)]

  # First col and row are set to 0 - no weight or no item
  for i in range(weight_count): 
    value[i][0] = 0
  value[0] = [0] * item_count

  for w_inter in range(1, weight_count):
    for i in range(1, item_count):
      take, leave = (-sys.maxsize, -sys.maxsize)
      weight_index = i - 1
      if w_inter >= w[i - 1]:
        take = value[w_inter - w[weight_index]][i - 1] + w[weight_index]
      leave = value[w_inter][i - 1]
      value[w_inter][i] = max(take, leave)

  return value[W][len(w)]

if __name__ == '__main__':
  input = sys.stdin.read()
  W, n, *w = list(map(int, input.split()))
  print(optimal_weight_dp(W, w))