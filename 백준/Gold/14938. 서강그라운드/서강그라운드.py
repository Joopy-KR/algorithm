import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, R = map(int, input().rstrip().split())

arr = [[INF] * (N + 1) for _ in range(N + 1)]

items = [0] + list(map(int, input().rstrip().split()))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            arr[i][j] = 0

for _ in range(R):
    a, b, l = map(int, input().rstrip().split())
    arr[a][b] = l
    arr[b][a] = l

for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            arr[r][c] = min(arr[r][c], arr[r][k] + arr[k][c])

max_result = 0
for n in range(1, N + 1):
    temp = 0
    for m in range(1, N + 1):
        if arr[n][m] != INF:
            if arr[n][m] <= M:
                temp += items[m]
    max_result = max(max_result, temp)

print(max_result)