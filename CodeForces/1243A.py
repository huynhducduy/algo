# f = open('input', 'r')
# for _ in range(int(f.readline())):
results = []
for _ in range(int(input())):
    # f.readline()
    input()
    # planks = list(map(int, f.readline().split(' ')))
    planks = list(map(int, input().split(' ')))
    max_plank = max(planks)
    num_plank = [0]*(max_plank+2)
    for i in planks:
        num_plank[i] += 1
    for i in reversed(range(1, max_plank+1)):
        num_plank[i] += num_plank[i+1]
        if num_plank[i] >= i:
            results.append(i)
            break

for i in results:
    print(i)
