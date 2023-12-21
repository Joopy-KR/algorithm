import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

coins = []
for _ in range(N):
    coins.append(int(input().rstrip()))

cnt = 0
for i in range(len(coins) - 1, -1, -1):
    while K - coins[i] >= 0:
        K -= coins[i]
        cnt += 1
    if K == 0:
        break

print(cnt)