N, K = map(int, input().split()) # N: 물품 수 K: 버틸 수 있는 무게

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append([W, V])

# dp[w] = 배낭을 무게 w까지 채웠을 때 얻을 수 있는 최대 가치
dp = [0] * (K + 1)

for W, V in items:
    for w in range(K, W - 1, -1):
        dp[w] = max(dp[w], dp[w - W] + V)

print(dp[K])