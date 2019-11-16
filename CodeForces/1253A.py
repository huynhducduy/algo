# f = open('input', 'r')
results = []

# for _ in range(int(f.readline())):
for _ in range(int(input())):
    # f.readline()
    input()
    # a = list(map(int, f.readline().split(' ')))
    # b = list(map(int, f.readline().split(' ')))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    if a == b:
        results.append('YES')
    else:
        i = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                break

        j = i+1
        for j in range(i+1, len(a)):
            if a[j] == b[j]:
                j -= 1
                break

        if a[j+1:] != b[j+1:]:
            results.append('NO')
            continue

        diff = b[i]-a[i]
        if diff > 0:
            if list(map(lambda s: s+diff, a[i:j+1])) == b[i:j+1]:
                results.append('YES')
                continue

        results.append('NO')

for i in results:
    print(i)
