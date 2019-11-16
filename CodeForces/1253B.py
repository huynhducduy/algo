# f = open('input', 'r')

def main():
    result = []

    # f.readline()
    input()
    # e = list(map(int, f.readline().split(' ')))
    e  = list(map(int, input().split(' ')))

    d = [0] * len(e)
    d[0] = e[0]

    for i in range(1, len(e)):
        d[i] = d[i-1]+e[i]
        if d[i] == 0:
            result.append(i)

    if d[-1] != 0:
        return -1

    for i in d:
        if i < 0:
            return -1


    if len(result) > 1:
        result = [result[0]+1] + [result[i]-result[i-1] for i in range(1,len(result))]
    elif len(result) > 0:
        result = [result[0]+1]
    else:
        return -1


    last = result[0]
    t = [(0, last)]
    for i in result[1:]:
        t.append((last, last+i))
        last = last+i

    for i,j in t:
        check = {}
        for z in e[i:j]:
            if (z > 0 and not check.get(z, False)):
                check[z] = True
            elif (z < 0 and not check.get(z*-1, False)):
                return -1
            else:
                check[z] = False

    return result

result = main()
if result == -1:
    print(-1)
else:
    print(len(result))
    print(*result)
