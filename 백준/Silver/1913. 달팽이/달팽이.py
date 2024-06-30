"""
[0, 0] 은 항상 N 제곱이다
즉, 시작점 기준으로 아래 방향부터 그려나가면 된다
사과를 깎는다고 생각하자. 밖에서부터 네모를 만들면서 가는거다

1. 시작점을 잡는다 (0, 0)
2. 시작점을 기준으로 N - 1만큼 아래, 오른쪽, 위로 이동한다
3. 그 다음부터는 두번씩 N - 2, N - 3.. 으로 1까지 이동한다.
4. 1인 상태로 두번 이동했다면 종료한다

5. 각각의 숫자 입력에서, 찾고자 하는 숫자이면 좌표를 기록해둔다
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [[0] * N for _ in range(N)]
# 찾아야 할 숫자
find_num = int(input().rstrip())
find_r = 0
find_c = 0

# 1. 시작점을 잡는다 (0, 0)
arr[0][0] = N ** 2
# 현재 숫자
cur_num = arr[0][0]
# 현재 좌표
cur_r = 0
cur_c = 0

# 2. 시작점을 기준으로 N - 1만큼 아래, 오른쪽, 위로 이동한다
first_dr = [1, 0, -1]
first_dc = [0, 1, 0]
# 몇번째 델타탐색을 돌아야 하는지 표시
idx = -1
for i in range(3):
    idx += 1
    # N - 1번만큼 진행방향으로 이동
    for j in range(1, N):
        # 가고 있는 방향으로 이동
        cur_r += first_dr[idx]
        cur_c += first_dc[idx]
        # 색칠
        cur_num -= 1
        arr[cur_r][cur_c] = cur_num
        if cur_num == find_num:
            find_r = cur_r
            find_c = cur_c

# 3. 그 다음부터는 두번씩 N - 2, N - 3.. 으로 1까지 이동한다.
total_cnt = 2
move_cnt = 0
idx = 0
# 델타 탐색은 왼, 아 / 오, 위 순으로 진행
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 4. 1인 상태로 두번 이동했다면 종료한다
while N - total_cnt > 0:
    cur_r += dr[idx]
    cur_c += dc[idx]

    # 색칠
    cur_num -= 1
    arr[cur_r][cur_c] = cur_num
    if cur_num == find_num:
        find_r = cur_r
        find_c = cur_c

    # N - total_cnt 만큼 움직이기
    move_cnt += 1
    if move_cnt == N - total_cnt:
        move_cnt = 0
        # 왼아 / 오위로 나뉘어진다. 구분하자
        if idx == 0 or idx == 2:
            idx += 1
        else:
            if idx == 3:
                idx = 0
            else:
                idx += 1
            total_cnt += 1


for r in range(N):
    if r != 0:
        print()
    for c in range(N):
        print(arr[r][c], end=' ')

print()
print(find_r + 1, find_c + 1)
