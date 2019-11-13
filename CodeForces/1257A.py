# f = open('input', 'r')
results = []
for _ in range(int(input())):
    n, x, a, b = map(int, input().split(' '))
    a,b = min(a,b), max(a,b)
    dis = b-a
    if x > (a-1)+(n-b):
        results.append(n-1)
    else:
        results.append(dis+x)
for i in results:
    print(i)
