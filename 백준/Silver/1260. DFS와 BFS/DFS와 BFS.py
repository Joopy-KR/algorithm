N, M, V = map(int, input().split())


# # 1차원 재귀 DFS
# stack = []
# result = []
# visited = [0] * (N + 1)
# visited[1] = 1
# result.append(1)
# def DFS(n, V, arr):
#     for w in arr[n]:
#         if visited[w] == 0:
#             stack.append(n)
#             result.append(w)
#             visited[w] = 1
#             DFS(w, V, arr)
#     else:
#         if stack:
#             n = stack.pop()
#             DFS(n, V, arr)
#         else:
#             return


# 1차원 배열 DFS
def DFS(n, V, arr):
    result = []
    stack = []
    visited = [0] * (V + 1)
    result.append(n)
    visited[n] = 1
    while True:
        for w in range(len(arr[n])):
            if arr[n][w] and visited[arr[n][w]] == 0:
                stack.append(n)
                n = arr[n][w]
                result.append(n)
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return result


# # 2차원 배열 DFS
# def DFS(n, V, arr):
#     result = []
#     stack = []
#     visited = [0] * (V + 1)
#     visited[n] = 1
#     result.append(n)
#     while True:
#         for w in range(1, V + 1):
#             if arr[n][w] == 1 and visited[w] == 0:
#                 stack.append(n)
#                 n = w
#                 result.append(n)
#                 visited[n] = 1
#                 break
#         else:
#             if stack:
#                 n = stack.pop()
#             else:
#                 break
#     return result


# 1차원 배열 BFS
def bfs(s, V, arr):
    result = []
    queue = []
    visited = [0] * (V + 1)
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        result.append(t)
        for w in arr[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
    return result


# # 2차원 배열 BFS
# def bfs(s, V, arr):
#     result = []
#     queue = []
#     visited = [0] * (V + 1)
#     queue.append(s)
#     visited[s] = 1
#     while queue:
#         t = queue.pop(0)
#         result.append(t)
#         for w in range(1, V + 1):
#             if arr[t][w] == 1 and visited[w] == 0:
#                 queue.append(w)
#                 visited[w] = visited[t] + 1
#     return result


# 1차원 배열로 받기
arr = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    r, c = map(int, input().split())
    arr[r].append(c)
    arr[c].append(r)

for i in arr:
    i.sort()

print(*DFS(V, N, arr))
print(*bfs(V, N, arr))


# # 2차원 배열로 받기
# arr = [[0] * (N + 1) for _ in range(N + 1)]
# for _ in range(M):
#     r, c = map(int, input().split())
#     arr[r][c] = 1
#     arr[c][r] = 1
#
# # print(*DFS(V, N, arr))
# print(*bfs(V, N, arr))
