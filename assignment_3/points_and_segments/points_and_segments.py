# Uses python3
import sys

# Memory hog!
def fast_count_segments_mem_hog(starts, ends, points):
    cnt = [0] * len(points)
    counts = {}
    for i in range(len(starts)):
        for j in range(starts[i], ends[i] + 1):
            if j in counts:
                counts[j] += 1
            else:
                counts[j] = 1
    for i in range(len(points)):
        if points[i] in counts:
            cnt[i] = counts[points[i]]
        else:
            cnt[i] = 0
    return cnt

def fast_count_segments(starts, end, points):
    cnt = [0] * len(points)
    segments = list(zip(starts, end))
    segments.sort(key = lambda tup: tup[0])
    for i in range(len(points)):
        for j in range(len(segments)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
            elif starts[j] > points[i]:
                break
    return cnt
            

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
