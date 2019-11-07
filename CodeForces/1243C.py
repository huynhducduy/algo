import math
n = int(input())


def divisorGenerator(n):
    large_divisors = []
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


result = n
divs = list(divisorGenerator(n))

if len(divs) > 0:
    for i in divs:
        result = math.gcd(result, i)

print(result)
