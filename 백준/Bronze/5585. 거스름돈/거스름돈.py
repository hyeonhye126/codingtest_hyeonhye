N = int(input())

coin_list = [500, 100, 50, 10, 5, 1]

money = 1000 - N

my_coin = 0
for coin in coin_list:
    my_coin += money // coin
    money %= coin

print(my_coin)

