import math

def getInput(fromFile=False):
    if fromFile:
        f = open('input', 'r')
        return lambda :f.readline()[:-1]
    return input


def main(fromFile = False):
    inp = getInput(fromFile)

    result = []

    inp()
    a = list(map(int, inp().split(' ')))
    check = [0] * (len(a)-1)

    for i in range(len(a)-1):
        check[i] = math.gcd(a[i], a[i+1]) == 1

    for i in range(len(a)-1):
        pass

    return result


print(main(fromFile=True))
