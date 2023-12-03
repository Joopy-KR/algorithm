"""
일단 시킨대로 다 구현하자

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.


2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.


3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = [[0] * (N + 1) for _ in range(N + 1)]
all_like_lst = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(N ** 2):
    current_student = list(map(int, input().rstrip().split()))

    student, *like_lst = current_student
    # 나중을 위해 학생별 좋아하는 목록은 따로 저장해주어야 함
    all_like_lst.append(current_student)

    possible_seat = []

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            # 1. 비어있는 칸 중에서
            if arr[r][c] == 0:
                # 좋아하는 학생이 인접한 칸에
                like_cnt = 0
                # 가장 많은 칸으로 자리를 정한다.
                empty_cnt = 0

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 1 <= nr < N + 1 and 1 <= nc < N + 1:
                        if arr[nr][nc] in like_lst:
                            like_cnt += 1

                        if arr[nr][nc] == 0:
                            empty_cnt += 1

                possible_seat.append((like_cnt, empty_cnt, r, c))

    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    possible_seat.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    arr[possible_seat[0][2]][possible_seat[0][3]] = student

# 다 끝났다면, 학생 순으로 정렬!
all_like_lst.sort()

# 학생 만족도 구하기
result = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 1 <= nr < N + 1 and 1 <= nc < N + 1:
                if arr[nr][nc] in all_like_lst[arr[r][c] - 1]:
                    cnt += 1

        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)