# Uses python3
import sys

def merge(l, r, middle):
    inversion_count = 0
    result = []
    l_i = 0
    r_i = 0
    while l_i < len(l) and r_i < len(r):
        if r[r_i] < l[l_i]:
            result.append(r[r_i])
            inversion_count += (middle - l_i)
            r_i += 1
        else:
            result.append(l[l_i])
            l_i += 1
    while l_i < len(l):
        result.append(l[l_i])
        l_i += 1
    while r_i < len(r):
        result.append(r[r_i])
        r_i += 1
    return (result, inversion_count)

def merge_sort_modified(a):
    if len(a) == 1:
        return (a, 0)
    middle = len(a) // 2
    l, l_inversion_count = merge_sort_modified(a[0 : middle])
    r, r_inversion_count = merge_sort_modified(a[middle : len(a)])
    result, inversion_count = merge(l, r, middle)
    return (result, inversion_count + l_inversion_count + r_inversion_count)

def get_inversion_count(a):
    sorted_a, inversion_count = merge_sort_modified(a)
    return inversion_count

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_inversion_count(a))
