import sys

def getInput(fromFile=False):
    if fromFile:
        f = open('input', 'r')
        return lambda :f.readline()[:-1]
    return input


def main(fromFile = False):
    inp = getInput(fromFile)

    result = []

    for _ in range(int(inp())):
        count = 0

        _, m = list(map(int, inp().split(' ')))
        a = list(map(int, inp().split(' ')))

        if m < len(a) or len(a) in [1,2]:
            result.append(-1)
            continue

        result.append(sum(a)*2)
        for i in range(len(a)-1):
            result.append(f"{i+1} {i+2}")
        result.append(f"{len(a)} 1")

    return result


for i in main(fromFile=False):
    print(i)
