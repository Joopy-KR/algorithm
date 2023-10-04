"""
간단한 DFS 미로찾기 문제
"""
import sys
input = sys.stdin.readline


def is_DFS(M, N, arr):
    d_r = [-1, 0, 1, 0]
    d_c = [0, 1, 0, -1]
    stack = []
    visited = [[0] * N for _ in range(M)]
    for i in range(N):
        if arr[0][i] == 0:
            visited[0][i] = 1
            start = [0, i]
            while True:
                for j in range(4):
                    nr = start[0] + d_r[j]
                    nc = start[1] + d_c[j]
                    if 0 <= nr < M and 0 <= nc < N:
                        if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                            stack.append(start)
                            start = [nr, nc]
                            visited[nr][nc] = 1
                            if nr == (M - 1):
                                return True
                            break
                else:
                    if stack:
                        start = stack.pop()
                    else:
                        break
    return False


M, N = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(M)]

if is_DFS(M, N, arr):
    print('YES')
else:
    print('NO')