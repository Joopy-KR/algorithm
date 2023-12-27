import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

distance = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())

    distance[A][B] = 1
    distance[B][A] = 1

for i in range(1, N + 1):
    distance[i][i] = 0

for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            distance[r][c] = min(distance[r][c], distance[r][k] + distance[k][c])

min_sum = INF

result = list()
for i in range(1, N):  # 건물 2개를 뽑는다.
    for j in range(2, N + 1):
        sum_ = 0
        for k in range(1, N + 1):  # 모든 집을 방문하면서 거리를 측정
            sum_ += min(distance[k][i], distance[k][j]) * 2  # k -> i, k -> j 중에 짧은 거리 합치기
        if sum_ < min_sum:
            min_sum = sum_
            result = [i, j, sum_]

print(*result)

