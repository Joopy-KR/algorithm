def dfs(n, N, arr):
    stack = []
    visited = [0] * (N + 1)
    visited[n] = 1
    while True:
        for w in range(len(arr[n])):
            if arr[n][w] and visited[arr[n][w]] == 0:
                stack.append(n)
                visited[arr[n][w]] = n
                n = arr[n][w]
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    for i in visited[2:]:
        print(i)


N = int(input())
arr = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    p, c = map(int, input().split())
    arr[p].append(c)
    arr[c].append(p)

dfs(1, N, arr)
