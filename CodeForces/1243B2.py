import string
results = []
# f = open('input', 'r')
for _ in range(int(input())):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    input()
    s = input().rstrip('\n')
    t = input().rstrip('\n')
    ds = []
    dt = []
    diff = 0
    for i in range(len(s)):
        d[s[i]] += 1
        d[t[i]] += 1
        if s[i] != t[i]:
            diff += 1
    no = False
    for i in d.values():
        if i != 0 and i % 2 != 0:
            no = True
            break
    if no:
        results.append(False)
        continue
    resultss = []
    while diff > 0 and len(resultss) < 2*len(s):
        for i in range(len(s)):
            # print('i', i)
            if s[i] != t[i]:
                swapped = False
                for j in range(i+1, len(s)):
                    # print('j', j)
                    if s[j] != t[j] and s[i] == s[j] and t[i] == t[j]:
                        tmp = s[i]
                        s = s[:i] + t[j] + s[i+1:]
                        t = t[:j] + tmp + t[j+1:]
                        diff -= 2
                        swapped = True
                        resultss.append((i+1, j+1))
                        break
                if swapped == False:
                    for j in range(i+1, len(s)):
                        # print('j', j)
                        if s[j] != t[j] and (s[i] == s[j] or t[i] == t[j]):
                            tmp = s[i]
                            s = s[:i] + t[j] + s[i+1:]
                            t = t[:j] + tmp + t[j+1:]
                            diff -= 1
                            swapped = True
                            resultss.append((i+1, j+1))
                            break
                if swapped == False:
                    tmp = s[i]
                    s = s[:i] + t[i] + s[i+1:]
                    t = t[:i] + tmp + t[i+1:]
                    resultss.append((i+1, i+1))
                    break
    if diff > 0:
        results.append(False)
    else:
        results.append(resultss)

for i in results:
    if i == False:
        print('No')
    else:
        print('Yes')
        print(len(i))
        for j in i:
            print(str(j[0]) + ' ' + str(j[1]))
