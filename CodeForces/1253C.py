# f = open('input', 'r')

# n, m = map(int, f.readline().split())
n, m = map(int, input().split())
# a = [0] + sorted(map(int, f.readline().split()))
a = [0] + sorted(map(int, input().split()))

x = [0] * m
s = 0
ans = [0] * n

for i in range(1, n+1):
    x[i%m] += a[i]
    s += x[i%m]
    ans[i-1] = s

print(*ans)
