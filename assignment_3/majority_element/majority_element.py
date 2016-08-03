# Uses python3
import sys

def is_majority(a, left, right, candidate):
    if candidate == -1:
        return False
    else:
        return (int((right - left + 1) / 2) + 1) <= len(list(filter(lambda x: x == candidate, a[left : right + 1])))

def get_majority_element(a, left, right):
    if left > right:
        return -1
    elif left == right:
        return a[left]
    else:
        midpoint = left + int((right - left) / 2)
        candidate_1 = get_majority_element(a, midpoint + 1, right)
        candidate_2 = get_majority_element(a, left, midpoint)
        if is_majority(a, left, right, candidate_1):
            return candidate_1
        elif is_majority(a, left, right, candidate_2):
            return candidate_2
        else:
            return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
