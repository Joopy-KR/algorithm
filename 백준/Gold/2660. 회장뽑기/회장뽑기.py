import sys
input = sys.stdin.readline
INF = sys.maxsize

# 정점 개수 N개
N = int(input().rstrip())
arr = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신한테 가는 거리는 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            arr[i][j] = 0

# 짱친끼리는 비용을 1로 만들어주기
while True:
    a, b = map(int, input().rstrip().split())
    if a == b == -1:
        break
    else:
        arr[a][b] = 1
        arr[b][a] = 1

# 플로이드 와샬 수행하기
for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            arr[r][c] = min(arr[r][c], arr[r][k] + arr[k][c])

# 개수 세주기
temp = []
for n in range(1, N + 1):
    arr[n].sort(reverse=True)
    temp.append(arr[n][1])

min_val = min(temp)

result_idx = []
result_cnt = 0

for l in range(len(temp)):
    # 최소값이라면
    if temp[l] == min_val:
        result_cnt += 1
        result_idx.append(str(l + 1))

print(min_val, result_cnt)
print(' '.join(result_idx))