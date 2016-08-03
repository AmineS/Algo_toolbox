# Uses python3

def edit_distance(s, t):
  s_length = len(s) + 1
  t_length = len(t) + 1

  edit_distance = [[None] * t_length for i in range(s_length)]

  for i in range(s_length): 
    edit_distance[i][0] = i

  for i in range(t_length):
    edit_distance[0][i] = i

  for i in range(1, s_length):
   for j in range(1, t_length):
    insertion = edit_distance[i][j - 1] + 1
    deletion = edit_distance[i - 1][j] + 1
    if s[i - 1] == t[j - 1]:
      edit_distance[i][j] = min(insertion, deletion, edit_distance[i - 1][j - 1])
    else:
      edit_distance[i][j] = min(insertion, deletion, edit_distance[i - 1][j - 1] + 1)
  return edit_distance[len(s)][len(t)]

if __name__ == "__main__":
  print(edit_distance(input(), input()))
