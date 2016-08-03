# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

max_val_index = -1
for i in range(0, n):
	if (max_val_index == -1) or (a[max_val_index] < a[i]):
		max_val_index = i

second_max_val_index = -1
for i in range(0, n):
	if (i != max_val_index) and ((second_max_val_index == -1) or (a[second_max_val_index] < a[i])):
		second_max_val_index = i

result = a[max_val_index] * a[second_max_val_index]

print(result)
