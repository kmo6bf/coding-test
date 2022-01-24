n, k = map(int, input().split())
loop = 0

while n > 1:
    if n % k != 0:
        n -= 1
        loop += 1
        continue
    n //= k
    loop += 1

print(loop)
