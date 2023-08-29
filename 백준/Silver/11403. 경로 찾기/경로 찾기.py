import sys
input = sys.stdin.readline

def dfs(s, e, N, arr):
    stack = []
    visited = [0] * N
    while True:
        for w in range(N):
            if arr[s][w] == 1 and visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

    if visited[e] == 1:
        return True
    else:
        return False


N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(N):
        i = r
        j = c
        if dfs(i, j, N, arr):
            result[i][j] = 1

for m in result:
    print(*m)
