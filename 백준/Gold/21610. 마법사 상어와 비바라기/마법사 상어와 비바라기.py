import sys
input = sys.stdin.readline

d_r = [None, 0, -1, -1, -1, 0, 1, 1, 1]
d_c = [None, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().rstrip().split())

arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
move = [list(map(int, input().rstrip().split())) for _ in range(M)]

# 초기 구름 좌표
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for di, si in move:
    moved_cloud = []
    # 모든 구름 이동하기
    for r, c in clouds:
        nr = (r + d_r[di] * si) % N
        nc = (c + d_c[di] * si) % N
        # 물 1씩 추가
        arr[nr][nc] += 1
        moved_cloud.append((nr, nc))

    # 이동한 구름 대각 4방향 조사 후 count만큼 물 양 추가하기
    d_r_four = [-1, -1, 1, 1]
    d_c_four = [-1, 1, -1, 1]
    for r, c in moved_cloud:
        cnt = 0
        for i in range(4):
            nr = r + d_r_four[i]
            nc = c + d_c_four[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > 0:
                    cnt += 1
        arr[r][c] += cnt

    # 5번 과정 수행하기
    new_cloud = []
    for r in range(N):
        for c in range(N):
            # 3에서 구름이 사라진 칸이 아니고, 물 양이 2 이상이라면
            if (r, c) not in moved_cloud:
                if arr[r][c] >= 2:
                    arr[r][c] -= 2
                    new_cloud.append((r, c))

    # 다음 구름 만들어주기
    clouds = new_cloud

# 물의 양 합산 후 출력
result = 0
for r in range(N):
    for c in range(N):
        result += arr[r][c]

print(result)