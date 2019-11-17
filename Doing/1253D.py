# GOT TLE, but AC with C++

def getInput(fromFile=False):
    if fromFile:
        f = open('input', 'r')
        return lambda :f.readline()[:-1]
    return input


def main(fromFile = False):
    inp = getInput(fromFile)

    def find(u):
        pa[u] = u if pa[u]==u else find(pa[u])
        return pa[u]

    def merge(x,y):
        X, Y = find(x), find(y)
        X, Y = min(X,Y), max(X,Y)
        pa[X] = Y

    n, m = map(int, inp().split(' '))
    pa = [i for i in range(0, n+1)]

    for i in range(m):
        x, y = map(int, inp().split(' '))
        if find(x) != find(y):
            merge(x,y)

    ans = 0
    i = 1
    while (i <= n):
        j = i+1
        while (j <=find(i)):
            if find(i) != find(j):
                ans += 1
                merge(i,j)
            j += 1
        i = find(i)+1

    return ans


print(main(fromFile=False))
