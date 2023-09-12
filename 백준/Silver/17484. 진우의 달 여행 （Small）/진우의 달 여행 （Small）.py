import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

ck = 0
min_val = 10000000
temp_val = 0


def check(r, c):
    global temp_val
    global min_val
    global ck
    # 만약에 r이 N보다 커지면
    if r == N:
        if temp_val < min_val:
            min_val = temp_val
        return

    else:
        temp_val += arr[r][c]
        # 맨 윗줄인 경우
        if ck == 0:
            # 아래로 가기 - ck가 2
            ck = 2
            check(r + 1, c)

            # 왼쪽으로 가기 - ck가 1
            if 0 <= c - 1:
                ck = 1
                check(r + 1, c - 1)

            # 오른쪽으로 가기 - ck가 3
            if c + 1 < M:
                ck = 3
                check(r + 1, c + 1)

        # 왼쪽으로 가서 왔을 경우
        elif ck == 1:
            # 아래로 가기 - ck가 2
            ck = 2
            check(r + 1, c)

            # 오른쪽으로 가기 - ck가 3
            if c + 1 < M:
                ck = 3
                check(r + 1, c + 1)

        # 직선으로 왔을 경우
        elif ck == 2:
            # 왼쪽으로 가기
            if 0 <= c - 1:
                ck = 1
                check(r + 1, c - 1)

            # 오른쪽으로 가기 - ck가 3
            if c + 1 < M:
                ck = 3
                check(r + 1, c + 1)

        # 오른쪽으로 가서 왔을 경우
        elif ck == 3:
            # 아래로 가기 - ck가 2
            ck = 2
            check(r + 1, c)

            # 왼쪽으로 가기
            if 0 <= c - 1:
                ck = 1
                check(r + 1, c - 1)
        temp_val -= arr[r][c]


for i in range(M):
    temp_val = 0
    ck = 0
    # 여기에 함수를 시작줄만 M번 돌릴꺼임
    check(0, i)


print(min_val)