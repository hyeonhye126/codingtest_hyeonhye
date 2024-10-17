N, K = map(int, input().split())

coin_list = []
for i in range(N):
    x = int(input())
    coin_list.append(x)

coin_list.sort(reverse=True)

coin_num = 0
for coin in coin_list:
    coin_num += K // coin
    K %= coin

print(coin_num)