"""
Queen을 1
Knight를 2
Pawn을 3이라고 하자
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

Q, *queen = list(map(int, input().split()))
K, *knight = list(map(int, input().split()))
P, *pawn = list(map(int, input().split()))

arr = [[0] * (M + 1) for _ in range(N + 1)]

# 말들을 먼저 배치하고
for q in range(0, len(queen), 2):
    arr[queen[q]][queen[q + 1]] = 1

for k in range(0, len(knight), 2):
    arr[knight[k]][knight[k + 1]] = 2

for p in range(0, len(pawn), 2):
    arr[pawn[p]][pawn[p + 1]] = 3

# 퀸의 델타탐색
q_dr = [-1, -1, 0, 1, 1, 1, 0, -1]
q_dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 나이트의 델타탐색
k_dr = [-2, -2, -1, 1, 2, 2, 1, -1]
k_dc = [-1, 1, 2, 2, 1, -1, -2, -2]

# 배열을 돌면서 위험한 칸을 지우고
for r in range(1, N + 1):
    for c in range(1, M + 1):
        # 현재 말이 퀸이라면
        if arr[r][c] == 1:
            for i in range(8):
                now_r = r
                now_c = c
                while True:
                    nr = now_r + q_dr[i]
                    nc = now_c + q_dc[i]
                    if 1 <= nr < N + 1 and 1 <= nc < M + 1:
                        if arr[nr][nc] == 0 or arr[nr][nc] == 999:
                            now_r = nr
                            now_c = nc
                            arr[nr][nc] = 999
                        else:
                            break
                    else:
                        break

        # 현재 말이 나이트라면
        elif arr[r][c] == 2:
            for j in range(8):
                nr = r + k_dr[j]
                nc = c + k_dc[j]
                if 1 <= nr < N + 1 and 1 <= nc < M + 1:
                    if arr[nr][nc] == 0 or arr[nr][nc] == 999:
                        arr[nr][nc] = 999

# 안전한 칸이 몇칸인지 O(N)으로 세자
result = 0
for r in range(1, N + 1):
    for c in range(1, M + 1):
        if arr[r][c] == 0:
            result += 1

print(result)