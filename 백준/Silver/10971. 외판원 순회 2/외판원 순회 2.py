""""
1. visited 찍고 다 돌고
2. 만약 전부 방문했다면 원래자리로 돌아오고1
3. 최소값 갱신하기
4. 만약, 이미 최소값보다 크거나 순회할 수 없다면
5. 더 볼필요도 없음
"""
import sys
input = sys.stdin.readline

min_val = 100000000
def backtracking(cnt):
    global min_val
    if cnt == N:
        if arr[path[-1] - 1][path[0] - 1] != 0:
            temp = 0
            for j in range(N - 1):
                temp += arr[path[j] - 1][path[j + 1] - 1]
            temp += arr[path[-1] - 1][path[0] - 1]
            min_val = min(min_val, temp)
        return
    for num in range(1, N + 1):
        if num in path:
            continue
        if cnt > 0 and arr[path[cnt - 1] - 1][num - 1] == 0:
            continue
        if cnt == N - 1:
            if arr[path[-1] - 1][path[0] - 1] == 0:
                continue

        path[cnt] = num
        backtracking(cnt + 1)
        path[cnt] = 0


N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
path = [0] * N
backtracking(0)
print(min_val)
