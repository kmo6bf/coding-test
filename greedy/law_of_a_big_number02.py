'''
가장 큰 수가 더해지는 횟수를 구하는 공식
int(m // (k + 1) * k + (m % (k + 1)))
'''
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

num_of_max = (m // (k + 1)) * (k + (m % (k + 1)))
first = array[-1]
second = array[-2]
result = num_of_max * first + (m - num_of_max) * second

print(result)