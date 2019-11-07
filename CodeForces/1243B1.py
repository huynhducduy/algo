results = []
# f = open('input', 'r')
for _ in range(int(input())):
    input()
    s = input()
    t = input()
    ds = []
    dt = []
    for i in range(len(s)):
        if s[i] != t[i]:
            ds.append(s[i])
            dt.append(t[i])
    if len(ds) == 2 and ds[0] == ds[1] and dt[0] == dt[1]:
        print('Yes')
    else:
        print('No')
