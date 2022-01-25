number_of_coin, change = map(int, input().split())
coins = [int(input()) for _ in range(number_of_coin)]
coins.reverse()
change_coin = 0

for i in coins:
    if (change == 0):
        break

    while (change >= i):
        change_coin += change // i
        change %= i

print(change_coin)

