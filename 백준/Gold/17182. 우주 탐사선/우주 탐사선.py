import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = float('INF')
visited = [False] * N
def solution(before_pos, current_pos, now, vst, cost):
    global result
    if now == N:
        result = min(result, cost)
        return
    for n in range(N):
        if not vst[n]:
            vst[n] = True
            cost += arr[current_pos][n]
            before_pos = current_pos
            current_pos = n
            solution(before_pos, current_pos, now + 1, vst, cost)
            vst[n] = False
            current_pos = before_pos
            cost -= arr[current_pos][n]

solution(K, K, 0, visited, 0)
print(result)