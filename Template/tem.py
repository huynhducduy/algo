def getInput(fromFile=False):
    if fromFile:
        f = open('input', 'r')
        return lambda :f.readline()[:-1]
    return input


def main(fromFile = False):
    inp = getInput(fromFile)


print(main(fromFile=True))
