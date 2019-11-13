# f = open('input', 'r')
results = []
# for _ in range(int(f.readline())):
for _ in range(int(input())):
    # a,b = map(int, f.readline()[:-1].split(' '))
    a,b = map(int, input().split(' '))
    if a == b:
        results.append('yes')
    elif a == 1:
        results.append('no')
    elif a <= 3:
        if b <= 3:
            results.append('yes')
        else:
            results.append('no')
    else:
        results.append('yes')
for i in results:
    print(i)
