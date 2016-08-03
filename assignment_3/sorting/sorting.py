# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    beg_x = l
    end_x = l
    for i in range(l + 1, r + 1):
        if a[i] == x:
            a[end_x + 1], a[i] = a[i], a[end_x + 1]
            end_x += 1
        elif a[i] < x:
            while i > beg_x:
                a[i], a[i - 1] = a[i - 1], a[i]
                i -= 1
            beg_x += 1
            end_x += 1
    return (beg_x, end_x)

def partition3_2(a, l, r):
    x = a[l]
    counts = {'lower': 0, 'equal': 1, 'greater': 0}
    for i in range(l + 1, r + 1):
        if a[i] == x:
            counts['equal'] += 1
        elif a[i] > x:
            counts['greater'] += 1
        else:
            counts['lower'] += 1
    lower_ptr = l
    equal_ptr = l + counts['lower']
    greater_ptr = l + counts['lower'] + counts['equal']
    for i in range(l + 1, r + 1):
        if a[i] == x:
            a[i], a[equal_ptr] = a[equal_ptr], a[i]
            equal_ptr += 1
        elif a[i] > x:
            a[i], a[greater_ptr] = a[greater_ptr], a[i]
            greater_ptr += 1
        else:
            a[i], a[lower_ptr] = a[lower_ptr], a[i]
            lower_ptr += 1

    return (l + counts['lower'], l + counts['lower'] + counts['equal'])


def partition3_3(a, l, r):
    x = a[l]
    m2 = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
    a[l], a[m2] = a[m2], a[l]
    x = a[m2]
    m1 = m2 - 1
    for i in range(l, m2):
        if a[i] == x:
            while a[m1] == x and m1 > l:
                m1 -= 1
            a[m1], a[i] = a[m1], a[i]
    return (m1, m2)


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3_3(a, l, r)
    randomized_quick_sort(a, l, m1);
    randomized_quick_sort(a, m2 + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
