def getInput(fromFile=False):
    if fromFile:
        f = open('input', 'r')
        return lambda :f.readline()[:-1]
    return input


def main(fromFile = False):
    inp = getInput(fromFile)
    result = []

    for _ in range(int(inp())):
        d, p = inp().split()
        def decode(s):
            num = ord(s)+int(d)
            if num > 122:
                num = num - 123 + 97
            return chr(num)
        p = list(map(decode, list(p)))
        result.append(''.join(p))

    return result



for i in main(fromFile=True):
    print(i)
