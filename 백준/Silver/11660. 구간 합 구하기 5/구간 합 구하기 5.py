# 29' 13''

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
arr_sum = [[0] * (N + 1) for _ in range(N + 1)]

for r in range(N):
    for c in range(N):
        # 왼쪽 합 + 위 합 + 자기 자신 - 대각선 왼쪽 합 = 자기의 구간 합 (위치를 벗어나면 0으로 간주해야함)
        arr_sum[r][c] = arr_sum[r][c - 1] + arr_sum[r - 1][c] + arr[r][c] - arr_sum[r - 1][c - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
    # 큰거 - 윗칸 싹다 - 왼쪽 싹다 + 겹친부분
    result = (arr_sum[x2][y2] - arr_sum[x1 - 1][y2] - arr_sum[x2][y1 - 1] + arr_sum[x1 - 1][y1 - 1])
    print(result)
