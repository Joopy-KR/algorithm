import sys
input = sys.stdin.readline

def dfs(n, N, arr):
    cnt = 0
    stack = []
    visited = [0] * (N + 1)
    visited[n] = 1
    cnt += 1
    while True:
        for w in range(1, N + 1):
            if arr[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                cnt += 1
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return cnt - 1

T = int(input().rstrip())
for tc in range(1, T + 1):
    N, M = map(int, input().rstrip().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]


    for i in range(M):
        p, c = map(int, input().rstrip().split())
        if i == 0:
            start = p
        arr[p][c] = 1
        arr[c][p] = 1

    print(dfs(start, N, arr))
