def getInput(fromFile=False):
    if fromFile:
        f = open('input', 'r')
        return lambda :f.readline()[:-1]
    return input


def main(fromFile = False):
    inp = getInput(fromFile)
    result = []
    q = []

    for i in range(int(inp())-2):
        q.append(map(int, inp().split(' ')))

    return result


print(*main(fromFile=False))
