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
        a, b = map(int, inp().split(' '))

        if b != a:
            if a > b:
                a, b = b, a

            count += int((b-a)/5)
            b -= count*5

            if b-a in [3,4]:
                count += 2
            elif b-a in [1,2]:
                count += 1

        result.append(count)
    return result


for i in main(fromFile=False):
    print(i)
