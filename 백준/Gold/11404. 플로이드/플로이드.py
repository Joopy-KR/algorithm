import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input().rstrip())
M = int(input().rstrip())

distance = [[INF] * (N + 1) for _ in range(N + 1)]


for _ in range(M):
    s, e, c = map(int, input().rstrip().split())
    distance[s][e] = min(distance[s][e], c)


for i in range(1, N + 1):
    distance[i][i] = 0


for k in range(1, N + 1):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            distance[r][c] = min(distance[r][c], distance[r][k] + distance[k][c])


for l in range(1, N + 1):
    for m in range(1, N + 1):
        if distance[l][m] == INF:
            print(0, end=' ')
        else:
            print(distance[l][m], end=' ')
    print()