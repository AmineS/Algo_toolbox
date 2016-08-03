# Uses python3
import sys
import time

DIV_2 = 'DIV_2'
DIV_3 = 'DIV_3'
DIFF_1 = 'DIFF_1'
NO_OP = 'NO_OP'

def optimal_sequence(n):
  sequence = []
  while n >= 1:
    sequence.append(n)
    if n % 3 == 0:
      n = n // 3
    elif n % 2 == 0:
      n = n // 2
    else:
      n = n - 1
  return reversed(sequence)

def optimal_sequence_dp(n):
  min_ops = [(sys.maxsize, NO_OP)] * (n + 1)

  min_ops[0] = (0, NO_OP) # Should not have to use this value
  min_ops[1] = (0, NO_OP)

  for i in range(2, n + 1):
    div_by_2 = (sys.maxsize, NO_OP)
    div_by_3 = (sys.maxsize, NO_OP)
    diff_1 = (sys.maxsize, NO_OP)

    if i % 2 == 0:
        div_by_2 = (min_ops[i // 2][0] + 1, DIV_2)
    if i % 3 == 0:
        div_by_3 = (min_ops[i // 3][0] + 1, DIV_3)
    diff_1 = (min_ops[i - 1][0] + 1, DIFF_1)

    min_ops[i] = min([div_by_2, div_by_3, diff_1], key = lambda x: x[0])
  
  i = n
  intermidiate_values = []
  while min_ops[i][0] > 0:
    intermidiate_values.append(i)
    if min_ops[i][1] == DIV_2:
        i = i // 2
    elif min_ops[i][1] == DIV_3:
        i = i // 3
    else:
        i = i - 1
  intermidiate_values.append(1)
  intermidiate_values.reverse()

  return (min_ops[n][0], intermidiate_values)


input = sys.stdin.read()
n = int(input)
result = optimal_sequence_dp(n)
print(result[0])
print(' '.join(map(str, result[1])))