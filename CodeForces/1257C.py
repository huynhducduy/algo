# f = open('input', 'r')

import sys
results = []

# for _ in range(int(f.readline())):
for _ in range(int(input())):
    # n = int(f.readline())
    n = int(input())
    # a = list(map(int, f.readline()[:-1].split(' ')))
    a = list(map(int, input().split(' ')))
    a = [0] + a
    pos = [0 for _ in a]
    res = sys.maxsize
    for i in range(1,len(a)):
        if pos[a[i]] == 0:
            pos[a[i]] = i
            continue
        res = min(res, i-pos[a[i]]+1)
        pos[a[i]] = i
    if res == sys.maxsize:
        results.append(-1)
    else:
        results.append(res)
for i in results:
    print(i)
